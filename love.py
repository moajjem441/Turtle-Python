import turtle

t=turtle.Turtle()

t.color("red")
t.fillcolor("red")

t.begin_fill()
t.left(140)
t.forward(100)
t.circle(-50,200)
t.left(120)
t.circle(-50,200)
t.forward(100)

t.end_fill()

turtle.done()