import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import multiprocessing
from joblib import Parallel, delayed

def calc_stuff(count):
	s0 = np.sin(2*np.pi*xRange + ((count/resolution)/2.0)*np.pi)
	s1 = np.sin(2*np.pi*xRange + ((count/resolution)/10.0)*np.pi)
	s2 = np.add(s0,s1)
	return s0, s1, s2

def plot_stuff(x):
	plt.clf()
	plt.plot(xRange, out1[x])
	plt.plot(xRange, out2[x])
	plt.plot(xRange, out3[x])
	plt.ylim(-2, 2)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Superposition Example')
	plt.grid(True)
	plt.text(1.75, 1.75, 'frame: {0}'.format(x))
	plt.savefig("output/test{0:04d}.png".format(x))


inputs = range(1000)
num_cores = multiprocessing.cpu_count()
resolution = 10.0
xRange = np.arange(0.0, 2.0, 0.01)

pool = multiprocessing.Pool(8)
out1, out2, out3 = zip(*pool.map(calc_stuff, range(0, 1000)))

Parallel(n_jobs=num_cores)(delayed(plot_stuff)(i) for i in inputs)
