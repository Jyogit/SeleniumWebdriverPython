#!/usr/bin/python
# -*- coding: utf-8 -*-

import time
import os
from selenium import webdriver  # pip install selenium==3.5.0
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

chromeDriverExe = 'utilities\chromedriver.exe'
delay_quick = 3  # sec
delay_medium = 5  # sec
delay_large = 9  # sec


def wait_for_following_page_title(driver_temp, expected_title):
    try:
        WebDriverWait(driver_temp, delay_quick).until(expected_conditions.title_contains(expected_title))
        return True
    except TimeoutException:
        raise Exception('************* Page with required title not found : ' + expected_title + ' actual title is: ' + driver_temp.title)


def get_chrome_driver_and_navigate_to_url_with_title(url,expected_title):
    driver_temp = webdriver.Chrome(executable_path=chromeDriverExe)
    #driver_temp = webdriver.Chrome()
    driver_temp.maximize_window()
    driver_temp.delete_all_cookies()
    driver_temp.get(url)
    wait_for_following_page_title(driver_temp,expected_title)
    return driver_temp


def webdriver_shutdown(driver_temp):
    driver_temp.close()
    driver_temp.quit()


def web_element_pop_up_example1(url):
    driver1 = get_chrome_driver_and_navigate_to_url_with_title(url,'Bootstrap Alerts')
    print ('  Clicking to invoke auto vanishing pop up')
    driver1.find_element_by_id("autoclosable-btn-success").click()
    time.sleep(6)
    print ('  Clicking to invoke sticky pop up')
    driver1.find_element_by_id("normal-btn-success").click()
    time.sleep(2)
    print ('  Click to close sticky pop up')
    driver1.find_element_by_class_name("close").click()
    time.sleep(2)
    webdriver_shutdown(driver1)


def web_element_pop_up_example2_javascript(url):
    driver2 = get_chrome_driver_and_navigate_to_url_with_title(url,'Bootstrap Modal Demo')
    print ('  Clicking to invoke javascript pop up type 1')
    driver2.find_element_by_css_selector("a[href='#myModal0']").click()
    time.sleep(6)
    print ('  Clicking to close java script pop up type 1')
    driver2.find_element_by_css_selector("a[data-dismiss='modal']").click()
    time.sleep(5)
    print ('  Clicking to invoke javascript pop up type 2')
    driver2.find_element_by_css_selector("a[href='#myModal']").click()
    time.sleep(3)
    print ('  Clicking to invoke additional on top of existing java script pop up type 2')
    driver2.find_element_by_css_selector("a[href='#myModal2']").click()
    time.sleep(5)
    print ('  Clicking to close additional java script on top of existing java script pop up type 2')
    driver2.find_elements_by_css_selector("a[data-dismiss='modal']")[2].click()
    time.sleep(3)
    print ('  Clicking to close java script pop up type 2')
    driver2.find_elements_by_css_selector("a[data-dismiss='modal']")[1].click()
    time.sleep(3)
    webdriver_shutdown(driver2)


def web_element_form_elements_part1(url):
    driver4 = get_chrome_driver_and_navigate_to_url_with_title(url,'Demo Form for practicing Selenium Automation')
    print ('  Sending text to text box')
    print("Sending text to text box")
    driver4.find_element_by_name("firstname").send_keys("Madhu")
    driver4.find_element_by_name("lastname").send_keys("Raj")
    print("Clicking on radio button")
    driver4.find_element_by_css_selector("input[id = 'sex-1']").click()
    driver4.find_element_by_css_selector("input[id = 'exp-3']").click()
    print("Clicking on tick box")
    driver4.find_element_by_css_selector("input[id = 'profession-1']").click()
    print("Selecting from drop down")
    continent_select = Select(driver4.find_element_by_id("continents"))
    continent_select.select_by_visible_text('Europe')
    time.sleep(3)
    webdriver_shutdown(driver4)

def web_element_window_handling(url):
    driver5 = get_chrome_driver_and_navigate_to_url_with_title(url,'Demo Windows for practicing Selenium Automation')
    print('  Performing window handling')
    current_w_handle = driver5.current_window_handle
    driver5.find_element_by_css_selector("button[onclick = 'if (!window.__cfRLUnblockHandlers) return false; newMsgWin()']").click()
    driver5.find_element_by_css_selector("button[onclick = 'if (!window.__cfRLUnblockHandlers) return false; newBrwWin()']").click()
    time.sleep(2)
    if 0 is not len(driver5.window_handles):
        # print (' Multiple windows found ' + len(driver11.window_handles))
        driver5.switch_to.window(driver5.window_handles[1])
        print ( ' New windows title is  ' + driver5.title)
        driver5.switch_to.window(current_w_handle)
    else:
        raise Exception('************* Multiple windows are not found ')
    time.sleep(2)
    webdriver_shutdown(driver5)
