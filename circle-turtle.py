import turtle
tao = turtle.Pen()
tao.shape('turtle')

def Circle():
    for i in range(5):
        tao.circle(60)
        tao.left(80)

        
def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

    
Go(360,360)
Circle()
Go(200,0)
Circle()
Go(150,150)
Circle()
Go(150,150)
Go(200,200)
Circle()
Go(-150,-150)
Circle()
Go(-200,250)
Circle()
