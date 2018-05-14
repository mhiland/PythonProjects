import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
from joblib import Parallel, delayed
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
	global fig, ax
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.text2D(0.35, 0.95, 'Lorenz Attractor', transform=ax.transAxes)
	ax.set_xlabel('X Axis')
	ax.set_ylabel('Y Axis')
	ax.set_zlabel('Z Axis')
	ax.set_xlim(-20,20)
	ax.set_ylim(-20,20)
	ax.set_zlim(0,50)

def calc_stuff():
	inputs = np.arange(0.0, 40.0, 0.01)
	initialState = [1.0, 1.0, 1.0]
	return odeint(lorenzFunction, initialState, inputs)

def plot_stuff(t):
	p1, = ax.plot(states[0:t,0], states[0:t,1], states[0:t,2], c='b')
	p2 = ax.scatter(states[t,0], states[t,1], states[t,2], c='r')
	fig.savefig("output/test{0:04d}.png".format(t))
	p1.remove()
	p2.remove()

def main():
	global states
	num_cores = multiprocessing.cpu_count()
	states = calc_stuff()
	initialize_plot()
	Parallel(n_jobs=num_cores)(delayed(plot_stuff)(t) for t in timeStep)

if __name__ == "__main__":
    main()

