#!/usr/bin/env python
# coding: utf-8

# In[43]:


import pandas as pd 
import numpy as np

import warnings
import operator
import math
warnings.filterwarnings('ignore')



df_st_mat = pd.read_csv("stu_matBig.csv")


# In[47]:


df_st_mat = df_st_mat.replace(to_replace = np.nan,  value=0)





df_st_mat.head()



df_vol_mat = pd.read_csv("vol_matBig.csv")



df_vol_mat = df_vol_mat.replace(to_replace = np.nan,  value=0)



df_vol_mat.head()



vol_tuple= []
for i in range (len(df_vol_mat)):
    vol_tuple.append(df_vol_mat.loc[i][1:])





np.asarray(vol_tuple)




vol_Array=np.asarray(vol_tuple)
print(vol_Array)
print(vol_Array.shape)




Stu_tuple= []
for i in range (len(df_st_mat)):
    Stu_tuple.append(df_st_mat.loc[i][1:])



stu_Array= np.asarray(Stu_tuple)
print(stu_Array)
print(stu_Array.shape)





stu_list = df_st_mat.values.tolist()
print(stu_list)





vol_list = df_vol_mat.values.tolist()
print(vol_list)


        
        
#         break
        
#     break


# # Finding Similarities and mapping with volunteer to all the students Volunteer to student confidence calculation

# In[65]:


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
        
        k=0
        
        for k in range(len(v1)):
#             print("3 is here")
            x=v1[k]
            y=v2[k]
#             print(v2)
            sumxx += x*x
            sumyy += y*y
            sumxy += x*y
            sim = sumxy/math.sqrt(sumxx*sumyy)
#         print("4 is here")
        tupList.append((v2[0],sim))

    sortby = sorted(tupList, key= lambda tup: tup[1],reverse=True)

    temp = sortby

    vol_stu_list.append((v1[0],temp))


print((vol_stu_list))



# print((vol_stu_list))
print("Volunteer count",len(vol_stu_list))
print("Student Count",len(vol_stu_list[0][1]))



selectedVal=[]
mapList=[]
p=0
size = len(vol_stu_list)
print(len(vol_stu_list[0][1]))
p=0
for q in range(len(vol_stu_list[0][1])):
    comst=[]
    for e in vol_stu_list:
        comst.append((e[0],e[1][p][0],e[1][p][1]))
    comstsort = sorted(comst, key= lambda tup: tup[2],reverse=True)
    mapList.append((comstsort[0:2])) # [0:3] will take top three neighbours
    p=p+1


# In[90]:

def main():
    return mapList






# In[ ]:




