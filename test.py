import turtle

score = turtle.Turtle()
# score.pencolor("white")
score.hideturtle()
score.penup()
score.forward(100)
score.write("Hello", font=("Comic Sans", 16, "bold"))

turtle.backward(100)

score.clear()

turtle.exitonclick()