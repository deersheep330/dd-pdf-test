from behave import *

@given("on ps page")
def on_ps_page(context):
    if context.dd_page.is_pdf_downloaded():
        return
    context.ps_page.navigate()

@then("login")
def login(context):
    if context.dd_page.is_pdf_downloaded():
        return
    context.ps_page.login_as_unlimited_user()

