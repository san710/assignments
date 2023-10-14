#!/usr/bin/env python
# coding: utf-8

# In[5]:


import datetime
import os
import random
import time
from multiprocessing import Process
from datetime import date, timedelta

# Task 1: Add the current date to the text file today.txt as a string
current_date = datetime.date.today()
with open("today.txt", "w") as file:
    file.write(str(current_date))

# Task 2: Read the text file today.txt into the string today_string
with open("today.txt", "r") as file:
    today_string = file.read()

# Task 3: Parse the date from today_string
parsed_date = datetime.datetime.strptime(today_string, "%Y-%m-%d").date()

# Task 4: List the files in your current directory
current_directory_files = os.listdir()

# Task 5: Create a list of all of the files in your parent directory
parent_directory = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
parent_directory_files = os.listdir(parent_directory)

# Task 6: Use multiprocessing to create three separate processes
def print_current_time(process_num):
    random_sleep_time = random.randint(1, 5)
    time.sleep(random_sleep_time)
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(f"Process {process_num}: Current Time - {current_time}")

if __name__ == '__main__':
    processes = []
    for i in range(3):
        p = Process(target=print_current_time, args=(i,))
        p.start()
        processes.append(p)
    
    for p in processes:
        p.join()

# Task 7: Create a date object of your day of birth

birth_date = datetime.date(2000,12,10)

# Task 8: What day of the week was your day of birth?
day_of_week = birth_date.strftime("%A")

# Task 9: When will you be (or when were you) 10,000 days old?
ten_thousand_days_old_date = birth_date + timedelta(days=10000)

print(f"My day of birth is {day_of_week}. I will be (or was) 10,000 days old on {ten_thousand_days_old_date}.")


# In[ ]:




