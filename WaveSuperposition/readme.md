
# Python Plotting and Optimization Project

This project was used to generate a video demonstration of two sinusoidal waves with constructive and destructive interference. see https://youtu.be/JUPs-31VVH4

The video is a composite of 1000 png images from which a mp4 video was created with ffmpeg.

The first script took nearly 3 minutes to run but with some optimization the time was cut down to ~20 seconds (8-core 4GHz). 

## SinWaveSuperPosition.py
While-loop for sequential data calculation, plot generating, and plot write to disk. 

## SinWaveSuperPosition_parallel_1.py
- Data calculation method extracted and run in parallel using multiprocessing.
- Initial calculations took <1 second but now there is overhead with data copying ~1 second.
- ffmpeg using cuda.

## SinWaveSuperPosition_parallel_2.py
- Large performance boost from writing images to disk in parallel.

## SinWaveSuperPosition_parallel_3.py
- Performance boost from matplotlib updating plot data rather than clearing and recreating figure.

![alt text](https://raw.githubusercontent.com/mhiland/PythonProjects/master/WaveSuperposition/includes/OptimizationChart.png)

