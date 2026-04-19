import turtle

t = turtle.Turtle()

t.color("orange")
t.fillcolor("brown")
t.begin_fill()
for i in range(10):
    t.circle(50)
    t.left(36)

t.end_fill()

turtle.done()