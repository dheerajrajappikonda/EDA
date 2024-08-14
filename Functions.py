def add_numbers(num1, num2):
    num_sum = num1 + num2
    return num_sum

num1 = int(input("Enter the First Number: "))
num2 = int(input("Enter the Second Number: "))
result = add_numbers(num1, num2)
print(f"Sum of {num1} and {num2} is {result}.")


def say_hello():
    print("Hello there!!")

say_hello()


def greet(name, greeting = "Hello"):
    print(f"{greeting} {name}!!")

greet("Dheeraj")
greet("Dheeraj", "Hi")


def add_numbers(x, y):
    result = x + y
    return result

result = add_numbers(3, 8)
print(result)


def subtract_numbers(x, y):
    result = x - y
    return result

result = subtract_numbers(8, 4)
print(result)

result = subtract_numbers(x = 8, y= 4)
print(result)

result_switched = subtract_numbers(y = 4, x = 8)
print(result_switched)


def make_pizza(*toppings):
    print("Making a Pizza with the following Toppings:")
    for toppings_name in toppings:
        print(f"- {toppings_name}")
    print("-------------------------------------------")

make_pizza("Cheese", "Pepperoni")
make_pizza("Sausage", "Tomoatoes", "Spinach")


def give_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")
    print("---------------------------")

give_info(Name = "Dheeraj", Age = "20", Gender = "Male")


def regular_square(x):
    result = x**2
    return result

result = regular_square(5)
print(result)


lambda_square = lambda x: x**2

result = lambda_square(5)
print(result)

float_num = 8.8
int_num = int(float_num)
print(int_num)

complex_num = complex(4, 8)
print(complex_num)

float_num = 4.567
rounded_num = round(float_num)
print(rounded_num)

num_list = [1, 78, 23, 87, 41, -8, 99]
min_value = min(num_list)
max_value = max(num_list)
print(f"The Minimum value is {min_value}.")
print(f"The Maximum value is {max_value}.")

num_tuple = (1, 5, 5, 0, -11)
num_list = [0, -2, -2, 1]
num_set = {1, 2, 2, 4, 0}
tuple_sum = sum(num_tuple)
list_sum = sum(num_list)
set_sum = sum(num_set)
print(f"The Sum of the Tuple is {tuple_sum}.")
print(f"The Sum of the List is {list_sum}.")
print(f"The Sum of the Set is {set_sum}.")

name = "Dheeraj Raj Appikonda"
character_count = name.count("a")
print(f"The Character 'a' appears {character_count} times in the given string.")

name = "Dheeraj Raj Appikonda"
lowercase_name = name.lower()
uppercase_name = name.upper()
print(lowercase_name)
print(uppercase_name)
capitalize_name = lowercase_name.capitalize()
print(capitalize_name)
title_name = lowercase_name.title()
print(title_name)

string = "Python is a Versatile language."
replaced_string = string.replace("Versatile", "Powerful")
print(replaced_string)
index = string.find("Versatile")
print(index)
split_string = string.split()
print(split_string)
date = input("Enter the Date(DD-MM-YYYY): ")
split_date_1 = date.split()
split_date_2 = date.split("-")
split_date_3 = date.split("-", 1)
print(split_date_1)
print(split_date_2)
print(split_date_3)

file_name = input("Enter the file name: ")
if file_name == "Functions.py":
    print("It is the Python Functions file.")
elif file_name.endswith(".py"):
    print("It is a Python file but not the Functions Python file.")
else:
    print("Invalid file.")

word_with_spaces = " Python "
cleaned_word = word_with_spaces.strip()
print(cleaned_word)
name_list = [" Appikonda", " Dheeraj", " Raj "]
cleaned_name_list = [names.strip() for names in name_list]
print(cleaned_name_list)

favorite_movies = []
for i in range(3):
    movie = input("Enter the Movie name: ")
    favorite_movies.append(movie)
print(f"Favorite movies are: {favorite_movies}")

list1 = ["Apples", "Cheese", "Eggs"]
print("List 1:", list1)
list2 = ["Spinach", "Bread", "Chocolates"]
print("List 2:", list2)
combined_list = list1.copy()
combined_list.extend(list2)
print("Extended List:", combined_list)

fruits_list = ["Apple", "Banana", "Kiwi"]
fruits_list.append("Watermelon")
print(fruits_list)
fruits_list.insert(1, "Papaya")
print(fruits_list)
fruits_list.reverse()
print(fruits_list)

num_list = [7, 5, 0, -9, 10]
num_pos = num_list.index(7)
print(num_pos)
num_list.sort()
print(num_list)
num_list.sort(reverse = True)
print(num_list)

