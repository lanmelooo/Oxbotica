#language: en

Feature: Test Selenium

      Background: Access site
          Given access site


      Scenario Outline: Operation math add
          Given selection build
          When insert first number 3 and second number 4
          And select math <operations>
          Then check answer <operations>
          And check answer if integers only

        Examples: many operations
          |  operations  |
          |     Add      |
          |   Subtract   |
          |   Multiply   |
          |    Divide    |
          | Concatenate  |

