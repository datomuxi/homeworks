from turtle import *


#we want to paint a house
shape("circle")
speed(10)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
 #end of square

 #drawing a door

forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing windows 
penup()
goto(20, 50)
pendown()
color("black")
begin_fill()

right(150)

forward(50)
right(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)
end_fill()

penup()
begin_fill()
goto(150, 50)
pendown()
right(90)
forward(50)
right(90)
forward(30)
right(90)
forward(50)
right(90)
forward(30)
end_fill()


















exitonclick()