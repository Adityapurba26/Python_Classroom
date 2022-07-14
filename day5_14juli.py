#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/nbaallelo.csv')


# In[2]:


df


# In[3]:


len(df)


# In[4]:


df.shape


# In[5]:


df.head()


# In[6]:


pd.set_option("display.max.columns", None)


# In[7]:


pd.set_option("display.precision", 2)


# In[8]:


df.tail()


# In[9]:


df.tail(3)


# In[10]:


df.info()


# In[11]:


df.describe()


# In[12]:


df["team_id"].value_counts()


# In[13]:


df["fran_id"].value_counts()


# In[14]:


df.loc[df["fran_id"] == "Lakers", "team_id"].value_counts()


# In[21]:


df.loc[df["team_id"] == "MNL", "date_game"]


# In[22]:


df.loc[df["team_id"] == "MNL", "date_game"].min()


# In[23]:


df.loc[df["team_id"] == "MNL", "date_game"].max()


# In[24]:


df.loc[df["team_id"] == "MNL", "date_game"].agg(("min", "max"))


# In[29]:


df.loc[df["team_id"] == "BOS", "pts"]


# In[43]:


df.loc[df["team_id"] == "MNL"] 


# In[44]:


df[(df["year_id"] > 1950) & (df["year_id"] <1980)]


# In[103]:


x= df[(df["team_id"] == "MNL" ) & (df["year_id"] > 1950) & (df["year_id"] <1980)]


# In[104]:


x


# In[116]:


x["tahun_game_id"]=x.game_id.apply(lambda a:a[-3:]) #mengaplikasian (), lamda a sebagai input a:a[:4]


# In[117]:


x


# In[49]:


revenues = pd.Series([5555, 7000, 1980])


# In[111]:


x["gabungan"]=x.lg_id + "_" + x.tahun_game_id


# In[112]:


x


# In[50]:


revenues


# In[51]:


revenues.values


# In[52]:


revenues.index


# In[53]:


city_revenues = pd.Series(
    [4200, 8000, 6500],
    index=["Amsterdam", "Toronto", "Tokyo"]
)
city_revenues


# In[54]:


city_employee_count = pd.Series({"Amsterdam": 5, "Tokyo": 8})
city_employee_count


# In[55]:


city_employee_count.keys()


# In[56]:


"Tokyo" in city_employee_count


# In[57]:


"Toyo" in city_employee_count


# In[60]:


city_revenues = pd.Series(
    [4200, 8000, 6500],
    index=["Amsterdam", "Toronto", "Tokyo"]
)
city_employee_count = pd.Series({"Amsterdam": 5, "Tokyo": 8})

city_data = pd.DataFrame({
    "revenue": city_revenues,
    "employee_count": city_employee_count
})


# In[59]:


city_data


# In[61]:


city_data.index


# In[62]:


city_data.values


# In[63]:


city_data.axes


# In[64]:


city_data.axes[0]


# In[65]:


city_data.axes[1]


# In[72]:


df.index


# In[73]:


df.axes


# In[77]:


city_data["employee_count"]==8.fillna(10, inplace = True)


# In[75]:


city_data


# In[78]:


city_data["employee_count"] = city_data["employee_count"].replace([8],10)


# In[79]:


city_data


# In[80]:


city_revenues


# In[81]:


city_revenues["Toronto"]


# In[84]:


city_revenues[1:]


# In[86]:


colors = pd.Series(
    ["red", "purple", "blue", "green", "yellow"],
    index=[1, 2, 3, 5, 8]
)
colors


# In[87]:


colors.iloc[1]


# In[88]:


colors.loc[1]


# In[92]:


colors.iloc[:]


# In[94]:


df.iloc[-1]


# In[95]:


df.loc[5555:5559, ["fran_id", "opp_fran", "pts", "opp_pts"]]


# In[96]:


df


# In[97]:


current_decade = df[df["year_id"] > 2010]
current_decade


