from turtle import *

def draw_panda():
    speed(10)  # Painting speed
    bgcolor("white")

    pensize(2)
    
    # Draw face
    up()
    goto(0, -100)
    down()
    begin_fill()
    fillcolor("white")
    circle(100)
    end_fill()

    # Left ear
    up()
    goto(-67, 80)
    setheading(45)
    down()
    begin_fill()
    fillcolor("black")
    circle(30)
    end_fill()

    # Right ear
    up()
    goto(67, 80)
    setheading(135)
    down()
    begin_fill()
    fillcolor("black")
    circle(-30)
    end_fill()

    # Left eye
    up()
    goto(-40, 20)
    setheading(0)
    down()
    begin_fill()
    fillcolor("black")
    circle(20)
    end_fill()

    up()
    goto(-40, 30)
    setheading(0)
    down()
    begin_fill()
    fillcolor("white")
    circle(5)
    end_fill()

    # Right eye
    up()
    goto(40, 20)
    setheading(0)
    down()
    begin_fill()
    fillcolor("black")
    circle(20)
    end_fill()

    up()
    goto(40, 30)
    setheading(0)
    down()
    begin_fill()
    fillcolor("white")
    circle(5)
    end_fill()

    # Nose
    up()
    goto(0, -10)
    setheading(0)
    down()
    begin_fill()
    fillcolor("black")
    circle(10)
    end_fill()

    # Mouth
    up()
    goto(0, -30)
    setheading(-90)
    width(3)
    down()
    circle(10, 135)
    up()
    goto(0, -30)
    setheading(-90)
    down()
    circle(-10, 135)
    
    hideturtle()
    exitonclick()  # Exit

draw_panda()
