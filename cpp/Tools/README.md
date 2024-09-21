* [make](#make)
* [cmake](#cmake)
    * [target_link_libraries](#target_link_libraries)
    * [FindPkgConfig](#findpkgconfig)
* [diff a and so](#a-and-so)

# make
## Why do Makefiles exist?
Makefiles are used to help decide which parts of a large program need to be recompiled. In the vast majority of cases, C or C++ files are compiled. Other languages typically have their own tools that serve a similar purpose as Make. Make can also be used beyond compilation too, when you need a series of instructions to run depending on what files have changed. This tutorial will focus on the C/C++ compilation use case.

Here's an example dependency graph that you might build with Make. If any file's dependencies changes, then the file will get recompiled:

![](https://makefiletutorial.com/assets/dependency_graph.png)

## What alternatives are there to Make?
Popular C/C++ alternative build systems are SCons, CMake, Bazel, and Ninja. Some code editors like Microsoft Visual Studio have their own built in build tools. For Java, there's Ant, Maven, and Gradle. Other languages like Go, Rust, and TypeScript have their own build tools.

Interpreted languages like Python, Ruby, and raw Javascript don't require an analogue to Makefiles. The goal of Makefiles is to compile whatever files need to be compiled, based on what files have changed. But when files in interpreted languages change, nothing needs to get recompiled. When the program runs, the most recent version of the file is used.

## Running the Examples
To run these examples, you'll need a terminal and "make" installed. For each example, put the contents in a file called Makefile, and in that directory run the command make. Let's start with the simplest of Makefiles:

```
hello:
	echo "Hello, World"
```

Note: Makefiles must be indented using TABs and not spaces or make will fail.

Here is the output of running the above example:

```
$ make
echo "Hello, World"
Hello, World
```

That's it! If you're a bit confused, here's a video that goes through these steps, along with describing the basic structure of Makefiles.

## Makefile Syntax
A Makefile consists of a set of rules. A rule generally looks like this:

```
targets: prerequisites
	command
	command
	command
```

* The targets are file names, separated by spaces. Typically, there is only one per rule.

* The commands are a series of steps typically used to make the target(s).  These need to start with a tab character, not spaces.

* The prerequisites are also file names, separated by spaces. These files need to exist before the commands for the target are run. These are also called dependencies

## The essence of Make
Let's start with a hello world example:

```
hello:
	echo "Hello, World"
	echo "This line will print if the file hello does not exist."
```

There's already a lot to take in here. Let's break it down:

* We have one target called hello
* This target has two commands
* This target has no prerequisites

We'll then run make hello. As long as the hello file does not exist, the commands will run. If hello does exist, no commands will run.

It's important to realize that I'm talking about hello as both a target and a file. That's because the two are directly tied together. Typically, when a target is run (aka when the commands of a target are run), the commands will create a file with the same name as the target. In this case, the hello target does not create the hello file.


# cmake

## Links
* [How to Learn CMake in Just 20 Minutes](https://medium.com/swlh/how-to-learn-cmake-in-just-20-minutes-b8eb4767f2c)
* [learning cmake a beginner guide](https://tuannguyen68.gitbooks.io/learning-cmake-a-beginner-s-guide/content/chap1/chap1.html)
* [modern cmake](https://cliutils.gitlab.io/modern-cmake/chapters/intro/running.html)


## How to Learn CMake in Just 20 Minutes
If you have ever worked or written a C or C++ project, you have probably heard of the build system called CMake. For programmers that are new to C or C++, the concept of a separate build system usage a separate language may seem odd. However, knowledge of how to properly to properly compile, build and package a project is absolutely essential knowledge for a C++ programmer. In this guide, the roles CMake plays as a build system will be explained, and the most essential aspects and features of CMake will be discussed. You will learn how to use CMake to build libraries and executables, in hopefully under 20 minutes.

### Why is CMake even used?
Unlike many other programming languages, there is no centralized distribution of one, singular C++ compiler. The C++ language is modeled after an ISO standard specification, which several vendors of compilers like Microsoft or Clang, then implement. Each of those compilers, has different settings and options, and runs on a different operating system. Most C++ programs are intended be written to run cross platforms and on any modern compiler, doing that with a custom build script would prove difficult. It would require detailed knowledge of each compiler and operating system, and a ton of boilerplate code.

CMake generates build systems for C++ projects from an abstract script written in the CMake language. CMake provides an interface to specify build options and processes, without being concerned with compiler or operating system specific details. Do note, it only covers cross platform functionality for building the project, you are still responsible for the actual source code running on different platforms.

### Project structure and the CMakeLists.txt file
There are multiple ways to layout a C++ project. Some projects split their header and source files, by having one include directory and a src directory, while some put both in the same directories. For this purpose, we will use combined header and source directories, so the project structure is a little more straightforward.

At the beginning of each project must be a CMakeLists.txt file. This is the file name CMake recognizes as a build script file. A project can have multiple CMakeLists.txt, but only one in each directory. For the one in the top level directory of the project, the following must be present at the top of the file

```
cmake_minimum_required(VERSION 3.6) 
project(foo)
```

These two lines denote the minimum version of cmake required to build the project, and the name of the project. The minimum version is not that important for this case, as long as it is at least 3.0. Let’s take a look at a sample project layout below:

```
- CMakeLists.txt
- some.h
- some.cpp
- main.cpp
```

Here, there is a CMake file, CMakeLists.txt, a header file, some.h , and a source file, some.cpp . There’s also another source file, main.cpp . In most C++ projects, there is a library that contains the project’s code to be consumed by other projects and programs, as well as an executable that allows some of the code in the project to be run as a CLI program. For this example, some.cpp will represent the core library code, and main.cpp will represent the executable that’s also built.

### Building the library
In order to have CMake build a library, the source files that compose that library need to be specified in the CMakeLists.txt file. To do that, we have to construct a list of the files and call the add_library function.

In CMake, it’s important to understand variables and data types work very differently than perhaps any other language. All variables in CMake are strings. Lists in CMake are strings which contain the separator ; . Variables are created and destroyed using the set() and unset() functions. Below is an example of creating a list and printing it.

```
set(some_var "a" "b" "c")
message("${some_var}")
```

This will print
```
a;b;c
```

Above is another important feature of CMake, variable access. After a variable is created via the set() function, it’s value can only be accessed via the syntax ${var} . This is because, in CMake, everything is a string. Even unquoted values are strings. The statement message(hello) , treats hello as a five character string.

Now, to build our library, we must add the following to the build file, CMakeLists.txt:
```
set(FOO_SOURCES some.cpp)
add_library(foos STATIC "${FOO_SOURCES}")
```

In the call to add_library() , the source variable is accessed via the ${} syntax. However, we also pass in another argument, SHARED . This tells CMake whether we want a static library or shared library.

### Adding the executable
Now that we have added a library to the build file, we can expand the file to include instructions on building an executable and linking our library to that executable. Let’s make up a simple C++ file, main.cpp , that calls a function from our library:
```
#include "some.h"
int main(int argc, char const* argv[]) {
    someFunc(); // defined in some.cpp
    return 0;
}
```
Then, we can add to the build file the following:
```
add_executable(foot main.cpp)
target_link_libraries(foot foos)
```

The add_executable function works very similarly to add_library it takes in a name variable and a list representing the source files. In this case, since we know our executable only has one additional source file, we don’t need a separate variable to represent the sources as a list, we can just pass it in directly. The target_link_libraries function takes a target as the first argument, and then a list of other targets that must be libraries, to like to the first argument.

In CMake, a “target” is an object that is built by the resulting build system that CMake produces. In this example, both the library and the executable are build targets. In more complicated projects, custom targets are sometimes used to represent the creation of files needed by the built project. But for now, lets just stick to the basic build targets.

### Putting it all together
Now that the process of writing a CMakeLists.txt file has been discussed, we can jump into running CMake and then using the build system generated by CMake to compile our code. If you don’t have CMake currently installed on your system, you can typically install it by running brew install cmake if you have home brew. Otherwise, try this link.

CMake is typically run in an empty directory, that references the path the CMakeLists.txt root file is in. For example, if one is currently in the directory of the project, these commands are often used:
```
mkdir build
cd build
cmake ..
```

This will run CMake, and get it to produce build files in the current directory. It will print out a lot of information, pertaining to the compiler it detected and is using to generate these files for.

Next, you will actually run the files CMake generated and compile the project. If you are on MacOS or Linux, you will run make . If you are on windows, you will typically run msbuild ALL_BUILD.vcxproj . This will cause the compiler to run and try to compile your code. Note: this might fail if your code has syntax errors or otherwise is incorrectly written. CMake does not detect or check language syntax, it is only concerned with the build process.

That’s all! Hopefully by now, you feel comfortable in CMake to the point you can write your own build files, and create simple projects in C++ using it. CMake, overall, is a vast framework with many specialized components that can help build almost any C++ project. As you advance and get more familiar with it, you will likely need more advanced and sophisticated CMake, like having multiple subdirectories, or adding in 3rd party libraries as dependencies to your project.

Sure! Let's dive into CMake step-by-step with clear explanations and plenty of examples. CMake is a cross-platform tool that helps manage the build process of software projects. It generates native build files (like Makefiles on Unix or project files for Visual Studio) from simple configuration files.

### Table of Contents
1. Basic Project Setup
2. Adding Libraries
3. Using External Libraries
4. Advanced Topics
    - Conditional Statements
    - Custom Commands and Targets
    - Packaging
5. Example Projects

### 1. Basic Project Setup

#### Example 1: Simple Hello World

1. **Project Structure:**
```
MyProject/
├── CMakeLists.txt
└── main.cpp
```

2. **main.cpp**
```cpp
#include <iostream>

int main() {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
```

3. **CMakeLists.txt**
```cmake
cmake_minimum_required(VERSION 3.10)

# Project name and version
project(MyProject VERSION 1.0)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add the executable
add_executable(MyProject main.cpp)
```

4. **Building the Project:**
```sh
mkdir build
cd build
cmake ..
cmake --build .
```

This will generate and build the project, resulting in an executable `MyProject`.

### 2. Adding Libraries

#### Example 2: Creating and Linking a Static Library

1. **Project Structure:**
```
MyProject/
├── CMakeLists.txt
├── main.cpp
└── MathFunctions/
    ├── CMakeLists.txt
    ├── MathFunctions.h
    └── MathFunctions.cpp
```

2. **MathFunctions/MathFunctions.h**
```cpp
#ifndef MATHFUNCTIONS_H
#define MATHFUNCTIONS_H

int add(int a, int b);

#endif // MATHFUNCTIONS_H
```

3. **MathFunctions/MathFunctions.cpp**
```cpp
#include "MathFunctions.h"

int add(int a, int b) {
    return a + b;
}
```

4. **MathFunctions/CMakeLists.txt**
```cmake
add_library(MathFunctions STATIC MathFunctions.cpp)
```

5. **main.cpp**
```cpp
#include <iostream>
#include "MathFunctions.h"

int main() {
    std::cout << "3 + 4 = " << add(3, 4) << std::endl;
    return 0;
}
```

6. **CMakeLists.txt**
```cmake
cmake_minimum_required(VERSION 3.10)

project(MyProject VERSION 1.0)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_subdirectory(MathFunctions)

add_executable(MyProject main.cpp)
target_link_libraries(MyProject PRIVATE MathFunctions)
```

7. **Building the Project:**
```sh
mkdir build
cd build
cmake ..
cmake --build .
```

### 3. Using External Libraries

#### Example 3: Using the Boost Library

1. **Install Boost:**
   Make sure Boost is installed on your system.

2. **Project Structure:**
```
MyProject/
├── CMakeLists.txt
└── main.cpp
```

3. **main.cpp**
```cpp
#include <iostream>
#include <boost/algorithm/string.hpp>
#include <vector>
#include <string>

int main() {
    std::string s = "Boost Libraries";
    std::vector<std::string> words;
    boost::split(words, s, boost::is_any_of(" "));
    
    for(const auto& word : words) {
        std::cout << word << std::endl;
    }
    
    return 0;
}
```

4. **CMakeLists.txt**
```cmake
cmake_minimum_required(VERSION 3.10)

project(MyProject VERSION 1.0)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

find_package(Boost 1.65 REQUIRED COMPONENTS algorithm)

add_executable(MyProject main.cpp)
target_link_libraries(MyProject PRIVATE Boost::algorithm)
```

5. **Building the Project:**
```sh
mkdir build
cd build
cmake ..
cmake --build .
```

### 4. Advanced Topics

#### Conditional Statements

```cmake
if(WIN32)
    message(STATUS "We are on Windows")
elseif(UNIX)
    message(STATUS "We are on Unix")
endif()
```

#### Custom Commands and Targets

```cmake
add_custom_command(
    OUTPUT ${CMAKE_BINARY_DIR}/generated_file.cpp
    COMMAND generate_code > ${CMAKE_BINARY_DIR}/generated_file.cpp
    DEPENDS generate_code
)

add_custom_target(run ALL
    COMMAND MyProject
    DEPENDS MyProject
)
```

#### Packaging

Create a `CPackConfig.cmake` file:

```cmake
include(InstallRequiredSystemLibraries)
set(CPACK_PACKAGE_NAME "MyProject")
set(CPACK_PACKAGE_VERSION "1.0.0")
include(CPack)
```

Add to `CMakeLists.txt`:

```cmake
install(TARGETS MyProject DESTINATION bin)
include(CPackConfig.cmake)
```

### 5. Example Projects

#### Example 4: A More Complex Project with Multiple Libraries

1. **Project Structure:**
```
MyComplexProject/
├── CMakeLists.txt
├── main.cpp
├── MathFunctions/
│   ├── CMakeLists.txt
│   ├── MathFunctions.h
│   └── MathFunctions.cpp
└── StringFunctions/
    ├── CMakeLists.txt
    ├── StringFunctions.h
    └── StringFunctions.cpp
```

2. **MathFunctions/MathFunctions.h**
```cpp
#ifndef MATHFUNCTIONS_H
#define MATHFUNCTIONS_H

int add(int a, int b);

#endif // MATHFUNCTIONS_H
```

3. **MathFunctions/MathFunctions.cpp**
```cpp
#include "MathFunctions.h"

int add(int a, int b) {
    return a + b;
}
```

4. **MathFunctions/CMakeLists.txt**
```cmake
add_library(MathFunctions STATIC MathFunctions.cpp)
```

5. **StringFunctions/StringFunctions.h**
```cpp
#ifndef STRINGFUNCTIONS_H
#define STRINGFUNCTIONS_H

#include <string>
#include <vector>

void split(const std::string &s, char delimiter, std::vector<std::string> &tokens);

#endif // STRINGFUNCTIONS_H
```

6. **StringFunctions/StringFunctions.cpp**
```cpp
#include "StringFunctions.h"
#include <sstream>

void split(const std::string &s, char delimiter, std::vector<std::string> &tokens) {
    std::stringstream ss(s);
    std::string token;
    while (std::getline(ss, token, delimiter)) {
        tokens.push_back(token);
    }
}
```

7. **StringFunctions/CMakeLists.txt**
```cmake
add_library(StringFunctions STATIC StringFunctions.cpp)
```

8. **main.cpp**
```cpp
#include <iostream>
#include "MathFunctions.h"
#include "StringFunctions.h"
#include <vector>

int main() {
    std::cout << "3 + 4 = " << add(3, 4) << std::endl;
    
    std::string s = "Hello,World";
    std::vector<std::string> tokens;
    split(s, ',', tokens);
    
    for(const auto& token : tokens) {
        std::cout << token << std::endl;
    }
    
    return 0;
}
```

9. **CMakeLists.txt**
```cmake
cmake_minimum_required(VERSION 3.10)

project(MyComplexProject VERSION 1.0)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_subdirectory(MathFunctions)
add_subdirectory(StringFunctions)

add_executable(MyComplexProject main.cpp)
target_link_libraries(MyComplexProject PRIVATE MathFunctions StringFunctions)
```

10. **Building the Project:**
```sh
mkdir build
cd build
cmake ..
cmake --build .
```

### Conclusion

This guide has covered the basics of CMake, from setting up a simple project to linking libraries and using external dependencies. By following these examples, you should be able to build and manage more complex projects with ease.

For further reading, the official [CMake documentation](https://cmake.org/documentation/) is an excellent resource.


## More
Understanding the differences between static and shared libraries is crucial for managing and optimizing your software builds. Here's an explanation of both types, along with their advantages and disadvantages:

### Static Libraries

A static library is a collection of object files that are linked directly into the final executable at compile time. This means that the code from the static library is copied into the executable file.

**Characteristics:**
- **File Extension:** Typically `.a` (archive) on Unix-like systems, `.lib` on Windows.
- **Linking Time:** Static libraries are linked at compile time.
- **Execution:** No need for the library file at runtime since the code is already included in the executable.
- **Size:** The executable size is larger because it contains the library code.

**Advantages:**
- **Self-contained Executable:** The resulting executable is self-contained and doesn't depend on external library files at runtime.
- **Version Control:** No issues with library versioning or dependencies at runtime since the library is part of the executable.

**Disadvantages:**
- **Size:** Larger executable size due to the inclusion of the library code.
- **Updates:** If the library code needs to be updated, the executable must be recompiled.

### Shared Libraries

A shared library (also called a dynamic library) is a collection of object files that are linked at runtime. The executable contains references to the shared library but not the library code itself.

**Characteristics:**
- **File Extension:** Typically `.so` (shared object) on Unix-like systems, `.dll` (dynamic link library) on Windows.
- **Linking Time:** Shared libraries are linked at runtime.
- **Execution:** The library file must be available at runtime for the executable to function.
- **Size:** The executable size is smaller since it doesn't contain the library code.

**Advantages:**
- **Size:** Smaller executable size since the library code is not included in the executable.
- **Updates:** Shared libraries can be updated independently of the executable. A new version of the library can be used without recompiling the executable.

**Disadvantages:**
- **Dependencies:** The executable depends on the shared library file being present and compatible at runtime.
- **Version Control:** Potential issues with library versioning (e.g., "DLL Hell" on Windows) where different versions of the shared library might cause conflicts.

### When to Use Each Type

- **Static Libraries:**
  - When you need a self-contained executable that can run without relying on external files.
  - For distributing software where you want to avoid dependency issues.
  - In environments where the deployment of additional files (like shared libraries) is difficult or undesirable.

- **Shared Libraries:**
  - When you want to save disk space and memory, as multiple executables can share the same library.
  - For applications that can benefit from modularity and the ability to update libraries independently.
  - In systems where managing dependencies and versions of libraries is straightforward.

### Example with CMake

Here’s how you can specify whether to build a static or shared library using CMake:

#### Static Library

```cmake
add_library(MyLibrary STATIC src/mylibrary.cpp)
```

#### Shared Library

```cmake
add_library(MyLibrary SHARED src/mylibrary.cpp)
```

### Example Project Structure

```text
MyProject/
├── CMakeLists.txt
├── src/
│   ├── main.cpp
│   └── mylibrary.cpp
└── include/
    └── mylibrary.h
```

#### CMakeLists.txt

```cmake
cmake_minimum_required(VERSION 3.10)
project(MyProject)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

include_directories(include)

# Create a static or shared library
add_library(MyLibrary STATIC src/mylibrary.cpp)  # Change STATIC to SHARED for a shared library

# Add the executable
add_executable(MyExecutable src/main.cpp)

# Link the library to the executable
target_link_libraries(MyExecutable PRIVATE MyLibrary)
```

### Conclusion

Both static and shared libraries have their own use cases and trade-offs. Choosing the right type depends on your project's requirements regarding deployment, update flexibility, and resource management. Understanding these differences helps in making informed decisions for efficient software development and deployment.


## target_link_libraries
My recommendation is to start simple, and then complicate your project further.

Let me try to explain how linking works in CMake. The idea is that you build modules in CMake, and link them together. Let's ignore header files for now, as they can be all included in your source files.

Say you have file1.cpp, file2.cpp, main.cpp. You add them to your project with:
```
ADD_LIBRARY(LibsModule 
    file1.cpp
    file2.cpp
)
```
Now you added them to a module called LibsModule. Keep that in mind. Say you want to link to pthread for example that's already in the system. You can combine it with LibsModule using the command:

```
target_link_libraries(LibsModule -lpthread)
```

And if you want to link a static library to that too, you do this:

```
target_link_libraries(LibsModule liblapack.a)
```

And if you want to add a directory where any of these libraries are 
located, you do this:

```
target_link_libraries(LibsModule -L/home/user/libs/somelibpath/)
```

Now you add an executable, and you link it with your main file:

```
ADD_EXECUTABLE(MyProgramExecBlaBla main.cpp)
```
(I added BlaBla just to make it clear that the name is custom). And then you link LibsModule with your executable module MyProgramExecBlaBla

```
target_link_libraries(MyProgramExecBlaBla LibsModule)
```

And this will do it.

What I see in your CMake file is a lot of redundancy. For example, why do you have texture_mapping, which is an executable module in your include directories? So you need to clean this up and follow the simple logic I explained. Hopefully it works.

In summary, it looks like this:
```
project (MyProgramExecBlaBla)  #not sure whether this should be the same 
name of the executable, but I always see that "convention"
cmake_minimum_required(VERSION 2.8)
ADD_LIBRARY(LibsModule 
    file1.cpp
    file2.cpp
)

target_link_libraries(LibsModule -lpthread)
target_link_libraries(LibsModule liblapack.a)
target_link_libraries(LibsModule -L/home/user/libs/somelibpath/)
ADD_EXECUTABLE(MyProgramExecBlaBla main.cpp)
target_link_libraries(MyProgramExecBlaBla LibsModule)
```

The most important thing to understand is the module structure, where you create modules and link them all together with your executable. Once this works, you can complicate your project further with more details. Good luck!

Note: Keep in mind that this is the simple way to use CMake. The better cross-platform way would be using find_package, which locates a package/library, and provides the libraries and includes in CMake variables so that you could link your program to them. Here's how to do this for boost, for example.


## Using target_link_libraries for Linking Libraries
target_link_libraries() is a function that allows you to specify which libraries a target should link against. It takes the name of the target as its first argument, and a list of libraries as subsequent arguments.

For example, target_link_libraries(myprog mylib) would specify that the myprog target should link against the mylib library.

This function is also used to specify dependencies between targets. If one target depends on another, you can use target_link_libraries() to ensure that the dependent target is built before the dependent one.

Sure! `target_link_libraries` in CMake is a command used to specify which libraries (and targets) a target (like an executable or another library) should be linked against. This helps in building the final executable or library with all the necessary dependencies.

Let's break it down step by step with an easy example.

### Basic Concept

- **Target**: This can be an executable or a library that you are building.
- **Library**: This is an external or internal library that your target depends on.

### Example

Let's say we have a project where we are building an executable called `myapp` which depends on a library called `mylib`.

Here's a simple directory structure:
```
/project
  |-- CMakeLists.txt
  |-- myapp.cpp
  |-- mylib/
      |-- CMakeLists.txt
      |-- mylib.cpp
      |-- mylib.h
```

### Step-by-Step Guide

#### Step 1: Create `mylib`

In the `mylib/CMakeLists.txt` file, we define the library `mylib`:

```cmake
# mylib/CMakeLists.txt

add_library(mylib mylib.cpp)
```

This tells CMake to create a library target named `mylib` from the source file `mylib.cpp`.

#### Step 2: Create `myapp`

In the main `CMakeLists.txt` file, we define the executable and link it with `mylib`:

```cmake
# CMakeLists.txt (at the root of the project)

cmake_minimum_required(VERSION 3.10)
project(MyProject)

# Add the library directory
add_subdirectory(mylib)

# Define the executable
add_executable(myapp myapp.cpp)

# Link the library to the executable
target_link_libraries(myapp PRIVATE mylib)
```

Here's what each line does:

1. **`cmake_minimum_required(VERSION 3.10)`**: This sets the minimum version of CMake required for this project.
2. **`project(MyProject)`**: This names the project.
3. **`add_subdirectory(mylib)`**: This tells CMake to process the `CMakeLists.txt` in the `mylib` directory, creating the `mylib` target.
4. **`add_executable(myapp myapp.cpp)`**: This creates an executable target called `myapp` from the source file `myapp.cpp`.
5. **`target_link_libraries(myapp PRIVATE mylib)`**: This links the `mylib` library to the `myapp` executable.

### Explanation of `target_link_libraries`

- **`target_link_libraries`**: This command links a target with libraries.
- **`myapp`**: The target executable we are linking libraries to.
- **`PRIVATE mylib`**: The `mylib` library we are linking to `myapp`. The `PRIVATE` keyword specifies that `mylib` is only used by `myapp` and is not exposed to other targets that link against `myapp`.

### Result

When you build this project with CMake, it will:

1. Compile `mylib.cpp` into the `mylib` library.
2. Compile `myapp.cpp` into the `myapp` executable.
3. Link the `mylib` library to the `myapp` executable so that `myapp` can use the functions and symbols defined in `mylib`.

This way, `target_link_libraries` ensures that all necessary libraries are linked, making sure your final executable has access to all the required code and functionalities.

### Summary

- **`add_library(mylib mylib.cpp)`**: Defines a library.
- **`add_executable(myapp myapp.cpp)`**: Defines an executable.
- **`target_link_libraries(myapp PRIVATE mylib)`**: Links the library to the executable.

This is a simple and easy-to-understand way to manage dependencies in CMake projects!

## FindPkgConfig
* [cmake link](https://cmake.org/cmake/help/latest/module/FindPkgConfig.html)

### A pkg-config module for CMake.
Finds the pkg-config executable and adds the pkg_get_variable(), pkg_check_modules() and pkg_search_module() commands. The following variables will also be set:

#### PKG_CONFIG_FOUND
True if a pkg-config executable was found.

#### PKG_CONFIG_VERSION_STRING
New in version 2.8.8.
The version of pkg-config that was found.

#### PKG_CONFIG_EXECUTABLE
The pathname of the pkg-config program.

#### PKG_CONFIG_ARGN
New in version 3.22.
A list of arguments to pass to pkg-config.

### pkg_check_modules
Checks for all the given modules, setting a variety of result variables in the calling scope.
```
pkg_check_modules(<prefix>
                  [REQUIRED] [QUIET]
                  [NO_CMAKE_PATH]
                  [NO_CMAKE_ENVIRONMENT_PATH]
                  [IMPORTED_TARGET [GLOBAL]]
                  <moduleSpec> [<moduleSpec>...])
```

When the REQUIRED argument is given, the command will fail with an error if module(s) could not be found.
When the QUIET argument is given, no status messages will be printed.

Each <moduleSpec> can be either a bare module name or it can be a module name with a version constraint (operators =, <, >, <= and >= are supported). The following are examples for a module named foo with various constraints:

* foo matches any version.
* foo<2 only matches versions before 2.
* foo>=3.1 matches any version from 3.1 or later.
* foo=1.2.3 requires that foo must be exactly version 1.2.3.

The following variables may be set upon return. Two sets of values exist: One for the common case (<XXX> = <prefix>) and another for the information pkg-config provides when called with the --static option (<XXX> = <prefix>_STATIC).

* \<XXX>_FOUND
set to 1 if module(s) exist

* \<XXX>_LIBRARIES
only the libraries (without the '-l')

* \<XXX>_LINK_LIBRARIES
the libraries and their absolute paths

* \<XXX>_LIBRARY_DIRS
the paths of the libraries (without the '-L')

* \<XXX>_LDFLAGS
all required linker flags

* \<XXX>_LDFLAGS_OTHER
all other linker flags

* \<XXX>_INCLUDE_DIRS
the '-I' preprocessor flags (without the '-I')

* \<XXX>_CFLAGS
all required cflags

* \<XXX>_CFLAGS_OTHER
the other compiler flags

All but <XXX>_FOUND may be a ;-list if the associated variable returned from pkg-config has multiple values.

### pkg_search_module
The behavior of this command is the same as pkg_check_modules(), except that rather than checking for all the specified modules, it searches for just the first successful match.
```
pkg_search_module(<prefix>
                  [REQUIRED] [QUIET]
                  [NO_CMAKE_PATH]
                  [NO_CMAKE_ENVIRONMENT_PATH]
                  [IMPORTED_TARGET [GLOBAL]]
                  <moduleSpec> [<moduleSpec>...])
```
New in version 3.16: If a module is found, the <prefix>_MODULE_NAME variable will contain the name of the matching module. This variable can be used if you need to run pkg_get_variable().

Example:
```
pkg_search_module (BAR libxml-2.0 libxml2 libxml>=2)
```

#### pkg_get_variable
New in version 3.4.

Retrieves the value of a pkg-config variable varName and stores it in the result variable resultVar in the calling scope.
```
pkg_get_variable(<resultVar> <moduleName> <varName>
                 [DEFINE_VARIABLES <key>=<value>...])
```
If pkg-config returns multiple values for the specified variable, resultVar will contain a ;-list.

Options:
```
DEFINE_VARIABLES <key>=<value>...
```
New in version 3.28.

Specify key-value pairs to redefine variables affecting the variable retrieved with pkg-config.

For example:
```
pkg_get_variable(GI_GIRDIR gobject-introspection-1.0 girdir)
```

`pkg_check_modules` is a CMake command used to find and configure packages using the pkg-config system. Pkg-config is a helper tool used when compiling applications and libraries. It provides information about installed libraries on the system, including the necessary compile and link flags.

Here's a step-by-step explanation and example to help you understand `pkg_check_modules`:

### Step-by-Step Explanation

1. **Include the `FindPkgConfig` Module**: First, you need to include the `FindPkgConfig` module in your CMake script. This module provides the `pkg_check_modules` command.

2. **Use `pkg_check_modules`**: Use the `pkg_check_modules` command to check for a specific package. This command will set various variables with the compile and link flags required for the package.

3. **Specify Variables and Options**:
    - `PREFIX`: The prefix for the variables that will be set.
    - `REQUIRED` (optional): If specified, the command will fail if the package is not found.
    - `QUIET` (optional): Suppress output messages.
    - `PACKAGE-NAME`: The name of the package you want to check.

4. **Variables Set by `pkg_check_modules`**:
    - `<PREFIX>_FOUND`: Indicates whether the package was found.
    - `<PREFIX>_VERSION`: The version of the package.
    - `<PREFIX>_INCLUDE_DIRS`: The include directories for the package.
    - `<PREFIX>_LIBRARIES`: The libraries to link against.
    - `<PREFIX>_CFLAGS`: The compile flags.
    - `<PREFIX>_LDFLAGS`: The linker flags.

### Example

Let's say you want to find and configure the `libpng` package.

#### CMakeLists.txt
```cmake
cmake_minimum_required(VERSION 3.10)
project(MyProject)

# Include the FindPkgConfig module
find_package(PkgConfig REQUIRED)

# Check for the libpng package
pkg_check_modules(PNG REQUIRED libpng)

# Include directories for libpng
include_directories(${PNG_INCLUDE_DIRS})

# Link libraries for libpng
link_directories(${PNG_LIBRARY_DIRS})

# Add your executable or library
add_executable(my_executable main.cpp)

# Link the executable with libpng
target_link_libraries(my_executable ${PNG_LIBRARIES})
```

#### Explanation

1. **Include the FindPkgConfig module**:
    ```cmake
    find_package(PkgConfig REQUIRED)
    ```

2. **Check for the `libpng` package**:
    ```cmake
    pkg_check_modules(PNG REQUIRED libpng)
    ```
    - `PNG`: The prefix for the variables.
    - `REQUIRED`: Ensures the configuration fails if `libpng` is not found.
    - `libpng`: The name of the package.

3. **Set up include directories**:
    ```cmake
    include_directories(${PNG_INCLUDE_DIRS})
    ```
    - `${PNG_INCLUDE_DIRS}`: The include directories for `libpng`.

4. **Set up link directories**:
    ```cmake
    link_directories(${PNG_LIBRARY_DIRS})
    ```
    - `${PNG_LIBRARY_DIRS}`: The library directories for `libpng`.

5. **Add the executable**:
    ```cmake
    add_executable(my_executable main.cpp)
    ```

6. **Link the executable with `libpng`**:
    ```cmake
    target_link_libraries(my_executable ${PNG_LIBRARIES})
    ```
    - `${PNG_LIBRARIES}`: The libraries to link against for `libpng`.

### Variables Set by `pkg_check_modules`

If `libpng` is found, `pkg_check_modules` will set the following variables:
- `PNG_FOUND`: TRUE if `libpng` is found.
- `PNG_VERSION`: The version of `libpng`.
- `PNG_INCLUDE_DIRS`: The include directories for `libpng`.
- `PNG_LIBRARIES`: The libraries for `libpng`.
- `PNG_CFLAGS`: The compile flags for `libpng`.
- `PNG_LDFLAGS`: The linker flags for `libpng`.

This example demonstrates how to integrate a library using `pkg_check_modules` in a CMake project, providing the necessary compile and link flags automatically.


# .a and .so
Sure! Let's delve into `.a` and `.so` files, which are types of library files used in software development.

### Static Libraries (.a files)
A `.a` file is a static library used mainly in Unix-like operating systems. It contains a collection of object files (`.o` files), which are compiled code modules.

#### Characteristics of Static Libraries:
1. **Static Linking**: When you link a program with a static library, the code from the library is copied into the executable at compile time.
2. **Size**: The resulting executable is larger because it includes the code from the library.
3. **Independence**: Once compiled, the executable does not need the `.a` file. The library code is part of the executable.
4. **No Runtime Overhead**: There’s no overhead of looking up library code at runtime.

#### Creating and Using Static Libraries:
1. **Create Object Files**:
    ```sh
    gcc -c file1.c -o file1.o
    gcc -c file2.c -o file2.o
    ```
2. **Create Static Library**:
    ```sh
    ar rcs libmylib.a file1.o file2.o
    ```
3. **Link Static Library**:
    ```sh
    gcc main.c -L. -lmylib -o myprogram
    ```

### Shared Libraries (.so files)
A `.so` file is a shared (or dynamic) library, used mainly in Unix-like operating systems. It is loaded into memory and linked dynamically at runtime.

#### Characteristics of Shared Libraries:
1. **Dynamic Linking**: When you link a program with a shared library, the code from the library is not copied into the executable. Instead, it is linked at runtime.
2. **Size**: The resulting executable is smaller because it doesn’t include the code from the library.
3. **Dependency**: The executable depends on the `.so` file being present at runtime.
4. **Runtime Overhead**: There is some overhead for looking up library code at runtime, but shared libraries can be shared among multiple programs, reducing overall memory usage.

#### Creating and Using Shared Libraries:
1. **Create Object Files**:
    ```sh
    gcc -fPIC -c file1.c -o file1.o
    gcc -fPIC -c file2.c -o file2.o
    ```
2. **Create Shared Library**:
    ```sh
    gcc -shared -o libmylib.so file1.o file2.o
    ```
3. **Link Shared Library**:
    ```sh
    gcc main.c -L. -lmylib -o myprogram
    ```
4. **Run Program with Shared Library**:
    ```sh
    export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
    ./myprogram
    ```

### Example in Detail

#### Static Library Example
1. **Code Files**:
    - `file1.c`:
        ```c
        // file1.c
        #include <stdio.h>
        void function1() {
            printf("Function 1\n");
        }
        ```
    - `file2.c`:
        ```c
        // file2.c
        #include <stdio.h>
        void function2() {
            printf("Function 2\n");
        }
        ```
    - `main.c`:
        ```c
        // main.c
        void function1();
        void function2();

        int main() {
            function1();
            function2();
            return 0;
        }
        ```

2. **Create Object Files**:
    ```sh
    gcc -c file1.c -o file1.o
    gcc -c file2.c -o file2.o
    ```

3. **Create Static Library**:
    ```sh
    ar rcs libmylib.a file1.o file2.o
    ```

4. **Link Static Library**:
    ```sh
    gcc main.c -L. -lmylib -o myprogram
    ```

5. **Run Program**:
    ```sh
    ./myprogram
    ```

#### Shared Library Example
1. **Code Files**: (same as above)

2. **Create Object Files**:
    ```sh
    gcc -fPIC -c file1.c -o file1.o
    gcc -fPIC -c file2.c -o file2.o
    ```

3. **Create Shared Library**:
    ```sh
    gcc -shared -o libmylib.so file1.o file2.o
    ```

4. **Link Shared Library**:
    ```sh
    gcc main.c -L. -lmylib -o myprogram
    ```

5. **Run Program with Shared Library**:
    ```sh
    export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
    ./myprogram
    ```

By understanding the differences and uses of static and shared libraries, you can better manage dependencies and optimize your applications.

Linking libraries in GCC can be done using command-line options. Here's a detailed guide on how to link both static and shared libraries in GCC.

### Linking Static Libraries
Static libraries have the file extension `.a`. To link a static library with your program, you use the `-l` and `-L` options.

#### Steps to Link a Static Library:
1. **Create Object Files**: First, compile your source files into object files.
    ```sh
    gcc -c file1.c -o file1.o
    gcc -c file2.c -o file2.o
    ```
2. **Create the Static Library**: Use the `ar` command to create a static library from the object files.
    ```sh
    ar rcs libmylib.a file1.o file2.o
    ```
3. **Link the Static Library**: Use the `-L` option to specify the directory where the library is located and the `-l` option to specify the library name (without the `lib` prefix and `.a` extension).
    ```sh
    gcc main.c -L. -lmylib -o myprogram
    ```
    - `-L.`: Tells the linker to look in the current directory for libraries.
    - `-lmylib`: Links against the library `libmylib.a`.

### Linking Shared Libraries
Shared libraries have the file extension `.so`. Linking a shared library is similar to linking a static library, but you also need to ensure that the shared library can be found at runtime.

#### Steps to Link a Shared Library:
1. **Create Object Files**: Compile your source files into position-independent code (PIC) object files.
    ```sh
    gcc -fPIC -c file1.c -o file1.o
    gcc -fPIC -c file2.c -o file2.o
    ```
2. **Create the Shared Library**: Use the `-shared` option to create a shared library from the object files.
    ```sh
    gcc -shared -o libmylib.so file1.o file2.o
    ```
3. **Link the Shared Library**: Use the `-L` option to specify the directory where the library is located and the `-l` option to specify the library name.
    ```sh
    gcc main.c -L. -lmylib -o myprogram
    ```
    - `-L.`: Tells the linker to look in the current directory for libraries.
    - `-lmylib`: Links against the library `libmylib.so`.

4. **Run the Program with the Shared Library**: Ensure the shared library can be found at runtime. One way to do this is by setting the `LD_LIBRARY_PATH` environment variable.
    ```sh
    export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
    ./myprogram
    ```

### Complete Example
Let's put it all together with a full example.

#### Source Files:
- `file1.c`:
    ```c
    #include <stdio.h>
    void function1() {
        printf("Function 1\n");
    }
    ```
- `file2.c`:
    ```c
    #include <stdio.h>
    void function2() {
        printf("Function 2\n");
    }
    ```
- `main.c`:
    ```c
    void function1();
    void function2();

    int main() {
        function1();
        function2();
        return 0;
    }
    ```

#### For Static Library:
1. **Compile Object Files**:
    ```sh
    gcc -c file1.c -o file1.o
    gcc -c file2.c -o file2.o
    ```
2. **Create Static Library**:
    ```sh
    ar rcs libmylib.a file1.o file2.o
    ```
3. **Link Static Library**:
    ```sh
    gcc main.c -L. -lmylib -o myprogram
    ```
4. **Run Program**:
    ```sh
    ./myprogram
    ```

#### For Shared Library:
1. **Compile Object Files**:
    ```sh
    gcc -fPIC -c file1.c -o file1.o
    gcc -fPIC -c file2.c -o file2.o
    ```
2. **Create Shared Library**:
    ```sh
    gcc -shared -o libmylib.so file1.o file2.o
    ```
3. **Link Shared Library**:
    ```sh
    gcc main.c -L. -lmylib -o myprogram
    ```
4. **Run Program with Shared Library**:
    ```sh
    export LD_LIBRARY_PATH=.:$LD_LIBRARY_PATH
    ./myprogram
    ```

By following these steps, you can link static and shared libraries in GCC to build your programs.

```
gcc -L / -l option flags
gcc -l links with a library file.

gcc -L looks in directory for library files.
```

Syntax
```
$ gcc [options] [source files] [object files] [-Ldir] -llibname [-o outfile]
```
 

Link -l with library name without the lib prefix and the .a or .so extensions.

Examples
Example1
For static library file libmath.a use -lmath:
```
$ gcc -static myfile.c -lmath -o myfile
```
 
Example2
For shared library file libmath.so use -lmath:
```
$ gcc myfile.c -lmath -o myfile
```
 
Example3
file1.c:
```
// file1.c
#include <stdio.h>

void main()
{
    printf("main() run!\n");
    myfunc();
}
```
 

file2.c:
```
// file2.c
#include <stdio.h>

void myfunc()
{
    printf("myfunc() run!\n");
}
```
 

Build file2.c, copy object file file2.o to libs directory and archive it to static library libmylib.a:
```
$ gcc -c file2.c
$ mkdir libs
$ cp file2.o libs
$ cd libs
$ ar rcs libmylib.a file2.o
```

Build file1.c with static library libmylib.a in libs directory.

Build without -L results with an error:
```
$ gcc file1.c -lmylib -o outfile
/usr/bin/ld: cannot find -llibs
collect2: ld returned 1 exit status
$
```
Build with -L and run:

```
$ gcc file1.c -Llibs -lmylib -o outfile
$ ./outfile
main() run!
myfunc() run!
$
```