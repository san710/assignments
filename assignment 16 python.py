#!/usr/bin/env python
# coding: utf-8

# In[3]:





# 1. Create a list of years
years_list = [1980, 1981, 1982, 1983, 1984]

# 2. Third birthday year
third_birthday_year = years_list[3]

# 3. Year when you were the oldest
oldest_year = years_list[-1]

# 4. List of things
things = ["mozzarella", "cinderella", "salmonella"]

# 5. Capitalize the element referring to a person
things[1] = things[1].capitalize()

# 6. Surprise list
surprise = ["Groucho", "Chico", "Harpo"]

# 7. Process the last element of the surprise list
surprise[-1] = surprise[-1].lower()[::-1].capitalize()

# 8. English-to-French dictionary
e2f = {
    "dog": "chien",
    "cat": "chat",
    "walrus": "morse"
}

# 9. French word for walrus
french_walrus = e2f["walrus"]

# 10. French-to-English dictionary
f2e = {value: key for key, value in e2f.items()}

# 11. English version of the French word "chien"
english_chien = f2e["chien"]

# 12. Set of English words
english_words = set(e2f.keys())

# 13. Multilevel dictionary - life
life = {
    'animals': {
        'cats': ['Henri', 'Grumpy', 'Lucy'],
        'octopi': {},
        'emus': {}
    },
    'plants': {},
    'other': {}
}

# 14. Top-level keys of life
top_level_keys = life.keys()

# 15. Keys for life['animals']
animal_keys = life['animals'].keys()

# 16. Values for life['animals']['cats']
cat_names = life['animals']['cats']

# Print the results
print("1. years_list:", years_list)
print("2. Third birthday year:", third_birthday_year)
print("3. Year when you were the oldest:", oldest_year)
print("4. things:", things)
print("5. Capitalized element in things:", things)
print("6. Surprise list:", surprise)
print("7. Processed surprise list:", surprise)
print("8. English-to-French dictionary (e2f):", e2f)
print("9. French word for walrus:", french_walrus)
print("10. French-to-English dictionary (f2e):", f2e)
print("11. English version of 'chien':", english_chien)
print("12. Set of English words:", english_words)
print("13. Multilevel dictionary (life):", life)
print("14. Top-level keys of life:", top_level_keys)
print("15. Keys for life['animals']:", animal_keys)
print("16. Values for life['animals']['cats']:", cat_names)



# In[ ]:




