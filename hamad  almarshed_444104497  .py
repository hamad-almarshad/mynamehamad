#!/usr/bin/env python
# coding: utf-8

# In[35]:


import pandas as pd
import numpy as np


# In[4]:


edu = pd.read_csv("desktop/educ_figdp_1_Data.csv",
                      
                     na_values =':',
                     usecols =["TIME","GEO","Value"])
edu


# In[5]:


edu.head()


# In[6]:


edu.tail ()


# In[7]:


edu.describe()


# In[8]:


edu['Value']


# In[9]:


edu[10:14]


# In[15]:


edu.loc [90:94, ['TIME', 'GEO']]


# In[16]:


edu[edu ['Value'] > 6.5].tail()


# In[20]:


edu[edu ['Value'] . isnull()].head()


# In[21]:


edu.max(axis = 0)


# In[28]:


"pandas max function:", edu ['Value'].max()


# In[29]:


"python max function:", max(edu ['Value'] )


# In[32]:


s=edu['Value']/100
s.head()


# In[36]:


s= edu ['Value'].apply (np.sqrt)
s.head()


# In[37]:


s=edu ['Value'].apply(lambda d: d**2)
s.head()


# In[38]:


edu['ValueNorm'] = edu['Value']/edu['Value'].max()
edu.tail()


# In[45]:


edu.drop ('ValueNorm', axis = 1,  inplace = True)
edu.head ()


# In[46]:


edu = edu .append({"TIME":2000,"Value": 5.00,"GEO": 'a'},
                  ignore_index= True)
edu.tail()


# In[47]:


edu.drop (max (edu.index), axis = 0 ,  inplace = True)
edu.tail ()


# In[53]:


eduDrop = edu.drop (edu ["Value"]. isnull(),  axis = 0 )
                        eduDrop.head ()


# In[57]:


eduDrop = edu. dropna (how = 'any', subset = ["Value"])
eduDrop.head()


# In[58]:


eduFilled = edu.fillna (value = {"Value": 0})
eduFilled.head()


# In[62]:


edu.sort_values (by = 'Value', ascending = False, 
                 inplace = True)
edu.head()


# In[63]:


edu.sort_index (axis = 0, ascending = True , inplace = True )
edu.head()


# In[64]:


group = edu [["GEO", "Value"]].groupby('GEO').mean()
edu.head()


# In[75]:


filtered_data = edu [edu["TIME"] > 2005 ]
pivedu = pd.pivot_table (filtered_data, values = 'Value',
                       index = ['GEO'],
                       columns =['TIME'])
pivedu.head ()


# In[78]:


pivedu.loc[['Spain', 'Portugal'], [2006,2011]]


# In[84]:


pivedu = pivedu.drop([
    'Euro area (13 countries)',
    'Euro area (15 countries)',
    'Euro area (17 countries)',
    'Euro area (18 countries)',
    'European Union (25 countries)',
    'European Union (27 countries)',
    'European Union (28 countries)'],
    axis = 0)

pivedu =pivedu.rename(index ={'Germany (until 1990 former territory of The FRG )':'Germany'})
pivedu =pivedu.dropna()
pivedu.rank(ascending = False , method ='first').head()


# In[98]:


totalsum = pivedu.sum(axis =1)
totalsum.rank(ascending = False ,method ='dense')
totalsum.sort_values()


# In[96]:


totalSum = pivedu.sum (axis = 1 )

totalSum.plot (kind = 'bar',  style = 'b', alpha = 0.4,
               title = "Total Values for Conutry")


# In[97]:


my_colors = ['b', 'r', 'g', 'y', 'm', 'c',]
ax = pivedu.plot (kind = 'barh', 
                  stacked = True,
                  color = my_colors)
ax.legend(loc = 'center left', bbox_toanchor = (1, .5))

