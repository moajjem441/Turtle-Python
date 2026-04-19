import turtle

t = turtle.Turtle()
t.speed(7)
t.color("orange")
t.fillcolor("brown")
t.begin_fill()

for _ in range(20):
    t.circle(50)
    t.left(20)
t.end_fill()

turtle.done()