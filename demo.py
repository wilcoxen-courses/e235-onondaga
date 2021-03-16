#! /bin/python3
#  Spring 2020 (PJW)

import csv
import json 
import numpy as np
from collections import defaultdict

data = [
   'date,state,pop\n',
   '02/03,IA,3106589\n',
   '02/11,NH,1327503\n',
   '02/22,NV,2839172\n',
   '02/29,SC,4834605\n',
   '03/01,AL,4841164\n',
   '03/01,AR,2968472\n',
   '03/01,CA,38654206\n',
   '03/01,CO,5359295\n',
   '03/01,ME,1329923\n',
   '03/01,MA,6742143\n',
   '03/01,MN,5450868\n',
   '03/01,NC,9940828\n',
   '03/01,OK,3875589\n',
   '03/01,TN,6548009\n',
   '03/01,TX,26956435\n',
   '03/01,UT,2948427\n',
   '03/01,VT,626249\n',
   '03/01,VA,8310301\n'
   ]

def newobj():
    new_object = {
        'states':[],
        'pops':[]}
    return new_object 

inp_reader = csv.DictReader(data)

primaries = defaultdict(newobj)

for rec in inp_reader:
    this_date = rec['date']
    this_state = rec['state']
    this_pop = rec['pop']
    
    prime_obj = primaries[this_date]
    prime_obj['states'].append( this_state )
    prime_obj['pops'].append( float(this_pop) )
    
print('\nPrimaries data object:\n')

print( json.dumps(primaries,indent=4))
    
print('\nPrimary dates and populations voting:\n')
for date in sorted(primaries):
    pop_list = primaries[date]['pops']
    state_list = " ".join(primaries[date]['states'])
    print( date, round(np.sum(pop_list)/1e6,1) )