# In[98]:


ers = df[df["fran_id"].str.endswith("ers")]
ers


# In[99]:


ers.shape


# In[101]:


df[
    (df["_iscopy"] == 0) & #df["_iscopy"] == 0 untuk hanya menyertakan entri yang bukan salinan/duplikat
    (df["pts"] > 100) &
    (df["opp_pts"] > 100) &
    (df["team_id"] == "BLB")
]


# In[102]:


df[
    (df["_iscopy"] == 0) &
    (df["team_id"].str.startswith("LA")) &
    (df["year_id"] == 1992) &
    (df["notes"].notnull())
]


# In[119]:


df.info()


# In[121]:


df.groupby("fran_id", sort=True)["pts"].sum()


# In[122]:


df[
    (df["fran_id"] == "Spurs") &
    (df["year_id"] > 2010)
].groupby(["year_id", "game_result"])["game_id"].count()


# In[123]:


df[
    (df["fran_id"] == "Warriors") &
    (df["year_id"] == 2015)
].groupby(["is_playoffs", "game_result"])["game_id"].count()


# In[124]:


nba = df.copy()


# In[126]:


#menentukan kolom baru berdasarkan yang sudah ada
nba["difference"] = df.pts - df.opp_pts
nba


# In[127]:


elo_columns = ["elo_i", "elo_n", "opp_elo_i", "opp_elo_n"]


# In[129]:


#menghapus elo_columns = ["elo_i", "elo_n", "opp_elo_i", "opp_elo_n"]
nba.drop(elo_columns, inplace=True, axis=1)
nba


# In[131]:


nba["date_game"] = pd.to_datetime(nba["date_game"])
nba


# In[133]:


#nilai unik
nba["game_location"].nunique()


# In[134]:


nba["game_location"].value_counts()


# In[136]:


nba.info()


# In[137]:


data_with_default_notes = nba.copy()


# In[138]:


data_with_default_notes["notes"].fillna(
    value="no notes at all",
    inplace=True
)
data_with_default_notes


# In[139]:


data_with_default_notes["notes"].describe()


# In[140]:


nba.describe()


# In[141]:


further_city_data = pd.DataFrame(
    {"revenue": [7000, 3400], "employee_count": [2, 2]},
    index=["New York", "Barcelona"]
)
further_city_data


# In[142]:


#menambahkan kota-kota ini ke city_data menggunakan .concat()
all_city_data = pd.concat([city_data, further_city_data], sort=False)
all_city_data


# In[143]:


city_countries = pd.DataFrame({
    "country": ["Holland", "Japan", "Holland", "Canada", "Spain"],
    "capital": [1, 1, 0, 0, 0]},
    index=["Amsterdam", "Tokyo", "Rotterdam", "Toronto", "Barcelona"]
)
city_countries


# In[145]:


cities = pd.concat([all_city_data, city_countries], axis=1, sort=False)
cities


# In[146]:


pd.concat([all_city_data, city_countries], axis=1, join="inner")


# In[148]:


countries = pd.DataFrame({
    "population_millions": [17, 127, 37],
    "continent": ["Europe", "Asia", "North America"]
}, index=["Holland", "Japan", "Canada"])
countries


# In[149]:


pd.merge(cities, countries, left_on="country", right_index=True)


# In[150]:


pd.merge(
    cities,
    countries,
    left_on="country",
    right_index=True,
    how="left"
)


# In[151]:


get_ipython().run_line_magic('matplotlib', 'inline')
nba[nba["fran_id"] == "Knicks"].groupby("year_id")["pts"].sum().plot()


# In[152]:


nba[nba["fran_id"] == "Knicks"].groupby("year_id")["pts"].sum()


# In[153]:


nba["fran_id"].value_counts().head(10).plot(kind="bar")


# In[154]:


nba["fran_id"].value_counts().head(10)


# In[155]:


cities


# In[ ]:




