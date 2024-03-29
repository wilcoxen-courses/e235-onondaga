"""
demo.py
Spring 2022 PJW

Demonstate features of Pandas and Matplotlib.
"""

import pandas as pd
import matplotlib.pyplot as plt

#
#  Set the default resolution for plots to 300 DPI

plt.rcParams['figure.dpi'] = 300

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
#  Copy the geocode data into the state_data dataframe aligning via the index
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

#
#  Print the total population using commas for grouping
#

tot_pop = state_data['pop'].sum()
print(f'Total population: {tot_pop:,}')

#%%
#
#  Very basic plot. First set up a blank figure and set of
#  axes (fig1 and ax1) and then draw the plot on ax1.
#

fig1, ax1 = plt.subplots()
reg_pop.plot.bar(title='Population',ax=ax1)
ax1.set_ylabel("Millions")

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
#  Plot a nicer figure. Sort bars by length from largest to smallest. The bars
#  will be plotted starting from the top of the dataframe, so counterintuitively
#  this puts the longest bars at the bottom of the figure.
#

fig2, ax2 = plt.subplots()

div_pop = div_pop.sort_values(ascending=False)
div_pop.plot.barh(title='Population',ax=ax2)

#  Add some labels and titles to the Axes object ax2

ax2.set_xlabel('Millions')

#  Clean up the layout and save it

fig2.tight_layout()
fig2.savefig('figure.png')
