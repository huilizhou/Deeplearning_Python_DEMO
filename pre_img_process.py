
# coding: utf-8

# In[2]:


import cv2
import os


# In[5]:


# 水平垂直翻转原图片，扩充数据集。
for root, dirs, files in os.walk("images"):
    #     print(root)
    #     print(dirs)
    #     print(files)
    if(files):
        for item in files:
            img = cv2.imread(os.path.join(root, item))
            dst = cv2.resize(img, (100, 100))
            cv2.imwrite(os.path.join(root, item), dst)

#     for i in files:
#         img=cv2.imread(os.path.join("images/health",i))
#         newfilename = ''.join(i.split('.')[:-1])
#         dst=cv2.flip(img,-1)
#         cv2.imwrite("images/new_health/"+newfilename+'_flip.bmp',dst)


# In[6]:


# 水平垂直翻转原图片，扩充数据集。
for root, dirs, files in os.walk("images/unhealth/"):
    #     print(root)
    #     print(dirs)
    #     print(files)
    for i in files:
        img = cv2.imread(os.path.join("images/unhealth", i))
        newfilename = ''.join(i.split('.')[:-1])
        dst = cv2.flip(img, 1)
        cv2.imwrite("images/new_unhealth/" + newfilename + '_flip1.bmp', dst)
