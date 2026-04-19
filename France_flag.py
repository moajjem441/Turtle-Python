import turtle

t=turtle.Turtle()
t.fillcolor("blue")
t.begin_fill()
for _ in range(2):
    t.forward(70)
    t.left(90)
    t.forward(150)
    t.left(90)
t.end_fill()

t.forward(70)
for _ in range(2):
    t.forward(70)
    t.left(90)
    t.forward(150)
    t.left(90)
t.forward(70)

t.fillcolor("red")
t.begin_fill()
for _ in range(2):
    t.forward(70)
    t.left(90)
    t.forward(150)
    t.left(90)
t.end_fill()
t.forward(70)
turtle.mainloop()