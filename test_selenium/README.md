# Selenium Test

Derive and create test cases for a simple calculator app.

## 🚀 Tools

* [Python 3.9+](https://www.python.org/)
* [pip](https://pypi.org/project/pip/)



### 🔧 Start Project

1. Install libraries simply:
    
    `pip install -r requirements.txt`


1. Run the automation ([Creating runtime modules in PyCharm](https://www.jetbrains.com/help/pycharm/run-debug-configuration.html))
    1. Run behave report.html
        'behave -f html -o behave-report.html'



### ⌨️Explanation

The code will go through "build 2" and operations: "Add", "Subtract", "Multiply", "Divide" and "Concatenate".

In the line "When insert first number ' ' and second number ' ' ", from "calculator.feature" file, it is defined which 
numbers will run in the test.

After running the tests, a file called "behave-report.html" will be generated, when opening it in the upper right corner, 
you will have the browser options. When selecting a browser, the test report will open.


## 🛠️ Build with

* [Behave](https://behave.readthedocs.io/en/stable/) - The software used to write the test
* [Selenium](https://selenium-python.readthedocs.io/) - The framework web used
* [Webdriver-manager](https://pypi.org/project/webdriver-manager/) - The management of binary drivers for different browsers
* [Ipdb](https://pypi.org/project/ipdb/) - The IPython debugger
* [Behave-html-formatter](https://pypi.org/project/behave-html-formatter/) - Used to bring in HTML report



## ✒️ Author

* **Developer** - [Álan Melo](https://github.com/lanmelooo)
