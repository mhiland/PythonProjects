import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import multiprocessing

resolution = 10.0
xRange = np.arange(0.0, 2.0, 0.01)


def calc_stuff(count):
	s0 = np.sin(2*np.pi*xRange + ((count/resolution)/2.0)*np.pi)
	s1 = np.sin(2*np.pi*xRange + ((count/resolution)/10.0)*np.pi)
	s2 = np.add(s0,s1)
	return s0, s1, s2

pool = multiprocessing.Pool(8)
out1, out2, out3 = zip(*pool.map(calc_stuff, range(0, 1000)))

for x in range(0, 1000):
	s1 = out1[x]
	s2 = out2[x]
	s3 = out3[x]

	plt.clf()
	plt.plot(xRange, s1)
	plt.plot(xRange, s2)
	plt.plot(xRange, s3)
	plt.ylim(-2, 2)

	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Superposition Example')
	plt.grid(True)
	plt.savefig("output/test{0:04d}.png".format(x))
