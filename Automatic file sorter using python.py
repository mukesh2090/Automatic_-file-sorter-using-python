#!/usr/bin/env python
# coding: utf-8

# In[37]:


import os, shutil
path = r"C:/Users/ADMIN/OneDrive/Pictures/"


# In[38]:


path = r"C:/Users/ADMIN/OneDrive/Pictures/"


# In[39]:


file_name = os.listdir(path)


# In[40]:


folder_names = ['csv files','image files', 'video files']
for loop in range(0,3):
    if not os.path.exists(path + folder_names[loop]):
        #print(path+folder_names[loop])
        os.makedirs(path+folder_names[loop])
for file in file_name:
    if".csv" in file and not os.path.exists(path + "csv files/" + file):
        shutil.move(path + file, path + "csv files/" + file)
    elif".png" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)
    elif".mp4" in file and not os.path.exists(path + "video files/" + file):
        shutil.move(path + file, path + "video files/" + file)    
    elif".jpg" in file and not os.path.exists(path + "image files/" + file):
        shutil.move(path + file, path + "image files/" + file)           


# In[36]:





# In[ ]:




