#!/bin/bash

# Paul Armstrong
# Script will run the python and java solutions for Day1

echo -e "__________________________________"
echo -e "ALL DAY 1 TESTS"
echo -e "^^^^^^^^^^^^^^^"
echo -e "__________________________________"
echo -e "PYTHON:\n"
python3 Day1.py
echo -e "__________________________________"
echo -e "JAVA:\n"
javac Day1Tests.java && java Day1Tests
echo -e
