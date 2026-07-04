# Employee Management System (Python OOP)

## 📌 Project Description

Employee Management System is a simple command-line application developed in Python using Object-Oriented Programming (OOP) concepts.

The project allows users to create and manage different types of employees such as Employees, Managers, and Developers. It demonstrates important OOP concepts like inheritance, method overriding, constructors, and polymorphism.

---

## 🚀 Features

- Create a normal Employee
- Create a Manager
- Create a Developer
- Display Employee Details
- Display Manager Details
- Display Developer Details
- Menu-driven program
- Stores multiple employee objects using lists
- Uses Inheritance and Method Overriding

---

## 🛠 Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

---

## 📚 OOP Concepts Used

### 1. Class
- Employee
- Manager
- Developer

### 2. Object
Objects are created from each class and stored inside lists.

Example:

```python
eobj = Employee(...)
mobj = Manager(...)
dobj = Developer(...)
```

---

### 3. Constructor (__init__)

Used to initialize object data.

Example:

```python
def __init__(self, name, age, employee_id, salary):
```

---

### 4. Inheritance

Manager and Developer inherit all properties from Employee.

```python
class Manager(Employee):
```

```python
class Developer(Employee):
```

---

### 5. Method Overriding

Both Manager and Developer override the `showInfo()` method.

```python
def showInfo(self):
```

---

### 6. Encapsulation (Protected Members)

Protected variables are used.

```python
self._name
self._age
self._employee_id
self._salary
```

---

### 7. Polymorphism

The same method (`showInfo()`) behaves differently for different classes.

---

## 📂 Project Structure

```
Employee Management System
│
├── Employee Class
│
├── Manager Class
│
├── Developer Class
│
├── Menu Driven Program
│
└── README.md
```

---

## ▶️ How to Run

1. Install Python 3.
2. Save the program as:

```
employee_management.py
```

3. Open Terminal or Command Prompt.

4. Run the program:

```bash
python employee_management.py
```

---

## 📋 Menu

```
Choose an operation:

1. Create an Employee
2. Create a Manager
3. Create a Developer
4. Show Details
5. Exit
```

---

## 💻 Sample Output

```
Choose an operation:

1. Create an Employee
2. Create a Manager
3. Create a Developer
4. Show Details
5. Exit

Enter your choice: 1

Enter Name : John
Enter Age : 25
Enter Employee ID : EMP101
Enter Salary : 50000

Employee created with Name : John,
Age : 25,
Employee ID : EMP101
Salary : 50000
```

---

## 📊 Data Storage

Objects are stored in three different lists.

```python
emp = []
man = []
dev = []
```

---

## 📌 Classes

### Employee

Attributes

- Name
- Age
- Employee ID
- Salary

Methods

- `__init__()`
- `showInfo()`

---

### Manager

Inherits Employee

Additional Attribute

- Department

Methods

- `showInfo()`

---

### Developer

Inherits Employee

Additional Attribute

- Programming Language

Methods

- `showInfo()`

---

## 🎯 Learning Outcomes

This project helps understand:

- Python Classes
- Objects
- Constructors
- Inheritance
- Method Overriding
- Polymorphism
- Protected Members
- List of Objects
- Menu-driven Programming

---

## 🔮 Future Improvements

- Update Employee Details
- Delete Employee
- Search Employee by ID
- File Handling
- JSON Database
- CSV Storage
- Exception Handling
- Salary Increment Feature
- Employee Count
- GUI using Tkinter
- MySQL Database Integration

---

## 👨‍💻 Author

**Mishva Thesiya**

Python OOP Project

---

## 📄 License

This project is created for learning and educational purposes.