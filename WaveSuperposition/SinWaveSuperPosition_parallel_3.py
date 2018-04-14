import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import multiprocessing
from joblib import Parallel, delayed

inputs = range(1000)
resolution = 10.0
xRange = np.arange(0.0, 2.0, 0.01)

def initialize_plot():	
	global fig, text, line1, line2, line3 
	fig = plt.figure()
	plt.xlim(0, 2)
	plt.ylim(-2, 2)
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Superposition Example')
	plt.grid(True)
	ax = fig.add_subplot(111)
	text = plt.text(1.75, 1.75, 'frame: {0}'.format(0))
	line1, = ax.plot(0, 0, 'r-')
	line2, = ax.plot(0, 0, 'g-')
	line3, = ax.plot(0, 0, 'b-')
	line1.set_xdata(xRange)
	line2.set_xdata(xRange)
	line3.set_xdata(xRange)

def calc_stuff(count):
	s0 = np.sin(2*np.pi*xRange + ((count/resolution)/2.0)*np.pi)
	s1 = np.sin(2*np.pi*xRange + ((count/resolution)/10.0)*np.pi)
	s2 = np.add(s0,s1)
	return s0, s1, s2

def plot_stuff(x):
	line1.set_ydata(out1[x])
	line2.set_ydata(out2[x])
	line3.set_ydata(out3[x])
	text.set_text('frame: {0}'.format(x))
	fig.savefig("output/test{0:04d}.png".format(x))

def main():
	global out1, out2, out3
	num_cores = multiprocessing.cpu_count()
	pool = multiprocessing.Pool(num_cores)
	out1, out2, out3 = zip(*pool.map(calc_stuff, inputs))

	initialize_plot()
	Parallel(n_jobs=num_cores)(delayed(plot_stuff)(i) for i in inputs)

if __name__ == "__main__":
    main()
