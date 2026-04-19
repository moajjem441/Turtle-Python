import turtle

t=turtle.Turtle()



t.fillcolor("red")
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(150)
t.left(90)
t.forward(200)
t.left(90)
t.forward(150)
t.end_fill()

t.penup()
t.left(90)
t.forward(30)
t.left(90)
t.forward(50)
t.right(90)
t.forward(50)

t.color("white")
t.fillcolor("white")
t.pendown()
t.begin_fill()
for _ in range(2):
    t.forward(20)
    t.left(90)
    t.forward(60)
    t.left(90)
t.end_fill()

t.penup()
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)

t.pendown()
t.begin_fill()
t.left(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.left(90)
t.forward(60)
t.end_fill()
  


turtle.mainloop()