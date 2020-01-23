# Open Brainfuck Interpreter (OBI)
A small and lightweight *(≈ 4KB)* interpreter for the [Brainfuck language](https://en.wikipedia.org/wiki/Brainfuck "Brainfuck language") written in Python in under 2 hours.
## Features
- **A Command Line Argument based interpreter**
- **Supports comments**
- **Always has the highground**
- **Supports error detection for:-**
	- Unbalanced loops
	- Unexpected Instruction in code
	- Empty inputs
	- Inputs larger than 1 Byte
	- Trying to to go beyond the start of memory tape
- **Uses dyanmic memory cell array**
- **Cell-size 1 Byte (as per convention)** 
- **Written in pure Python**

## Prequisites
**THIS INTERPRETER REQUIRES PYTHON 3.xx TO BE INSTALLED (duh!)**
## Basic syntax
`Python bf.py -f <filename> -c 0|1`
## Command line arguments
| Parameters | Description                    |
| --------------------- | ------------------------------ |
| `-f`      | filename      |
| `-c 0 \| 1 (optional)`   |comments present `-c 1 ` or not `-c 0 `  default `1`|

## Versions
The alternative folder in the versions folder contains a version of the compiler **without** the support for special characters like the new line character '\n' which is needed for some bf programs. 
The normal version by default supports these inputs.
## Supported Inputs
In compliance with the brainfuck conventions, 1 ascii character is supported as an input.

*NOTE: This has to be kept in mind as this break arithematic operations if the solution is greater than 10. Some workaround has to be implemented to prevent overflow and return of garbage values.*
## Examples
One "Hello world" program is included in the 'examples' folder to test the interpreter.
Though some examples are available at [this github page](https://github.com/ryantenney/brainfuck/tree/master/examples "this") or at this really great website [brainfuck.org](http://brainfuck.org/ "brainfuck.org").


## Author
Kinshuk Dua

[Github](http://https://github.com/kinshukdua/ "website")