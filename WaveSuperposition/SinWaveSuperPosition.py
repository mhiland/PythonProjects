import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

count = 0
resolution = 10.0
while (count < 100*resolution):
	xRange = np.arange(0.0, 2.0, 0.01)
	s0 = np.sin(2*np.pi*xRange + ((count/resolution)/2.0)*np.pi)
	s1 = np.sin(2*np.pi*xRange + ((count/resolution)/10.0)*np.pi)
	s2 = s0+s1
	
	plt.clf()
	plt.plot(xRange, s0)
	plt.plot(xRange, s1)
	plt.plot(xRange, s2)
	plt.ylim(-2, 2)

	plt.xlabel('x')
	plt.ylabel('y')
	plt.text(1.75, 1.75, 'frame: {0}'.format(count))
	plt.title('Superposition Example')
	plt.grid(True)
	plt.savefig("output/test{0:04d}.png".format(count))
	count = count + 1
