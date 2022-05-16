#!/usr/bin/env python
# coding: utf-8

# ### Welcome to the Airbnb Mini Practice Project
# 
# Throughout this unit on Python Data Analytics, you'be been introduced the the following powerful libraries:
# 
# <li> Matplotlib </li>
# <li> Seaborn </li>
# <li> Pandas </li> 
#     
# Each of these libraries will enhance your data analysis capabilities.
# 
# We've created this challenging exercise to reinforce your understanding of how these libraries work. 
# 
# Please note, there is a particular emphasis on the Pandas Library. This is the most critical Python library for data analytics. You'll see many similarities between Pandas and Pivot Tables!
#     
# <b> The most important thing you can do to build confidence with Python is to practice programming, all the time. This way you will build muscle memory. Don't simply copy the code you've written previously. Write it again and again so you store it in your memory. </b> 
# 
# <b> As this is a practice exercise, we've included a copy of what the outputs *should* look like for the majority of the questions to give you some guidance. </b>
# 
# <H3>  Time to get started! </H3>

# Import the airbnb_2.csv file.
# 
# Once you do this, you can start your analysis.
# 
# <b> Don't forget to import the libraries you need to read .csv files! </b> 
# 
# 

# ### Step 1: <span style="color:green">Import Libraries</span> 
# <b> Put your code in the box below. </b>
# 

# In[11]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# ### Step 2: <span style="color:green">Import the Airbnb Dataset</span> 

# Now that you have the Pandas Libraries imported, it's time to import the Airbnb dataset.
# 
# <b> i) Import the Airbnb dataset.
# 
# ii) Use .info() function to better understand the variables inside your dataset.
# <p>    
# 
# <b> Put your code in the box below </b>

# In[15]:


airbnb = pd.read_csv('/Users/jakeclement/Documents/airbnb_2.csv', index_col=0)


# In[16]:


print(airbnb.info())


# ### Step 3: <span style="color:green">Exploring your data with Pandas</span> 
# 
# The rest of these questions will have you focus on using the following Pandas Skills:
# 
# <li> Subsetting a Pandas DataFrame using [] and boolean operators </li>
# <li> Summing up records with value_counts()</li>
# <li> Creating calculated fields </li>
# <li> Group By in Pandas </li> 
# <li> Creating Bar Plots with Matplotlib</li> 
# 
# 

# <b> i)  Please count how many Airbnb listings are in each of the 5 Neighbourhood Groups (Manhattan, Brooklyn, Queens, Bronx, Staten Island), then identify which Neighbourhood Groups have the greatest number of Airbnb listings. </b>
# <p>
#     <b> Put your code in the box below </b>

# In[17]:


airbnb["neighbourhood_group"].value_counts()


# We want to focus our attention on the 3 most popular Neighbourhood Groups, by listing volume.
# 
# <b> ii) Calculate the percentage of Airbnb listings that each Neighbourhood Group contains. </b>
# 
# See this resource for more details <a href = https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.value_counts.html>. </a>
# 
# <b> Put your code in the box below. </b>

# In[18]:


airbnb["neighbourhood_group"].value_counts(normalize= True, ascending= False)


# <b> iii) Create a new calculated field called Revenue and place this into the Airbnb DataFrame. This is to be calculated by using the Price Column x Number_Of_Reviews Columns </b>
# 
# <b> Put your code in the box below </b>

# In[21]:


airbnb["Revenues"]= airbnb["price"] * airbnb["number_of_reviews"]


# <b> iv) Create a Bar Plot that shows which Neighbourhood Group has the highest average revenues. In order to best
# calculate this, you'd want to consider how you can use the .groupby() syntax to assist you! </b>
# 
# If you're stuck, we recommend you go back to this <a href = https://learn.datacamp.com/courses/manipulating-dataframes-with-pandas> DataCamp link</a>. Specifically, Chapter 4 which covers how GROUP BY is used in Pandas.
# 
# <b> Put your code in the box below. </b>

# In[45]:


airbnb["Revenues"].groupby(airbnb["neighbourhood_group"]).sum().sort_values(ascending=False).plot(kind='bar')#.plot(x= "neighbourhood_group", kind='bar')


# <h3> <span style="color:green">Challenge Questions</span> </h3>

