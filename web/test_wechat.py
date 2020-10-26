import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWeChat:

    def setup(self):
        self.driver = webdriver.Chrome()

    # 复用浏览器
    def test_chromdriver(self):
        options=Options()
        options.debugger_address="127.0.0.1:9222"
        self.driver=webdriver.Chrome(options=options)
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
        sleep(3)
        self.driver.refresh()
        sleep(3)
        cookies=self.driver.get_cookies()
        print(cookies)
        print(type(cookies))
        db=shelve.open("cookies")
        db["cookie"]=cookies
        db.close()
    #导入联系人
    def test_add_contact(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome_baidu")
        db=shelve.open("cookies")
        cookies=db["cookie"]
        db.close()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()
        self.driver.find_element_by_xpath("//span[text()='通讯录']").click()
        sleep(2)
        self.driver.find_elements_by_xpath("//div[text()='批量导入/导出']")[1].click()
        self.driver.find_elements_by_xpath("//a[contains(@class,'js_import_member')]")[2].click()
        sleep(3)
        self.driver.find_element_by_tag_name("input").send_keys(r"C:\Users\63599\Downloads\通讯录批量导入模板.xlsx")
        sleep(5)
        self.driver.find_element_by_xpath("//a[contains(@class,'ww_fileImporter_submit')]").click()
        sleep(5)
        result:str=self.driver.find_elements_by_xpath("//a[contains(@class,'ww_btn_Blue')]")[1].text
        assert result.strip()=="完成"