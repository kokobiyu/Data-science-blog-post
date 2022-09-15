#!/usr/bin/env python
# coding: utf-8

# # Load Library and Data

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from IPython import display
import seaborn as sb

get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv("ds_salaries.csv")
df.head()


# In[2]:


df.shape


# In[3]:


df.info()


# # Data Wrangling

# In[42]:


us = df[df['company_location']== 'US']
top10 = us['job_title'].value_counts()[:10]

plt.figure(figsize = (9,5))
#plot for first chart
sb.barplot(x = top10.index.values, y = top10)
#adding text on the bar
for i in range (top10.shape[0]): 
    count = top10[i]
    plt.text(i, count-0.5, count, ha = 'center', va='top', color = 'black', fontsize = 14)

#customizing chart
plt.title('Top 10 Job Titles in US', fontsize = 15)
plt.xlabel(' ')
plt.ylabel('Frequency', fontsize = 15)
plt.xticks(rotation=-30, ha ='left', fontsize = 14);


# # Plotting

# In[17]:


#filtering data
salary = df[['experience_level', 'job_title','salary_in_usd']]
da = salary.query('job_title.str.contains("Data Analyst")', engine = 'python').drop
de = salary.query('job_title.str.contains("Data Engineer")', engine = 'python').drop(41) #dropping suspicious data
ds = salary.query('job_title.str.contains("Data Scientist")', engine = 'python')


# making new dataframe

# In[18]:


en = ds[ds['experience_level']== 'EN'].groupby(['job_title']).mean().reset_index()
mi = ds[ds['experience_level']== 'MI'].groupby(['job_title']).mean().reset_index()
se = ds[ds['experience_level']== 'SE'].groupby(['job_title']).mean().reset_index()
ex = ds[ds['experience_level']== 'EX'].groupby(['job_title']).mean().reset_index()

en.insert(1, column = 'level', value = 'Entry')
mi.insert(1, column = 'level', value = 'Junior')
se.insert(1, column = 'level', value = 'Senior')
ex.insert(1, column = 'level', value = 'Executive')
    
DataFrame = [en, mi, se, ex] 
dsm = pd.concat(DataFrame).drop_duplicates().reset_index(drop=True)
dsm = dsm.groupby(['level']).mean().reset_index()
dsm.insert(0,column="title", value="Data Scientist")

en = de[de['experience_level']== 'EN'].groupby(['job_title']).mean().reset_index()
mi = de[de['experience_level']== 'MI'].groupby(['job_title']).mean().reset_index()
se = de[de['experience_level']== 'SE'].groupby(['job_title']).mean().reset_index()
ex = de[de['experience_level']== 'EX'].groupby(['job_title']).mean().reset_index()


en.insert(1, column = 'level', value = 'Entry')
mi.insert(1, column = 'level', value = 'Junior')
se.insert(1, column = 'level', value = 'Senior')
ex.insert(1, column = 'level', value = 'Executive')

DataFrame = [en, mi, se, ex] 
dem = pd.concat(DataFrame).drop_duplicates().reset_index(drop=True)
dem = dem.groupby(['level']).mean().reset_index()
dem.insert(0,column="title", value="Data Engineer")

en = da[da['experience_level']== 'EN'].groupby(['job_title']).mean().reset_index()
mi = da[da['experience_level']== 'MI'].groupby(['job_title']).mean().reset_index()
se = da[da['experience_level']== 'SE'].groupby(['job_title']).mean().reset_index()
ex = da[da['experience_level']== 'EX'].groupby(['job_title']).mean().reset_index()

en.insert(1, column = 'level', value = 'Entry')
mi.insert(1, column = 'level', value = 'Junior')
se.insert(1, column = 'level', value = 'Senior')
ex.insert(1, column = 'level', value = 'Executive')

DataFrame = [en, mi, se, ex] 
dam = pd.concat(DataFrame).drop_duplicates().reset_index(drop=True)
dam = dam.groupby(['level']).mean().reset_index()
dam.insert(0,column="title", value="Data Analyst")

print(dam)
print(dem)
print(dsm)


# In[19]:


salary2 = [dam,dem,dsm]
new_df = pd.concat(salary2)
new_df


# In[20]:


plt.figure(figsize = (10,6))

#plot the second bar
sb.barplot(data = new_df, x = 'title', y = 'salary_in_usd', hue = 'level', hue_order = ['Entry', 'Junior', 'Senior', 'Executive'])

#customizing chart
plt.title('Top 3 Job by Experience L', fontsize = 15)
plt.xlabel(" ")
plt.ylabel("Salary (AVG)", fontsize = 14)
plt.grid(axis = 'y')
plt.xticks(fontsize = 14)
plt.show();


# In[11]:


#data wrangling third chart
w2020 = df.loc[(df['work_year'] == 2020)]
w2021 = df.loc[(df['work_year'] == 2021)]
w2022 = df.loc[(df['work_year'] == 2022)]
hist_data = [w2020['salary_in_usd'],w2021['salary_in_usd'],w2022['salary_in_usd']]
group_labels = ['2020 salary','2021 salary','2022 salary']
colors = ['white','red','blue']

#making datframe for third chart
year_salary = pd.DataFrame(columns=['2020','2021','2022'])
year_salary['2020'] = w2020.groupby('work_year').mean('salary_in_usd')['salary_in_usd'].values
year_salary['2021'] = w2021.groupby('work_year').mean('salary_in_usd')['salary_in_usd'].values
year_salary['2022'] = w2022.groupby('work_year').mean('salary_in_usd')['salary_in_usd'].values
year_salary.values.tolist()[0]


# In[12]:


x = year_salary.columns
y = year_salary.values.tolist()[0]

plt.figure(figsize = (8,6))

#plot third chart
fig2 = sb.barplot(x = x, y = y, palette = ['yellow', 'orangered', 'dodgerblue'])
#adding text to the bar
fig2.bar_label(fig2.containers[0], label_type='edge', labels = np.round([num/1000 for num in y], 3), padding = -20, fontsize = 15)

#customizing chart
fig2.margins(y=0.2)

plt.xticks(fontsize = 18)
plt.title('Average Salary by Work Year', fontsize = 20)
("")


# In[ ]:




