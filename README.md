# Week 3 Assignment: Grade Reporter & Bug Hunt

## Overview
- `grade_reporter.py`: Calculates individual letter grades, pass/fail totals, and the rounded average score from a list of student marks using loops and conditionals.
- `bug_hunt.py`: Fixes three bugs (syntax, logic, and type conversion errors) in a Python script to correctly compute the sum of numbers 1 through 5.

## Bug Hunt Reflection
The logic error in the condition (`count < 5`) was the hardest bug to find because Python executed the script without raising any exceptions or error messages. I knew something was wrong because the program printed `10` instead of the expected sum of `15`. Since there was no stack trace to guide me, I had to trace the loop iterations manually to realize that `5` was never being added to `total`.