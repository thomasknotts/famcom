# classes is part of famcom for comparing compounds in the DIPPR database.  #
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
# classes.py                                                                #
#                                                                           #
# Thomas A. Knotts IV                                                       #
# Brigham Young University                                                  #
# Department of Chemical Engineering                                        #
# Provo, UT  84606                                                          #
# Email thomas.knotts@byu.edu                                               #
# ========================================================================= #
# Version 1.0 - September 2022                                              #
# ========================================================================= #


This module is part of famcom. It defines the classes needed for program. 
The classes are below.

    compound   a class that holds the information for each compound
    tprop      a class holding the information for a temperature-dependent
                 property

# The class for each tdep property
class tprop:
    def __init__(self):
        #self.prop=prop       # property name
        self.tmin=0.0      # min temp of correlation
        self.tmax=0.0      # max temp of correlation
        self.eq=0.0        # correlation eqation number
        self.a=0.0         # a coefficient of correlation
        self.b=0.0         # b coefficient of correlation
        self.c=0.0         # c coefficient of correlation
        self.d=0.0         # d coefficient of correlation
        self.e=0.0         # e coefficient of correlation
        self.f=0.0         # f coefficient of correlation
        self.g=0.0         # g coefficient of correlation

        
# The class to hold the compound information
class compound:
    def __init__(self):
        self.name=None
        self.ChemID=None
        self.MW=0.0
        self.TC=0.0
        self.PC=0.0
        self.VC=0.0
        self.ZC=0.0
        self.MP=0.0
        self.TPT=0.0
        self.TPP=0.0
        self.NBP=0.0
        self.LVOL=0.0
        self.HFOR=0.0
        self.GFOR=0.0
        self.ENT=0.0
        self.HSTD=0.0
        self.GSTD=0.0
        self.SSTD=0.0
        self.HFUS=0.0
        self.HCOM=0.0
        self.ACEN=0.0
        self.RG=0.0
        self.SOLP=0.0
        self.DM=0.0
        self.VDWA=0.0
        self.VDWV=0.0
        self.RI=0.0
        self.FP=0.0
        self.FLVL=0.0
        self.FLVU=0.0
        self.FLTL=0.0
        self.FLTU=0.0
        self.AIT=0.0
        self.HSUB=0.0
        self.PAR=0.0
        self.DC=0.0
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
   
        
    
        
