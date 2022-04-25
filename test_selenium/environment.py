from pages.calculator_pages import BasicCalculator
from ipdb import spost_mortem


def before_all(context):
    context.page = BasicCalculator()


def after_all(context):
    context.page.browser_quit()


def after_step(context, step):
    if context.config.userdata.getbool("debug") and step.status == 'failed':
        spost_mortem(step.exc_traceback)
