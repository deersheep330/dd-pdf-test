from behave import *

@given("on ps page")
def on_ps_page(context):
    if context.is_background_met():
        return
    context.ps_page.navigate()

@then("login")
def login(context):
    if context.is_background_met():
        return
    context.ps_page.login_as_unlimited_user()

