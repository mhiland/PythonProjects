import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
from joblib import Parallel, delayed
from matplotlib.gridspec import GridSpec
import multiprocessing

numberOfFrames=4000.0
timeStep = range(np.int(numberOfFrames))
rho = 28.0
sigma = 10.0
beta = 8.0 / 3.0

def lorenzFunction(state, t):
  x, y, z = state
  return sigma * (y - x), x * (rho - z) - y, x * y - beta * z

def initialize_plot():	
	global fig, ax1, ax2, ax3, ax4
	fig = plt.figure()
	gs = GridSpec(3,3)
	ax1 = fig.add_subplot(gs[:-1, :], projection='3d')
	ax1.text2D(0.35, 0.95, 'Lorenz Attractor', transform=ax1.transAxes)
	ax1.set_xlabel('X Axis')
	ax1.set_ylabel('Y Axis')
	ax1.set_zlabel('Z Axis')
	ax1.set_xlim(-20,20)
	ax1.set_ylim(-20,20)
	ax1.set_zlim(0,50)

	ax2 = fig.add_subplot(gs[2,0])
	ax2.set_xlabel('X/Y Axis')
	#ax2.set_ylabel('Y Axis')
	ax2.set_xlim(-30,30)
	ax2.set_ylim(-30,30)

	ax3 = fig.add_subplot(gs[2,1])
	ax3.set_xlabel('X/Z Axis')
	#ax3.set_ylabel('Z Axis')
	ax3.set_xlim(-30,30)
	ax3.set_ylim(0,50)

	ax4 = fig.add_subplot(gs[2,2])
	ax4.set_xlabel('Y/Z Axis')
	#ax4.set_ylabel('Z Axis')
	ax4.set_xlim(-30,30)
	ax4.set_ylim(0,50)

def calc_stuff():
	inputs = np.arange(0.0, 40.0, 0.01)
	initialState = [1.0, 1.0, 1.0]
	return odeint(lorenzFunction, initialState, inputs)

def plot_stuff(t):
	p1, = ax1.plot(states[0:t,0], states[0:t,1], states[0:t,2], c='b')
	p2 = ax1.scatter(states[t,0], states[t,1], states[t,2], c='r')

	p3, = ax2.plot(states[0:t,0], states[0:t,1], c='b')
	p4 = ax2.scatter(states[t,0], states[t,1], c='r')

	p5, = ax3.plot(states[0:t,0], states[0:t,2], c='b')
	p6 = ax3.scatter(states[t,0], states[t,2], c='r')
	
	p7, = ax4.plot(states[0:t,1], states[0:t,2], c='b')
	p8 = ax4.scatter(states[t,1], states[t,2], c='r')

	fig.savefig("output/test{0:04d}.png".format(t))

	p1.remove()
	p2.remove()
	p3.remove()
	p4.remove()
	p5.remove()
	p6.remove()
	p7.remove()
	p8.remove()

def main():
	global states
	num_cores = multiprocessing.cpu_count()
	states = calc_stuff()
	initialize_plot()
	Parallel(n_jobs=num_cores)(delayed(plot_stuff)(t) for t in timeStep)

if __name__ == "__main__":
    main()

