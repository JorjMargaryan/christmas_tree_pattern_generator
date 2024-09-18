# Symmetrical Christmas tree Pattern Generator

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Tests](#running-the-tests)
- [Viewing the Test Report](#viewing-the-test-report)

## Introduction

This project generates a symmetrical christmas tree pattern with a specified number of levels and saves it to a file. The tree pattern includes a star at the top, alternating rows of stars and special characters, and a trunk at the bottom.

## Prerequisites

Before starting, please make sure the following requirements are met.
1. Python 3.x installed.
2. One of the IDEs is installed (PyCharm, VisualStudioCode, etc...)
3. The following Python packages are installed

    - `pathlib` - library for working with file paths
    - `os` - library for interacting with the operating system
    - `logging` - library for generating log messages
    - `unittest-xml-reporting` - for generating XML report files
    - `HtmlTestReport` - for generating HTML report files
  
## Installation

1. Clone the repository to your local machine:

        git clone [repository_url]

2. Navigate to the project directory:
3. Install the required Python packages:

        pip install -r requirements.txt

## Running the Tests

To run the tests, follow these steps:
1. Ensure your test environment is set up correctly.
2. Run the tests using the following commands:
   1. For generating HTML report after tests are processed run regressionRunner.py(or other runner file)
   (file location - tests_/common_/runners_/htmlRunners_/regressionRunner.py)
   2. For generating XML report after tests are processed run regressionRunner.py(or other runner file)
   (file location - tests_/common_/runners_/xmlRunners_/regressionRunner.py)
      
```
    python regressionRunner.py
```
Alternatively, you can run the tests directly from your IDE by executing the `regressionRunner.py` file or test files.

### Running Tests in PyCharm
- Open PyCharm and navigate to `regressionRunner.py`.
- Right-click the file and select "Run".
- Ensure that your Python interpreter is set up properly under `File > Settings > Project: christmas_tree_pattern_generator > Python Interpreter`.

### Running Tests in Visual Studio Code
- Open the project in Visual Studio Code.
- Install the Python and Test extensions if not already installed.
- Open `regressionRunner.py` and click "Run" in the top-right corner.
- Ensure your Python environment is correctly configured in VSCode.

## Viewing the Test Report

### Locate the HTML Report:
Once the tests are complete, navigate to the `reports_` directory in project folder. Find the HTML report file there, typically named something like `report_DD-MM-YYYY_HH-MM-SS.html`.

### Open the Report
To view the report, simply open the `report_DD-MM-YYYY_HH-MM-SS.html` file by double-clicking the file, which should open it in default web browser.

### Review the Report
The HTML report will display a detailed summary of test results, including which tests passed, failed, or were skipped. It will also provide any error messages and additional details for failed tests.
