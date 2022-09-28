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

"""
This module is part of famcom. It defines the classes needed for program. 
The classes are below.

    compound   a class that holds the information for each compound
    tprop      a class holding the information for a temperature-dependent
                 property
"""

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
    def __init__(self,name,id):
        self.name=name
        self.ChemID=int(id)
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
