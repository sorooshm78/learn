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

## C# Keywords
A keyword is a reserved word. You cannot use it as a variable name, constant name etc.

```
int class // class is reserved

int @class // not error
```


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


## Local Variable Scope
Code-Block Level Scope
A variable declared within a loop or any block within brackets has the code-block level scope. A variable declared within a loop or code block cannot be accessed outside of it, whereas a variable declared outside of the loop can be accessible within the loop.

```
class Program
{
    static void Main(string[] args)
    {
        int count = 0;
       
        for (int i = 0; i < 5; i++)
            Console.WriteLine(i);
        
        //Console.WriteLine(i); //can't access i because it has loop level scope
        
        if (count == 0)
        {
            count++; //can access method variables

            int x = 10; //declared block level variable
        }
        
        //Console.WriteLine(x); //can't access block level variable
    }
}
```

In the above example, a variable i declared within a for loop. So, it can only be accessed within the for loop block and cannot be accessed outside for loop. In the same way, x is declared within the if block, so it can only be accessed in that block but not outside of it.

A variable must be declared outside of the code block to make it accessible to outside code.

```
int a = 1;

if(true)
{
  var b = a + 1; // accessing a from outer scope
  int a = 2; // conflicts
}
```

Arg vs Param
```
void PrintHellow(string name) // name is param
{
    Console.WriteLine(name);
}

PrintHellow("sm") // "sm" is arg
```

## Type Casting
```
string str_num = "10";
int num = int.Parse(str_num);
Console.WriteLine(num++);
// 15
```

## String Interpolation
```
int number1 = 10
int number2 = 1
int sum = number1 + number2

Console.WriteLine($"{number1} + {number2} = {sum}");
// 10 + 1 = 11
```

# Char | String 
```
string str = "string"; // " -> String
char ch = 'A'; // ' -> Char
```


### Postfix increment operator
The result of x++ is the value of x before the operation, as the following example shows:
```
int i = 3;
Console.WriteLine(i);   // output: 3
Console.WriteLine(i++); // output: 3
Console.WriteLine(i);   // output: 4
```

### Prefix increment operator
The result of ++x is the value of x after the operation, as the following example shows:
```
int a = 1;
Console.WriteLine(a);   // output: 1
Console.WriteLine(++a); // output: 2
Console.WriteLine(a);   // output: 2
```

## Create an Array
If you are familiar with C#, you might have seen arrays created with the new keyword, and perhaps you have seen arrays with a specified size as well. In C#, there are different ways to create an array:
```
// Create an array of four elements, and add values later
string[] cars = new string[4];

// Create an array of four elements and add values right away 
string[] cars = new string[4] {"Volvo", "BMW", "Ford", "Mazda"};

// Create an array of four elements without specifying the size 
string[] cars = new string[] {"Volvo", "BMW", "Ford", "Mazda"};

// Create an array of four elements, omitting the new keyword, and without specifying the size
string[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
```

# Last Element
```
int[] array = { 1, 3, 5 };
var lastItem = array[^1]; // 5
var secondItem = array[^2] // 3
```

## Multidimensional Arrays
In the previous chapter, you learned about arrays, which is also known as single dimension arrays. These are great, and something you will use a lot while programming in C#. However, if you want to store data as a tabular form, like a table with rows and columns, you need to get familiar with multidimensional arrays.
A multidimensional array is basically an array of arrays.
Arrays can have any number of dimensions. The most common are two-dimensional arrays (2D).
Two-Dimensional Arrays
To create a 2D array, add each array within its own set of curly braces, and insert a comma (,) inside the square brackets:

```
int[,] numbers = { {1, 4, 2}, {3, 6, 8} };
```

Good to know: The single comma [,] specifies that the array is two-dimensional. A three-dimensional array would have two commas: int[,,].

## Access Elements of a 2D Array
To access an element of a two-dimensional array, you must specify two indexes: one for the array, and one for the element inside that array. Or better yet, with the table visualization in mind; one for the row and one for the column (see example below).

This statement accesses the value of the element in the first row (0) and third column (2) of the numbers array:

