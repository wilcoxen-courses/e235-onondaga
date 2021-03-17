#! /bin/python3
#  Spring 2020 (PJW)

import pandas as pd
import matplotlib.pyplot as plt

#
#  Read the geocodes data
#

geocodes = pd.read_csv('state-geocodes.csv',dtype=str)
geocodes = geocodes.set_index('Name')

#
#  Read the population and income data
#
                       
state_data = pd.read_csv('state-data.csv',index_col='name')

#%%
#
#  Merge the geocode data into the state_data dataframe
#

for col in geocodes.columns:
    state_data[col] = geocodes[col]

#%%
#
#  Group by region
#

by_reg = state_data.groupby('Region') 

print( by_reg )

#
#  Grab the populations and sum them
#

reg_pop = by_reg['pop'].sum()/1e6

print( reg_pop )

#%%
#
#  Simple plot
#

plt.figure()
ax = reg_pop.plot.bar()

#%%
#
#  Population by division
#

by_div = state_data.groupby('Division') 

div_pop = by_div['pop'].sum()/1e6

#%%
#
#  Rename the index values
#

div_names = {
    '1':'New England',
    '2':'Middle Atlantic',
    '3':'East North Central',
    '4':'West North Central',
    '5':'South Atlantic',
    '6':'East South Central',
    '7':'West South Central',
    '8':'Mountain',
    '9':'Pacific'
    }

div_pop = div_pop.rename(index=div_names)

print( div_pop )

#%%
#
#  Plot a nicer figure
#

plt.figure()
ax = div_pop.plot.barh()
ax.set_xlabel('Millions')
ax.set_title('Population')
