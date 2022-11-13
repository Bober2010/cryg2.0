x = 0
def setup():
    size(400,400)
def draw():
    global x
    fill(1,x)
    triangle(220,130,160,220,280,220)
    x += 1
