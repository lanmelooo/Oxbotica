import time

import ipdb

from elements.elements import Elements


class BasicCalculator(Elements):

    def access_page(self):
        self.browser.get(self.element_url)

    def build(self):
        time.sleep(1)
        self.find(*self.element_build).send_keys('2')
        time.sleep(1)

    def numbers(self, number_one, number_two):
        time.sleep(1)
        self.find(*self.element_first_number).send_keys(number_one)
        time.sleep(1)
        self.find(*self.element_second_number).send_keys(number_two)
        time.sleep(1)

    def operation(self, operations):
        time.sleep(1)
        self.find(*self.element_operation).send_keys(operations)
        time.sleep(1)
        self.find(*self.element_calculate).click()

    def answer(self, operations):
        first = int(self.find(*self.element_first_number).get_attribute('value'))
        second = int(self.find(*self.element_second_number).get_attribute('value'))
        answer = float(self.find(*self.element_answer).get_attribute('value'))
        operation = self.find(*self.element_operation).text

        if operations == 'Add':
            var = first + second
            assert var == answer, f'O valor esperado era {var} e o valor recebido foi {answer}'
            self.find(*self.element_clear).click()

        elif operations == 'Subtract':
            var = first - second
            assert var == answer, f'O valor esperado era {var} e o valor recebido foi {answer}'
            self.find(*self.element_clear).click()

        elif operations == 'Multiply':
            var = first * second
            assert var == answer, f'O valor esperado era {var} e o valor recebido foi {answer}'
            self.find(*self.element_clear).click()

        elif operations == 'Divide':
            var = first / second
            assert var == answer, f'O valor esperado era {var} e o valor recebido foi {answer}'
            self.find(*self.element_clear).click()


        elif operations == 'Concatenate':
            var = str(first) + str(second)
            assert var == answer, f'O valor esperado era {var} e o valor recebido foi {answer}'
            self.find(*self.element_clear).click()
