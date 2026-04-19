import turtle

t=turtle.Turtle()

t.color("yellow")
t.fillcolor("brown")

t.speed(3)

t.begin_fill()
for _ in range(5):
    t.forward(150)
    t.left(144)

t.end_fill()

turtle.mainloop()