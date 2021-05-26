from behave import *

@given("on ps page")
def on_ps_page(context):
    context.ps_page.navigate()

@then("login")
def login(context):
    context.ps_page.login_as_unlimited_user()

