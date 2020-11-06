#!/usr/bin/env python
# coding: utf-8

# # PANDAS FOUNDATION

# ## INGESTION AND INSPECTION

# Importing the libraries

# In[7]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[8]:


worldpopulation=pd.read_csv ('C://Users//paul//Documents//STUTERN PANDAS PROJECT//World Bank World Development Indicators.csv')


# In[9]:


worldpopulation


# ## Inspecting data (Head, Tail)

# In[10]:


worldpopulation.head()


# In[11]:


worldpopulation.tail()


# ## Answer;   
# for the first and last row ;First: 1960, 92495902.0; Last: 2014, 15245855.0.

# ## NumPy and pandas working together

# ###### Creating  np_vals (array of DataFrame values )

# In[12]:


np_vals = worldpopulation[['Total Population', 'Urban population (% of total)']].values


# In[13]:


np_vals


# Creating Log 10 values

# In[14]:


np_valslog10 = np.log10(np_vals)


# In[15]:


np_valslog10


# ## DataFrame data types

# In[16]:


worldpopulation.info()


# ## Zip lists to build a DataFrame

# In[17]:


countries = [ 'United States', 'Russia', 'Germany'] 


# In[18]:


total = [1127, 726, 578]


# In[19]:


list_keys = [ 'countries', 'total']


# In[20]:


list_values = [countries, total]


# In[21]:


zipped = list(zip(list_keys, list_values))


# In[22]:


zipped


# In[23]:


data = dict(zipped)


# In[24]:


df = pd.DataFrame(data)
                     


# In[25]:


print(df)


# # Labeling your data

# In[26]:


df=pd.read_csv ('C://Users//paul//Documents//STUTERN PANDAS PROJECT//Billboards.csv')


#  Create a list of new column labels with 'year', 'artist', 'song', 'chart weeks', and assign it to list_labels. Assign your list of labels to df.columns.
# 

# In[27]:


df.columns= ['year','artist','song', 'chart weeks']


# In[28]:


df


# ## Building DataFrames with broadcasting

# Make a string object with the value 'PA' and assign it to state.
# Construct a dictionary with 2 key:value pairs: 'state':state and 'city':cities.
# Construct a pandas DataFrame from the dictionary you created and assign it to df.

# In[29]:


cities = ['city', 'city', 'city', 'city', 'city', 'city', 'city'] 


# In[30]:


data = {'city':  cities, 'state': 'PA'} 


# In[31]:


df = pd.DataFrame(data) 


# In[32]:


df


# ### Reading a flat file

# In[39]:


df_b ='C://Users//paul//Documents//STUTERN PANDAS PROJECT//World Bank World Development Indicators.csv'


# In[40]:


worldpopulation_b = pd.read_csv(df_b)


# In[41]:


worldpopulation_b


# In[42]:


# Create a list of the new column labels: new_labels
new_labels = ['country', 'country code', 'year', 'population', 'urban population as percentage of total']

# # Read in the file, specifying the header and names parameters
worldpopulation_c = pd.read_csv(df_b, header=0, names = new_labels)

# check
worldpopulation_c


# ### Delimiters, headers, and extensions

# In[49]:


# get the file path
messy = 'C://Users//paul//Documents//STUTERN PANDAS PROJECT//messy.csv'

# read the messy file as a csv
df_c = pd.read_csv(messy)


# In[50]:


# Read in the file with the correct parameters: df2
df_d = pd.read_csv(messy, delimiter=' ', header = 3, comment = '#')

#check
df_d.head()


# In[51]:


# Save the cleaned up DataFrame to a CSV file without the index
df_d.to_csv('file_clean', index=False)

# Save the cleaned up DataFrame to an excel file without the index
df_d.to_excel('clean.xlsx', index=False)


# ### Plotting series using pandas

# In[53]:


# Austin temperature data
temperature_data = 'C://Users//paul//Documents//STUTERN PANDAS PROJECT//2010 Austin weather.csv'

# read in the data set
austin = pd.read_csv(temperature_data)


# In[54]:


austin


# In[55]:


# temperature column 
temp = austin.iloc[:700, 0]

# Create a plot with color='red'
temp.plot(color = 'red')

# title
plt.title('Temperature in Austin')

# Specify the x-axis
plt.xlabel('Hours since midnight August 1, 2010')

# Specify the y-axis label
plt.ylabel('Temperature (degrees F)')

# Display the plot
plt.show()


# ### Plotting with DataFrames

# In[56]:


# lets get only the temperature column
temp = austin.iloc[:800, 0]
temp


# In[60]:


# Get just the numeric columns
austin_col = austin.iloc[0:700, 0:3]


# In[61]:


austin_col


# In[62]:


# plot all columns in same figure
austin_col.plot()


# In[63]:


# make separate subplots for each column
austin_col.plot(subplots=True)
plt.show()


# In[65]:


# plot just one columns data
austin_col['DewPoint'].plot()
plt.show()


# In[66]:


# plot two columns data
austin_col[['Temperature', 'DewPoint']].plot()
plt.show()


# # Exploratory Data Analysis
# 

# In[68]:


# lets transpose the messy data we cleaned in order to get the stock prices data
df_e = df_d.transpose()
df_e


# In[69]:


# assign the new column names
df_e.rename(columns= {0:'IBM', 1:'MSFT', 2:'GOOGLE', 3:'APPLE'}, inplace = True)

# check
df_e


# In[70]:


# Change the index column to a column series
df_e.reset_index(inplace=True)

# check
df_e


# In[71]:


# rename the index column to months
df_e.rename(columns= {'index': 'Month'}, inplace = True)

# check
df_e


# In[72]:


# delete the first row that repeats the header row
df_e.drop(0, axis=0, inplace=True)

# check
df_e


# In[74]:


# plot stock prices data
y_columns = ['APPLE', 'IBM']

# plot months against stock prices
df_e.plot(x='Month', y=y_columns)

# give the plot a title
plt.title('Monthly stock prices')

# Add the y-axis label
plt.ylabel('Price ($US)')

# display the plot
plt.show()


# In[ ]:




