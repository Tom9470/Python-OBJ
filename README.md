# Python-OBJ
A simple library for creating basic WaveFront OBJ models from heightmaps stored as 2 dimensional nested lists.

## Installing
Run:

`pip install HM2OBJ`

## Usage

Python-OBJ contains 2 functions for creating OBJ files, One for creating a surface, and one for creating an object with walls and a base.

First, import the package with:

`import OBJ`

To create a surface, run:

`OBJ.CreateSurface(filename,data)`

Where `filename` is the filename of the target object, and `data` is the 2 dimensional nested list of the heightmap.

To create an Object, run:

`OBJ.CreateObject(filename,data)`

Where `filename` is the filename of the target object, and `data` is the 2 dimensional nested list of the heightmap.