# <b> V) Filter the Airbnb DataFrame to include only the Neighbourhood Groups Manhattan, Brooklyn, and Queens. 
#     
# Then, identify the top 3 Revenue Generating Neighborhoods within each of the 3 Neighbourhood_Groups. This should give us 9 Overall Rows: 3 of the top generating neighbourhoods within each of the 3 Neighbourhood_Groups </b>
# 
# This is a tricky question that will *test* your group-by skills.
# 
# We recommend you consider the following:
# 
#     condition1 = someDataFrame['someColumn']=='someCondition'
#     condition2 = someDataFrame['someColumn']=='someCondition'
#     
#     Step One - Filter the DataFrame using the Conditions
#     filtered_dataframe = someDataFrame[condition1 OR condition 2] 
#     #Hint: You might want to look up what the OR symbol in Python is represented as in operator form (i.e. AND (&) )
#     
#     Step Two - Group the Data by Neighbourhood_Group and Neighbourhood. Don't forget you're looking to SUM up the Revenues.
#     
#     The remaining steps we recommend you think very carefully about.
#     
#     You might want to make use of the .reset_index(inplace=True) function to help reset the indexes in 
#     your Grouped Up Dataframe...!
#     
#     
# <b> Put your code in the box below. </b>

# In[67]:


condition1 = airbnb['neighbourhood_group'] == "Brooklyn"
condition2 = airbnb['neighbourhood_group'] == "Manhattan"
condition3 = airbnb['neighbourhood_group'] == "Queens"

df = airbnb[condition1|condition2|condition3]

df2 = airbnb[airbnb['neighbourhood_group'].isin(['Manhattan','Brooklyn','Queens'])]
df3 = df2.groupby(['neighbourhood_group', 'neighbourhood']).sum()['Revenues'].sort_values(ascending= False).reset_index()


b = df3[df3['neighbourhood_group'] == "Brooklyn"].head(3)
m = df3[df3['neighbourhood_group'] == "Manhattan"].head(3)
q = df3[df3['neighbourhood_group'] == "Queens"].head(3)

pd.concat([b,m,q],axis=0)


# <b> VI) Filter the Airbnb Dataframe to include only the top 3 Neighbroos within each neighbourhood_group. 
#     
# After doing this, identify the top average revenue-generating room-type for each of the nine neighbourhoods and plot this  in a Bar Chart.</b>
# 
# This is a tricky question that will *test* your group-by skills. Think back to the previous question and how you approached this; you can approach this in a similar manner. 
# 
# We recommend you consider the following:
# 
#     condition1 = someDataFrame['someColumn']=='someCondition'
#     condition2 = someDataFrame['someColumn']=='someCondition'
#     
#     Step One - Filter the Dataframe using the Conditions
#     filtered_dataframe = someDataFrame[condition1 OR condition 2] 
#     #Hint: You might want to look up what the OR symbol in Python is represented as in operator form (i.e. AND (&) )
#     
#     Step Two - Group the Data by Neighbourhood_Group and Neighbourhood. Don't forget you're looking to SUM up the Revenues.
#     
#     The remaining steps we recommend you think very carefully about.
#     
#     You might want to make use of the .reset_index(inplace=True) function to help reset the indexes in 
#     your Grouped Up Dataframe...!
#     
#     
#  <b> Put your code in the box below. </b>      

# In[145]:


df4= airbnb[airbnb['neighbourhood'].isin(['Williamsburg', 'Bedford-Stuyvesant', 'Bushwick', 'Harlem', "Hell's Kitchen", 'East Village', 'Astoria', 'Long Island City', 'Flushing'])] 
df5= df4.groupby(['neighbourhood_group', 'neighbourhood', 'room_type']).sum()['Revenues'].sort_values(ascending= False).reset_index()
df5.head(29)
c= df5[df5['neighbourhood'] == 'Williamsburg'].head(1)
d= df5[df5['neighbourhood'] == 'Bedford-Stuyvesant'].head(1)
e= df5[df5['neighbourhood'] == 'Bushwick'].head(1)
f= df5[df5['neighbourhood'] == 'Harlem'].head(1)
g= df5[df5['neighbourhood'] == "Hell's Kitchen"].head(1)
h= df5[df5['neighbourhood'] == 'East Village'].head(1)
i= df5[df5['neighbourhood'] == 'Astoria'].head(1)
j= df5[df5['neighbourhood'] == 'Long Island City'].head(1)
k= df5[df5['neighbourhood'] == 'Flushing'].head(1)

df6= pd.concat([c,d,e,f,g,h,i,j,k], axis=0)
df6.head(9)
ax= sns.catplot(data=df6, x='neighbourhood', y='Revenues', hue='room_type', kind='bar')
ax.set_xticklabels(rotation=90)


# In[ ]:




