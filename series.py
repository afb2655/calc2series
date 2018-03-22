"""
@Author: Aiden Buchheister
@File: series.py

This file will calculate whether a series converges or diverges, and plots the series
"""

import matplotlib.pyplot as plt
from statistics import mean



def seriesmaker(k,p0,iterations):
    """
    Seriesmaker makes the list for the series, at least the Y coordinates, by using a hardcoded function
    :param k: constant value
    :param p0: initial series value
    :param iterations: number of iteratiions
    :return: list of Y values of the series
    """
    serieslist = []
    serieslist.append(p0)
    i = 0
    temp = p0
    for i in range(iterations):
        temp = k * temp *(1-temp)
        serieslist.append(temp)
        i += 1
    return(serieslist)


def tuplecreator(k,p0,iterations):
    """
    Turns the series into tuples
    :param k: constant value
    :param p0: initial series value
    :param iterations: number of iterations
    :return: returns a list of tuples corresponding to 'X,Y' for the series
    """
    datalist = seriesmaker(k,p0,iterations)
    xlist = []
    x = 0
    xlist.append(x)
    i = 0
    for i in range(iterations):
        x+=1
        xlist.append(x)
        i += 1
    z = list(zip(xlist,datalist))
    return z



def grapher(k,p0,iterations):
    """
    Graphs the list of tuples using matplotlib
    :param k: constant for the series
    :param p0: initial series value
    :param iterations: number of iterations
    :return: returns none, only displays a graph and prints out the list of tuples that is the series
    """
    data = tuplecreator(k, p0, iterations)
    plt.scatter(*zip(*data))
    plt.xlabel('X axis')
    plt.ylabel('Y axis')
    i = 0
    Whys = []
    converge = True
    for i in range(len(data)):
        Whys.append(data[i][1])

    derivative = []
    for i in range(len(Whys)-1):
        derivative.append(Whys[i+1] - Whys[i])

    try:
        i = -3
        testerval = derivative[len(derivative)-1]
        converge = True
        while i < 0:
            if derivative[i] <= (testerval + .00001):
                i+=1
                continue
            else:
                converge = False
                break
    except IndexError:
        print("There was an index out of bounds error! add more iterations next time")

    # titlestring = ""
    if converge == True:
        titlestring = ('Plot of the series when k =', k, ' p0 =', p0, ' iterations =', iterations, ' Converges on ',Whys[len(Whys)-1])
    else:
        titlestring = ('Plot of the series when k =', k, ' p0 =', p0, ' iterations =', iterations, ' Does not converge')


    plt.title(titlestring)
    print("Series data for this specific series: ",data)
    plt.show()






if __name__ == '__main__':
    """
    Runs the program
    """
    grapher(2,.5,30) #K = 2, P0 = .5, Iterations = 30
    grapher(1.5,.5,30) #K = 1.5, P0 = .5, Iterations = 30
    grapher(2,.7,30) #K = 2, P0 = .7, Iterations = 30
    grapher(1.5,.7,30) #K = 1.5, P0 = .7, Iterations = 30
    print("\n****************************************************************")
    print("Limit does not matter with choice of p, only the choice of K")
    print("****************************************************************\n")

    grapher(3.3,.5,30) #K = 3.3, P0 = .5, Iterations = 30
    print("\n****************************************************************")
    print("If a K value is picked between 3 and 3.4, the series will never converge, but it will oscillate between "
          "two numbers")
    print("****************************************************************\n")

    grapher(3.8,.5,100) #K = 3.8, P0 = .5, Iterations = 100
    grapher(3.8,.501,100) #K = 3.8, P0 = .501, Iterations = 100
    print("\n****************************************************************")
    print("Changing P by .001 yielded a radically different graph, which is chaotic behavior")
    print("****************************************************************\n")

