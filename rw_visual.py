import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    #    只要程序处于活动状态，就不断的模拟随机漫步
    rw = RandomWalk(500000)
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values,rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none',s=1)

    # plt.scatter(rw.x_values, rw.y_values, s=15)

    plt.scatter(0,0, c='green',edgecolors='none',s=100)
    plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',edgecolors='none',s=2)
    plt.show()

    keep_running = input("make another walk? (y/n):")
    if keep_running == 'n':
        break