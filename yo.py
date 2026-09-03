from pyscript import display

display("Specify the data types below", target="spec") #target the text element

#variables

a = 'avongers' #str
b = 2026 #int
c = 9.8 #float
d = True #bool
e = ["Brand New Day", "Doomsday", "Backrooms"] #list
f = (5,10,15) #tuple
g = {'mushroom', 'hamburg', 'fries'} #set
h = {
    "name" : "bruh",
    "age" : 18,
    "desc" : "pogi"
} # dict

display(type(a), target="spec")
display(type(b), target="spec")
display(type(c), target="spec")
display(type(d), target="spec")
display(type(e), target="spec")
display(type(f), target="spec")
display(type(g), target="spec")
display(type(h), target="spec")
display('My favorite movie is ', e[0])
display('mushroom' in g)
display(h["desc"], h["name"])
display(g, target="output")