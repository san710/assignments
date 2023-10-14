#!/usr/bin/env python
# coding: utf-8

# In[6]:


#1. Assign the value 7 to the variable guess_me. Then, write the conditional tests (if, else, and elif) 
#to print the string 'too low' if guess_me is less than 7, 'too high' if greater than 7, and 'just right' if equal to 7.
guess_me = 7
if guess_me < 7:
    print('too low')
elif guess_me > 7:
    print('too high')
else:
    print('just right')


# In[7]:


#2. Assign the value 7 to the variable guess_me and the value 1 to the variable start. 
#Write a while loop that compares start with guess_me. Print too low if start is less than guess me. 
#If start equals guess_me, print 'found it!' and exit the loop.
#If start is greater than guess_me, print 'oops' and exit the loop. Increment start at the end of the loop.


guess_me = 7
start = 1

while start <= guess_me:
    if start < guess_me:
        print('too low')
    elif start == guess_me:
        print('found it!')
        break
    else:
        print('oops')
        break
    start += 1


# In[8]:


#3. Print the following values of the list [3, 2, 1, 0] using a for loop
for num in [3, 2, 1, 0]:
    print(num)


# In[9]:


#4 Use a list comprehension to make a list of the even numbers in range(10)
even_numbers = [num for num in range(10) if num % 2 == 0]
print(even_numbers)


# In[10]:


#5. Use a dictionary comprehension to create the dictionary squares. Use range(10) to return the keys, and use the square of each key as its value.
squares = {num: num**2 for num in range(10)}
print(squares)


# In[11]:


#6. Construct the set odd from the odd numbers in the range using a set comprehension (10).

odd = {num for num in range(10) if num % 2 != 0}
print(odd)


# In[12]:


#7
generator = ('Got ' + str(num) for num in range(10))
for item in generator:
    print(item)


# In[15]:


#8
def good():
    return ['Harry', 'Ron', 'Hermione']

good()


# In[16]:


#9
def get_odds():
    for num in range(10):
        if num % 2 != 0:
            yield num

# Use a for loop to find and print the third value returned.
count = 0
for number in get_odds():
    count += 1
    if count == 3:
        print("Third odd number:", number)
        break


# In[17]:


#10
class OopsException(Exception):
    pass

try:
    raise OopsException("An oops occurred")
except OopsException as e:
    print('Caught an oops')


# In[18]:


#11
titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']
movies = dict(zip(titles, plots))
print(movies)


# In[ ]:




