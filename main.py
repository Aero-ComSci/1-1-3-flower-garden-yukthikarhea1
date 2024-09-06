#CODE THAT WORKS SO FAR
from turtle import screesi

def draw_petal():
  """Draws a single petal."""
  trtl.color("LightPink")
  trtl.begin_fill()
  trtl.circle(25, 180)  # Draw half-circle petal
  trtl.right(180)
  trtl.circle(25, 180)  # Draw the other half-circle petal
  trtl.end_fill()
  trtl.left(90) 
  for _ in range(6):  # 6 petals
    trtl.forward(50)  # Move to petal start position
    draw_petal()      # Draw a single petal
    trtl.right(60)    # Rotate for the next petal
    trtl.penup()
    trtl.backward(50) # Move back to the center
    trtl.pendown()

flower = ""
howmany = 0

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
  #pi[n].isnumeric():
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
      print("Sorry, we don't have that flower.")
    import turtle as trtl
    OverflowError = trtl.Turtle()
    trtl.penup()
    trtl.goto(100,200)
    if flower == "roses" or flower == "rose":
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
        
