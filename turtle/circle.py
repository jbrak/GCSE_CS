from turtle import *
color('red')
begin_fill()

def circle(l):
    for i in range(360):
        forward(l)
        right(1)

circle(3)

end_fill()
done()
