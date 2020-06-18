#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1 Write a program to print the triangle
n = int(input(" Enter Value:"))
for i in range(0,n):
  v = i
  for k in range(1,i+1):
    print(v,end=" ")
    v +=1
  print("\n")    


# In[4]:


#2 
n = int(input(" Enter Value:"))
for i in range(0,n):
    for k in range(0, i):
        print("* ", end=" ")
    print("\n")


# In[11]:


#3
n = int(input(" Enter Value:"))
val = n
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(j,end=" ")
    print("\n")   
    


# In[16]:


#4
n = int(input(" Enter Value:"))
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("\n")    


# In[23]:


#5
n = int(input(" Enter Value:"))
for i in range(1,n):
    for j in range(i,n+1):
        print(j, end=" ")
    print('')
val = n
for i in range(n,0,-1):
    for j in range(i,n+1):
        print(j,end=" ")
    print('')    


# In[25]:


#6 Find the length of a string without using len functions
n = input()
count = 0
for i in n:
    count += 1
print(count)    


# In[26]:


#7 Find the no of words and characters in a string
n = input()
count = 0
let = 0
for i in n:
    if i == " ":
        count += 1
    let += 1
word = let - count
print("The no. of words",count+1)
print("The no. of char",word)


# In[28]:


#8 Find the no of occurrences of a word in a string
n = input("Enter String")
w = input("Enter Word")
c = 0
l=n.split(" ")
for i in range(0, len(l)):
    if w == l[i]:
        c = c+1
print(c)

        


# In[ ]:




