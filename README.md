# Readme for the implementation of the console within the AirBnB clone project

## THE CONSOLE
The console is meant to be a command interpreter that will allow us to manage the AirBnB projects: HTML/CSS templating, database storage, API, front-end integration..

---
## LEARNING OBJECTIVES :
- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

---
## REQUIREMENTS :

### Pyton Scripts :
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation 
(python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").- MyClass.my_function.__doc__)')
- A documentation is not a simple word, its a real sentence explaining whats the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests :
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
- e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
- e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation 
(python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you dont miss any edge case

---
## EXECUTION :
- Your shell should work like this in interactive mode:

```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

- But also in non-interactive mode: (like the Shell in C):

```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

---
## DESCRIPTION OF THE COMMAND INTERPRETER :






---
## FILES

| File | Description |
| --- | --- |
| base_model.py | File that contains all attributes of the parent class BaseModel |
| file_storage.py | Class FileStorage that stores all objects that have been created into a json file so that they can be used by other programs |
| console.py | File that defines the console which will be the entry point of the
command interpreter |
| __init__.py | File that creates a unique FileStorage instance for the application |
| user.py | File that define a User class that sets the users infos  |
| amenity.py, city.py, place.py, review.py, state.py | Files that define the classes
of the main elements that will structure the AirBnB project |

---
## AUTHORS : 

Arsene Giriteka <giritekaaarsene@gmail.com>
Gilles Richard <gilles-richard76@hotmail.com>