Example
```
int[,] numbers = { {1, 4, 2}, {3, 6, 8} };
Console.WriteLine(numbers[0, 2]);  // Outputs 2
```

## Change Elements of a 2D Array
You can also change the value of an element.

The following example will change the value of the element in the first row (0) and first column (0):

Example
```
int[,] numbers = { {1, 4, 2}, {3, 6, 8} };
numbers[0, 0] = 5;  // Change value to 5
Console.WriteLine(numbers[0, 0]); // Outputs 5 instead of 1
```

Loop Through a 2D Array
You can easily loop through the elements of a two-dimensional array with a foreach loop:

Example
```
int[,] numbers = { {1, 4, 2}, {3, 6, 8} };

foreach (int i in numbers)
{
  Console.WriteLine(i);
} 
```

You can also use a for loop. For multidimensional arrays, you need one loop for each of the array's dimensions.

Also note that we have to use GetLength() instead of Length to specify how many times the loop should run:

Example
```
int[,] numbers = { {1, 4, 2}, {3, 6, 8} };

for (int i = 0; i < numbers.GetLength(0); i++) 
{ 
  for (int j = 0; j < numbers.GetLength(1); j++) 
  { 
    Console.WriteLine(numbers[i, j]); 
  } 
} 
```

## foreach Loop
There is also a foreach loop, which is used exclusively to loop through elements in an array:
Syntax
```
foreach (type variableName in arrayName) 
{
  // code block to be executed
}
```

Example
```
string[] cars = {"Volvo", "BMW", "Ford", "Mazda"};
foreach (string i in cars) 
{
  Console.WriteLine(i);
}
```

## C# List
List<T> is a class that contains multiple objects of the same data type that can be accessed using an index. For example,
```
// list containing integer values 
List<int> number = new List<int>() { 1, 2, 3 };
```
Here, number is a List containing integer values (1, 2 and 3).

## out C#
The out parameter in C# is used to pass arguments to methods by reference. It differs from the ref keyword in that it does not require parameter variables to be initialized before they are passed to a method.
The out keyword must be explicitly declared in the method’s definition​ as well as in the calling method.

```
Declaration of out Parameter:  

// No need to initialize 
// the variable here
data_type variable_name;

Method_Name(out variable_name);

// you can also convert both above two 
// lines of codes as follows from
//  C# 7.0 onwards
Method_Name(out data_type variable_name);
```

```
void AddOne(int number)
{
    number += 1;
}

int number = 0;

Console.WriteLine($"number is {number}"); // 0
// pass by value
AddOne(number);
Console.WriteLine($"number is {number}"); // 0
```

```
void AddOne(out int number)
{
    number = 0; 
    number += 1;
}


// int number;
// AddOne(out number)
// or
// AddOne(out int number);

// pass by refrence
AddOne(out int number);
Console.WriteLine($"number is {number}"); // 1
```

The out is a keyword in C# which is used for the passing the arguments to methods as a reference type. It is generally used when a method returns multiple values.

* It is similar to ref keyword. But the main difference between ref and out keyword is that ref needs that the variable must be initialized before it passed to the method. But out parameter doesn’t require the variables to be initialized before it passed to the method. But before it returns a value to the calling method, the variable must be initialized in the called method.

```
void AddOne(out int number)
{
    number = 0; 
    number += 1;
}


// int number;
// AddOne(out number)
// or
// AddOne(out int number);

int number = -1;
Console.WriteLine($"number is {number}"); // -1
// pass by refrence
AddOne(out number);
Console.WriteLine($"number is {number}"); // 1
```

```
class ReferenceTypeExample
{
  static void Enroll(out Student student)
  {
    //We need to initialize the variable in the method before we can do anything
    student = new Student();
    student.Enrolled = false;
  }

  static void Main()
  {
    Student student;

    Enroll(out student); // student will be equal to the value in Enroll. Name will be null and Enrolled will be false.
  }
}

public class Student {
  public string Name {get;set;}
  public bool Enrolled {get;set;}
}
```

* For using out keyword as a parameter both the method definition and calling method must use the out keyword explicitly.

