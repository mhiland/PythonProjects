import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import multiprocessing
from joblib import Parallel, delayed
from numpy import cos, sin

res=6000.0
inputs = range(np.int(res))
t = np.arange(-100.0, 100.0, 0.01)
k = 1

def initialize_plot():	
	global fig, text, line1, line2, line3 
	fig = plt.figure()
	plt.xlim(-1, 1)
	plt.ylim(-1, 1)
	plt.xlabel(r'x = cos(K$\theta$)cos($\theta$)')
	plt.ylabel(r'y = cos(k$\theta$)sin($\theta$)')
	plt.title('Rhodonea Curve')
	plt.grid(True)
	ax = fig.add_subplot(111)
	text = plt.text(0.70, 1.05, 'k: {0}/{1}'.format(0,res))
	line1, = ax.plot(0, 0, 'r-')

def calc_stuff(count):
	x = cos((count/res)*t)*cos(t)
	y = cos((count/res)*t)*sin(t)
	return x, y

def plot_stuff(x):
	line1.set_xdata(out1[x])
	line1.set_ydata(out2[x])
	text.set_text('k: {0}/{1}'.format(x,res))
	fig.savefig("output/test{0:04d}.png".format(x))

def main():
	global out1, out2
	num_cores = multiprocessing.cpu_count()
	pool = multiprocessing.Pool(num_cores)
	out1, out2 = zip(*pool.map(calc_stuff, inputs))

	initialize_plot()
	Parallel(n_jobs=num_cores)(delayed(plot_stuff)(i) for i in inputs)

if __name__ == "__main__":
    main()
