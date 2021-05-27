from behave import *

@then("navigate to dd page")
def navigate_to_dd_page(context):
    context.dd_page.navigate()

@then("import patents")
def import_patents(context):
    context.dd_page.upload_file()

@then("start analysis")
def start_analysis(context):
    context.dd_page.start_analysis()

@then("download pdf")
def download_pdf(context):
    context.dd_page.download_pdf()
    context.dd_page.get_downloaded_pdf()