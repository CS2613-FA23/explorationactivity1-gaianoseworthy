 # NetworkX
 ## A Network Creation, Manipulation, and Study Package for Python 3
 ## By Gaia Noseworthy - 3554411

 ### Introduction
 In this GitHub repo, you will be introduced to NetworkX, a Python 3 library for the generation, manipulation, and study of various networks. In this document, you will find a summary of this repo, which will include both a wiki section to answer common questions, as well as sample code that serves a rough purpose for both demonstration and usage of NetworkX.

 ### How To Use
 If you wish to run the code here, you will need to install NetworkX in some way. If you are in a Linux distribution like Arch or Ubuntu, this may be as simple as running one of the following:

 UBUNTU
 ```
 apt-get install networkx
 ```

 MANJARO
 ```
 pamac install networkx
 ```

 In general, you may also decide to use Pip to install your Python packages. In this case, you can run the following code
 ```
 pip install networkx[default]
 ```

 You can then import NetworkX into Python using
 ```Python
 import networkx as nx
 ```

 The sample program in this repo will include that import statement, so it does not need to be included for running the sample.

 ### Purpose
 The provided code in this repo will exist to complete 2 tasks:
 1. It will generate and compare a few primary graphs, showing their average level of connectivity and how they look. The wiki section will cover why the particular graphs were chosen.
 2. It will allow the user to generate or import a graph, which will then be saved as a file titled "UserGraph.txt" if it was generated. This graph will then be drawn, and details about the graph (average shortest path length, connectivity, and so on) will be calculated and shown to the user.

 ### Sample Input/Output
