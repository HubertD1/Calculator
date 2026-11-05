# Calculator

A Python 3 calculator used from the Terminal, built step by step in SCCM4910.
## What it will do
Add, subtract, multiply and divide two numbers; display the result.
## How to run it
Run: python3 calculator.py
OR Run: ~/h-drive/calculator/run.sh
Enter the first number, operator (+ - * /), then second number.
The program prints Result: followed by the answer
## How to quit the program
Press Ctrl + C to exit program
##how to test calculator.py
run ./check.sh in the calculator folder
should result in 5 outputs which can each pass or fail.
check the exit status using echo $? and if all tests pass it should be 0, otherwise it should be non zero.
