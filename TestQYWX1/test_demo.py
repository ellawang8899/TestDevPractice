import random
import string
import time
import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestQYWX:
  def setup(self):
      self.driver = webdriver.Chrome()
      self.driver.implicitly_wait(5)
      self.driver.maximize_window()
  def test_getranphonum(self):
      prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
                 "153", "155", "156", "157", "158", "159", "186", "187", "188"]
      return random.choice(prelist) + "".join(random.choice("0123456789") for i in range(8))

  def test_getck_addcont(self):
    opt = webdriver.ChromeOptions()
    opt.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=opt)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    cookie = driver.get_cookies()
    with open("data.yaml", "w", encoding="UTF-8") as f:
        yaml.dump(cookie, f)

    self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
    with open("data.yaml", encoding="UTF-8") as f:
        yaml_data = yaml.safe_load(f)
        for cookie in yaml_data:
            self.driver.add_cookie(cookie)
    self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    self.driver.find_element(By.CSS_SELECTOR, "#menu_contacts > .frame_nav_item_title").click()
    self.driver.find_element(By.LINK_TEXT, "添加成员").click()
    self.driver.find_element_by_id("username").send_keys("王思")
    self.driver.find_element_by_id("memberAdd_english_name").send_keys("wangsi")
    menid = ''.join(random.choice("0123456789") for i in range(8))
    self.driver.find_element_by_id("memberAdd_acctid").send_keys(menid)
    phonum = self.test_getranphonum()
    self.driver.find_element_by_id("memberAdd_phone").send_keys(phonum)
    self.driver.find_element_by_link_text("保存").click()
    getphnum = self.driver.find_elements(By.XPATH, '//*[@id="member_list"]//tr//td/span')

    realnum = []
    for i in getphnum:
        realnum.append(i.text)
    for x in realnum:
        if x != phonum:
            continue
        else:
            print("success")
            break





