# L-system with python
2D and 3D drawing of L-system on python, using the turtle module of python for 2D drawings and "Géotortue" (http://geotortue.free.fr/index.php) for 3D drawings

The code of the project is in python/ and the book (pdf version) on which the project is based is located in doc/.

## Examples of figures obtained :

### With bracketed L-system:
![fig2](doc/fig2.png)

### With stochastic L-system:
* Two examples at level 4 :

![fig3-1](doc/fig3-1.png)
![fig3-2](doc/fig3-2.png)

* And two examples of the same l-system at level 7 :

![fig4-1](doc/fig4-1.png)
![fig4-2](doc/fig4-2.png)

### In 3D:

We can extend the L-system to 3D by adding new symbols to control the rotation of the turtle :

![vectors](doc/3d_turtle.png)

With this we can now draw flowers :

![fig5-1](doc/fig5-1.png)
![fig5-2](doc/fig5-2.png)

And by adding parameters to the different growth functions, we can draw real plants. Here we draw the *Capsella bursa-pastoris* :
* At level 15 :

![fig6-1](doc/fig6-1.png)
* At level 25 :

![fig6-2](doc/fig6-2.png)
