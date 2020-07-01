![AirBnB clone - The console](https://github.com/tatsOre/AirBnB_clone/blob/master/cover_hbnb.png)

## Description 

## Installation
All files are interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
* Clone repository: git clone "https://github.com/tatsOre/AirBnB_clone.git"
* Access to AirBnb directory: cd AirBnB_clone

## Execution
The console executes in non-interactive mode:
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb) 
$
```
But also in interactive mode: **Use help command followed by < command > to get specific information about usage**
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help create

        Create command to create a new instance according Class name.
        Print the assigned id.
        Usage: create <class name>
        Classes: [BaseModel, User, Place, State, City, Amenity, Review]
        
(hbnb) 
(hbnb) quit
$
```
## Command interpreter options:
* **create** - Creates a new instance based on the < class name >, saves it (to a JSON file) and prints the < id >. Ex: `$ create BaseModel`
* **show** - Prints the string representation of an instance based on the < class name > and < id >. Ex: `$ show BaseModel 1234-1234-1234`
* **destroy** - Deletes an instance based on the < class name > and < id > (saves changes into a JSON file). Ex: `$ destroy BaseModel 1234-1234-1234`
* **all** - Prints all string representation of all instances based or not on the < class name >. Ex: `$ all BaseModel` or `$ all`
* **update** - Updates an instance based on the < class name > and < id > by adding or updating attribute (saves changes into a JSON file). Ex: `$ update BaseModel 1234-1234-1234 email "aibnb@holbertonschool.com"`
* **EOF** - Quits the program by EOF (CTRL+D).
* **quit** - Exits the console.
* < emptyline > - Replaces default emptyline(), with an empty line + ENTER.

## Examples of use
```bash
$ ./console.py
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb)
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2020, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2020, 10, 2, 3, 10, 25, 903300)}"]
(hbnb)
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2020, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2020, 10, 2, 3, 10, 25, 903300)}
(hbnb)
```

```bash
$ ./console.py
(hbnb) destroy
** class name missing **
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
(hbnb)
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2020, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2020, 10, 2, 3, 10, 25, 903300)}
(hbnb) destroy
** class name missing **
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'first_name': 'Betty', 'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2020, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2020, 10, 2, 3, 11, 3, 49401)}
(hbnb)
```
*  **Count instances and update from dictionary** - update an instance based on its ID with a dictionary: 
```bash
$ ./console.py
(hbnb) User.all()
["[User] (2fcc6d8d-ec16-4155-8683-ea92b9ab583b) {'id': '2fcc6d8d-ec16-4155-8683-ea92b9ab583b', 'created_at': datetime.datetime(2020, 6, 30, 15, 57, 55, 166650), 'updated_at': datetime.datetime(2020, 6, 30, 15, 57, 55, 166675)}", "[User] (785e3e40-8afd-443f-a737-4cfa475cc70c) {'id': '785e3e40-8afd-443f-a737-4cfa475cc70c', 'created_at': datetime.datetime(2020, 6, 30, 15, 58, 0, 386424), 'updated_at': datetime.datetime(2020, 6, 30, 15, 58, 0, 386444)}"]
(hbnb) User.count()
2
(hbnb) User.destroy("2fcc6d8d-ec16-4155-8683-ea92b9ab583b")
(hbnb) User.count()
1
(hbnb) User.destroy("Goodbye to All")
** no instance found **
(hbnb)
(hbnb) User.update("785e3e40-8afd-443f-a737-4cfa475cc70c", {'first_name': "Susie", 'age': 35, 'fav_band': "Joy Division"})
(hbnb) all
["[User] (785e3e40-8afd-443f-a737-4cfa475cc70c) {'id': '785e3e40-8afd-443f-a737-4cfa475cc70c', 'created_at': datetime.datetime(2020, 6, 30, 15, 58, 0, 386424), 'updated_at': datetime.datetime(2020, 6, 30, 15, 58, 0, 386444), 'first_name': 'Susie', 'age': 35, 'fav_band': 'Joy Division'}"]
```

### Project Learning Objectives:
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