#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 17:53:50 2021

@author: pallavi
"""

import izhikevich_cells as izh

class cCell(izh.izhCell):
    def __init__(self,stimVal):
        super().__init__(stimVal)
        self.celltype = "Chattering"
        self.C = 50
        #self.vr = -60
        #self.vt = -40
        self.k = 1.5
        #self.a = 0.03
        self.b = 1
        self.c = -40
        self.d = 150
        self.vpeak = 25
        
myCell = cCell(4000)
myCell.simulate()

if __name__=='__main__':
    izh.plotMyData(myCell)