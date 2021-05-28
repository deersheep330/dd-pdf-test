import os
from pdf.utils import get_latest_file_from_folder, get_file_count_from_folder
from pdf.utils import parse_pdf as _parse_pdf
from pdf.virtual_page import VirtualPage


class DDPage(VirtualPage):

    def __init__(self, driver, url):

        super().__init__(driver)
        self.url = url

        self.add_element("DDLogo", "//*[contains(@class, 'upload')]//*[contains(@class, 'logo')]")

        self.add_element("ChangeLang", "//*[@class='lang']")
        self.add_element("EnglishLang", "//*[@class='lang-option' and contains(text(), 'English')]")

        # Patent No. tab
        self.add_element("PatentNumberTab", "(//li[contains(@class, 'upload__tab')])[1]")

        # Patent No. tab -> upload file sub-tab
        self.add_element("UploadFileTab", "(//li[contains(@class, 'upload__tab')])[1]")
        self.add_element("UploadFileHint", "//span[@i18n-txt='due.upload.excel.filetype']")
        self.add_element("UploadFileDragAndDrop", "//input[@class='form-control-file']")
        self.add_element("UploadFileConfirm", "//button[@i18n-txt='due.button.confirm']")

        # Patent No. tab -> input sub-tab
        self.add_element("InputTab", "//div[contains(text(),'Input Numbers')]")
        self.add_element("InputBox", "(//textarea[@class='form-textarea form-control'])[2]")
        self.add_element("InputConfirm", "//button[@i18n-txt='due.button.confirm']")

        # Party tab
        self.add_element("PartyTab", "//li[contains(text(), 'Party')]")

        # Import from PV tab
        self.add_element("ImportFromProjectTab", "//li[contains(text(), 'Patent Vault')]")

        # History tab
        self.add_element("HistoryTab", "//li[contains(text(), 'History')]")
        self.add_element("PurchasedTab", "//*[contains(text(),'Analysis Result')]")

        # Temp CRIF History tab
        self.add_element("TempCRIFHistoryTab", "//li[contains(text(), 'Temp CRIF History')]")

        # Saved in PV tab
        self.add_element("SavedInPVTab", "//a[contains(text(),'Saved in Patent Vault')]")

        # upload success
        self.add_element("UploadSuccess", "//label[@class='title']")
        self.add_element("CSTab", "//span[@i18n-txt='due.page.coveragestatus']")

        self.add_element("StartAnalysis", "//*[@i18n-txt='due.button.startanalytics']")

        # tabs
        self.add_element("CSTab", "//span[@i18n-txt='due.page.coveragestatus']")
        self.add_element("TECHTab", "//span[@i18n-txt='due.page.technology']")
        self.add_element("OITab", "//span[@i18n-txt='due.page.inventorapplicant']")
        self.add_element("HHTab", "//span[@i18n-txt='due.page.historicalhighlight']")
        self.add_element("QVTab", "//span[@i18n-txt='due.page.qualityvalue']")
        self.add_element("QHTab", "//span[@i18n-txt='due.page.qualityhighlight']")
        self.add_element("VHTab", "//span[@i18n-txt='due.page.valuehighlight']")

        self.add_element("CS1Title", "//span[@i18n-txt='due.chartname.coverage' or @i18n-txt='due.report.title.cs1']")
        self.add_element("TECH1Title", "//span[@i18n-txt='due.chartname.technicalfield' or @i18n-txt='due.report.title.te1']")
        self.add_element("OI1Title", "//span[@i18n-txt='due.chartname.cownership']")
        self.add_element("HH2Title", "//span[@i18n-txt='due.chartname.validity']")
        self.add_element("QV2Title", "//span[@i18n-txt='due.chartname.valuequality']")
        self.add_element("QH2Title", "//span[@i18n-txt='due.chartname.eligibility']")
        self.add_element("VH1Title", "//span[@i18n-txt='due.chartname.potentialtarget']")

        # charts
        self.add_element("CS1", "//div[@id='custMap']")
        self.add_element("CS2", "//div[@id='stackedArea']")
        self.add_element("CS3", "//div[@id='StackedChart']")
        self.add_element("TECH1", "//div[@id='technical-field']")
        self.add_element("TECH2", "//div[contains(@class, 'stream-graph')]")
        self.add_element("OI1", "//div[contains(@class, 'ownership-issue')]")
        self.add_element("OI2", "//div[contains(@class, 'spark-line-chart')]")
        self.add_element("OI3", "//div[contains(@class, 'owner-inventor-chart')]")
        self.add_element("HH1", "//div[@id='hh_1']")
        self.add_element("HH2", "//div[@id='MultiColorBarChart']")
        self.add_element("QV1", "//div[contains(@class, 'family-size-bubble-chart')]")
        self.add_element("QV2", "//div[@id='bubbleChart']")
        self.add_element("QV3", "//div[contains(@id, 'negitiveChart')]")
        self.add_element("QH1", "//div[@id='QH-1-chart']")
        self.add_element("QH2", "//div[@id='QH-2-chart']")
        self.add_element("VH1", "//div[contains(@class, 'invest-target-chart')]")
        self.add_element("VH2", "//div[contains(@class, 'spark-line-chart')]")
        self.add_element("VH3", "//div[contains(@class, 'sankey-chart')]")

        # filter dropdown
        self.add_element("1stChartLegalStatusDropdown", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[1]/button")
        self.add_element("1stChartLegalStatusSelectAll", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[1]/ul/div/li[1]/form//*[contains(text(), 'Select All')]")
        self.add_element("1stChartLegalStatusActive", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[1]/ul/div/li[1]/form//*[contains(text(), 'Active')]")
        self.add_element("1stChartLegalStatusPending", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[1]/ul/div/li[1]/form//*[contains(text(), 'Pending')]")
        self.add_element("1stChartLegalStatusInactive", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[1]/ul/div/li[1]/form//*[contains(text(), 'Inactive')]")
        self.add_element("1stChartLegalStatusSubmit", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[1]/ul/div/button")

        self.add_element("2ndChartLegalStatusDropdown", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[2]/button")
        self.add_element("2ndChartLegalStatusSelectAll", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[2]/ul/div/li[1]/form//*[contains(text(), 'Select All')]")
        self.add_element("2ndChartLegalStatusActive", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[2]/ul/div/li[1]/form//*[contains(text(), 'Active')]")
        self.add_element("2ndChartLegalStatusPending", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[2]/ul/div/li[1]/form//*[contains(text(), 'Pending')]")
        self.add_element("2ndChartLegalStatusInactive", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[2]/ul/div/li[1]/form//*[contains(text(), 'Inactive')]")
        self.add_element("2ndChartLegalStatusSubmit", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[2]/ul/div/button")

        self.add_element("3rdChartLegalStatusDropdown", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[3]/button")
        self.add_element("3rdChartLegalStatusSelectAll", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[3]/ul/div/li[1]/form//*[contains(text(), 'Select All')]")
        self.add_element("3rdChartLegalStatusActive", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[3]/ul/div/li[1]/form//*[contains(text(), 'Active')]")
        self.add_element("3rdChartLegalStatusPending", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[3]/ul/div/li[1]/form//*[contains(text(), 'Pending')]")
        self.add_element("3rdChartLegalStatusInactive", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[3]/ul/div/li[1]/form//*[contains(text(), 'Inactive')]")
        self.add_element("3rdChartLegalStatusSubmit", "(//div[contains(@class, 'dropdown b-dropdown filter-dropdwon')])[3]/ul/div/button")

        # filter options
        self.add_element("1stChartFilterButton", "(//span[@i18n-txt='due.chartcommon.filter'])[1]")
        self.add_element("2ndChartFilterButton", "(//span[@i18n-txt='due.chartcommon.filter'])[2]")
        self.add_element("3rdChartFilterButton", "(//span[@i18n-txt='due.chartcommon.filter'])[3]")
        self.add_element("FilterSubmit", "//button[@i18n-txt='due.button.submit']")
        self.add_element("FilterClear", "//*[contains(@class, 'show')]//*[contains(text(), 'lear')]")
        self.add_element("FilterCN", "//*[@i18n-txt='name.cn']")

        # count by
        self.add_element("1stChartCountByButton", "(//div[contains(@i18n-txt, 'due.unit.')])[1]")
        self.add_element("2ndChartCountByButton", "(//div[contains(@i18n-txt, 'due.unit.')])[2]")
        self.add_element("3rdChartCountByButton", "(//div[contains(@i18n-txt, 'due.unit.')])[3]")
        self.add_element("1stChartCountByFamily", "(//button/span[@i18n-txt='due.unit.simplefamily'])[1]")
        self.add_element("2ndChartCountByFamily", "(//button/span[@i18n-txt='due.unit.simplefamily'])[2]")
        self.add_element("3rdChartCountByFamily", "(//button/span[@i18n-txt='due.unit.simplefamily'])[3]")

        # select data
        self.add_element("TECH1SelectData", "//div[contains(@class,'technical-field')]//*[name()='svg' and contains(@class, 'fa-cog')]")
        self.add_element("TECH2SelectData", "//div[contains(@class,'stream-graph')]//*[name()='svg' and contains(@class, 'fa-cog')]")
        self.add_element("OI2SelectData", "//div[contains(@class, 'spark-line-chart')]//*[name()='svg' and contains(@class, 'fa-cog')]")
        self.add_element("OI2SelectDataInventors", "//span[@i18n-txt='due.chart.inventor']")
        self.add_element("OI2SelectDataApplicants", "//span[@i18n-txt='due.chart.applicant']")
        self.add_element("OI3SelectData", "//div[contains(@class,'owner-inventor-chart')]//*[name()='svg' and contains(@class, 'fa-cog')]")
        self.add_element("HH1SelectData", "//*[contains(@class, 'fa-cog')]")
        self.add_element("VH1SelectData", "//div[contains(@class,'invest-target-chart')]//*[name()='svg' and contains(@class, 'fa-cog')]")
        self.add_element("VH2SelectData", "//div[contains(@class,'spark-line-chart')]//*[name()='svg' and contains(@class, 'fa-cog')]")
        self.add_element("VH3FamilyIdSelectData", "(//div[contains(@class,'sankey-chart')]//i[@class='fal fa-cog'])[1]")
        self.add_element("VH3PotentialTargetSelectData", "(//div[contains(@class,'sankey-chart')]//i[@class='fal fa-cog'])[2]")

        # download pdf
        self.add_element("DownloadPdf", "//*[contains(@i18n-txt, 'due.page.downloadreport')]//*[name()='svg' and contains(@class, 'fa-file-download')]")
        self.add_element("DownloadPdfModal", "//*[contains(text(), 'Download Report')]")
        self.add_element("DownloadPdfConfirm", "//*[@i18n-txt='due.button.confirm']")
        self.add_element("DownloadPdfCustomize", "//*[contains(text(), 'Customize')]")
        self.add_element("DownloadPdfClear", "//*[@i18n-txt='due.chart.clear']")

        self.add_element("DownloadPdfCS1", "//*[@for='CS1']")
        self.add_element("DownloadPdfCS2", "//*[@for='CS2']")
        self.add_element("DownloadPdfCS3", "//*[@for='CS3']")

        self.add_element("DownloadPdfTECH1", "//*[@for='TECH1']")
        self.add_element("DownloadPdfTECH2", "//*[@for='TECH2']")

        self.add_element("DownloadPdfOI1", "//*[@for='OI1']")
        self.add_element("DownloadPdfOI2_Assignees", "//*[@for='OI2_ASSIGNEES']")
        self.add_element("DownloadPdfOI2_Inventors", "//*[@for='OI2_INVENTORS']")
        self.add_element("DownloadPdfOI3", "//*[@for='OI3']")

        self.add_element("DownloadPdfHH1", "//*[@for='HH1_TRANSACTED']")
        self.add_element("DownloadPdfHH2", "//*[@for='HH3']")

        self.add_element("DownloadPdfQV1", "//*[@for='QV1']")
        self.add_element("DownloadPdfQV2", "//*[@for='QV2']")
        self.add_element("DownloadPdfQV3", "//*[@for='QV3_DEFAULT_TOP_1']")

        self.add_element("DownloadPdfQH1", "//*[@for='QH1']")
        self.add_element("DownloadPdfQH2", "//*[@for='QH2']")

        self.add_element("DownloadPdfVH1_Quantity", "//*[@for='VH2_QUANTITY']")
        self.add_element("DownloadPdfVH1_Percentage", "//*[@for='VH2_PERCENTAGE']")
        self.add_element("DownloadPdfVH2", "//*[@for='VH1']")

        self.add_element("DownloadPdfVH3_Potential", "//*[@for='VH3_POTENTIAL']")
        self.add_element("DownloadPdfVH3_Family", "//*[@for='VH3_FAMILYID']")

        self.pdf_content = ''
        self.pdf_fields = {
            'cs': 'Coverage and Status',
            'cs_1': 'Global Coverage',
            'cs_2': 'Remaining Life',
            'cs_3': 'Pending Patents',

            'tech': 'Technologies',
            'tech_1': 'Technical Fields',
            'tech_2': 'Technology Timeline',

            'oi': 'Owner/Inventor/Applicant',
            'oi_1': 'Co-Ownerships and Co-Applicants',
            'oi_2_assignees': 'Top 10 Assignees',
            'oi_2_inventors': 'Top 10 Inventors',
            'oi_3': 'Current Patent Owners',

            'hh': 'Historical Highlights',
            'hh_1': 'Transacted Patents',
            'hh_2': 'Litigated Patents',

            'qv': 'Quality and Value',
            'qv_1': 'High-Value Patent Families',
            'qv_2': 'Quality of High-Value Patents',
            'qv_3': 'Peer Comparison in the Same Field',

            'qh': 'Quality Highlights',
            'qh_1': 'Abandoned and Revoked Family Members',
            'qh_2': 'Eligibility and Novelty Issues',

            'vh': 'Value Highlights',
            'vh_1': 'Potential Targets of the Portfolio',
            'vh_2': 'Filing Dates of Potential Targets in the Relevant Art',
            'vh_3': 'Patents Against the Potential Targets',

            'families': '# of Patent Families in the chart',
            'applications': '# of Applications in the chart',

            'summary': 'Summary'
        }

    def navigate(self):
        self.op.navigate_to(self.url)
        self.op.wait_for(self.get_element("DDLogo"))
        # wait for being redirected to history tab
        self.op.sleep(5)

    def change_lang_to_english(self):
        self.op.click_and_wait_for(self.get_element("ChangeLang"), self.get_element("EnglishLang"))
        self.op.click(self.get_element("EnglishLang"))

    def upload_file(self):

        wait_time = 180

        self.op.click_and_wait_for(self.get_element("PatentNumberTab"), self.get_element("UploadFileTab"))
        self.op.click_and_wait_for(self.get_element("UploadFileTab"), self.get_element("UploadFileHint"))

        file_path = os.path.join(os.getcwd(), "files", "import_smoke.csv")
        self.op.send_text(self.get_element("UploadFileDragAndDrop"), file_path)
        self.op.click(self.get_element("UploadFileConfirm"))

        try:
            self.op.wait_for(self.get_element("UploadSuccess"), wait_time)
        except Exception:
            raise RuntimeError("Import File Failed.")

    def start_analysis(self):
        self.op.click_and_wait_for(self.get_element("StartAnalysis"), self.get_element("CSTab"))

    def download_pdf(self):
        download_path = os.path.join(os.getcwd(), 'downloads')
        orig_file_count = get_file_count_from_folder(download_path)

        self.op.click_and_wait_for(self.get_element("DownloadPdf"), self.get_element("DownloadPdfModal"))
        self.op.click(self.get_element("DownloadPdfConfirm"))
        self.op.wait_for_response('/dd-api/export/downloadFile', wait_for_timeout=180)

        retry = 0
        max_retry = 20
        sleep_time = 3
        while retry < max_retry:
            current_file_count = get_file_count_from_folder(download_path)
            if current_file_count > orig_file_count:
                return
            else:
                self.op.sleep(sleep_time)
                retry += 1
        raise RuntimeError('download pdf failed')

    def get_downloaded_pdf(self):
        download_path = os.path.join(os.getcwd(), 'downloads')
        return get_latest_file_from_folder(download_path)

    def parse_pdf(self, pdf):
        self.pdf_content = _parse_pdf(pdf)
        print(self.pdf_content)

    def validate_pdf(self):
        pass

    def wait_for_CS1(self):
        self.op.click_and_wait_for(self.get_element("CSTab"), self.get_element("CS1Title"))
        self.op.wait_for(self.get_element("CS1"))

    def wait_for_CS2(self):
        self.op.click_and_wait_for(self.get_element("CSTab"), self.get_element("CS1Title"))
        self.op.wait_for(self.get_element("CS2"))

    def wait_for_CS3(self):
        self.op.click_and_wait_for(self.get_element("CSTab"), self.get_element("CS1Title"))
        self.op.wait_for(self.get_element("CS3"))

    def wait_for_TECH1(self):
        self.op.click_and_wait_for(self.get_element("TECHTab"), self.get_element("TECH1Title"))
        self.op.wait_for(self.get_element("TECH1"))

    def wait_for_TECH2(self):
        self.op.click_and_wait_for(self.get_element("TECHTab"), self.get_element("TECH1Title"))
        self.op.wait_for(self.get_element("TECH2"))

    def wait_for_OI1(self):
        self.op.click_and_wait_for(self.get_element("OITab"), self.get_element("OI1Title"))
        self.op.wait_for(self.get_element("OI1"))

    def wait_for_OI2(self):
        self.op.click_and_wait_for(self.get_element("OITab"), self.get_element("OI1Title"))
        self.op.wait_for(self.get_element("OI2"))

    def wait_for_OI3(self):
        self.op.click_and_wait_for(self.get_element("OITab"), self.get_element("OI1Title"))
        self.op.wait_for(self.get_element("OI3"))

    def wait_for_HH1(self):
        self.op.click_and_wait_for(self.get_element("HHTab"), self.get_element("HH2Title"))
        self.op.wait_for(self.get_element("HH1"))

    def wait_for_HH2(self):
        self.op.click_and_wait_for(self.get_element("HHTab"), self.get_element("HH2Title"))
        self.op.wait_for(self.get_element("HH2"))

    def wait_for_QV1(self):
        self.op.click_and_wait_for(self.get_element("QVTab"), self.get_element("QV2Title"))
        self.op.wait_for(self.get_element("QV1"))

    def wait_for_QV2(self):
        self.op.click_and_wait_for(self.get_element("QVTab"), self.get_element("QV2Title"))
        self.op.wait_for(self.get_element("QV2"))

    def wait_for_QV3(self):
        self.op.click_and_wait_for(self.get_element("QVTab"), self.get_element("QV2Title"))
        self.op.wait_for(self.get_element("QV3"))

    def wait_for_QH1(self):
        self.op.click_and_wait_for(self.get_element("QHTab"), self.get_element("QH2Title"))
        self.op.wait_for(self.get_element("QH1"))

    def wait_for_QH2(self):
        self.op.click_and_wait_for(self.get_element("QHTab"), self.get_element("QH2Title"))
        self.op.wait_for(self.get_element("QH2"))

    def wait_for_VH1(self):
        self.op.click_and_wait_for(self.get_element("VHTab"), self.get_element("VH1Title"))
        self.op.wait_for(self.get_element("VH1"))

    def wait_for_VH2(self):
        self.op.click_and_wait_for(self.get_element("VHTab"), self.get_element("VH1Title"))
        self.op.wait_for(self.get_element("VH2"))

    def wait_for_VH3(self):
        self.op.click_and_wait_for(self.get_element("VHTab"), self.get_element("VH1Title"))
        self.op.wait_for(self.get_element("VH3"))

    def quit(self):
        self.op.quit()
