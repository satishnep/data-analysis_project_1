#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import python libraries

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[15]:


dataset = pd.read_csv("C:\\Users\\Dell\\Desktop\\new project_1\\Diwali Sales Data.csv",  encoding= 'unicode_escape')


# In[16]:


dataset = pd.read_csv("C:\\Users\\Dell\\Desktop\\new project_1\\Diwali Sales Data.csv",  encoding= 'unicode_escape')


# In[17]:


dataset.shape


# In[19]:


dataset.head(10)


# In[20]:


dataset.info()


# In[23]:


#drop unrelated/blank columns
dataset.drop(['Status', 'unnamed1'], axis=1, inplace=True)


# In[24]:


dataset.isnull() .sum()


# In[25]:


dataset.dropna(inplace = True)


# In[26]:


# change data type
dataset['Amount'] = dataset['Amount'].astype('int')


# In[28]:


# check data type
dataset['Amount'].dtypes


# In[29]:


dataset.columns


# In[30]:


#rename column
dataset.rename(columns= {'Marital_Status':'Shaadi'})


# In[31]:


# describe() method returns description of the data in the DataFrame (i.e. count, mean, std, etc)
dataset.describe()


# In[32]:


# use describe() for specific columns
dataset[['Age', 'Orders', 'Amount']].describe()


# # Exploratory Data Analysis

# # Gender

# In[33]:


# plotting a bar chart for Gender and it's count

ax = sns.countplot(x = 'Gender',data = dataset)

for bars in ax.containers:
    ax.bar_label(bars)


# In[34]:


# plotting a bar chart for gender vs total amount

sales_gen = dataset.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)


# # Age

# In[35]:


ax = sns.countplot(data = dataset, x = 'Age Group', hue = 'Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[36]:


# Total Amount vs Age Group
sales_age = dataset.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)


# In[37]:


# total number of orders from top 10 states

sales_state = dataset.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data = sales_state, x = 'State',y= 'Orders')


# In[39]:


ax = sns.countplot(data = dataset, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[40]:


sales_state = dataset.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# # occp

# In[41]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = dataset, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[42]:


sales_state = dataset.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# # product

# In[43]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = dataset, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[44]:


sales_state = dataset.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# In[45]:


sales_state = dataset.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[46]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
dataset.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# # conclusion

# # Married women age group 26-35 yrs from UP, Maharastra and Karnataka working in IT, 
# Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronics category
# 

# In[ ]:




