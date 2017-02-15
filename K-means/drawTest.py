import matplotlib.pyplot as plot

def draw(xCords, yCords, keyword, pointerColor="black"):
    # size = len(self.data)
    plot.xlabel("x")
    plot.ylabel("y")
    plot.title("Initial Plot")
    plot.legend()
    plot.scatter(xCords, yCords, label="mainGraph", color=pointerColor, s=100)
    if keyword:
        plot.show()


x=[-2,-1,0,1,2,3,4,5,6]
y=[0,1,2,3,4,5,6,7,8]
z=[-5.39,-1.315,0,2.76,-2,-1,0]
u=[0,-4.151,-3.72,0,6,7,8]
draw(x,y,False,"red")
draw(z,u,True, "green")


'''
gap stastic, use this to find the optimal number of clusters
'''
