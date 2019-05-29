#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import cv2
import numpy as np


# In[2]:


img=cv2.imread("cat.jpg")
img.shape


# In[3]:


#cv2.imshow("new",img)


# In[4]:


cv2.waitKey(0)


# In[5]:


#cv2.destroyWindo("window name")
cv2.destroyAllWindows()


# In[6]:


# to crop
crop=img[:500,:600]


# In[7]:


crop


# In[8]:


crop.shape


# In[9]:


#to save
cv2.imwrite("new.jpg",crop)


# In[10]:


get_ipython().run_line_magic('matplotlib', 'inline')
#The line above is necesary to show Matplotlib's plots inside a Jupyter Notebook


from matplotlib import pyplot as plt


# In[11]:


plt.imshow(crop)


# In[12]:


blur=cv2.blur(img,(20,20))


# In[13]:


plt.imshow(blur)


# In[14]:


plt.imshow(img)


# In[15]:


blur1 = cv2.GaussianBlur(img, (5,5),0)


# In[16]:


plt.imshow(blur1)


# In[17]:


blur2=cv2.medianBlur(img,1)


# plt.imshow(blur2)

# In[18]:


plt.imshow(blur2)


# In[19]:


blur3=cv2.bilateralFilter(img,10,50,50)


# In[20]:


plt.imshow(blur3)


# In[21]:


img1=cv2.imread("dog.jpg")


# In[22]:


plt.imshow(img1)


# In[23]:


new=img[:300,:400]


# In[24]:


img[:300,:400]=new


# In[25]:


plt.imshow(new)


# In[26]:



com=np.zeros((900,900))


# In[27]:


vis = np.concatenate((img,img), axis=0)


# In[28]:


plt.imshow(vis)


# In[29]:


a=img[:300,:300]
b=img1[:300,:300]


# In[30]:


x=np.concatenate((a,b,),axis=1)


# In[31]:


plt.imshow(x)


# In[32]:


plt.imshow(b)


# In[33]:


next=img1[:140,100:300]


# In[34]:


plt.imshow(next)


# In[39]:


#s_img = cv2.imread("smaller_image.png")
#l_img = cv2.imread("larger_image.jpg")
x_offset=150
y_offset=80
img[y_offset:y_offset+next.shape[0], x_offset:x_offset+next.shape[1]] = next


# In[40]:


plt.imshow(img)


# In[ ]:




