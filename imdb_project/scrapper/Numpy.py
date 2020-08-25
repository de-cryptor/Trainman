#!/usr/bin/env python
# coding: utf-8

# In[139]:


import lxml
import re
import numpy as np
import pandas as pd
import bs4
from bs4 import BeautifulSoup
import requests


# In[140]:


url = "https://www.imdb.com/chart/top/"


# In[141]:


request = requests.get(url)


# In[142]:


soup_data = BeautifulSoup(request.text,'html.parser')


# In[143]:


soup_data.title.text


# In[144]:


movies = soup_data.findAll('td',{'class':"titleColumn"})
movies


# In[145]:


m = movies[0].a
#soup_data = BeautifulSoup(movies[0].text,'html.parser')
#soup_data
link = m.get('href')
link


# In[146]:


movie_link = "https://www.imdb.com" + link


# In[147]:


movie_link


# In[158]:


movie_request  = requests.get(movie_link)
movie_data = BeautifulSoup(movie_request.text,'html.parser')
movie_data


# In[159]:


movie_data = movie_data.find('script',{'type':"application/ld+json"})


# In[166]:


print(movie_data)


# In[195]:


movie_data
#m = BeautifulSoup(movie_data,'html.parser')


# In[198]:


import json
print(len(str(movie_data)))
m = str(movie_data)[35:-9]
#print(m)
data = json.loads(m)
print(data['name')




