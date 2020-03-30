import matplotlib
matplotlib.use('TkAgg')

import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from animate import camera, alg_title, graph_title, Plot


def BubbleSort(data):
    # repeat until no swaps
    swapped = True
    while swapped:
        swapped = False
    # check from 0 to n-2
        for i in range( len( data ) - 1 ):
    # swap if i-th and (i+1)-th element out of order
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
    Plot(i + 1, data)

def insertionSort( data):
    count=0
    for i in range( 1, len( data ) ):
        elem = data.pop( i )
        insertPos = i
        for j in range(i):
            if elem < data[j]:
                insertPos = j
                break
        data.insert(insertPos, elem )
    Plot(data)

def selectionSort(data):
    for i in range( len( data ) ):
        min = i
        for j in range( i + 1, len( data ) ):
            if data[j] < data[min]:
                min = j
                data[i], data[min] = data[min], data[i]
    Plot(data)

try:
    data_size = int(input('Data size(defaut 30):'))
except ValueError:
    data_size = 30

data = random.sample(range(data_size), data_size)

algorithms = {'1': BubbleSort, '2': insertionSort, '3': selectionSort}

alg = input('Select the a;gorithm: (1)BubbleSort, (2)InsertionSort, (3) SelectionSort')

gph = input('Select the graph(1 for bar, 2 for scatter):')

graph_title(gph)
alg_title(alg)

func = alogrithms[alg]

func(data)

interval_time = 20
animation = camera.animate(interval=interval_time)

# To save as gif install imagemagick, to save as mp4 install ffmpeg(if not already installed)
if save:
    #animation.save('animation.gif', dpi=60, writer='imagemagick')
    animation.save('animation.mp4')

plt.show()
