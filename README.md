# 0x00. AirBnB clone - The console
### Execution
The console works like this in interactive mode:
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
But also in non-interactive mode:
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
### Learning Objectives:
* How to create a Python package
* How to create a command interpreter in Python using the cmd module
* What is Unit testing and how to implement it in a large project
* How to serialize and deserialize a Class
* How to write and read a JSON file
* How to manage `datetime`
* What is an `UUID`
* What is `*args` and how to use it
* What is `**kwargs` and how to use it
* How to handle named arguments in a function

### Resources:
* [Python cmd Module](https://docs.python.org/3.4/library/cmd.html)
* [cmd – Create line-oriented command processors](https://pymotw.com/2/cmd/)
* [Python uuid Module](https://docs.python.org/3.4/library/uuid.html)
* [uuid — Universally Unique IDentifier](https://realpython.com/python-random/#one-last-candidate-uuid)
* [Python datetime Module](https://docs.python.org/3.4/library/datetime.html)
* [Datetime Module](https://realpython.com/python-datetime/#using-the-python-datetime-module)
* [Unit testing framework](https://docs.python.org/3.4/library/unittest.html#module-unittest)
* [Python Tutorial: Unit Testing Your Code with the unittest Module](https://www.youtube.com/watch?v=6tNS--WetLI&start=1828s)
* [A simple Python unittest](https://www.pythonsheets.com/notes/python-tests.html)
* [Args & Kwargs](https://realpython.com/python-kwargs-and-args/)
* [Python Packages](https://realpython.com/python-modules-packages/#python-packages)
* [How To Use *args and **kwargs in Python 3](https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3)

### Authors:
* Juan Felipe Bustamante Muñoz | [Github](https://github.com/jfbm74)
* Tatiana Orejuela Zapata | [Github](https://github.com/tatsOre)

##### Foundations - Higher-level programming ― AirBnB clone
##### June, 2020. Cali, Colombia.