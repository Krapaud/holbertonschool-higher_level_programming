# Python - Import & modules

This project focuses on understanding Python modules, imports, and command line arguments. It covers the fundamentals of code organization and reusability in Python.

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, **without the help of Google**:

### General
* Why Python programming is awesome
* How to import functions from another file
* How to use imported functions
* How to create a module
* How to use the built-in function `dir()`
* How to prevent code in your script from being executed when imported
* How to use command line arguments with your Python programs

## Requirements

### General
* Allowed editors: `vi`, `vim`, `emacs`
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using `wc`

## Files

This directory contains Python scripts that demonstrate various aspects of imports and modules:

* **0-add.py**: Program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result
* **1-calculation.py**: Program that imports functions from the file `calculator_1.py`, does some Maths, and prints the result
* **2-args.py**: Program that prints the number of and the list of its arguments
* **3-infinite_add.py**: Program that prints the result of the addition of all arguments
* **4-hidden_discovery.py**: Program that prints all the names defined by the compiled module `hidden_4.pyc`
* **5-variable_load.py**: Program that imports the variable `a` from the file `variable_load_5.py` and prints its value

## Usage

To run any of these scripts:

```bash
./script_name.py [arguments]
```

Example:
```bash
./2-args.py Hello Holberton School
```

## Author

This project is part of the Holberton School curriculum.
