# AirBnB clone - The console

## Description

This is ALX program team project which is the first step for creating a full web application:an AirBnB clone. It consists command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging) and for data management, and the base classes for the storage of this data.

# Command interpreter

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

## Installation

- Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/AirBnB_clone.git
```

## Usage

The console works both in interactive mode and non-interactive mode, much like a Unix shell. It prints a prompt (hbnb) and waits for the user for input.

## How to Start the Console

- Navigate to the project directory:

```bash
cd AirBnB_clone
```

- Start the console by running:

```bash
./console.py
```

```python
(hbnb)
```

## How to Use the Console

- Once the console is running, you can enter commands in the following format:

- commands: The action to perform

  - create - Creates an instance based on given class

  - destroy - Destroys an object based on class and UUID

  - show - Shows an object based on class and UUID

  - all - Shows all objects the program has access to, or all objects of a given class

  - update - Updates existing attributes an object based on class name and UUID

  - quit - Exits the program (EOF will as well)
  - help - this action is provided by default by cmd but you should keep it updated and documented as you work through tasks

- class: The name of the class of the object e.g.

  - BaseModel
  - User
  - Place
  - City
  - State
  - Amenity
  - Review

## Examples

- Create a new User:

```python
(hbnb) create class
```

- Show details of a specific User:

```python
(hbnb) show class user_id
```

- Update a User's information:

```python
(hbnb) update class user_id attribute new_value
```

- Delete a User:

```python
(hbnb) destroy class user_id
```

- Display all instances of a class:

```python
(hbnb) class.all()
```

- Quit the console:

```python
(hbnb) quit
```

- Get help on using the console:

```python
(hbnb) help
```

## Models

- directory will contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.

## File Storage

- Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

- In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

## Tests

- directory will contain all unit tests.
