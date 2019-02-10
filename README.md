[![Build Status](https://travis-ci.com/ruben69695/python-chat.svg?branch=master)](https://travis-ci.com/ruben69695/python-chat)
[![CodeFactor](https://www.codefactor.io/repository/github/ruben69695/python-chat/badge)](https://www.codefactor.io/repository/github/ruben69695/python-chat)
[![codecov](https://codecov.io/gh/ruben69695/python-chat/branch/master/graph/badge.svg)](https://codecov.io/gh/ruben69695/python-chat)

# PyChat
This is an open source project to develop an open chat platform with the objective of improving our Python skills. Made by the Intergalactic Python Team.

# Getting Started
1.  Clone the Repository
2.  Install Python
3.  Create a virtual environment (pipenv suggested)
4.  Install requirements with 'pip install -r requirements.txt'
5.  Open the Project with your code editor
6.  Run the main Python file

# Testing
Before pushing your modifications, please check all tests can run.

If your modifications don't pass all the tests, that indicates you might have broken something.

To run them, you have different options. At the command line you can use:
-   pytest runs all tests inside /tests folder
-   add -v flag for a more verbose testing
-   add -q flag for a less verbose testing
-   add -s flag for enable print function
-   add -x flag to stop after the first failure
-   add -k "WORD" to run only tests functions containing 'WORD' (ie -k "dequeue" to run all tests with 'dequeue' inside
the method's name) 
-   add -k "WORD1 and WORD2" to run tests containing 'WORD1' and 'WORD2' 
-   add -k "WORD1 or WORD2" to run tests containing 'WORD1' or 'WORD2'
-   add --maxfail=3 to stop after the third failure 
-   run "pytest tests/FILE_NAME.py" to run only the tests at FILE_NAME.py. For example: pytest tests/test_queue.py
-   run "pytest tests/FILE_NAME.py::METHOD_NAME" to run only METHOD_NAME test at FILE_NAME.py.
    For example: pytest tests/test_queue.py::test_enqueue


You can add as many flags you want as long they are not contradictory. 
For example:
To run only the tests at test_queue.py, verbose, stopping at the first error, run:
-   pytest tests/test_queue.py -v -s

# Technologies
- Python
- Pytest
- SQLAlchemy
- PostgreSQL
- Travis CI
- Codefactor
- Codecov
- VSCode and PyCharm
- Windows, Linux and Mac

# Contribute
If you want to contribute, please, don't wait and send us a message to add you to collaborate in this open source project. We are waiting for your help. Happy coding! 
