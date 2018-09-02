#!/bin/bash

# Paul Armstrong
# Script will run the python and java solutions for Day2

echo -e "__________________________________"
echo -e "ALL DAY 2 TESTS"
echo -e "^^^^^^^^^^^^^^^"

echo -e "__________________________________"
echo -e "PYTHON:\n"
python3 Day2.py

echo -e "__________________________________"
echo -e "JAVA:\n"
javac Day2Tests.java && java Day2Tests && rm *.class

echo -e
