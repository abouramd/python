programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# printf an item from dictionary
print(programming_dictionary["Bug"])

# add new item to dictionary
programming_dictionary["name"] = "abdelhay bouramdane"
print(programming_dictionary)

# creat an empty dictionary
empty_dictionary = {}

# wipe an existing dictionary
#programming_dictionary = {}


# edit an item in dictionary
programming_dictionary["Bug"] = "hello"

# loop through a dictionary
for item in programming_dictionary:
    print(item)
    print(programming_dictionary[item])


    #######################################

#Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

#Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

#Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

#Nesting Dictionaries in Lists

travel_log = [
{
  "country": "France", 
  "cities_visited": ["Paris", "Lille", "Dijon"], 
  "total_visits": 12,
},
{
  "country": "Germany",
  "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
  "total_visits": 5,
},
]