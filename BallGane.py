class Ball():

    def __init__(self):
        self.balls = []

    def show(self,x,y):
        self.balls.append(x)
        self.balls.append(y)
        print(self.balls)


b1 = Ball()
b1.show(10,12)

b2 = Ball()
b2.show(100,100)
