from selenium.webdriver.common.by import By
from browser import Browser

class Elements(Browser):
    element_url = ('https://testsheepnz.github.io/BasicCalculator.html')
    element_build = (By.ID, 'selectBuild')
    element_first_number = (By.ID, 'number1Field')
    element_second_number = (By.ID, 'number2Field')
    element_operation = (By.ID, 'selectOperationDropdown')
    element_calculate = (By.ID, 'calculateButton')
    element_answer = (By.XPATH, '//input[@name="numberAnswer"]')
    element_integers_only = (By.ID, 'integerSelect')
    element_clear = (By.ID, 'clearButton')
