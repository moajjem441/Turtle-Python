import turtle 

t=turtle.Turtle()

t.color("purple")
t.fillcolor("orange")
for _ in range(6):
    t.forward(100)
    t.left(60)

turtle.mainloop()