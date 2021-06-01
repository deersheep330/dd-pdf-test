from behave import *

@then("navigate to dd page")
def navigate_to_dd_page(context):
    if context.dd_page.is_pdf_downloaded():
        return
    context.dd_page.navigate()

@then("import patents")
def import_patents(context):
    if context.dd_page.is_pdf_downloaded():
        return
    context.dd_page.upload_file()

@then("start analysis")
def start_analysis(context):
    if context.dd_page.is_pdf_downloaded():
        return
    context.dd_page.start_analysis()

@then("download pdf")
def download_pdf(context):
    if context.dd_page.is_pdf_downloaded():
        return
    context.dd_page.download_pdf()
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@given("on pdf downloaded")
def on_pdf_downloaded(context):
    is_downloaded = context.dd_page.is_pdf_downloaded()
    if not is_downloaded:
        raise RuntimeError('pdf content not found!')

@then("validate cs summary")
def validate_cs_summary(context):
    context.dd_page.validate_cs_summary()

@then("validate cs1")
def validate_cs1(context):
    context.dd_page.validate_cs1()

@then("validate cs2")
def validate_cs2(context):
    context.dd_page.validate_cs2()

@then("validate cs3")
def validate_cs3(context):
    context.dd_page.validate_cs3()

@then("validate tech summary")
def validate_tech_summary(context):
    context.dd_page.validate_tech_summary()

@then("validate tech1")
def validate_tech1(context):
    context.dd_page.validate_tech1()

@then("validate tech2")
def validate_tech2(context):
    context.dd_page.validate_tech2()

@then("validate oi summary")
def validate_oi_summary(context):
    context.dd_page.validate_oi_summary()

@then("validate oi1")
def validate_oi1(context):
    context.dd_page.validate_oi1()

@then("validate oi2 assignees")
def validate_oi2_assignees(context):
    context.dd_page.validate_oi2_assignees()

@then("validate oi2 inventors")
def validate_oi2_inventors(context):
    context.dd_page.validate_oi2_inventors()

@then("validate oi3")
def validate_oi3(context):
    context.dd_page.validate_oi3()

@then("validate hh summary")
def validate_hh_summary(context):
    context.dd_page.validate_hh_summary()

@then("validate hh1")
def validate_hh1(context):
    context.dd_page.validate_hh1()

@then("validate hh1 transferred")
def validate_hh1_transferred(context):
    context.dd_page.validate_hh1_transferred()

@then("validate hh2")
def validate_hh2(context):
    context.dd_page.validate_hh2()

@then("validate qv summary")
def validate_qv_summary(context):
    context.dd_page.validate_qv_summary()

@then("validate qv1")
def validate_qv1(context):
    context.dd_page.validate_qv1()

@then("validate qv2")
def validate_qv2(context):
    context.dd_page.validate_qv2()

@then("validate qv3")
def validate_qv3(context):
    context.dd_page.validate_qv3()

@then("validate qh summary")
def validate_qh_summary(context):
    context.dd_page.validate_qh_summary()

@then("validate qh1")
def validate_qh1(context):
    context.dd_page.validate_qh1()

@then("validate qh2")
def validate_qh2(context):
    context.dd_page.validate_qh2()

@then("validate vh summary")
def validate_vh_summary(context):
    context.dd_page.validate_vh_summary()

@then("validate vh1")
def validate_vh1(context):
    context.dd_page.validate_vh1()

@then("validate vh2")
def validate_vh2(context):
    context.dd_page.validate_vh2()

@then("validate vh3 potential targets")
def validate_vh3_potential_targets(context):
    context.dd_page.validate_vh3_potential_targets()

@then("validate vh3 family id")
def validate_vh3_family_id(context):
    context.dd_page.validate_vh3_family_id()
