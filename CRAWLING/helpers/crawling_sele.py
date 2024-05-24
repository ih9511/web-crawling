from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.remote_connection import LOGGER, logging
from selenium.webdriver.common.action_chains import ActionChains

from urllib.parse import quote_plus

import subprocess
import os
import time

chrome_driver = r"D:\Project 1\Crawling\CRAWLING\driver\chromedriver.exe"


class User:

    # def __init__(self, mode="n"):
    #     # 작동 시작 로그

    #     # 작동 중인 브라우저를 컨트롤할 것인지, (상대적으로 까다로움.)

    #     # 새로운 브라우저를 컨트롤할 것인지(일단은 요걸로)
    #     # debugging 모드를 열어서 현재 포트를 확인해야함.
    #     # 확인된 포트를 통해 Chrome에 접근.

    #     self.driver = Options()
    #     self.chrome_options = Options()  # 필요한 옵션 지정.
    #     # browser = webdriver.Chrome(
    #     #     chrome_driver, options=self.options
    #     # )  # 드라이버와 옵션을 지정해서 browser를 생성.
    #     # browser.get("https://www.naver.com")
    #     if mode == "n":
    #         self.browser = webdriver.Chrome(options=self.chrome_options)
    #     else:
    #         cmd = [
    #             "C:\Program Friles\Google\Chrome\Application\chrome.exe",
    #             "--remote-debuggint-port=9222",
    #             '--user-data-dir="C:\ChromeTEMP"',
    #         ]

    #         pro = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    #         pro.kill()

    #         # os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
    #         self.chrome_options.add_experimental_option(
    #             'debuggerAddress', '127.0.0.1:9222'
    #         )

    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        self.chrome_driver = chrome_driver
        self.browser = webdriver.Chrome(options=self.chrome_options)
        # self.driver.maximize_window() # 새로운 페이지 열 때 무조건 최대화(노트북 상황이니까 어쩔 수 없이 배제...)

    def move_page(self, page):
        self.browser.get(page)

    def select_obj(self, user_xpath):
        self.browser.find_element(By.XPATH, user_xpath).send_keys()

    def cover_obj(self, user_xpath, item_name):
        self.browser.find_element(By.XPATH, user_xpath).send_keys(item_name)

    # 객체 선택하고 클릭
    def press_key(self, user_xpath):
        self.browser.find_element(By.XPATH, user_xpath).click()

    # def click_obj(self, user_xpath):
    #     self.browser.find_element(By.XPATH, user_xpath).click()

    def crawl_text(self, user_xpath):
        self.browser.find_element(By.XPATH, user_xpath).text

    def paging(self, user_full_xpath):
        self.browser.find_element(By.XPATH, user_full_xpath).click()

    def close_connection(self):
        self.browser.close()  # 창을 닫는건 아니고 connection만 끊는 것.
        print("작업완료됨 로그 찍기")

    # 셀레니움 자체 딜레이
    def delay_sele(self, second=1):
        self.browser.implicitly_wait(second)

    # time 라이브러리 활용 딜레이
    def delay_normal(self, second=1):
        time.sleep(second)

    def new_window(self, idx):
        print(self.browser.window_handles)
        self.browser.switch_to.window(self.browser.window_handles[idx])

    def moving_cursor(self):
        ac = ActionChains(self.browser)
        ac.move_by_offset(0, 350)
        ac.click()
        ac.perform()
