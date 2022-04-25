from behave import *


@given('access site')
def step_impl(context):
    context.page.access_page()


@given('selection build')
def step_impl(context):
    context.page.build()


@when('insert first number {number_one} and second number {number_two}')
def step_impl(context,number_one, number_two):
    context.page.numbers(number_one, number_two)


@when('select math {operations}')
def step_impl(context, operations):
    context.page.operation(operations)


@then('check answer {operations}')
def step_impl(context, operations):
    context.page.answer(operations)
