# famcom is a program for comparing DIPPR compounds.                        #
# Copyright (C) 2022 Thomas Allen Knotts IV - All Rights Reserved           #
#                                                                           #
# This program is free software you can redistribute it and/or modify       #
# it under the terms of the GNU General Public License as published by      #
# the Free Software Foundation, either version 3 of the License, or         #
# (at your option) any later version.                                       #
#                                                                           #
# This program is distributed in the hope that it will be useful,           #
# but WITHOUT ANY WARRANTY; without even the implied warranty of            #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
# GNU General Public License for more details.                              #
#                                                                           #
# You should have received a copy of the GNU General Public License         #
# along with this program.  If not, see httpwww.gnu.orglicenses.            #
# ========================================================================= #
# famcom.py                                                                 #
#                                                                           #
# Thomas A. Knotts IV                                                       #
# Brigham Young University                                                  #
# Department of Chemical Engineering                                        #
# Provo, UT  84606                                                          #
# Email thomas.knotts@byu.edu                                               #
# ========================================================================= #
# Version 1.0 - September 2022                                              #
# ========================================================================= #

"""
This module reads the data in a compound file into
a variable of class `compound`.

    compound       a class that holds the information for each compound
    tcoeff         a class holding the information for a temperature-dependent
                     property
    read_compound  a method from class `compound` that reads in the data 
                     for a compound into a text file 
"""
import sys, os, string, math
import matplotlib.pyplot as plt
import numpy as np
import byutpl.equations.dippreqns as eq

def isnumber(s):
    try:
        float(s)
        return(True)
    except ValueError:
        return(False)

# The class for each tdep property
class tcoeff:
    def __init__(self):
        self.prop=''            # property
        self.tmin=float("nan")  # min temp of correlation
        self.tmax=float("nan")  # max temp of correlation
        self.eq=float("nan")    # correlation eqation number
        self.c=np.array([])     # coefficients
        
