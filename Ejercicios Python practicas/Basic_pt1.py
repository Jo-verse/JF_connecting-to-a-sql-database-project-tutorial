# 1) Formatted Twinkle Poem
print("""
      Twinkle, twinkle, little star,
        How I wonder what you are!
            Up above the world so high,
            Like a diamond in the sky.
      Twinkle, twinkle, little star,
        How I wonder what you are
      """)

# 2) Python Version
import sys
print("Python Version")
print(sys.version)

# 3) Current Date and Time
import datetime
print("Current Date and Time")
print(datetime.datetime.now())

# 4) Area of a Circle
from math import pi 
radius = float(input("Input the radius of the circle: "))
area = pi * radius ** 2
print("The area of the circle with radius", radius, "is", area)

# 5) Reverse First and Last Name
name = input("Enter your name: ")
name = name.split()
print("Reverse First and Last Name")
print(name[-1], name[0])

# 6) List and Tuple
sample_data = 3, 5, 7, 23
print("List and Tuple")
print("Sample data: ", sample_data)
print("List: ", list(sample_data))

# 7) File Extension
file_name = input("Enter the file name: ")
file_name = file_name.split(".")
print("File Extension")
print("The extension of the file is: ", file_name[-1])

# 8) First and Last Colors
color_list = ["Red", "Green", "White", "Black"]
print("First and Last Colors")
print("First color: ", color_list[0])
print("Last color: ", color_list[-1])

# 9) Days Between Dates
from datetime import date
first_date = date(2014, 7, 2)
last_date = date(2014, 7, 11)
delta = last_date - first_date
print("Days Between Dates")
print(delta.days)

# 10) Even Numbers
print("Even Numbers")
for i in range(1, 237, 3):
    print(i)


# 11) Print a Pattern