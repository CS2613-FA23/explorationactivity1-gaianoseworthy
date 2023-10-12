 # NetworkX
 ## A Network Creation, Manipulation, and Study Package for Python 3
 ## By Gaia Noseworthy - 3554411

 ### Introduction
 In this GitHub repo, you will be introduced to NetworkX[1], a Python 3 library for the generation, manipulation, and study of various networks. In this document, you will find a summary of this repo, which will include both a wiki section to answer common questions, as well as sample code that serves a rough purpose for both demonstration and usage of NetworkX.

 ### How To Use
 If you wish to run the code here, you will need to install NetworkX in some way. If you are in a Linux distribution like Arch or Ubuntu, this may be as simple as running one of the following:

 **Ubuntu**
 ```
 apt-get install python3-networkx
 ```

 **Arch/Manjaro**
 ```
 pamac install python-networkx
 ```

 In general, you may also decide to use `Pip` to install your Python packages. In this case, you can run the following code
 ```Python
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
 #### Input
 Almost all of input and output for the provided code is handled automatically, except for the case of a user-inputed network. In this case, the file must meet the following structure requirements:
 ```
 NODE NODE {}
 NODE NODE {}
 NODE NODE {}
 ...
 NODE NODE {}
 ```

 The value of `NODE` should be a number indicating the identifier of the node.

 #### Output
 Almost all of the output of this code will be done either in the command line, through images, or by saving a file. Command line output will be formatted be allowing for user input, as follows:
 ```Bash
 Welcome to the NetwokX Demonstrator!

 Pick your desired option:
 1. Demonstrate a few NetworkX graphs
 2. Get network details using NetworkX
 q. Quit
 2
 Would you like to import a network? (y/n):  y
 Please input file path:  Example_Network.txt
 ```

 In the above example, "2", "y", and "Example_Network.txt" were typed by the user.

 The next major form of output is in the network graphs generated through MatPlotLib. Thus, it is recommended to run this code in an environment that allows for viewing of these plots. One option is Jupyter notebooks (in which this code was originally produced), but any IDE that shows Python plots is acceptable. The graphs will mostly appear as follows:
 ![Watts Strogatz Graph Example](Example.png)

 The final form of output is the same as the input, in an edge-network text file containing a list of which nodes are connected to each other. This will be formatted like above, but to give an example, here is a sample output:
 ```
 0 1 {}
 0 2 {}
 0 3 {}
 0 4 {}
 0 5 {}
 0 6 {}
 0 7 {}
 0 8 {}
 1 4 {}
 2 4 {}
 2 5 {}
 2 6 {}
 2 7 {}
 2 8 {}
 3 5 {}
 3 6 {}
 4 7 {}
 4 9 {}
 5 8 {}
 5 9 {}
 6 9 {}
 ```

 ### References
 [1] Aric A. Hagberg, Daniel A. Schult and Pieter J. Swart, “Exploring network structure, dynamics, and function using NetworkX”, in Proceedings of the 7th Python in Science Conference (SciPy2008), Gäel Varoquaux, Travis Vaught, and Jarrod Millman (Eds), (Pasadena, CA USA), pp. 11–15, Aug 2008

 ### License
 The NetworkX License is as follows:
 > Copyright (C) 2004-2023, NetworkX Developers
> Aric Hagberg <hagberg@lanl.gov>
> Dan Schult <dschult@colgate.edu>
> Pieter Swart <swart@lanl.gov>
> All rights reserved.

> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

> > * Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.

> > Redistributions in binary form must reproduce the above
    copyright notice, this list of conditions and the following
    disclaimer in the documentation and/or other materials provided
    with the distribution.

> > Neither the name of the NetworkX Developers nor the names of its
    contributors may be used to endorse or promote products derived
    from this software without specific prior written permission.

> THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
