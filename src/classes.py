# classes is part of famcom for comparing DIPPR compounds.                  #
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
import sys, os, string

def isnumber(s):
    try:
        float(s)
        return(True)
    except ValueError:
        return(False)

# The class for each tdep property
class tprop:
    def __init__(self):
        self.tmin=float("nan")  # min temp of correlation
        self.tmax=float("nan")  # max temp of correlation
        self.eq=float("nan")    # correlation eqation number
        self.a=float("nan")     # a coefficient of correlation
        self.b=float("nan")     # b coefficient of correlation
        self.c=float("nan")     # c coefficient of correlation
        self.d=float("nan")     # d coefficient of correlation
        self.e=float("nan")     # e coefficient of correlation
        self.f=float("nan")     # f coefficient of correlation
        self.g=float("nan")     # g coefficient of correlation

        
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
        self.LDN=tprop()
        self.SDN=tprop()
        self.ICP=tprop()
        self.LCP=tprop()
        self.SCP=tprop()
        self.HVP=tprop()
        self.SVR=tprop()
        self.ST=tprop()
        self.LTC=tprop()
        self.VTC=tprop()
        self.VP=tprop()
        self.SVP=tprop()
        self.LVS=tprop()
        self.VVS=tprop()
    #@classmethod
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