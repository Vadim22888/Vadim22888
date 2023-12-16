x = 500
y = 500
def setup():
    size(1000,1000)
def draw():
    global x,y
    background(0)
    fill(random(255),random(255),random(255))
    ellipse(x,y,50,50)
    if key == 'd':
        x = x + 10
    if key == 's':
        y = y + 10
    if key == 'a':
        x = x - 10
    if key == 'w':
        y = y - 10
    if y > 1000: y = 500
    if y < 0: y = 500
    if x > 1000: x = 500
    if x < 0: x = 500
