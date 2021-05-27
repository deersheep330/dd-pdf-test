import os

from pdf.utils import read_variable_from_config
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

        self.add_element("DownloadPdf", "//*[contains(@i18n-txt, 'due.page.downloadreport')]//*[name()='svg' and contains(@class, 'fa-file-download')]")
        self.add_element("DownloadPdfModal", "//*[contains(text(), 'Download Report')]")
        self.add_element("DownloadPdfConfirm", "//*[@i18n-txt='due.button.confirm']")

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
        self.op.click_and_wait_for(self.get_element("DownloadPdf"), self.get_element("DownloadPdfModal"))
        self.op.click(self.get_element("DownloadPdfConfirm"))
        self.op.sleep(1)
        for entry in self.driver.get_log('performance'):
            print(entry)

    def quit(self):
        self.op.quit()