fruits_list = ["Apple", "Banana", "Orange", "Apple", "Watermelon"]
fruits_list.remove("Apple")
print(fruits_list)

boolean_values = [False, True, True, False]
is_any_true = any(boolean_values)
is_all_true = all(boolean_values)
if is_all_true:
    print("All values are True.")
elif is_any_true:
    print("Atleast one value is True.")
else:
    print("No value is True.")

room_temp = []
for i in range(5):
    temp_num = int(input("Enter the Temperature readings: "))
    room_temp.append(temp_num)
print(f"Room temperatures are: {room_temp}")
is_any_above = any(temp_num > 30 for temp_num in room_temp)
are_all_above = all(temp_num > 30 for temp_num in room_temp)
if are_all_above:
    print("All the Temperature readings are above 30 Degrees.")
elif is_any_above:
    print("Atleast one Temperature reading is above 30 Degrees.")
else:
    print("No Temperature reading is above 30 Degrees.")

color_palette = ("red", "blue", "black", "violet", "green")
color_name = input("Please enter the Color: ").lower()
if color_name in color_palette:
    print(f"{color_name.capitalize()} is available for use.")
else:
    print("Color not found.")

fruits_list_1 = {"Apple", "Banana", "Grapes"}
fruits_list_2 = {"Kiwi", "Orange", "Watwermelon", "Banana"}
combined_fruits_list = fruits_list_1.union(fruits_list_2)
common_fruits_list = fruits_list_1.intersection(fruits_list_2)
print(combined_fruits_list)
print(common_fruits_list)

person_info = {"Name": "Dheeraj", "Age": 20 , "City": "Visakhapatnam"}
keys_list = person_info.keys()
values_list = person_info.values()
items_list = person_info.items()
print(keys_list)
print(values_list)
print(items_list)
person_info.update({"Occupation": "Undergraduate Student"})
print(person_info)
person_info.update({"Name": "Dheeraj Raj Appikonda"})
print(person_info)
additional_person_info = {"Email": "dheerajrajappikonda@gmail.com", "Phone Number": 8143763439}
person_info.update(additional_person_info)
print(person_info)
person_age = person_info.get("Age", "Not Available")
print(person_age)
person_salary = person_info.get("Salary", "Not Available")
print(person_salary)

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
popped_num = num_list.pop()
print(popped_num)
print(num_list)
popped_num = num_list.pop(3)
print(popped_num)
print(num_list)

num_dictionary = {"A": 1, "B": 2, "C": 3}
popped_num = num_dictionary.pop("B")
print(popped_num)
print(num_dictionary)
popped_num = num_dictionary.pop("D", "Not Available")
print(popped_num)
print(num_dictionary)

def send_invitation(name):
    invitation_message = f"Hello {name}. Hope you are doing good!!"
    print(invitation_message)

name = input("Enter the name: ")
send_invitation(name)


def class_strength_dictionary():
    strength_dictionary = {}
    for i in range(3):
        class_name = input(f"Enter the class name for Class {i+1}: ")
        class_strength = int(input(f"Enter the Class {i+1} Strength: "))
        strength_dictionary[class_name] = class_strength
    return strength_dictionary

class_name_and_strength = class_strength_dictionary()
print(class_name_and_strength)


def add_names_list():
    names_list = []
    for i in range(3):
        name = input("Enter the Student Name: ")
        names_list.append(name)
    return names_list

def marks_dictionary(names_list):
    marks_dictionary = {}
    for name in names_list:
        marks = int(input(f"Enter {name}'s marks: "))
        marks_dictionary[name] = marks
    return marks_dictionary

def display_name_and_marks(marks_dictionary):
    print("Name\t\tMarks")
    for name, marks in marks_dictionary.items():
        print(f"{name}\t\t{marks}")

names_list = add_names_list()
marks_dictionary = marks_dictionary(names_list)
display_name_and_marks(marks_dictionary)


def number_square(number):
    number_square = number**2
    return number_square

def sum_of_squares(number):
    sum_of_squares = 0
    for num in number:
        square = number_square(num)
        sum_of_squares += square
    return sum_of_squares

number_list = [2, 4, 6, 8, 10]
result = sum_of_squares(number_list)
print(result)


def number_square(number):
    number_square = number**2
    return number_square

numbers_list = [1, 2, 3, 4, 5]
squared_numbers = list(map(number_square, numbers_list))
squared_numbers_lambda = list(map(lambda x : x**2, numbers_list))
print(numbers_list)
print(squared_numbers)
print(squared_numbers_lambda)
