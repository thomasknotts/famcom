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
# read_compound.py                                                          #
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
This module is part of famcom. It read the data in a .famcom file into
a variable of class compound.

    compound   a class that holds the information for each compound
    tprop      a class holding the information for a temperature-dependent
                 property
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
        self.prop=None          # property
        self.tmin=float("nan")  # min temp of correlation
        self.tmax=float("nan")  # max temp of correlation
        self.eq=float("nan")    # correlation eqation number
        self.c=np.array([])
        
# The class to hold the compound information
class compound:
    def __init__(self):
        self.name=None
        self.ChemID=None
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
            key=linetext[0]
            val=linetext[1:]
            # Place the key and value into the dictionary
            data[key]=val
        #MWget=data.get('MW')
        #print(MWget)
        #print(isnumber(MWget[0]))
        #if (isnumber(MWget[0])): self.MW=float(MWget[0])
        self.name=data.get('Name')[0]
        self.ChemID=int(data.get('ChemID')[0])
        self.MW=float(data.get('MW')[0])
        self.TC=float(data.get('TC')[0])
        self.PC=float(data.get('PC')[0])
        self.VC=float(data.get('VC')[0])
        self.ZC=float(data.get('ZC')[0])
        self.MP=float(data.get('MP')[0])
        self.TPT=float(data.get('TPT')[0])
        self.TPP=float(data.get('TPP')[0])
        self.NBP=float(data.get('NBP')[0])
        self.LVOL=float(data.get('LVOL')[0])
        self.HFOR=float(data.get('HFOR')[0])
        self.GFOR=float(data.get('GFOR')[0])
        self.ENT=float(data.get('ENT')[0])
        self.HSTD=float(data.get('HSTD')[0])
        self.GSTD=float(data.get('GSTD')[0])
        self.SSTD=float(data.get('SSTD')[0])
        self.HFUS=float(data.get('HFUS')[0])
        self.HCOM=float(data.get('HCOM')[0])
        self.ACEN=float(data.get('ACEN')[0])
        self.RG=float(data.get('RG')[0])
        self.SOLP=float(data.get('SOLP')[0])
        self.DM=float(data.get('DM')[0])
        self.VDWA=float(data.get('VDWA')[0])
        self.VDWV=float(data.get('VDWV')[0])
        self.RI=float(data.get('RI')[0])
        self.FP=float(data.get('FP')[0])
        self.FLVL=float(data.get('FLVL')[0])
        self.FLTL=float(data.get('FLTL')[0])
        self.FLVU=float(data.get('FLVU')[0])
        self.FLTU=float(data.get('FLTU')[0])
        self.AIT=float(data.get('AIT')[0])
        self.HSUB=float(data.get('HSUB')[0])
        self.PAR=float(data.get('PAR')[0])
        self.DC=float(data.get('DC')[0])
        
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
        if self.coeff['LDN'].eq == 116 or self.coeff['LDN'].eq == 119: t = 1-t/self.TC
        return(eq.eq(t,self.coeff['LDN'].c,self.coeff['LDN'].eq))
    
    def SDN(self,t):
        return(eq.eq(t,self.coeff['SDN'].c,self.coeff['SDN'].eq))
    
    def ICP(self,t):
        return(eq.eq(t,self.coeff['ICP'].c,self.coeff['ICP'].eq))
    
    def LCP(self,t):
        if self.coeff['LCP'].eq == 114 or self.coeff['LCP'].eq == 124: t = 1-t/self.TC
        return(eq.eq(t,self.coeff['LCP'].c,self.coeff['LCP'].eq))
    
    def SCP(self,t):
        return(eq.eq(t,self.coeff['SCP'].c,self.coeff['SCP'].eq))
    
    def HVP(self,t):
        if self.coeff['HVP'].eq == 106: t = t/self.TC
        return(eq.eq(t,self.coeff['HVP'].c,self.coeff['HVP'].eq))
    
    def SVR(self,t):
        return(eq.eq(t,self.coeff['SVR'].c,self.coeff['SVR'].eq))
    
    def ST(self,t):
        if self.coeff['ST'].eq == 106: t = t/self.TC
        return(eq.eq(t,self.coeff['ST'].c,self.coeff['ST'].eq))
    
    def LTC(self,t):
        if self.coeff['LTC'].eq == 123: t = 1-t/self.TC
        return(eq.eq(t,self.coeff['LTC'].c,self.coeff['LTC'].eq))
    
    def VTC(self,t):
        return(eq.eq(t,self.coeff['VTC'].c,self.coeff['VTC'].eq))
    
    def STC(self,t):
        return(eq.eq(t,self.coeff['STC'].c,self.coeff['STC'].eq))
    
    def VP(self,t):
        return(eq.eq(t,self.coeff['VP'].c,self.coeff['VP'].eq))
    
    def SVP(self,t):
        return(eq.eq(t,self.coeff['SVP'].c,self.coeff['SVP'].eq))
    
    def LVS(self,t):
        return(eq.eq(t,self.coeff['LVS'].c,self.coeff['LVS'].eq))
    
    def VVS(self,t):
        return(eq.eq(t,self.coeff['VVS'].c,self.coeff['VVS'].eq))
        
def cgraph(c,p):
    # check if `c` is a list
    if type(c) != list:
        print('Graphing requires a list of compound objects which was not supplied.')
        #return(False)
    # sort c on MW
    c.sort(key=lambda x: x.MW)
    # Determine the index of the compounds in `c` have data for property `p`
    cindex=[i for i, x in enumerate(c) if not math.isnan(getattr(x,p))]
    
    if not cindex: # only graph if data are present
        print('No data for ' + p + ' were found in the supplied files.')
        #return(False)
    else:
        names=[c[i].name for i in cindex]
        xdata=[c[i].MW for i in cindex]
        ydata=[getattr(c[i],p) for i in cindex]
        plt.plot(xdata,ydata,'o')
        plt.ylabel(p)
        plt.xlabel('MW')
        plt.title(p + ' vs MW')
        plt.show()
        print(names)
        
def tgraph(c,p):
    # check if `c` is a list
    if type(c) != list:
        print('Graphing requires a list of compound objects which was not supplied.')
        #return(False)
    # sort c on MW
    c.sort(key=lambda x: x.MW)
    # Determine the index of the compounds in `c` have data for property `p`
    cindex=[i for i, x in enumerate(c) if not math.isnan(x.coeff[p].eq)]
    
    if not cindex: # only graph if data are present
        print('No data for ' + p + ' were found in the supplied files.')
        #return(False)
    else:
        names=[c[i].name for i in cindex]  
        for i in range(len(cindex)):
            xdata=np.linspace(c[cindex[i]].coeff[p].tmin, c[cindex[i]].coeff[p].tmax, 50)
            yf=getattr(c[cindex[i]],p)
            ydata=yf(xdata)
            if p in ['VP','SVP','LVS']:
                xdata=1.0/xdata
                ydata=np.log(ydata)
            plt.plot(xdata,ydata,label=c[cindex[i]].name)
        if p in ['VP','SVP','LVS']:
            plt.ylabel('ln(' + p +')')
            plt.xlabel('1/T')
        else:
            plt.ylabel(p)
            plt.xlabel('T')
        plt.title('Temperature Behavior of ' + p)
        plt.legend()
        plt.show()