import turtle

t = turtle.Turtle()
t.speed(0)
t.color("orange")
t.fillcolor("brown")
t.begin_fill()

for _ in range(36):
    t.circle(100)
    t.left(10)
t.end_fill()

turtle.done()