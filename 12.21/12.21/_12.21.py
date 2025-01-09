'''
import matplotlib.pyplot as plt
x_volue=[1,2,3,4]
y_volte=[11,22,33,44]
fig,ax=plt.subplots()
ax.plot(x_volue,y_volte,linewidth=3)
#set tab label biaoqian

ax.set_title('time',fontsize=14)
ax.set_xlabel('value',fontsize=14)
#set gap jiange
ax.tick_params(axis='both',labelsize=14)


plt.show()

import matplotlib.pyplot as plt
x_volue=[1,2,3,4]
y_volte=[11,22,33,44]
fig,ax=plt.subplots()
ax.scatter(x_volue,y_volte,c=y_volte,cmap=plt.cm.Blues,s=222)
ax.axis([1,5,6,50])
plt.show()
'''
from io import BufferedRWPair
from random import choice

class RandomWalk:
        def __init__(self,num_points=4333):
            self.num_points=num_points
            self.x_values=[0]
            self.y_values=[0]
        def fill_walk(self):
                        while len(self.x_values)<self.num_points:
                            x_dirction=choice([1,-1])
                            x_distance=choice([0,1,2,3,4])
                            x_step=x_dirction*x_distance
                            y_dirctio=choice([1,-7])
                            y_distanc=choice([0,1,2,3,4])
                            y_step=y_dirctio*y_distanc
                            if x_step==0 and y_step==0:
                                continue
                            x=self.x_values[-1]+x_step
                            y=self.y_values[-1]+y_step
                            self.x_values.append(x) 
                            self.y_values.append(y)
pan=True
while pan:
    import matplotlib.pyplot as plt
    rw=RandomWalk()
    rw.fill_walk()
    fig,ax=plt.subplots()
    ax.scatter(rw.x_values,rw.y_values,s=15)
    plt.show()
    pa=input('t/c')
    if pa=='t':
        pan=False
    else:
        pan=True
                         