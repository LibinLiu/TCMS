from selenium import selenium
from env import *
import unittest, time, re

class Bug658160(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug658160(self):
        sel = self.selenium
        sel.open("/accounts/"+env.user+"/recent/")   ###
        for i in range(60):
            try:
                if "Nitrate" == sel.get_title(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Nitrate", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link="+env.testrunName): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link="+env.testrunName))   ###
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link="+env.testrunName)   ###
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "Status IDLE PASSED FAILED RUNNING PAUSED BLOCKED ERROR WAIVED" == sel.get_text("//form[@id='id_form_case_runs']/div/div[2]/div[2]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Status", sel.get_text("//form[@id='id_form_case_runs']/div/div[2]/div[2]/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//body[@id='body']/div[@id='content']/div[5]/table[1]/tbody[1]/tr[1]/td[1]/input[1]")
        sel.mouse_over("//form[@id='id_form_case_runs']/div/div[2]/div[2]/span")
        for i in range(60):
            try:
                if sel.is_element_present("link=BLOCKED"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=BLOCKED"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=BLOCKED")
        sel.wait_for_page_to_load("30000")
        self.failUnless(re.search(r"^Are you sure you want to change the status[\s\S]$", sel.get_confirmation()))
        for i in range(60):
            try:
                if env.testcaseName == sel.get_text("link_1"): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(env.testcaseName, sel.get_text("link_1"))   ###
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "" == sel.get_text("//table[@id='id_table_cases']/tbody/tr[1]/td[11]/img"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("", sel.get_text("//table[@id='id_table_cases']/tbody/tr[1]/td[11]/img"))
        except AssertionError, e: self.verificationErrors.append(str(e))

        sel.click("//body[@id='body']/div[@id='content']/div[5]/table[1]/tbody[1]/tr[1]/td[1]/input[1]")
        sel.mouse_over("//form[@id='id_form_case_runs']/div/div[2]/div[2]/span")
        for i in range(60):
            try:
                if sel.is_element_present("link=PAUSED"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=PAUSED"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=PAUSED")
        sel.wait_for_page_to_load("30000")
        self.failUnless(re.search(r"^Are you sure you want to change the status[\s\S]$", sel.get_confirmation()))
        for i in range(60):
            try:
                if sel.is_element_present("//table[@id='id_table_cases']/tbody/tr[1]/td[11]/img"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//table[@id='id_table_cases']/tbody/tr[1]/td[11]/img"))
        except AssertionError, e: self.verificationErrors.append(str(e))

        sel.select_window("null")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
