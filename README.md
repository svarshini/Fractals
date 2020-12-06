# Fractals

![Cover Image](/results/mandeljulia.jpg)

## Overview
Fractals are among the most fascinating mathematical visuals capturing infinitely complex patterns that are self-similar and exhibit finer detail when magnified recursively. 

This project visualizes some of these fractals, particularly Julia Sets and the Mandelbrot Set. The latter popularly depicts the aesthetic beauty of mathematics. Fractals are witnessed in nature as well, in snowflakes, leaves and blood vessels, to name a few.

All images were generated using Python and the Python Imaging Library (PIL).

## Project Page

More details can be found at the project page - [Fractals](https://svarshini.github.io/index_project_fractal.html).


## Code Usage

### Julia Sets

The equation for Julia Sets is *z = z<sup>2</sup> + c* for a complex number *z* and constant *c*.

Modify the following parameters in *julia.py* to generate your own animations:

```
for angle in np.arange(start, stop, step):

c = complex(k1 + k2*math.sin(angle), k3*math.cos(angle))

```
Here, *start* and *stop* denote the angles to begin and stop the animation at, incremented by *step* for each Julia Set. 
The constant *c* can also be a complex number, which has constants *k1*, *k2* and *k3* in this case and is a parameter that can be tweaked arbitrarily. 

## Visualizations

### Julia Sets

<img src="/results/julia_1.png" width="512" height="272"/> 

<img src="/results/julia_3.png" width="512" height="272"/>

<img src="/results/julia_4.png" width="512" height="272"/>

<img src="/results/julia_7.png" width="512" height="272"/>


### Mandelbrot Set

The Mandelbrot Set  is also computed using the function *f(z) = z<sup>2</sup> + c*, except that *c* differs for each pixel. 
Thus the Mandelbrot Set can be considered as a map of all Julia Sets because it uses a different *c* at every location.

<img src="/results/mandelbrot.png" width="512" height="512"/>


## Animations

* Visualizing Julia Sets for varying values of the complex constant *c* = A + *i* B in *f(z)* = *z<sup>2</sup>* + *c*. 
Here, A = -1 + 0.3sin(θ) and B = 0.3cos(θ), with θ varying from 0 to 2Π, in increments of 15°.

<img src="/results/julia.gif" width="512" height="512"/>


