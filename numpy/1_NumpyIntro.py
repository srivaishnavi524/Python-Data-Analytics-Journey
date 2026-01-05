# what is numpy?
# numpy is a python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices.
# NumPy stands for numerical Python. 

# Why use of Numpy?
# In python we have lists that serve the purpose of arrays, but the are slow to process.
# numpy aims to provide an array object that is up to 50x faster that traditional python list.

# Why is numpy faster than lists?
# NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

# which language is NumPy written in?
# NumPy is a python library and written paritially in python, but most of the parts that required fast computation are written in C or C++

# Where is the numPy codebase?
# the source code for numpy is located at this github repository
#     https://github.com/numpy/numpy
    #    numpy.org

# Installation of NumPy
# pip install numpy
#  -m pip install numpy
#------------------------------------------------------
import numpy as np
print(np.__version__)
