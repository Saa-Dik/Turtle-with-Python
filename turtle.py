import turtle

# Set up the screen
screen = turtle.Screen()

# Set up the turtle
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")

# Start filling the shape
t.begin_fill()

# Draw a square
for _ in range(4):
    t.forward(100)
    t.right(90)

# End filling the shape
t.end_fill()

# Close the window on click
screen.exitonclick()