# The class to hold the compound information
class compound:
    def __init__(self):
        self.Name=''
        self.ChemID=-1
        self.MW=float("nan")
        self.TC=float("nan")
        self.PC=float("nan")
        self.VC=float("nan")
        self.ZC=float("nan")
        self.MP=float("nan")
        self.TPT=float("nan")
        self.TPP=float("nan")
        self.NBP=float("nan")
        self.LVOL=float("nan")
        self.HFOR=float("nan")
        self.GFOR=float("nan")
        self.ENT=float("nan")
        self.HSTD=float("nan")
        self.GSTD=float("nan")
        self.SSTD=float("nan")
        self.HFUS=float("nan")
        self.HCOM=float("nan")
        self.ACEN=float("nan")
        self.RG=float("nan")
        self.SOLP=float("nan")
        self.DM=float("nan")
        self.VDWA=float("nan")
        self.VDWV=float("nan")
        self.RI=float("nan")
        self.FP=float("nan")
        self.FLVL=float("nan")
        self.FLVU=float("nan")
        self.FLTL=float("nan")
        self.FLTU=float("nan")
        self.AIT=float("nan")
        self.HSUB=float("nan")
        self.PAR=float("nan")
        self.DC=float("nan")
        tprops=['LDN','SDN','ICP','LCP','SCP','HVP','SVR','ST', \
                'LTC','VTC','STC','VP','SVP','LVS','VVS']
        self.coeff={}
        for i in tprops:
            self.coeff[i]=tcoeff()

    def read_compound(self,fn):
    """reads the property data into the self `compound` object
    
    Parameter
    ----------
    fn : string
         name of file containing the data for the compound in 
         'key\tvalue(s)' form
        
    """
        # check to see if the input files exists
        if not os.path.isfile(fn): 
            print("Input file \"" + fn +"\" does not exist.\n")
            import warnings
            warnings.filterwarnings("ignore")
            sys.exit("Error: Input file missing.")
        
        # Parse the input file
        fi=open(fn)        # open the file
        content=fi.readlines()  # read the file into a variable
        fi.close()              # close the file
        data={}               # make a dicitonary to hold the keywords and values
        for line in content:          # interate through each line of text in file
            linetext=line.strip()     # get rid of whitespace on each end of line
            linetext=linetext.rstrip('\t') # remove triling tabs
            if not linetext: continue # skip empty lines
            # Remove the end of line comment (everything after '#') and
            # and split the lines at all commas
            linetext=linetext.split('#',1)[0].split('\t')
            if not linetext: continue # skip a line that was only comments
            # Separate the line into the key and the value pair
            if len(linetext) > 1: # ignore keys without values
                key=linetext[0]            
                val=linetext[1:]
                # Place the key and value into the dictionary
                data[key]=val
        # Assign constant data
        cprops=['MW','TC','PC','VC','ZC','MP','TPT','TPP','NBP','LVOL','HFOR','GFOR', \
                'ENT','HSTD','GSTD','SSTD','HFUS','HCOM','ACEN','RG','SOLP','DM', \
                'VDWA','VDWV','RI','FP','FLVL','FLTL','FLVU','FLTU','AIT','HSUB', \
                'PAR','DC']
        if 'Name' in data.keys(): self.Name=data.get('Name')[0]
        if 'ChemID' in data.keys(): self.ChemID=int(data.get('ChemID')[0])
        for i in cprops:
            if i in data: # check if prop was in file
                setattr(self, i, float(data.get(i)[0]))
        
        # tdep coefficients
        tprops=['LDN','SDN','ICP','LCP','SCP','HVP','SVR','ST', \
                'LTC','VTC','STC','VP','SVP','LVS','VVS']
        for i in tprops:
            if i in data: # check if prop was in file
                self.coeff[i].eq=int(data.get(i)[0])
                self.coeff[i].tmin=float(data.get(i)[1])
                self.coeff[i].tmax=float(data.get(i)[2])
                self.coeff[i].c=np.array(data.get(i)[3:]).astype(float)
                
    def LDN(self,t):
    """liquid density of the compound
    
    Parameter
    ----------
    t : float
        temperature (K)
        
    Returns
    -------
    float
        the liquid density of the compound at temperature `t` in kmol/m**3
    """
        if self.coeff['LDN'].eq == 116 or self.coeff['LDN'].eq == 119: t = 1-t/self.TC
        return(eq.eq(t,self.coeff['LDN'].c,self.coeff['LDN'].eq))
    
    def SDN(self,t):
    """solid density of the compound
    
    Parameter
    ----------
    t : float
        temperature (K)
        
    Returns
    -------
    float
        the solid density of the compound at temperature `t` in kmol/m**3
    """
        return(eq.eq(t,self.coeff['SDN'].c,self.coeff['SDN'].eq))
    
    def ICP(self,t):
    """ideal gas heat capacity of the compound
    
    Parameter
    ----------
    t : float
        temperature (K)
        
    Returns
    -------
    float
        the ideal gas heat capacity of the compound at temperature `t` in J/(kmol*K)
    """
        return(eq.eq(t,self.coeff['ICP'].c,self.coeff['ICP'].eq))
    
    def LCP(self,t):
    """liquid heat capacity of the compound
    
    Parameter
    ----------
    t : float
        temperature (K)
        
    Returns
    -------
    float
        the liquid heat capacity of the compound at temperature `t` in J/(kmol*K)
    """
        if self.coeff['LCP'].eq == 114 or self.coeff['LCP'].eq == 124: t = 1-t/self.TC
        return(eq.eq(t,self.coeff['LCP'].c,self.coeff['LCP'].eq))
    
    def SCP(self,t):
    """solid heat capacity of the compound
    
    Parameter
    ----------
    t : float
        temperature (K)
        
    Returns
    -------
    float
        the solid heat capacity of the compound at temperature `t` in J/(kmol*K)
    """
        return(eq.eq(t,self.coeff['SCP'].c,self.coeff['SCP'].eq))
    
    def HVP(self,t):
    """heat of vaporization of the compound
    
    Parameter
    ----------
    t : float
        temperature (K)
        
    Returns
    -------
    float
        the heat of vaporization of the compound at temperature `t` in J/kmol
    """
        if self.coeff['HVP'].eq == 106: t = t/self.TC
        return(eq.eq(t,self.coeff['HVP'].c,self.coeff['HVP'].eq))
    
    def SVR(self,t):
    """second virial coefficient of the compound
    
    Parameter
    ----------
    t : float
        temperature (K)
        
    Returns
    -------
    float
        the second virial coefficient of the compound at temperature `t` in m**3/kmol
    """
        return(eq.eq(t,self.coeff['SVR'].c,self.coeff['SVR'].eq))
    
    def ST(self,t):
    """ surface tension of the compound
    
    Parameter
    ----------
    t : float
        temperature (K)
        
    Returns
    -------
    float
        the surface tension of the compound at temperature `t` in N/m
    """
        if self.coeff['ST'].eq == 106: t = t/self.TC
        return(eq.eq(t,self.coeff['ST'].c,self.coeff['ST'].eq))
    
    def LTC(self,t):
    """ liquid thermal conductivity of the compound
    
    Parameter
    ----------
    t : float
        temperature (K)
        
    Returns
    -------
    float
        the liquid thermal conductivity of the compound at temperature `t` in W/(m*K)
    """
        if self.coeff['LTC'].eq == 123: t = 1-t/self.TC
        return(eq.eq(t,self.coeff['LTC'].c,self.coeff['LTC'].eq))
    
    def VTC(self,t):
    """ vapor thermal conductivity of the compound
    
    Parameter
    ----------
    t : float
        temperature (K)
        
    Returns
    -------
    float
        the vapor thermal conductivity of the compound at temperature `t` in W/(m*K)
    """
        return(eq.eq(t,self.coeff['VTC'].c,self.coeff['VTC'].eq))
    
    def STC(self,t):
    """ solid thermal conductivity of the compound
    
    Parameter
    ----------
    t : float
        temperature (K)
        
    Returns
    -------
    float
        the solid thermal conductivity of the compound at temperature `t` in W/(m*K)
    """
        return(eq.eq(t,self.coeff['STC'].c,self.coeff['STC'].eq))
    
    def VP(self,t):
    """ liquid vapor pressure of the compound
    
    Parameter
    ----------
    t : float
        temperature (K)
        
    Returns
    -------
    float
        the saturated vapor pressure of the compound at temperature `t` in Pa
    """
        return(eq.eq(t,self.coeff['VP'].c,self.coeff['VP'].eq))
    
    def SVP(self,t):
    """ solid vapor pressure of the compound
    
    Parameter
    ----------
    t : float
        temperature (K)
        
    Returns
    -------
    float
        the pressure of the vapor in equilibrium with the solid of the compound at temperature `t` in Pa
    """
        return(eq.eq(t,self.coeff['SVP'].c,self.coeff['SVP'].eq))
    
    def LVS(self,t):
    """ liquid viscosity of the compound
    
    Parameter
    ----------
    t : float
        temperature (K)
        
    Returns
    -------
    float
        the liquid viscosity of the compound at temperature `t` in Pa*s
    """
        return(eq.eq(t,self.coeff['LVS'].c,self.coeff['LVS'].eq))
    
    def VVS(self,t):
    """ vapor viscosity of the compound
    
    Parameter
    ----------
    t : float
        temperature (K)
        
    Returns
    -------
    float
        the low-pressure vapor viscosity of the compound at temperature `t` in Pa*s
    """
        return(eq.eq(t,self.coeff['VVS'].c,self.coeff['VVS'].eq))
        
