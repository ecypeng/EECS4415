# DELETE AFTER. TESTING BUT NOT IT

import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import style

style.use('ggplot') # visually apealing
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# i = interval
# uses iterable frames 
def animate(i):
	graph_data = open('graph_data.txt','r').read() #reads line in file
	lines = graph_data.split('\n')
	xs = []
	ys = []
	for line in lines:
		if len(line) > 1:
			x,y = line.split() # split hashtag and count
			xs.append(x)
			ys.append(int(y))
	ax.clear()
	ax.barh(xs, ys, align='center', color='red') #horizontal bar graph
	ax.set_xlabel('# Occurrences', fontsize=13)
	ax.plot()

ani = animation.FuncAnimation(fig, animate, interval=2000) #call animate function, interval = 2sec
#plt.tight_layout()
plt.show()
