from pyscript import document, display

name = "Jeremiah Michael P. Velasco" #string
age = 14 #integer
heightincm_172 = 170.18 #floating-number
fav_country101_ = ["Malaysia","Spain","Italy"] #list
student_type = False #boolean
descriptions = {
    "color":"Red",
    "car_brand":"Toyota",
    "shoe_size":6.8,
    "best_friend":"Wenz Paragas"
} #dictionary
my_fav_fruits = {"lychee","blueberry","banana","green grapes","strawberry"} #set
days_of_the_week = ("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday") #tuple 

display(f'Name: {name}', target ="display")
display(f'Age: {age}', target ="display")
display(f'Height: {heightincm_172} cm', target="display")
display(f'Countries I want to travel to: ', f'{fav_country101_[0]},' + f' {fav_country101_[1]},' + f' and {fav_country101_[2]}', target="display")
display(f'Student Type: {student_type}', target="display")
display(f'Favorite Color, Car Brand, Shoe Size, and Best Friend: ',  f'{descriptions["color"]},' + f' {descriptions["car_brand"]}'+ f' and { descriptions["shoe_size"]}', descriptions["best_friend"], target="display")
display(f'Favorite Fruits: {my_fav_fruits}', target="display")
display(f'Ranking Days of the Week: {days_of_the_week[0]} - 3rd Place, {days_of_the_week[1]} - 5th Place, {days_of_the_week[2]} - 6th Place, {days_of_the_week[3]} - 7th Place, {days_of_the_week[4]} - 4th Place, {days_of_the_week[5]} - 2nd Place, {days_of_the_week[6]} - 1st Place', target="display")

def adding(e):
    document.getElementById("output").innerHTML = ""
    num1= float(document.getElementById("input1").value)
    num2= float(document.getElementById("input2").value)
    result= num1 + num2
    display(f'Your sum is equal to {result}.', target="output")

def subtracting(e):
    document.getElementById("output").innerHTML = ""
    num1= float(document.getElementById("input1").value)
    num2= float(document.getElementById("input2").value)
    result= num1 - num2
    display(f'Your difference  is equal to {result}.', target="output")

def multiplying(e):
    document.getElementById("output").innerHTML = ""
    num1= float(document.getElementById("input1").value)
    num2= float(document.getElementById("input2").value)
    result= num1 * num2
    display(f'Your product  is equal to {result}.', target="output")

def dividing(e):
    document.getElementById("output").innerHTML = ""
    num1= float(document.getElementById("input1").value)
    num2= float(document.getElementById("input2").value)
    result= num1 / num2
    display(f'Your quotient  is equal to {result}.', target="output")

def floor_divide(e):
    document.getElementById("output").innerHTML = ""
    num1= float(document.getElementById("input1").value)
    num2= float(document.getElementById("input2").value)
    result= num1 // num2
    display(f'Your quotient (rounded down) is equal to {result}.', target="output")

def modulo(e):
    document.getElementById("output").innerHTML = ""
    num1= float(document.getElementById("input1").value)
    num2= float(document.getElementById("input2").value)
    result= num1 % num2
    display(f'Your remainder is equal to {result}.', target="output")

def exponentation(e):
    document.getElementById("output").innerHTML = ""
    num1= float(document.getElementById("input1").value)
    num2= float(document.getElementById("input2").value)
    result= num1 ** num2
    display(f'Your exponent power is equal to {result}.', target="output")