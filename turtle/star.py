from turtle import *
color('red','steelblue')
begin_fill()

def star(l):
    for i in range(8):
        forward(l)
        right(135)

star(300)
end_fill()
done()
