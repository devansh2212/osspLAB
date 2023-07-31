#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("HELLO WORLD")


# In[27]:


for i in range(2):
    print("RAM RAM")


# In[16]:


def bubblesort(a):
    for i in range(len(a)):
        for j in range(len(a)):
          if a[i]<a[j]:
            b=a[i]
            a[i]=a[j]
            a[j]=b
    print(a)
bubblesort([4,2,3,7,8,2,4,6,9,5])


# In[25]:


def insertionSort(a):
    for i in range(len(a)): 
        key = a[i]
        j = i-1
        while j >=0 and key < a[j] :
                a[j+1] = a[j]
                j -= 1
        a[j+1] = key
    print(a)    
insertionSort([21,54,78,45,65,84,25,75,49])


# In[26]:


def selectionSort(a, s):
    
    for i in range(s):
        m = i
        for j in range(i + 1, s):
            if a[j] < a[m]:
                m = j
        (a[i], a[m]) = (a[m], a[i])
    print(a)
selectionSort([23,45,6,7,23,45,68,76,98,34,6,78,3,75],14)


# In[ ]:




