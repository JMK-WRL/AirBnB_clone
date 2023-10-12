# AirBnB Clone - The Console

## Project Description

This project is an implementation of a command-line interpreter for an AirBnB clone. The interpreter allows users to create, manage, and interact with various data models, such as User, State, City, Place, Amenity, and Review.

## Command Interpreter

### How to Start

To start the command interpreter, follow these steps:

1. Clone the project repository from [GitHub](https://github.com/JMK-WRL/AirBnB_clone.git).
2. Navigate to the project directory in your terminal.

### How to Use

The command interpreter supports various commands to interact with the available data models. Here's a list of commands and their usage:

- **create**: Create a new instance of a specified class and save it to the JSON file.
  - Usage: `create <class name>`
  
- **show**: Print the string representation of an instance based on the class name and ID.
  - Usage: `show <class name> <id>`
  
- **destroy**: Delete an instance based on the class name and ID (save the change into the JSON file).
  - Usage: `destroy <class name> <id>`
  
- **all**: Print all string representations of instances based on the class name or all instances.
  - Usage: `all [<class name>]`
  
- **update**: Update an instance based on the class name and ID by adding or updating an attribute (save the change into the JSON file).
  - Usage: `update <class name> <id> <attribute name> "<attribute value>"`
  
- **quit/EOF**: Quit the program.

### Examples

Here are some examples of how to use the command interpreter:

1. Creating a User instance:


2. Showing a User instance by ID:


3. Deleting a User instance by ID:


4. Listing all instances of a class:

5. Updating an instance's attribute:


6. Quitting the program:



## Authors

Victor Njeru | Email: [ynwvroy](mailto:bennetfrmdao@gmail.com)

Jonathan Kyule | Email: [JMK-WRL](mailto:jonathankyule2@gmail.com)
                