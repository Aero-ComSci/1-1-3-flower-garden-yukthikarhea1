from turtle import Turtle
def draw_petal(Turtle, radius, angle):
    trtl.begin_fill()
    trtl.circle(radius, angle)
    trtl.left(180 - angle)
    trtl.circle(radius, angle)
    trtl.left(180 - (180 - angle))
    trtl.end_fill()

flower = ""
howmany = 0
numoftimes=0
prompt = input("Enter a prompt on what flowers you would like? Make sure to include a number, even if its 1 rose.")
p1 = prompt.split()
allowed = ["roses", "tulips", "sunflowers", "daisies", "lillies"]
final = []
i = 0
if p1 in allowed:
  final.append(p1)
print(final)

for n in range(len(p1)):
  if p1[n].isnumeric():
    if p1[n + 1] == "roses" or p1[n + 1] == "rose":
      howmany = int(p1[n])
      flower = p1[n + 1]
      print(howmany, flower)

      # Print the flower name 'howmany' times
      for _ in range(howmany):
        print(flower) 

      howmany = int(howmany) + 1

    elif p1[ n + 1] == "tulips" or p1[n + 1] == "tulip":
      howmany = int(p1[n])
      flower = p1[n + 1]
      print(howmany, flower)

      # Print the flower name 'howmany' times
      for _ in range(howmany):
        print(flower) 

      howmany = int(howmany) + 1

    elif p1[n + 1] == "sunflowers" or p1[n + 1] == "sunflower":
      howmany = int(p1[n])
      flower = p1[n + 1]
      print(howmany, flower)

      # Print the flower name 'howmany' times
      for _ in range(howmany):
        print(flower) 

      howmany = int(howmany) + 1

    elif p1[n+1] == "daisies" or p1[n + 1] == "daisy":
      howmany = int(p1[n])
      flower = p1[n+1]
      print(howmany, flower)

      # Print the flower name 'howmany' times
      for _ in range(howmany):
        print(flower) 

      howmany = int(howmany) + 1
    elif p1[n + 1] == "lillies" or p1[n + 1] == "lily":
      howmany = int(p1[n])
      flower = p1[n + 1]
      print(howmany, flower)


      for _ in range(howmany):
        print(flower) 
    else:
      print("Sorry, we don't have that flower")
    import turtle as trtl
    OverflowError = trtl.Turtle()
    trtl.speed(20)
    trtl.penup()
    trtl.goto(100,200)
    if flower == "roses" or flower == "rose":
        trtl.goto(100,200)
     #insert rose code instead of the circle thingy magingy 
        for _ in range(howmany-1):

          trtl.pendown()
          trtl.color("maroon")
          trtl.begin_fill()
          trtl.circle(50)
          trtl.end_fill()
          trtl.fillcolor("firebrick")
          trtl.begin_fill()
          trtl.circle(45)
          trtl.end_fill()
          trtl.fillcolor("darkred")
          trtl.circle(25)
          trtl.end_fill()
          trtl.circle(10)
          trtl.right(90)
          trtl.color("Green")
          trtl.forward(100)
          trtl.right(90)
          trtl.color("White")
          trtl.forward(100)
          trtl.penup()
          trtl.right(180)
       


    if flower == "sunflowers" or flower == "sunflower":
        trtl.goto(300,200)
        for _ in range(howmany-1):
              trtl.pendown()
              trtl.color("White")
              trtl.fillcolor("brown")
              trtl.begin_fill()
              trtl.circle(52) 
              trtl.end_fill()
              trtl.color("Yellow")
              trtl.forward(55)
              trtl.fillcolor("yellow")
              trtl.begin_fill()
              trtl.circle(35)
              trtl.end_fill()
              trtl.left(90)
              trtl.forward(85)
              trtl.fillcolor("yellow")
              trtl.begin_fill()
              trtl.circle(35)
              trtl.end_fill()
              trtl.left(90)
              trtl.forward(120)
              trtl.left(90)
              trtl.color("yellow")
              trtl.begin_fill()
              trtl.circle(35)
              trtl.end_fill()
              trtl.right(90)
              trtl.forward(25)
              trtl.left(90)
              trtl.forward(25)
              trtl.fillcolor("yellow")
              trtl.begin_fill()
              trtl.circle(35)
              trtl.end_fill()
              trtl.forward(20)
              trtl.left(90)
              trtl.right(90)
              trtl.forward(50)
              trtl.left(90)
              trtl.forward(20)
              trtl.fillcolor("yellow")
              trtl.begin_fill()
              trtl.circle(35)
              trtl.end_fill()
              trtl.forward(5)
              trtl.right(90)
              trtl.forward(15)
              trtl.fillcolor("yellow")
              trtl.begin_fill()
              trtl.circle(35)
              trtl.end_fill()
              trtl.left(90)
              trtl.forward(57)
              trtl.right(90)
              trtl.forward(5)
              trtl.fillcolor("yellow")
              trtl.begin_fill()
              trtl.circle(37)
              trtl.end_fill()
              trtl.color("Green")
              trtl.forward(200)
              trtl.right(270)


    if flower == "lillies" or flower == "lily":
       trtl.goto(500,200)
       for _ in range(howmany):
                  trtl.pendown()
                  trtl.color("White")
                  trtl.fillcolor("yellow")
                  trtl.begin_fill()
                  trtl.circle(52) 
                  trtl.end_fill()
                  trtl.color("lightpink")
                  trtl.forward(55)
                  trtl.fillcolor("lightpink")
                  trtl.begin_fill()
                  trtl.circle(35)
                  trtl.end_fill()
                  trtl.left(90)
                  trtl.forward(85)
                  trtl.fillcolor("lightpink")
                  trtl.begin_fill()
                  trtl.circle(35)
                  trtl.end_fill()
                  trtl.left(90)
                  trtl.forward(120)
                  trtl.left(90)
                  trtl.color("lightpink")
                  trtl.begin_fill()
                  trtl.circle(35)
                  trtl.end_fill()
                  trtl.right(90)
                  trtl.forward(25)
                  trtl.left(90)
                  trtl.forward(25)
                  trtl.fillcolor("lightpink")
                  trtl.begin_fill()
                  trtl.circle(35)
                  trtl.end_fill()
                  trtl.forward(20)
                  trtl.left(90)
                  trtl.right(90)
                  trtl.forward(50)
                  trtl.left(90)
                  trtl.forward(20)
                  trtl.fillcolor("lightpink")
                  trtl.begin_fill()
                  trtl.circle(35)
                  trtl.end_fill()
                  trtl.forward(5)
                  trtl.right(90)
                  trtl.forward(15)
                  trtl.fillcolor("lightpink")
                  trtl.begin_fill()
                  trtl.circle(35)
                  trtl.end_fill()
                  trtl.left(90)
                  trtl.forward(57)
                  trtl.right(90)
                  trtl.forward(5)
                  trtl.fillcolor("lightpink")
                  trtl.begin_fill()
                  trtl.circle(37)
                  trtl.end_fill()
                  trtl.color("Green")
                  trtl.forward(200)
                  trtl.left(90)


    if flower == "daisies" or flower == "daisy":
        trtl.goto(700,200)
        for _ in range(howmany-1):
                  trtl.pendown()
                  trtl.color("LightGrey")
                  trtl.fillcolor("White")
                  trtl.begin_fill()
                  trtl.circle(50)
                  trtl.end_fill()
                  trtl.fillcolor("Yellow")
                  trtl.begin_fill()
                  trtl.circle(25)
                  trtl.end_fill()
                  trtl.color("Green")
                  trtl.right(90)
                  trtl.forward(100)
                  trtl.right(90)
                  trtl.color("White")
                  trtl.forward(100)
                  trtl.penup()
                  trtl.right(180)

    if flower == "tulips" or flower == "tulip":
      trtl.goto(-200,200)
      for _ in range(howmany-1):
                trtl.pendown()
                trtl.fillcolor("Orange")
                trtl.begin_fill()
                draw_petal(Turtle, 100, 60)
                trtl.right(90)
                trtl.setheading(60)
                draw_petal(Turtle, 100, 60)
                trtl.right(90)
                trtl.setheading(120)
                draw_petal(Turtle, 100, 60)
                trtl.end_fill()
                trtl.right(150)
                trtl.color("green")
                trtl.forward(110)   
                trtl.right(270)

import turtle as trtl
OverflowError = trtl.Turtle()
    
trtl.mainloop()
