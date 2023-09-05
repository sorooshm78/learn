# .NET
Every C# file start *.cs

*.cs -> C# compiler -> *.dll

*.csproj file representing the project

dll -> Dynamic Link Library

A Dynamic Link library (DLL) is a library that contains functions and codes that can be used by more than one program at a time. 
Once we have created a DLL file, we can use it in many applications. 
The only thing we need to do is to add the reference/import the DLL File. 
Both DLL and .exe files are executable program modules but the difference is that we cannot execute DLL files directly.

Dynamic-Link Library (DLL) is a shared library concept that was introduced in the Microsoft Windows Operating System. DLLs are collections of code, data, and resources that can be used by multiple applications simultaneously. They offer several advantages over static libraries, such as reduced memory consumption, faster startup time, and easier maintenance. In this article, we will see what a DLL is in C# and how it can be used to build modular and extensible applications.

# What is a DLL?
A DLL is a binary file that has code and data that can be utilized by multiple applications at the same time. The DLL is loaded into the memory of each application that uses it, and the code and data can be accessed by those applications as if they were part of the application's code. This makes DLLs a powerful tool for building modular and extensible applications.

A DLL can contain any type of code or data that can be used by an application, including functions, classes, variables, and resources. When an application needs to use a DLL, it loads the DLL into memory and calls the functions or uses the data it contains. Once the application is done with the DLL, it can unload it from memory.

In C#, a DLL is a compiled assembly that contains .NET Framework code. It is created by compiling one or more C# source files into a DLL file. The DLL file can then be referenced by other C# projects, allowing them to use the code and data that it contains

## Advantages of Using DLLs in C#:
There are several advantages to using DLLs in C#:

* Reusability:

DLLs allow code to be shared between multiple applications. This can help reduce development time and improve code maintainability.

* Modularity:

DLLs allow code to be organized into separate modules, each of which can be loaded and unloaded independently. This can help reduce memory usage and improve application startup time.

* Extensibility:

DLLs can be used to add functionality to an application without modifying its existing code. This can be useful for adding plugins or extensions to an application.

* Versioning:

DLLs can be versioned, which allows different versions of a DLL to be used by different applications. This can help prevent compatibility issues between applications that use different versions of the same DLL.

## Conclusion:
DLLs are a powerful tool for building modular and extensible applications in C#. They allow code to be shared between multiple applications, organized into separate modules, and added to an application without modifying its existing code. Creating a DLL in C# is a straightforward process that involves creating a new project, adding code to the project, building the project, and referencing the DLL file from other C# projects. Once a DLL has been created and referenced, its code and data can be accessed by other applications as if they were part of the application's own code.

## Compile C# Code
```
csc filename.cs
```

# C# Variables
Variables are containers for storing data values.

In C#, there are different types of variables (defined with different keywords), for example:

int - stores integers (whole numbers), without decimals, such as 123 or -123
double - stores floating point numbers, with decimals, such as 19.99 or -19.99
char - stores single characters, such as 'a' or 'B'. Char values are surrounded by single quotes
string - stores text, such as "Hello World". String values are surrounded by double quotes
bool - stores values with two states: true or false

## Declaring (Creating) Variables
To create a variable, you must specify the type and assign it a value:

```
type variableName = value;
```

### Convention C# for variable name lower camel case
```
int isExist = true;
```

### Expilicitly Typed Variable
```
int newNumber1 = 10;
string newName1 = "soroush";
```

### Impilicitly Typed Variable
```
var newNumber2 = 100;
var newName2 = "soroush";
```
```
var name; // Error
```

# Comment

Single Line 
```
// single comment
comment -> Ctrl + k + c
uncomment -> Ctrl + k + u 
```


# And, Or Operators
```
int number = 18
isValid = number < 20 || number > 30 
// number < 20 is true and number > 30 not check for optimized
```

```
int number = 18
isValid = number > 20 && number < 30 
// number > 20 is false and number < 30 not check for optimized
```

/**This optimized called short-circutting**/


