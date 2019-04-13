""" 15-1 Cubes """

#import matplotlib.pyplot as plt

#x_values = list(range(5000))
#y_values = [x**3 for x in x_values]

#plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Purples, s=40)

# Set chart title and label axes
#plt.title("Cubes", fontsize=24)
#plt.xlabel("Value", fontsize=14)
#plt.ylabel("Cube of Value", fontsize=14)

# Set size of tick labels
#plt.tick_params(axis='both', which='major', labelsize=14)

# Set range for each axis
#plt.axis([1, 5000, 0, 125_000_000_000])

#plt.show()

""" 15-3 """

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks as long as the program is active
while True:
	# Make a random walk, and plot the points
	rw = RandomWalk(5_000)
	rw.fill_walk()
	
	# Set the size of the plotting window 
	plt.figure(dpi=128, figsize=(10,6))
	
	point_numbers = list(range(rw.num_points))
	plt.plot(rw.x_values, rw.y_values, linewidth=5)
		
	# Remove the axes
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
		
	plt.show()
	
	keep_running = input("Make another walk? (y/n): ")
	if keep_running == 'n':
		break