## ref C#
The ref keyword in C# is a powerful tool that allows developers to pass arguments by reference, rather than by value. By using the ref keyword, developers can modify the original value of a variable, rather than just a copy of that value. This can be especially useful when working with large or complex data structures, as it can help to reduce memory usage and improve performance.

### Basic Definition
The ref keyword in C# is used to pass arguments to methods by reference. When a variable is passed by reference, the method can modify the value of the variable and the changes will be reflected in the calling code. This is in contrast to passing arguments by value, where a copy of the variable’s value is passed to the method, and any changes made to the variable in the method are not reflected in the calling code.

### Ref vs Out Keyword
The ref keyword is often confused with the out keyword, which is also used to pass arguments by reference. The main difference between the two is that with ref, the variable must be initialized before it is passed to the method, whereas with out, the variable does not need to be initialized before it is passed. In addition, with out, the method is required to assign a value to the variable before it returns, whereas with ref, the value of the variable can be modified without being assigned a new value.

### Ref vs In Keyword
The in keyword is another keyword that is used to pass arguments to methods, but it is used to pass arguments by read-only reference. This means that the method cannot modify the value of the variable, but it can read its value. The in keyword is useful when you want to pass large objects to a method without incurring the overhead of copying the object.

When using the ref keyword, it is important to keep in mind that the method can modify the value of the variable, which can lead to unexpected behavior if not used carefully. It is also important to ensure that the variable is initialized before it is passed to the method, to avoid null reference exceptions.

In summary, the ref keyword is a powerful feature of C# that allows methods to modify the value of variables in the calling code. It is important to use it carefully, and to understand the differences between ref, out, and in keywords.

## in C#
The in modifier is most often used for performance reasons and was introduced in C# 7.2. The motivation of in is to be used with a struct to improve performance by declaring that the value will not be modified. When using with reference types, it only prevents you from assigning a new reference.

The in keyword in C# is used to specify that a method parameter is passed by reference, but the called method cannot modify the argument. This is useful for parameters that are not modified by the called method, but must be passed by reference in order for the calling method to access the results.

C# 7 introduced the in modifier. It got the name by being the opposite of out keyword. It makes the reference (alias) read only; and the caller does have to initialize the value.

```
void DoSomeTask(in Employee emp)
{
  //emp can't be altered here.
}
```

## The TryParse() method
TryParse() converts the string data type into another data type. It returns 0 if the conversion fails. TryParse() is a safer approach because it does not terminate the execution of the program.

### Syntax
Use the following syntax to convert string into any variable.

```
data_type.TryParse(string, out output_variable);
```

### Parameters

The TryParse() method receives two parameters. The first parameter is the string to be converted. The second parameter is the variable to store the converted value. The out keyword is used before the second parameter.

### Return value

The TryParse() method returns True or False value based on successful or unsuccessful conversion.

### Example
```
string textExample = "Seven";
Console.WriteLine(textExample);

int textExampleInt;
int.TryParse(textExample, out textExampleInt);
// "Seven" cannot be converted to int, hence textExampleInt store 0 value.
Console.WriteLine(textExampleInt);

string textExample2 = "5.5";
Console.WriteLine(textExample2);

float textExampleFloat;
float.TryParse(textExample2, out textExampleFloat);
// "5.5" will be converted to float value 5.5 and stored in textExampleFloat
Console.WriteLine(textExampleFloat);
```

## C# int.TryParse Method
Convert a string representation of number to an integer, using the int.TryParse() method in C#. If the string cannot be converted, then the int.TryParse() method returns false i.e. a Boolean value.

Let’s say you have a string representation of a number.

```
string myStr = "12";
```

Now to convert it to an integer, use the int.TryParse(). It will get converted and will return True.

```
int.TryParse(myStr, out a);
```

```
int number;
string myStr = "12";
isConvertToNumber = int.TryParse(myStr, out a);
if (isConvertToNumber)
{
  Console.WriteLine("number " + number);
}
```

If the string can not be converted to an integer, then
```
int.Parse() will throw an exception
int.TryParse() will return false (but not throw an exception)
```