def graphs(c,p):
    """Graphs the data for the compounds in `c` for property `p`
    
    
    
    Parameters
    ----------
    c : list of `famcom.compound` objects
        
    p : string
        DIPPR property to graph
        Must be one of the following: MW, TC, PC, VC, ZC, MP, TPT, TPP,
        NBP, LVOL, HFOR, GFOR, ENT, HSTD, GSTD, SSTD, HFUS, HCOM, ACEN,
        RG, SOLP, DM, VDWA, VDWV, RI, FP, FLVL, FLTL, FLVU, FLTU, AIT,
        HSUB, PAR, DC, LDN, SDN, ICP, LCP, SCP, HVP, SVR, ST, LTC, VTC,
        STC, VP, SVP, LVS, VVS.
    
    Graphs property `p` for all compounds in `c`. If `p` is a constant
    property, the graph is done vs molecular weight (`p` vs MW). If `p`
    is a temperature-dependent property, the graph is `p` vs `T`.
    Different lines will appear on the graph if multiple compounds
    are found in `c`.
    """
    # check if `c` is a list
    if type(c) != list:
        print('Graphing requires a list of compound objects which was not supplied.')
        return()
   
    # check whether the property is constant, tdep, or not a DIPPR prop
    cprops=['MW','TC','PC','VC','ZC','MP','TPT','TPP','NBP','LVOL','HFOR','GFOR', \
            'ENT','HSTD','GSTD','SSTD','HFUS','HCOM','ACEN','RG','SOLP','DM', \
            'VDWA','VDWV','RI','FP','FLVL','FLTL','FLVU','FLTU','AIT','HSUB', \
            'PAR','DC']
    tprops=['LDN','SDN','ICP','LCP','SCP','HVP','SVR','ST', \
            'LTC','VTC','STC','VP','SVP','LVS','VVS']
    ptype=''
    if p in cprops: ptype='const'
    elif p not in tprops:
        print('Property ' + p + ' is not a DIPPR property.')
        return()
    
    # sort c on MW if MW is available
    mwindex=[i for i, x in enumerate(c) if not math.isnan(x.MW)]
    if(bool(mwindex)): c.sort(key=lambda x: x.MW)
    
    # Determine the index of the compounds in `c` have data for property `p`
    if ptype == 'const': cindex=[i for i, x in enumerate(c) if not math.isnan(getattr(x,p))]
    else: cindex=[i for i, x in enumerate(c) if not math.isnan(x.coeff[p].eq)]
 
    if not cindex: # only graph if data are present
        print('No data for ' + p + ' were found in the supplied files.') 
        return()
    else:
        if ptype == 'const':
            names=[c[i].name for i in cindex]
            xdata=[c[i].MW for i in cindex]
            ydata=[getattr(c[i],p) for i in cindex]
            plt.plot(xdata,ydata,'o')
            plt.ylabel(p)
            plt.xlabel('MW')
            plt.title(p + ' vs MW')
            print(names)
        else:
            for i in range(len(cindex)):
                xdata=np.linspace(c[cindex[i]].coeff[p].tmin, c[cindex[i]].coeff[p].tmax-1, 50)
                yf=getattr(c[cindex[i]],p)
                ydata=yf(xdata)
                if p in ['VP','SVP','LVS']:
                    xdata=1.0/xdata
                    ydata=np.log(ydata)
                plt.plot(xdata,ydata,label=c[cindex[i]].Name)
            if p in ['VP','SVP','LVS']:
                plt.ylabel('ln(' + p +')')
                plt.xlabel('1/T')
            else:
                plt.ylabel(p)
                plt.xlabel('T')
            plt.title('Temperature Behavior of ' + p)
            plt.legend(loc=(1.04, 0))
        plt.show()
 
 