"""
demo.py
Spring 2022 PJW

Demonstrate features of Pandas and Matplotlib.
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

for col in state_data.columns:
    geocodes[col] = state_data[col]

#
#  Washington, DC will have missing data: it's in the geocodes list but not
#  the state data list
#

print(geocodes)

#
#  Trim to just states with data
#

merged = geocodes.dropna()
print("\nRows dropped by dropna call:",len(geocodes)-len(merged))

#%%
#
#  Group by region
#

by_reg = merged.groupby('Region')

print( by_reg )

#
#  Grab the populations and sum them
#

reg_pop = by_reg['pop'].sum()/1e6

print( reg_pop )

#
#  Print the total population using commas for grouping
#

tot_pop = merged['pop'].sum()
print(f'Total population: {tot_pop:,}')

#%%
#
#  Very basic plot. First set up a blank figure and set of
#  axes (fig1 and ax1) and then draw the plot on ax1.
#

fig, ax = plt.subplots()
reg_pop.plot.bar(title='Population',ax=ax)
ax.set_ylabel('Millions')

#%%
#
#  Population by division
#

by_div = merged.groupby('Division')

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

fig, ax = plt.subplots()

div_pop = div_pop.sort_values(ascending=False)
div_pop.plot.barh(title='Population',ax=ax)

#  Add some labels and titles to the Axes object ax2

ax.set_xlabel('Millions')

#  Clean up the layout and save it

fig.tight_layout()
fig.savefig('figure.png')
