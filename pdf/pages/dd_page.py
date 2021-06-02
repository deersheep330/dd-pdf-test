import os
import re
from pdf.utils import get_latest_file_from_folder, get_file_count_from_folder, parse_int_from_str
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
        self.add_element("HH2", "//div[@id='HH-3']")
        self.add_element("QV1", "//div[contains(@class, 'family-size-bubble-chart')]")
        self.add_element("QV2", "//div[@id='bubbleChart']")
        self.add_element("QV3", "//div[contains(@id, 'negitiveChart')]")
        self.add_element("QH1", "//div[@id='QH-1-chart']")
        self.add_element("QH2", "//div[@id='QH-2-chart']")
        self.add_element("VH1", "(//div[contains(@class, 'invest-target-chart')])[1]")
        self.add_element("VH2", "//div[contains(@class, 'spark-line-chart')]")
        self.add_element("VH3", "//div[contains(@class, 'sankey-chart')]")

        # vh3 tabs
        self.add_element("VH3PotentialTargetsTab", "//*[@i18n-txt='due.chart.againsttargets']")
        self.add_element("VH3PotentialTargetsTabActive", "//*[@i18n-txt='due.chart.againsttargets' and contains(@class, 'active')]")
        self.add_element("VH3FamilyIdTab", "//*[@i18n-txt='export.familyId']")
        self.add_element("VH3FamilyIdTabActive", "//*[@i18n-txt='export.familyId' and contains(@class, 'active')]")

        # chart numbers
        self.add_element("FirstChartTotalNumber", "(//*[contains(@class, 'chart__container') or contains(@class, 'chartBlock ')][1]//*[contains(@class, 'main__subtitle')]//*[contains(@class, 'bold')])[1]")
        self.add_element("SecondCharTotaltNumber", "(//*[contains(@class, 'chart__container') or contains(@class, 'chartBlock ')][2]//*[contains(@class, 'main__subtitle')]//*[contains(@class, 'bold')])[1]")
        self.add_element("ThirdChartTotalNumber", "(//*[contains(@class, 'chart__container') or contains(@class, 'chartBlock ')][3]//*[contains(@class, 'main__subtitle')]//*[contains(@class, 'bold')])[1]")
        self.add_element("FirstChartActualNumber", "(//*[contains(@class, 'chart__container') or contains(@class, 'chartBlock ')][1]//*[contains(@class, 'main__subtitle')]//*[contains(@class, 'bold')])[2]")
        self.add_element("SecondChartActualNumber", "(//*[contains(@class, 'chart__container') or contains(@class, 'chartBlock ')][2]//*[contains(@class, 'main__subtitle')]//*[contains(@class, 'bold')])[2]")
        self.add_element("ThirdChartActualNumber", "(//*[contains(@class, 'chart__container') or contains(@class, 'chartBlock ')][3]//*[contains(@class, 'main__subtitle')]//*[contains(@class, 'bold')])[2]")

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
        self.add_element("FilterCancel", "//button[@i18n-txt='due.button.cancel']")
        self.add_element("FilterClear", "//*[contains(@class, 'filter')]//*[contains(@class, 'show')]//*[contains(text(), 'lear')]")
        self.add_element("FilterCN", "//*[contains(@class, 'filter')]//*[contains(@class, 'show')]//*[@i18n-txt='name.cn']")
        self.add_element("FilterEP", "//*[contains(@class, 'filter')]//*[contains(@class, 'show')]//*[@i18n-txt='name.ep']")

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
        self.add_element("DownloadPdfHH1_Transferred", "//*[@for='HH1_TRANSFERRED']")
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
            'hh_1_transferred': 'Transacted Patents - Transferred',
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
            'vh_3_potential_targets': 'Ranked by Potential Targets',
            'vh_3_family_id': 'Ranked by Family in Portfolio (ID)',

            'families': '# of Patent Families in the chart',
            'applications': '# of Applications in the chart',
            'total': 'Total # of Applications',

            'summary': 'Summary'
        }

        self.defaults = {
            'cs_1': 229,
            'cs_2': 43,
            'cs_3': 26,
            'tech_1': 157,
            'tech_2': 195,
            'oi_1': 79,
            'oi_2_assignees': 206,
            'oi_2_inventors': 41,
            'oi_3': 197,
            'hh_1': 22,
            'hh_1_transferred': 21,
            'hh_2': 69,
            'qv_1': 40,
            'qv_2': 42,
            'qv_3': 42,
            'qh_1': 15,
            'qh_2': 24,
            'vh_1': 267,
            'vh_2': 267,
            'vh_3_potential_targets': 267,
            'vh_3_family_id': 231
        }

        self.delimiter = r'[,; ()%\n]+'
        self.wait_for_timeout = 30

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

    def is_on_workspace(self):
        if self.op.is_alert_exist():
            self.op.click_alert_ok()
        elif self.op.is_exist(self.get_element("FilterCancel")):
            self.op.click_and_wait_until_disappear(self.get_element("FilterCancel"), self.get_element("FilterCancel"))
        elif self.op.is_exist(self.get_element("CSTab")):
            return True
        else:
            return False

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

    def download_customized_pdf(self, chart):
        download_path = os.path.join(os.getcwd(), 'downloads')
        orig_file_count = get_file_count_from_folder(download_path)

        self.op.click_and_wait_for(self.get_element("DownloadPdf"), self.get_element("DownloadPdfModal"))
        self.op.click_and_wait_for(self.get_element("DownloadPdfCustomize"), self.get_element("DownloadPdfClear"))
        self.op.click(self.get_element("DownloadPdfClear"))
        self.op.click(self.get_element("DownloadPdf" + chart))
        self.op.click(self.get_element("DownloadPdfConfirm"))
        self.op.wait_for_response('/dd-api/export/downloadFile', wait_for_timeout=180)

        retry = 0
        max_retry = 20
        sleep_time = 3
        while retry < max_retry:
            self.op.sleep(sleep_time)
            current_file_count = get_file_count_from_folder(download_path)
            if current_file_count > orig_file_count:
                return
            else:
                retry += 1
        raise RuntimeError('download pdf failed')

    def get_downloaded_pdf(self):
        download_path = os.path.join(os.getcwd(), 'downloads')
        return get_latest_file_from_folder(download_path)

    def parse_pdf(self, pdf):
        self.pdf_content = _parse_pdf(pdf)
        self.pdf_content = self.pdf_content.replace("\n", " ")
        print(self.pdf_content)

    def is_pdf_downloaded(self):
        if self.pdf_content == '':
            return False
        else:
            return True

    def __should_be_equal(self, expect, num):
        if expect * 0.9 < num < expect * 1.1:
            return True
        else:
            return False

    def __should_not_be_equal(self, expect, num):
        if num < expect * 0.5:
            return True
        else:
            return False

    def __get_section_of_chart(self, chart, size=256):
        end = len(self.pdf_content) - 1
        start = self.pdf_content.find(chart)
        if start == -1:
            raise RuntimeError(f'Cannot find {chart} in pdf!')
        else:
            _start = int(start - size / 2)
            _end = start + size
            if _end > end:
                _end = end
            if _start < 0:
                _start = 0
            return self.pdf_content[_start:_end]

    def __get_sentence_in_substring(self, substring, keyword, size=64):
        end = len(substring) - 1
        start = substring.find(keyword)
        if start == -1:
            raise RuntimeError(f'Cannot find {keyword} in substring: {substring}!')
        else:
            _end = start + size
            if _end > end:
                _end = end
            return substring[start:_end]

    def __get_num_list_from_str(self, string, delimiter):
        tokens = re.split(delimiter, string)
        _list = []
        for token in tokens:
            res = parse_int_from_str(token)
            if res is not None:
                _list.append(res)
        return _list

    def __get_first_num_from_str(self, string, delimiter):
        tokens = re.split(delimiter, string)
        for token in tokens:
            res = parse_int_from_str(token)
            if res is not None:
                return res
        raise RuntimeError(f'Cannot get number from {string}')

    def validate_cs_summary(self):
        cs = self.__get_section_of_chart(self.pdf_fields['cs'], size=4096)
        active = self.__get_sentence_in_substring(cs, 'Active', 32)
        print(f'active = {active}')
        pending = self.__get_sentence_in_substring(cs, 'Pending', 32)
        inactive = self.__get_sentence_in_substring(cs, 'Inactive', 32)
        if len(self.__get_num_list_from_str(active, self.delimiter)) < 2:
            raise RuntimeError(f'expect active summary but its {active}')
        if len(self.__get_num_list_from_str(pending, self.delimiter)) < 2:
            raise RuntimeError(f'expect pending summary but its {pending}')
        if len(self.__get_num_list_from_str(inactive, self.delimiter)) < 2:
            raise RuntimeError(f'expect inactive summary but its {inactive}')

    def validate_cs1(self, filtered=False):
        cs1 = self.__get_section_of_chart(self.pdf_fields['cs_1'])
        print(f'cs1 = {cs1}')
        sent = self.__get_sentence_in_substring(cs1, self.pdf_fields['applications'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['cs_1'], num):
            raise RuntimeError(f'expect number {self.defaults["cs_1"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['cs_1'], num):
            raise RuntimeError(f'expect number != {self.defaults["cs_1"]} but its {num}')

    def validate_cs2(self, filtered=False):
        cs2 = self.__get_section_of_chart(self.pdf_fields['cs_2'])
        print(f'cs2 = {cs2}')
        sent = self.__get_sentence_in_substring(cs2, self.pdf_fields['applications'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['cs_2'], num):
            raise RuntimeError(f'expect number {self.defaults["cs_2"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['cs_2'], num):
            raise RuntimeError(f'expect number != {self.defaults["cs_2"]} but its {num}')

    def validate_cs3(self, filtered=False):
        cs3 = self.__get_section_of_chart(self.pdf_fields['cs_3'])
        print(f'cs3 = {cs3}')
        sent = self.__get_sentence_in_substring(cs3, self.pdf_fields['applications'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['cs_3'], num):
            raise RuntimeError(f'expect number {self.defaults["cs_3"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['cs_2'], num):
            raise RuntimeError(f'expect number != {self.defaults["cs_3"]} but its {num}')

    def validate_tech_summary(self):
        tech = self.__get_section_of_chart(self.pdf_fields['tech'], size=4096)
        field_1 = self.__get_sentence_in_substring(tech, 'Main technical fields 1', 256)
        print(f'field_1 = {field_1}')
        field_2 = self.__get_sentence_in_substring(tech, 'Main technical fields 2', 256)
        field_3 = self.__get_sentence_in_substring(tech, 'Main technical fields 3', 256)
        if len(self.__get_num_list_from_str(field_1, self.delimiter)) < 2:
            raise RuntimeError(f'expect Main technical field 1 summary but its {field_1}')
        if len(self.__get_num_list_from_str(field_2, self.delimiter)) < 2:
            raise RuntimeError(f'expect Main technical field 2 summary but its {field_2}')
        if len(self.__get_num_list_from_str(field_3, self.delimiter)) < 2:
            raise RuntimeError(f'expect Main technical field 3 summary but its {field_3}')

    def validate_tech1(self, filtered=False):
        tech1 = self.__get_section_of_chart(self.pdf_fields['tech_1'])
        print(f'tech1 = {tech1}')
        sent = self.__get_sentence_in_substring(tech1, self.pdf_fields['families'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['tech_1'], num):
            raise RuntimeError(f'expect number {self.defaults["tech_1"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['tech_1'], num):
            raise RuntimeError(f'expect number != {self.defaults["tech_1"]} but its {num}')

    def validate_tech2(self, filtered=False):
        tech2 = self.__get_section_of_chart(self.pdf_fields['tech_2'])
        print(f'tech2 = {tech2}')
        sent = self.__get_sentence_in_substring(tech2, self.pdf_fields['families'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['tech_2'], num):
            raise RuntimeError(f'expect number {self.defaults["tech_2"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['tech_2'], num):
            raise RuntimeError(f'expect number != {self.defaults["tech_2"]} but its {num}')

    def validate_oi_summary(self):
        oi = self.__get_section_of_chart(self.pdf_fields['oi'], size=4096)
        co_ownerships = self.__get_sentence_in_substring(oi, 'Co-ownerships')
        print(f'co_ownerships = {co_ownerships}')
        co_applications = self.__get_sentence_in_substring(oi, 'Co-applications')
        if len(self.__get_num_list_from_str(co_ownerships, self.delimiter)) < 2:
            raise RuntimeError(f'expect Co-ownerships summary but its {co_ownerships}')
        if len(self.__get_num_list_from_str(co_applications, self.delimiter)) < 2:
            raise RuntimeError(f'expect Co-applications summary but its {co_applications}')

    def validate_oi1(self, filtered=False):
        oi1 = self.__get_section_of_chart(self.pdf_fields['oi_1'])
        print(f'oi1 = {oi1}')
        sent = self.__get_sentence_in_substring(oi1, self.pdf_fields['applications'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['oi_1'], num):
            raise RuntimeError(f'expect number {self.defaults["oi_1"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['oi_1'], num):
            raise RuntimeError(f'expect number != {self.defaults["oi_1"]} but its {num}')

    def validate_oi2_assignees(self, filtered=False):
        oi2_assignees = self.__get_section_of_chart(self.pdf_fields['oi_2_assignees'])
        print(f'oi2_assignees = {oi2_assignees}')
        sent = self.__get_sentence_in_substring(oi2_assignees, self.pdf_fields['applications'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['oi_2_assignees'], num):
            raise RuntimeError(f'expect number {self.defaults["oi_2_assignees"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['oi_2_assignees'], num):
            raise RuntimeError(f'expect number != {self.defaults["oi_2_assignees"]} but its {num}')

    def validate_oi2_inventors(self, filtered=False):
        oi2_inventors = self.__get_section_of_chart(self.pdf_fields['oi_2_inventors'])
        print(f'oi2_inventors = {oi2_inventors}')
        sent = self.__get_sentence_in_substring(oi2_inventors, self.pdf_fields['applications'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['oi_2_inventors'], num):
            raise RuntimeError(f'expect number {self.defaults["oi_2_inventors"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['oi_2_inventors'], num):
            raise RuntimeError(f'expect number != {self.defaults["oi_2_inventors"]} but its {num}')

    def validate_oi3(self, filtered=False):
        oi3 = self.__get_section_of_chart(self.pdf_fields['oi_3'])
        print(f'oi3 = {oi3}')
        sent = self.__get_sentence_in_substring(oi3, self.pdf_fields['applications'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['oi_3'], num):
            raise RuntimeError(f'expect number {self.defaults["oi_3"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['oi_3'], num):
            raise RuntimeError(f'expect number != {self.defaults["oi_3"]} but its {num}')

    def validate_hh_summary(self):
        hh = self.__get_section_of_chart(self.pdf_fields['hh'], size=4096)
        transferred = self.__get_sentence_in_substring(hh, 'Transferred')
        print(f'transferred = {transferred}')
        licensed = self.__get_sentence_in_substring(hh, 'Licensed')
        pledged = self.__get_sentence_in_substring(hh, 'Pledged')
        litigated = self.__get_sentence_in_substring(hh, 'Litigated')
        if len(self.__get_num_list_from_str(transferred, self.delimiter)) < 2:
            raise RuntimeError(f'expect Transferred summary but its {transferred}')
        if len(self.__get_num_list_from_str(licensed, self.delimiter)) < 2:
            raise RuntimeError(f'expect Licensed summary but its {licensed}')
        if len(self.__get_num_list_from_str(pledged, self.delimiter)) < 2:
            raise RuntimeError(f'expect Pledged summary but its {pledged}')
        if len(self.__get_num_list_from_str(litigated, self.delimiter)) < 2:
            raise RuntimeError(f'expect Litigated summary but its {litigated}')

    def validate_hh1(self, filtered=False):
        hh1 = self.__get_section_of_chart(self.pdf_fields['hh_1'])
        print(f'hh1 = {hh1}')
        sent = self.__get_sentence_in_substring(hh1, self.pdf_fields['applications'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['hh_1'], num):
            raise RuntimeError(f'expect number {self.defaults["hh_1"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['hh_1'], num):
            raise RuntimeError(f'expect number != {self.defaults["hh_1"]} but its {num}')

    def validate_hh1_transferred(self, filtered=False):
        hh1_transferred = self.__get_section_of_chart(self.pdf_fields['hh_1_transferred'])
        print(f'hh1_transferred = {hh1_transferred}')
        sent = self.__get_sentence_in_substring(hh1_transferred, self.pdf_fields['applications'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['hh_1_transferred'], num):
            raise RuntimeError(f'expect number {self.defaults["hh_1_transferred"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['hh_1_transferred'], num):
            raise RuntimeError(f'expect number != {self.defaults["hh_1_transferred"]} but its {num}')

    def validate_hh2(self, filtered=False):
        hh2 = self.__get_section_of_chart(self.pdf_fields['hh_2'])
        print(f'hh2 = {hh2}')
        sent = self.__get_sentence_in_substring(hh2, self.pdf_fields['total'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['hh_2'], num):
            raise RuntimeError(f'expect number {self.defaults["hh_2"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['hh_2'], num):
            raise RuntimeError(f'expect number != {self.defaults["hh_2"]} but its {num}')

    def validate_qv_summary(self):
        qv = self.__get_section_of_chart(self.pdf_fields['qv'], size=4096)
        qv_summary = self.__get_sentence_in_substring(qv, 'MANICURING OR OTHER COSMETIC TREATMENT', 256)
        print(f'qv_summary = {qv_summary}')
        if len(self.__get_num_list_from_str(qv_summary, self.delimiter)) < 4:
            raise RuntimeError(f'expect qv summary but its {qv_summary}')

    def validate_qv1(self, filtered=False):
        qv1 = self.__get_section_of_chart(self.pdf_fields['qv_1'])
        print(f'qv1 = {qv1}')
        sent = self.__get_sentence_in_substring(qv1, self.pdf_fields['families'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['qv_1'], num):
            raise RuntimeError(f'expect number {self.defaults["qv_1"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['qv_1'], num):
            raise RuntimeError(f'expect number != {self.defaults["qv_1"]} but its {num}')

    def validate_qv2(self, filtered=False):
        qv2 = self.__get_section_of_chart(self.pdf_fields['qv_2'])
        print(f'qv2 = {qv2}')
        sent = self.__get_sentence_in_substring(qv2, self.pdf_fields['applications'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['qv_2'], num):
            raise RuntimeError(f'expect number {self.defaults["qv_2"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['qv_2'], num):
            raise RuntimeError(f'expect number != {self.defaults["qv_2"]} but its {num}')

    def validate_qv3(self, filtered=False):
        qv3 = self.__get_section_of_chart(self.pdf_fields['qv_3'])
        print(f'qv3 = {qv3}')
        sent = self.__get_sentence_in_substring(qv3, self.pdf_fields['applications'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['qv_3'], num):
            raise RuntimeError(f'expect number {self.defaults["qv_3"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['qv_3'], num):
            raise RuntimeError(f'expect number != {self.defaults["qv_3"]} but its {num}')

    def validate_qh_summary(self):
        qh = self.__get_section_of_chart(self.pdf_fields['qh'], size=4096)
        qh_summary = self.__get_sentence_in_substring(qh, 'Summary', 512)
        print(f'qh_summary = {qh_summary}')
        if len(self.__get_num_list_from_str(qh_summary, self.delimiter)) < 6:
            raise RuntimeError(f'expect qh summary but its {qh_summary}')

    def validate_qh1(self, filtered=False):
        qh1 = self.__get_section_of_chart(self.pdf_fields['qh_1'])
        print(f'qh1 = {qh1}')
        sent = self.__get_sentence_in_substring(qh1, self.pdf_fields['families'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['qh_1'], num):
            raise RuntimeError(f'expect number {self.defaults["qh_1"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['qh_1'], num):
            raise RuntimeError(f'expect number != {self.defaults["qh_1"]} but its {num}')

    def validate_qh2(self, filtered=False):
        qh2 = self.__get_section_of_chart(self.pdf_fields['qh_2'])
        print(f'qh2 = {qh2}')
        sent = self.__get_sentence_in_substring(qh2, self.pdf_fields['applications'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['qh_2'], num):
            raise RuntimeError(f'expect number {self.defaults["qh_2"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['qh_2'], num):
            raise RuntimeError(f'expect number != {self.defaults["qh_2"]} but its {num}')

    def validate_vh_summary(self):
        vh = self.__get_section_of_chart(self.pdf_fields['vh'], size=4096)
        vh_summary = self.__get_sentence_in_substring(vh, 'Summary')
        print(f'vh_summary = {vh_summary}')
        if len(self.__get_num_list_from_str(vh_summary, self.delimiter)) < 3:
            raise RuntimeError(f'expect vh summary but its {vh_summary}')

    def validate_vh1(self, filtered=False):
        vh1 = self.__get_section_of_chart(self.pdf_fields['vh_1'])
        print(f'vh1 = {vh1}')
        sent = self.__get_sentence_in_substring(vh1, self.pdf_fields['families'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['vh_1'], num):
            raise RuntimeError(f'expect number {self.defaults["vh_1"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['vh_1'], num):
            raise RuntimeError(f'expect number != {self.defaults["vh_1"]} but its {num}')

    def validate_vh2(self, filtered=False):
        vh2 = self.__get_section_of_chart(self.pdf_fields['vh_2'], 512)
        print(f'vh2 = {vh2}')
        sent = self.__get_sentence_in_substring(vh2, self.pdf_fields['families'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['vh_2'], num):
            raise RuntimeError(f'expect number {self.defaults["vh_2"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['vh_2'], num):
            raise RuntimeError(f'expect number != {self.defaults["vh_2"]} but its {num}')

    def validate_vh3_potential_targets(self, filtered=False):
        vh3_potential_targets = self.__get_section_of_chart(self.pdf_fields['vh_3_potential_targets'], 512)
        print(f'vh3_potential_targets = {vh3_potential_targets}')
        sent = self.__get_sentence_in_substring(vh3_potential_targets, self.pdf_fields['families'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['vh_3_potential_targets'], num):
            raise RuntimeError(f'expect number {self.defaults["vh_3_potential_targets"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['vh_3_potential_targets'], num):
            raise RuntimeError(f'expect number != {self.defaults["vh_3_potential_targets"]} but its {num}')

    def validate_vh3_family_id(self, filtered=False):
        vh3_family_id = self.__get_section_of_chart(self.pdf_fields['vh_3_family_id'], 512)
        print(f'vh3_family_id = {vh3_family_id}')
        sent = self.__get_sentence_in_substring(vh3_family_id, self.pdf_fields['families'])
        num = self.__get_first_num_from_str(sent, self.delimiter)
        if not filtered and not self.__should_be_equal(self.defaults['vh_3_family_id'], num):
            raise RuntimeError(f'expect number {self.defaults["vh_3_family_id"]} but its {num}')
        elif filtered and not self.__should_not_be_equal(self.defaults['vh_3_family_id'], num):
            raise RuntimeError(f'expect number != {self.defaults["vh_3_family_id"]} but its {num}')

    def wait_for_cs1(self):
        if not self.op.is_exist(self.get_element("CS1Title")):
            self.op.click_and_wait_for(self.get_element("CSTab"), self.get_element("CS1Title"))
        self.op.wait_for(self.get_element("CS1"), self.wait_for_timeout)

    def wait_for_cs2(self):
        if not self.op.is_exist(self.get_element("CS1Title")):
            self.op.click_and_wait_for(self.get_element("CSTab"), self.get_element("CS1Title"))
        self.op.wait_for(self.get_element("CS2"), self.wait_for_timeout)

    def wait_for_cs3(self):
        if not self.op.is_exist(self.get_element("CS1Title")):
            self.op.click_and_wait_for(self.get_element("CSTab"), self.get_element("CS1Title"))
        self.op.wait_for(self.get_element("CS3"), self.wait_for_timeout)

    def wait_for_tech1(self):
        if not self.op.is_exist(self.get_element("TECH1Title")):
            self.op.click_and_wait_for(self.get_element("TECHTab"), self.get_element("TECH1Title"))
        self.op.wait_for(self.get_element("TECH1"), self.wait_for_timeout)

    def wait_for_tech2(self):
        if not self.op.is_exist(self.get_element("TECH1Title")):
            self.op.click_and_wait_for(self.get_element("TECHTab"), self.get_element("TECH1Title"))
        self.op.wait_for(self.get_element("TECH2"), self.wait_for_timeout)

    def wait_for_oi1(self):
        if not self.op.is_exist(self.get_element("OI1Title")):
            self.op.click_and_wait_for(self.get_element("OITab"), self.get_element("OI1Title"))
        self.op.wait_for(self.get_element("OI1"), self.wait_for_timeout)

    def wait_for_oi2(self):
        if not self.op.is_exist(self.get_element("OI1Title")):
            self.op.click_and_wait_for(self.get_element("OITab"), self.get_element("OI1Title"))
        self.op.wait_for(self.get_element("OI2"), self.wait_for_timeout)

    def wait_for_oi3(self):
        if not self.op.is_exist(self.get_element("OI1Title")):
            self.op.click_and_wait_for(self.get_element("OITab"), self.get_element("OI1Title"))
        self.op.wait_for(self.get_element("OI3"), self.wait_for_timeout)

    def wait_for_hh1(self):
        if not self.op.is_exist(self.get_element("HH2Title")):
            self.op.click_and_wait_for(self.get_element("HHTab"), self.get_element("HH2Title"))
        self.op.wait_for(self.get_element("HH1"), self.wait_for_timeout)

    def wait_for_hh2(self):
        if not self.op.is_exist(self.get_element("HH2Title")):
            self.op.click_and_wait_for(self.get_element("HHTab"), self.get_element("HH2Title"))
        self.op.wait_for(self.get_element("HH2"), self.wait_for_timeout)

    def wait_for_qv1(self):
        if not self.op.is_exist(self.get_element("QV2Title")):
            self.op.click_and_wait_for(self.get_element("QVTab"), self.get_element("QV2Title"))
        self.op.wait_for(self.get_element("QV1"), self.wait_for_timeout)

    def wait_for_qv2(self):
        if not self.op.is_exist(self.get_element("QV2Title")):
            self.op.click_and_wait_for(self.get_element("QVTab"), self.get_element("QV2Title"))
        self.op.wait_for(self.get_element("QV2"), self.wait_for_timeout)

    def wait_for_qv3(self):
        if not self.op.is_exist(self.get_element("QV2Title")):
            self.op.click_and_wait_for(self.get_element("QVTab"), self.get_element("QV2Title"))
        self.op.wait_for(self.get_element("QV3"), self.wait_for_timeout)

    def wait_for_qh1(self):
        if not self.op.is_exist(self.get_element("QH2Title")):
            self.op.click_and_wait_for(self.get_element("QHTab"), self.get_element("QH2Title"))
        self.op.wait_for(self.get_element("QH1"), self.wait_for_timeout)

    def wait_for_qh2(self):
        if not self.op.is_exist(self.get_element("QH2Title")):
            self.op.click_and_wait_for(self.get_element("QHTab"), self.get_element("QH2Title"))
        self.op.wait_for(self.get_element("QH2"), self.wait_for_timeout)

    def wait_for_vh1(self):
        if not self.op.is_exist(self.get_element("VH1Title")):
            self.op.click_and_wait_for(self.get_element("VHTab"), self.get_element("VH1Title"))
        self.op.wait_for(self.get_element("VH1"), self.wait_for_timeout)

    def wait_for_vh2(self):
        if not self.op.is_exist(self.get_element("VH1Title")):
            self.op.click_and_wait_for(self.get_element("VHTab"), self.get_element("VH1Title"))
        self.op.wait_for(self.get_element("VH2"), self.wait_for_timeout)

    def wait_for_vh3(self):
        if not self.op.is_exist(self.get_element("VH1Title")):
            self.op.click_and_wait_for(self.get_element("VHTab"), self.get_element("VH1Title"))
        self.op.wait_for(self.get_element("VH3"), self.wait_for_timeout)

    def vh3_switch_to_family_id_tab(self):
        self.op.click_and_wait_for(self.get_element("VH3FamilyIdTab"), self.get_element("VH3FamilyIdTabActive"))
        # self.wait_for_vh3()

    def change_cs1_filter(self):
        self.op.click(self.get_element("1stChartLegalStatusDropdown"))
        self.op.click(self.get_element("1stChartLegalStatusSelectAll"))
        self.op.click(self.get_element("1stChartLegalStatusPending"))
        self.op.click(self.get_element("1stChartLegalStatusSubmit"))
        self.op.sleep(2)
        self.wait_for_cs1()

    def change_cs2_filter(self):
        self.op.click(self.get_element("2ndChartFilterButton"))
        self.op.click(self.get_element("FilterClear"))
        self.op.click(self.get_element("FilterEP"))
        self.op.click(self.get_element("FilterSubmit"))
        self.op.sleep(2)
        self.wait_for_cs2()

    def change_cs3_filter(self):
        self.op.click(self.get_element("3rdChartFilterButton"))
        self.op.click(self.get_element("FilterClear"))
        self.op.click(self.get_element("FilterEP"))
        self.op.click(self.get_element("FilterSubmit"))
        self.op.sleep(2)
        self.wait_for_cs3()

    def change_tech1_filter(self):
        self.op.click(self.get_element("1stChartLegalStatusDropdown"))
        self.op.click(self.get_element("1stChartLegalStatusSelectAll"))
        self.op.click(self.get_element("1stChartLegalStatusPending"))
        self.op.click(self.get_element("1stChartLegalStatusSubmit"))
        self.op.sleep(2)
        self.wait_for_tech1()

    def change_tech2_filter(self):
        self.op.click(self.get_element("2ndChartLegalStatusDropdown"))
        self.op.click(self.get_element("2ndChartLegalStatusSelectAll"))
        self.op.click(self.get_element("2ndChartLegalStatusPending"))
        self.op.click(self.get_element("2ndChartLegalStatusSubmit"))
        self.op.sleep(2)
        self.wait_for_tech2()

    def change_oi1_filter(self):
        self.op.click(self.get_element("1stChartLegalStatusDropdown"))
        self.op.click(self.get_element("1stChartLegalStatusSelectAll"))
        self.op.click(self.get_element("1stChartLegalStatusPending"))
        self.op.click(self.get_element("1stChartLegalStatusSubmit"))
        self.op.sleep(2)
        self.wait_for_oi1()

    def change_oi2_filter(self):
        self.op.click(self.get_element("2ndChartLegalStatusDropdown"))
        self.op.click(self.get_element("2ndChartLegalStatusSelectAll"))
        self.op.click(self.get_element("2ndChartLegalStatusPending"))
        self.op.click(self.get_element("2ndChartLegalStatusSubmit"))
        self.op.sleep(2)
        self.wait_for_oi2()

    def change_oi3_filter(self):
        self.op.click(self.get_element("3rdChartLegalStatusDropdown"))
        self.op.click(self.get_element("3rdChartLegalStatusSelectAll"))
        self.op.click(self.get_element("3rdChartLegalStatusPending"))
        self.op.click(self.get_element("3rdChartLegalStatusSubmit"))
        self.op.sleep(2)
        self.wait_for_oi3()

    def change_hh1_filter(self):
        self.op.click(self.get_element("1stChartFilterButton"))
        self.op.click(self.get_element("FilterClear"))
        self.op.click(self.get_element("FilterCN"))
        self.op.click(self.get_element("FilterSubmit"))
        self.op.sleep(2)
        self.wait_for_hh1()

    def change_hh2_filter(self):
        self.op.click(self.get_element("2ndChartLegalStatusDropdown"))
        self.op.click(self.get_element("2ndChartLegalStatusSelectAll"))
        self.op.click(self.get_element("2ndChartLegalStatusActive"))
        self.op.click(self.get_element("2ndChartLegalStatusSubmit"))
        self.op.sleep(2)
        self.wait_for_hh2()

    def change_qv1_filter(self):
        self.op.click(self.get_element("1stChartFilterButton"))
        self.op.click(self.get_element("FilterClear"))
        self.op.click(self.get_element("FilterEP"))
        self.op.click(self.get_element("FilterSubmit"))
        self.op.sleep(2)
        self.wait_for_qv1()

    def change_qv2_filter(self):
        self.op.click(self.get_element("2ndChartFilterButton"))
        self.op.click(self.get_element("FilterClear"))
        self.op.click(self.get_element("FilterEP"))
        self.op.click(self.get_element("FilterSubmit"))
        self.op.sleep(2)
        self.wait_for_qv2()

    def change_qv3_filter(self):
        self.op.click(self.get_element("3rdChartFilterButton"))
        self.op.click(self.get_element("FilterEP"))
        self.op.click(self.get_element("FilterSubmit"))
        self.op.sleep(2)
        self.wait_for_qv3()

    def change_qh1_filter(self):
        self.op.click(self.get_element("1stChartFilterButton"))
        self.op.click(self.get_element("FilterClear"))
        self.op.click(self.get_element("FilterEP"))
        self.op.click(self.get_element("FilterSubmit"))
        self.op.sleep(2)
        self.wait_for_qh1()

    def change_qh2_filter(self):
        self.op.click(self.get_element("2ndChartLegalStatusDropdown"))
        self.op.click(self.get_element("2ndChartLegalStatusActive"))
        self.op.click(self.get_element("2ndChartLegalStatusSubmit"))
        self.op.sleep(2)
        self.wait_for_qh2()

    def change_vh1_filter(self):
        self.op.click(self.get_element("1stChartLegalStatusDropdown"))
        self.op.click(self.get_element("1stChartLegalStatusActive"))
        self.op.click(self.get_element("1stChartLegalStatusSubmit"))
        self.op.sleep(2)
        self.wait_for_vh1()

    def change_vh2_filter(self):
        self.op.click(self.get_element("2ndChartFilterButton"))
        self.op.click(self.get_element("FilterClear"))
        self.op.click(self.get_element("FilterEP"))
        self.op.click(self.get_element("FilterSubmit"))
        self.op.sleep(2)
        self.wait_for_vh2()

    def change_vh3_filter(self):
        self.op.click(self.get_element("3rdChartFilterButton"))
        self.op.click(self.get_element("FilterClear"))
        self.op.click(self.get_element("FilterEP"))
        self.op.click(self.get_element("FilterSubmit"))
        self.op.sleep(2)
        self.wait_for_vh3()

    def quit(self):
        self.op.quit()
