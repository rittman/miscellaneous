# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 22:27:24 2016

@author: tim
"""

import postcodes as pc
from geopy.distance import vincenty

# hospital postcodes
hosps = {"Addenbrookes":"CB2 0QQ",
         "NNUH":"NR4 7UY",
         "Romford":"RM7 0AG"}

# person object including postcode and starting hospital
class person:
    def __init__(self, name, postcode, starthosp="NNUH"):
        self.name = name
        self.pc = postcode
        self.postcode = pc.get(self.pc)
        self.starthosp = starthosp
        self.petrol = 0.24  # pounds per mile
        self.totalExpenses = 0.
        
        # hospital postcodes
        self.hosps = {"Addenbrookes":"CB2 0QQ",
                 "NNUH":"NR4 7UY",
                 "Romford":"RM7 0AG",
                 "QS":"WC1N 3BG"}
        
    def dist(self):
        
        hosp = pc.get(hosps[self.starthosp])
        self.startll = (self.postcode['geo']['lat'],self.postcode['geo']['lng'])
        hospll = (hosp['geo']['lat'],hosp['geo']['lng'])
        
        self.miles = vincenty(self.startll,hospll).miles
        
    def expenses(self, hosp, months):
        commutingDays = 21 # in pounds assumption of commuting 21 days per month
        
        # calculate the distance the hospital from home
        hosp = hosp
        hosp = pc.get(self.hosps[hosp])
        hospll = (hosp['geo']['lat'],hosp['geo']['lng'])
        
        self.hospMiles = vincenty(self.startll, hospll).miles
        
        # get difference in distance between commutes
        diff = self.hospMiles - self.miles
        if diff>0:
            expenses = diff*self.petrol*commutingDays
        else:
            expenses = 0.
            
        self.totalExpenses += expenses

