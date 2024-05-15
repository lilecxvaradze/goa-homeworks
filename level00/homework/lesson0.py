from turtle import *  


#we want to paint a house

#step 1: draw a square
width(6)
color('blue')
begin_fill()
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door

forward(70)
color('yellow')
begin_fill()
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
     
penup()
goto(200,200)
pendown()

color('red')
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(200,200)
pendown()
color('blue')    #right window
begin_fill()
left(30)
forward(20)
color('orange')
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()

penup()
goto(0,200)
pendown()

right(90)      #left window
color('blue')

forward(20)
color('orange')
begin_fill()
left(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
end_fill()     #end of windows

#ground

left(90)
color('blue')
forward(130)
color('green')
begin_fill()
right(-90)
forward(470)
right(90)
forward(390)
right(90)
forward(940)
right(90)
forward(390)
right(90)
forward(470)
end_fill()    #end of ground

#tree ;)
color('brown')
left(90)
left(90)
color('green')
forward(220)

color('brown')
begin_fill()
right(90)
forward(210)
left(90)
forward(30)
left(90)
forward(210)
end_fill()

#leafes
color('green')
begin_fill()
speed(6)
penup()
goto(-310,250)
pendown()

circle(80)
end_fill()

exitonclick()