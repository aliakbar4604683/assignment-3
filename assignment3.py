#!/usr/bin/env python
# coding: utf-8

# # question 1
# #Write a Python program to print the following string in a specific format (see theoutput).
# 
# print("   Twinkle, twinkle, little star,") 
#     print("   How I wonder what you are! ")
# 

# In[12]:


print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are! ")
print("\t\tUp above the world so high,")
print("\t\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star, ")
print("\tHow I wonder what you are ")


# # question2
# #Write a Python program to get the Python version you are using 

# In[13]:


import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)


# # question3
# #Write a Python program to display the current date and time.

# In[14]:


from datetime import datetime
dm = datetime.now()
print("now =", dm)
dt_string = dm.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)


# # question4
# #Write a Python program which accepts the radius of a circle from the user and compute
# the area. 

# In[15]:


from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle with radius " + str(r) + " is: " + str(pi * r**2))


# # question5
# #Write a Python program which accepts the user's first and last name and print them in
# reverse order with a space between them. 

# In[16]:


fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print ("reverse order " + lname + " " + fname)


# # question6
# #Write a python program which takes two inputs from user and print them addition

# In[18]:


a = int(input("enter first number: "))
b = int(input("enter second number: "))
sum = a + b
print("sum:", sum)


# # question7
# #Write a program which takes 5 inputs from user for different subject’s marks, total it
# and generate mark sheet using grades ? 

# In[20]:


sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80 and avg<90):
    print("Grade: B")
elif(avg>=70 and avg<80):
    print("Grade: C")
elif(avg>=60 and avg<70):
    print("Grade: D")
else:
    print("Grade: F")


# # question8
# #Write a program which take input from user and identify that the given number is even
# or odd?
# 

# In[22]:


num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# # QUESTION9
# #Write a program which print the length of the list? 

# In[23]:


alist=["ali","akbar","sattar","bhatti","hamza"]


# In[26]:


len(alist)


# # question10
# #.Write a Python program to sum all the numeric items in a list?

# In[73]:


a=0
for number in[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]:
    
    a=number+a

print(f"sum of all element are :", a)


# # question11
# #Write a Python program to get the largest number from a numeric list. 

# In[64]:


abc=[1,2,3,34,51,62,37,85,95,10,11,12,13,14,15,16,19,0]
abc.sort()
print("Largest element is:", abc[-1])


# # question12
# #Take a list, say for example this one:
# 
# #a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  #Write a program that prints out all the elements of the list that are less than 5. 

# In[65]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for char in a:
    if(char<5):
        print(char)
    else:
        continue
        


# In[ ]:





# In[ ]:





# In[ ]:




