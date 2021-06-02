from behave import *

@then("navigate to dd page")
def navigate_to_dd_page(context):
    if context.is_background_met():
        return
    context.dd_page.navigate()

@then("import patents")
def import_patents(context):
    if context.is_background_met():
        return
    context.dd_page.upload_file()

@then("start analysis")
def start_analysis(context):
    if context.is_background_met():
        return
    context.dd_page.start_analysis()

@then("download pdf")
def download_pdf(context):
    if context.is_background_met():
        return
    context.dd_page.download_pdf()
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@given("on pdf downloaded")
def on_pdf_downloaded(context):
    is_downloaded = context.dd_page.is_pdf_downloaded()
    if not is_downloaded:
        raise RuntimeError('pdf content not found!')

@given("on workspace")
def on_workspace(context):
    is_on_workspace = context.dd_page.is_on_workspace()
    if not is_on_workspace:
        raise RuntimeError('not on workspace!')

@then("wait for cs1")
def wait_for_cs1(context):
    context.dd_page.wait_for_cs1()

@then("wait for cs2")
def wait_for_cs2(context):
    context.dd_page.wait_for_cs2()

@then("wait for cs3")
def wait_for_cs3(context):
    context.dd_page.wait_for_cs3()

@then("wait for tech1")
def wait_for_tech1(context):
    context.dd_page.wait_for_tech1()

@then("wait for tech2")
def wait_for_tech2(context):
    context.dd_page.wait_for_tech2()

@then("wait for oi1")
def wait_for_oi1(context):
    context.dd_page.wait_for_oi1()

@then("wait for oi2")
def wait_for_oi2(context):
    context.dd_page.wait_for_oi2()

@then("wait for oi3")
def wait_for_oi3(context):
    context.dd_page.wait_for_oi3()

@then("wait for hh1")
def wait_for_hh1(context):
    context.dd_page.wait_for_hh1()

@then("wait for hh2")
def wait_for_hh2(context):
    context.dd_page.wait_for_hh2()

@then("wait for qv1")
def wait_for_qv1(context):
    context.dd_page.wait_for_qv1()

@then("wait for qv2")
def wait_for_qv2(context):
    context.dd_page.wait_for_qv2()

@then("wait for qv3")
def wait_for_qv3(context):
    context.dd_page.wait_for_qv3()

@then("wait for qh1")
def wait_for_qh1(context):
    context.dd_page.wait_for_qh1()

@then("wait for qh2")
def wait_for_qh2(context):
    context.dd_page.wait_for_qh2()

@then("wait for vh1")
def wait_for_vh1(context):
    context.dd_page.wait_for_vh1()

@then("wait for vh2")
def wait_for_vh2(context):
    context.dd_page.wait_for_vh2()

@then("wait for vh3")
def wait_for_vh3(context):
    context.dd_page.wait_for_vh3()

@then("vh3 switch to family id tab")
def vh3_switch_to_family_id_tab(context):
    context.dd_page.vh3_switch_to_family_id_tab()

@then("download cs1 pdf")
def download_cs1_pdf(context):
    context.dd_page.download_customized_pdf("CS1")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download cs2 pdf")
def download_cs2_pdf(context):
    context.dd_page.download_customized_pdf("CS2")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download cs3 pdf")
def download_cs3_pdf(context):
    context.dd_page.download_customized_pdf("CS3")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download tech1 pdf")
def download_tech1_pdf(context):
    context.dd_page.download_customized_pdf("TECH1")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download tech2 pdf")
def download_tech2_pdf(context):
    context.dd_page.download_customized_pdf("TECH2")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download oi1 pdf")
def download_oi1_pdf(context):
    context.dd_page.download_customized_pdf("OI1")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download oi2 assignees pdf")
def download_oi2_assignees_pdf(context):
    context.dd_page.download_customized_pdf("OI2_Assignees")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download oi2 inventors pdf")
def download_oi2_inventors_pdf(context):
    context.dd_page.download_customized_pdf("OI2_Inventors")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download oi3 pdf")
def download_oi3_pdf(context):
    context.dd_page.download_customized_pdf("OI3")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download hh1 pdf")
def download_hh1_pdf(context):
    context.dd_page.download_customized_pdf("HH1")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download hh1 transferred pdf")
def download_hh1_transferred_pdf(context):
    context.dd_page.download_customized_pdf("HH1_Transferred")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download hh2 pdf")
def download_hh2_pdf(context):
    context.dd_page.download_customized_pdf("HH2")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download qv1 pdf")
def download_qv1_pdf(context):
    context.dd_page.download_customized_pdf("QV1")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download qv2 pdf")
def download_qv2_pdf(context):
    context.dd_page.download_customized_pdf("QV2")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download qv3 pdf")
def download_qv3_pdf(context):
    context.dd_page.download_customized_pdf("QV3")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download qh1 pdf")
def download_qh1_pdf(context):
    context.dd_page.download_customized_pdf("QH1")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download qh2 pdf")
def download_qh2_pdf(context):
    context.dd_page.download_customized_pdf("QH2")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download vh1 quantity pdf")
def download_vh1_quantity_pdf(context):
    context.dd_page.download_customized_pdf("VH1_Quantity")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download vh1 percentage pdf")
def download_vh1_percentage_pdf(context):
    context.dd_page.download_customized_pdf("VH1_Percentage")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download vh2 pdf")
def download_vh2_pdf(context):
    context.dd_page.download_customized_pdf("VH2")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download vh3 potential targets pdf")
def download_vh3_potential_targets_pdf(context):
    context.dd_page.download_customized_pdf("VH3_Potential")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

@then("download vh3 family id pdf")
def download_vh3_family_id_pdf(context):
    context.dd_page.download_customized_pdf("VH3_Family")
    pdf_path = context.dd_page.get_downloaded_pdf()
    context.dd_page.parse_pdf(pdf_path)

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

@then("validate customized cs1")
def validate_customized_cs1(context):
    context.dd_page.validate_cs1(True)

@then("validate customized cs2")
def validate_customized_cs2(context):
    context.dd_page.validate_cs2(True)

@then("validate customized cs3")
def validate_customized_cs3(context):
    context.dd_page.validate_cs3(True)

@then("validate customized tech1")
def validate_customized_tech1(context):
    context.dd_page.validate_tech1(True)

@then("validate customized tech2")
def validate_customized_tech2(context):
    context.dd_page.validate_tech2(True)

@then("validate customized tech2 class")
def validate_customized_tech2_class(context):
    context.dd_page.validate_tech2(True, 'Class')

@then("validate customized tech2 subclass")
def validate_customized_tech2_subclass(context):
    context.dd_page.validate_tech2(True, 'Subclass')

@then("validate customized tech2 group")
def validate_customized_tech2_group(context):
    context.dd_page.validate_tech2(True, 'Group')

@then("validate customized tech2 subgroup")
def validate_customized_tech2_subgroup(context):
    context.dd_page.validate_tech2(True, 'Subgroup')

@then("validate customized oi1")
def validate_customized_oi1(context):
    context.dd_page.validate_oi1(True)

@then("validate customized oi2 assignees")
def validate_customized_oi2_assignees(context):
    context.dd_page.validate_oi2_assignees(True)

@then("validate customized oi2 inventors")
def validate_customized_oi2_inventors(context):
    context.dd_page.validate_oi2_inventors(True)

@then("validate customized oi3")
def validate_customized_oi3(context):
    context.dd_page.validate_oi3(True)

@then("validate customized hh1")
def validate_customized_hh1(context):
    context.dd_page.validate_hh1(True)

@then("validate customized hh1 transferred")
def validate_customized_hh1_transferred(context):
    context.dd_page.validate_hh1_transferred(True)

@then("validate customized hh2")
def validate_customized_hh2(context):
    context.dd_page.validate_hh2(True)

@then("validate customized qv1")
def validate_customized_qv1(context):
    context.dd_page.validate_qv1(True)

@then("validate customized qv2")
def validate_customized_qv2(context):
    context.dd_page.validate_qv2(True)

@then("validate customized qv3")
def validate_customized_qv3(context):
    context.dd_page.validate_qv3(True)

@then("validate customized qh1")
def validate_customized_qh1(context):
    context.dd_page.validate_qh1(True)

@then("validate customized qh2")
def validate_customized_qh2(context):
    context.dd_page.validate_qh2(True)

@then("validate customized vh1")
def validate_customized_vh1(context):
    context.dd_page.validate_vh1(True)

@then("validate customized vh2")
def validate_customized_vh2(context):
    context.dd_page.validate_vh2(True)

@then("validate customized vh3 potential targets")
def validate_customized_vh3_potential_targets(context):
    context.dd_page.validate_vh3_potential_targets(True)

@then("validate customized vh3 family id")
def validate_customized_vh3_family_id(context):
    context.dd_page.validate_vh3_family_id(True)

@then("change cs1 filter")
def change_cs1_filter(context):
    context.dd_page.change_cs1_filter()

@then("change cs2 filter")
def change_cs2_filter(context):
    context.dd_page.change_cs2_filter()

@then("change cs3 filter")
def change_cs3_filter(context):
    context.dd_page.change_cs3_filter()

@then("change tech1 filter")
def change_tech1_filter(context):
    context.dd_page.change_tech1_filter()

@then("change tech2 filter")
def change_tech2_filter(context):
    context.dd_page.change_tech2_filter()

@then("change oi1 filter")
def change_oi1_filter(context):
    context.dd_page.change_oi1_filter()

@then("change oi2 filter")
def change_oi2_filter(context):
    context.dd_page.change_oi2_filter()

@then("change oi3 filter")
def change_oi3_filter(context):
    context.dd_page.change_oi3_filter()

@then("change hh1 filter")
def change_hh1_filter(context):
    context.dd_page.change_hh1_filter()

@then("change hh2 filter")
def change_hh2_filter(context):
    context.dd_page.change_hh2_filter()

@then("change qv1 filter")
def change_qv1_filter(context):
    context.dd_page.change_qv1_filter()

@then("change qv2 filter")
def change_qv2_filter(context):
    context.dd_page.change_qv2_filter()

@then("change qv3 filter")
def change_qv3_filter(context):
    context.dd_page.change_qv3_filter()

@then("change qh1 filter")
def change_qh1_filter(context):
    context.dd_page.change_qh1_filter()

@then("change qh2 filter")
def change_qh2_filter(context):
    context.dd_page.change_qh2_filter()

@then("change vh1 filter")
def change_vh1_filter(context):
    context.dd_page.change_vh1_filter()

@then("change vh2 filter")
def change_vh2_filter(context):
    context.dd_page.change_vh2_filter()

@then("change vh3 filter")
def change_vh3_filter(context):
    context.dd_page.change_vh3_filter()

@then("change tech1 select data")
def change_tech1_select_data(context):
    context.dd_page.change_tech1_select_data()

@then("change tech2 class select data")
def change_tech2_class_select_data(context):
    context.dd_page.change_tech2_class_select_data()

@then("change tech2 subclass select data")
def change_tech2_subclass_select_data(context):
    context.dd_page.change_tech2_subclass_select_data()

@then("change tech2 group select data")
def change_tech2_group_select_data(context):
    context.dd_page.change_tech2_group_select_data()

@then("change tech2 subgroup select data")
def change_tech2_subgroup_select_data(context):
    context.dd_page.change_tech2_subgroup_select_data()

@then("change oi2 inventors select data")
def change_oi2_inventors_select_data(context):
    context.dd_page.change_oi2_inventors_select_data()

@then("change oi2 applicants select data")
def change_oi2_applicants_select_data(context):
    context.dd_page.change_oi2_applicants_select_data()

@then("change oi3 select data")
def change_oi3_select_data(context):
    context.dd_page.change_oi3_select_data()

@then("change hh1 select data")
def change_hh1_select_data(context):
    context.dd_page.change_hh1_select_data()

@then("change vh1 select data")
def change_vh1_select_data(context):
    context.dd_page.change_vh1_select_data()

@then("change vh2 select data")
def change_vh2_select_data(context):
    context.dd_page.change_vh2_select_data()

@then("change vh3 potential targets select data")
def change_vh3_potential_targets_select_data(context):
    context.dd_page.change_vh3_potential_targets_select_data()

@then("change vh3 family id select data")
def change_vh3_family_id_select_data(context):
    context.dd_page.change_vh3_family_id_select_data()