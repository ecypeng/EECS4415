# ## source: https://pythonprogramming.net/bar-chart-histogram-matplotlib-tutorial/
# ## https://pythonprogramming.net/live-graphs-matplotlib-tutorial/
# ## https://pythonprogramming.net/annotations-text-matplotlib-tutorial/?completed=/live-graphs-matplotlib-tutorial/

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

hashtagCount = {
    '#Ford': 0,
    '#Jeep': 0,
    '#Toyota': 0,
    '#nissan': 0,
    '#honda': 0
}

def animate(i):
    objects = []
    performance = []
    for key, value in hashtagCount.iteritems():
        objects.append(key)
        performance.append(value)
    y_pos = np.arange(len(objects))
    graph_data = open('graph_info_a.txt','r').read()
    lines = graph_data.split('\n')
    for line in lines:
        if len(line) > 1:
            hashtag, count = line.split()
            hashtagCount[hashtag] += int(count)
    print(hashtagCount)

    plt.bar(y_pos, performance, align='center')
    plt.xticks(y_pos, objects)
    plt.ylabel('Hashtag Count')
    plt.title('Hashtag Name')

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()
