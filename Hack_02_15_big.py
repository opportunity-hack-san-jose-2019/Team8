#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np

import warnings
import operator
import math
warnings.filterwarnings('ignore')


# In[2]:


#Full Name	Student ID	First	Last	Cohort	Evening	Location	Phone Number	Email	Career Interests for Matching	Attendance	Module Score	Project Score	Bonus	Total Score


# In[3]:


# df_st_mat = pd.read_csv("stu_matBig.csv")
df_st_mat = pd.read_csv("stu_mat.csv")


# In[4]:


df_st_mat = df_st_mat.replace(to_replace = np.nan,  value=0)


# In[5]:


df_st_mat.head()


# In[6]:


# df_vol_mat = pd.read_csv("vol_matBig.csv")
df_vol_mat = pd.read_csv("vol_mat.csv")


# In[7]:


df_vol_mat = df_vol_mat.replace(to_replace = np.nan,  value=0)


# In[8]:


df_vol_mat.head()


# In[9]:


vol_tuple= []
for i in range (len(df_vol_mat)):
#     vol_tuple.append(df_vol_mat.loc[i][1:])
    vol_tuple.append(df_vol_mat.loc[i][:])


# In[10]:


np.asarray(vol_tuple)


# # Volunteer Jaccard Array

# In[11]:


vol_Array=np.asarray(vol_tuple)



# # Student Jaccard Array

# In[12]:


Stu_tuple= []
for i in range (len(df_st_mat)):
#     Stu_tuple.append(df_st_mat.loc[i][1:])
    Stu_tuple.append(df_st_mat.loc[i][:])


# In[13]:


stu_Array= np.asarray(Stu_tuple)



# # student Data

# In[14]:


stu_list = df_st_mat.values.tolist()



# In[16]:


#backup loop
# vol_s =[]
# vol_sim={}
# stu_s =[]
# stu_sim={}
# for i in vol_list:
#     v1= i
#     vol_s.append(v1[0:2])
# #     viarr = int(v1[1:])
#     print(v1[1:])
#     sumxx,sumyy,sumxy =0,0,0
# #     print(vol_s[0][1])
# #     print(vol_s)
#     for j in stu_list:
#         v2=j
#         print (v2[1:])
#         stu_s.append(v2[0:2])
#         #cosine
# #         x=v1[2:]
# #         y=v2[2:]
# #         sumxx += x*x
# #         sumyy += y*y
# #         sumxy += x+y
# #         print(sumxy/math.sqrt(sumxx*sumyy))
# #         print(viarr)
        
        
#         break
        
#     break


# # Finding Similarities and mapping with volunteer to all the students Volunteer to student confidence calculation

# In[17]:


vol_stu_list=[]
for i in vol_Array:
    tupList=[]
    vol_stu_List = []
    sim=0
    v1=i
#     print("1 is here")
    sumxx,sumyy,sumxy =0,0,0
    for j in stu_Array:
#         print("2 is here")
        v2=j
        
#         k=0
        k=0
        
        for k in range(len(v1)-1):
#             print("3 is here")
            x=v1[k+1]
            y=v2[k+1]
#             print(v2)
            sumxx += x*x
            sumyy += y*y
            sumxy += x*y
            sim = sumxy/math.sqrt(sumxx*sumyy)
#         print("4 is here")
        tupList.append((v2[0],v2[1],sim))
#         print(v2[1])
#     print(tupList)
    sortby = sorted(tupList, key= lambda tup: tup[1],reverse=True)
#     print(len(sortby))
#     print(v1)
#     print(sortby[:3])
#     print("here" , v1[0])
    temp = sortby
#     print(temp,'temp')
#     print(v1[0])
    vol_stu_list.append((v1[0],v1[1],temp))
#     print(list(vol_stu_list))
#     break
# print(vol_stu_list)
   
    
# print(len(vol_stu_list))
    
    
        
#         sortby = tupList.sort(key = lambda tup: tup[0])
#         for q in tupList:
#             print(q)
    
#         print(tupList)
        #2nd for end
        

#     break
# print(vol_stu_list)
# p=0
# for l in (vol_stu_list):
# #     print(vol_stu_list)
# #     print(p,"p")
#     print(vol_stu_list[p][0][0], vol_stu_list[p][1])
#     p=p+1

# list(map(lambda x:print(x),vol_stu_map))




# # Mapping for reccomendation

# In[19]:


selectedVal=[]
mapList=[]
p=0
size = len(vol_stu_list[0][2])

p=0
for q in range(len(vol_stu_list[0][2])):
    comst=[]
    for e in vol_stu_list:
#         print("e[2]",e[2][p][1])
#         print("e[1][0][0]",e[0],"  ",e[1], "mapped",e[2][p][0],"  1hello " , e[2][p][1], "score", e[2][p][2])
        comst.append((e[0],e[1],e[2][p][0],e[2][p][1],e[2][p][2]))
    comstsort = sorted(comst, key= lambda tup: tup[4],reverse=True)
#     print(comstsort)
    mapList.append((comstsort[0:2])) # [0:3] will take top three neighbours
#     print(mapList)
    p=p+1


# In[20]:


# for 


# In[26]:





# In[22]:


# # df = pd.DataFrame(mapList[1:][1], columns=["Volunteer", "Student","Match"])
# a= pd.DataFrame(mapList)
# print(a.head())
# df = pd.DataFrame(mapList[1:][1],columns=["Volunteer Name", "Volunteer ID","Student Name"," Student Match"])
# # print(df.head())


# df1 = pd.DataFrame(mapList[2:][1],columns=["Volunteer Name", "Volunteer ID","Student Name"," Student Match"])
# # df1.head()


# In[23]:


# pd.pivot_table(df,index = df[0][0],values=df[0][1])


# In[24]:


# import csv

# # with open('file.csv', 'w') as f:
# #   reader = csv.reader(f)
# #   your_list = list(mapList)

# # print(your_list)

# with open('file.csv', 'w') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerows(mapList)


# In[25]:


# with open('file_small.csv', 'w') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerows(mapList)


# In[ ]:


def main():
    return mapList

