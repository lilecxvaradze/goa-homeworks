from turtle import *

#drawing castle

#drawing walls
color("grey")
begin_fill()

color("white")
forward(20)
right(90)
forward(80)
color("grey")
left(90)
forward(320)
left(90)
forward(250)
left(90)
forward(80)
right(90)
forward(90)
left(90)
forward(90)
left(90)
forward(90)
right(90)
forward(80)
right(90)
forward(150)
left(90)
forward(90)
left(90)
forward(150)
right(90)
forward(80)
right(90)
forward(90)
left(90)
forward(90)
left(90)
forward(90)
right(90)
forward(90)
left(90)
forward(250)
left(90)
forward(390)
end_fill()
#end of walls

#drawing door

color("brown")
begin_fill()

left(90)
forward(160)
left(90)
forward(170)
left(90)
forward(160)
left(90)
forward(170)
end_fill()
#end of door

#drawing right windows
color("yellow")
penup()
goto(280,120)
pendown()

begin_fill()
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
right(90)
forward(100)
end_fill()

#drawing left window
left(180)
color("grey")
forward(370)

color("yellow")
begin_fill()

left(90)
forward(102)
right(90)
forward(100)
right(90)
forward(102)
right(90)
forward(102)
end_fill()

color("grey")
left(180)
forward(110)
right(180)
#end of windows

#drawing ground

begin_fill()
color("grey")
right(90)
forward(200)
color("green")
left(90)
forward(950)
right(90)
forward(320)
right(90)
forward(1500)
right(90)
forward(320)
right(90)
forward(550)
end_fill()
#end of ground

#drawing king


color("black")
left(180)
color("green")
forward(100)
right(60)
color("black")
forward(60)
left(120)
forward(60)
right(180)
forward(60)
left(30)
forward(60)
left(180)
forward(30)
left(40)
forward(40)
right(180)
forward(40)
left(100)
forward(40)

speed(10)

right(180)
forward(40)
left(40)
forward(30)
color("white")
right(60)
forward(9)
color("black")
circle(20)

#crown
color("white")
left(60)
forward(36)

color("orange")
begin_fill()
forward(20)
left(140)
forward(10)
right(90)
forward(10)
left(130)
forward(20)
end_fill()
#end of crown

color("white")
right(120)
forward(230)
left(30)
color("brown")
begin_fill()
forward(30)
left(90)
forward(270)
left(90)
forward(30)
left(90)
forward(270)
end_fill()

#bush

color("green")
begin_fill()
right(90)
forward(-10)
circle(90)
end_fill()
#end of tree

#drawing goa flag ;)


color("green")
left(90)
forward(135)
right(90)
color("green")
forward(80)
color("white")
right(90)
forward(5)
left(90)
forward(1)
left(90)
forward(5)
right(90)
forward(500)

#flag 

color("black")
begin_fill()
left(90)
forward(80)
left(90)
forward(100)
left(90)
forward(70)
left(90)
forward(100)
end_fill()

width(3)
left(90)
forward(50)
left(90)
color("black")
forward(80)
color("Green")
circle(8)
left(180)
forward(8)
right(90)
forward(30)
right(90)
forward(18)

right(180)
forward(18)
color("black")
forward(18)
left(90)
forward(30)
right(90)
forward(10)
color("green")
circle(8)
color("black")
forward(20)
color("green")
right(110)
forward(30)
left(180)
forward(30)
right(140)
forward(30)
left(180)
forward(15)
left(70)
forward(10)

penup()
goto(100,100)
pendown()











exitonclick()




