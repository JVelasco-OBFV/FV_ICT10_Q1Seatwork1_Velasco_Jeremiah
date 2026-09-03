from pyscript import display

name = "Jerm" #string
age = 14 #integer
heightincm_172 = 172.72 #floating-number
favorite_country101_ = ["Malaysia","Spain","Italy"] #list
student_type = False #boolean
descriptions = {
    "color":"red",
    "car_brand":"Toyota",
    "shoe_size":6.8,
    "best_friend":"Isaias"
} #dictionary
my_fav_fruits = {"lychee","blueberry","banana","green grapes","strawberry"} #set
days_of_the_week = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday") #tuple 

display(name, target ="display")
display(age, target ="display")
display(heightincm_172, target="display")
display(favorite_country101_[0], target="display")
display(student_type, target="display")
display(descriptions, target="display")
display(my_fav_fruits, target="display")
display(days_of_the_week, target="display")

