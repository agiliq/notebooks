
# coding: utf-8

# In[1]:

import pandas as pd


# In[2]:

df = pd.read_csv("./buildings.csv")
df.head()


# In[3]:

df.describe()


# We want to get the first 10 results
# `SELECT * FROM buildings LIMIT 10`
#

# In[4]:

df[:10]


# Get only the City and Building name
# `SELECT city, building FROM buildings LIMIT 3`

# In[5]:

df[["City", "Building"]][:3]


# What are the three oldest buildings in our data
# `SELECT city, building, built FROM buildings ORDER BY built LIMIT 3`
#

# In[ ]:


# In[6]:

df.sort("Built")[["City", "Building", "Built"]][:3]


# What the the three highest buildings?
# `SELECT city, building, height FROM buildings ORDER BY height desc LIMIT 3`

# In[7]:

df.sort("Height", ascending=False)[["City", "Building", "Height"]][:3]


# What are the three tallest buildings in Dubai?
#
#     SELECT city, building, height FROM buildings
#     WHERE city='Dubai' ORDER BY height LIMIT 3;
#

# In[9]:

df[df["City"] == 'Dubai'].sort("Height", ascending=False)[:3]


# What are the five tallest buildings in Dubai or Chicago?
#
#     SELECT * FROM buildings WHERE city='Dubai'
#     or city=='Chicago' ORDER BY height desc LIMIT 5;

# In[10]:

df[(df["City"] == 'Dubai') | (df["City"] == "Chicago")].sort("Height", ascending=False)[:5]


# Among the buildings built in 20th century, which has the most floors?
#
#     SELECT * FROM buildings WHERE built < 2000
#     ORDER BY floors DESC LIMIT 1;

# In[11]:

df[df["Built"] < 2000].sort("Floors", ascending=False)[:1]


# Among the buildings built in 20th century, which is the tallest?
#
#     SELECT * FROM buildings WHERE built < 2000
#     ORDER BY height DESC LIMIT 1;

# In[12]:

df[df["Built"] < 2000].sort("Height", ascending=False)[:1]


# How many different countries and cities do we have in our data?
#
#     SELECT COUNT(DISTINCT(country)) FROM buildings;
#     SELECT COUNT(DISTINCT(city)) FROM buildings;

# In[13]:

len(df["Country"].unique())
len(df["City"].unique())


# Which cities make an apperance in top 20 tallest building list?
#
#     SELECT DISTINCT(city) from
#     (SELECT * FROM buildings ORDER BY height DESC LIMIT 20);
#

# In[15]:

df[:20].sort("Height", ascending=False)["City"].unique()


# How many appearances dos each conutry make in a top 100 list?
#
#     SELECT country, COUNT(country) AS building_count
#     FROM
#     (select * from buildings order by height limit 100)
#     GROUP BY country
#     ORDER BY building_count DESC;
#
#

# In[16]:

df[:100]["Country"].value_counts()


# What is the average floors and average height, per country.
#
#     SELECT country, AVG(floors), AVG(height) from
#         (SELECT * FROM buildings ORDER BY height DESC LIMIT 100)
#         GROUP BY country;

# In[17]:

df.sort("Height")[:100].groupby("Country").mean()[["Floors", "Height"]]


# What is the average floors and average height, per country, sorted by height
#
#     SELECT country, AVG(floors) as avg_floor, AVG(height) as avg_height from
#         (SELECT * FROM buildings ORDER BY height DESC LIMIT 100)
#         GROUP BY country
#         ORDER by avg_height DESC;

# In[ ]:


# In[18]:

df[:100].groupby("Country").mean()[["Floors", "Height"]].sort("Height", ascending=False)


# What years were the buildings completed?
#
#     SELECT built, count(built) FROM buildings GROUP BY built;

# In[19]:

df.groupby("Built").count()["Building"]


# In[ ]:


# In[ ]:
