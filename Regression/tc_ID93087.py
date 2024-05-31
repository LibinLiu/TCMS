from selenium import selenium
from env import *
import unittest, time, re

class Bug590809(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug590809(self):
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
                if "Test Runs" == sel.get_text("//div[@id='content']/div[2]/div[1]/table/tbody/tr[1]/th/div/div[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Test Runs", sel.get_text("//div[@id='content']/div[2]/div[1]/table/tbody/tr[1]/th/div/div[1]"))
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
                if env.testrunName == sel.get_text("display_title"): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(env.testrunName, sel.get_text("display_title"))   ###
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link="+env.testcaseId): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link="+env.testcaseId))   ###
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("//body[@id='body']/div[@id='content']/div[5]/table[@id='id_table_cases']/tbody[1]/tr[1]/td[1]/input[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//body[@id='body']/div[@id='content']/div[5]/table[@id='id_table_cases']/tbody[1]/tr[1]/td[1]/input[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//body[@id='body']/div[@id='content']/div[5]/table[@id='id_table_cases']/tbody[1]/tr[1]/td[1]/input[1]")
        for i in range(60):
            try:
                if "Status IDLE PASSED FAILED RUNNING PAUSED BLOCKED ERROR WAIVED" == sel.get_text("//form[@id='id_form_case_runs']/div/div[2]/div[2]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Status IDLE PASSED FAILED RUNNING PAUSED BLOCKED ERROR WAIVED", sel.get_text("//form[@id='id_form_case_runs']/div/div[2]/div[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link=WAIVED"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=WAIVED"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=WAIVED")
        self.failUnless(re.search(r"^Are you sure you want to change the status[\s\S]$", sel.get_confirmation()))
        for i in range(60):
            try:
                if sel.is_element_present("//table[@id='id_table_cases']/tbody/tr[1]/td[11]/img"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//table[@id='id_table_cases']/tbody/tr[1]/td[11]/img"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.refresh()
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if sel.is_element_present("//body[@id='body']/div[@id='content']/div[5]/table[@id='id_table_cases']/tbody[1]/tr[1]/td[1]/input[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//body[@id='body']/div[@id='content']/div[5]/table[@id='id_table_cases']/tbody[1]/tr[1]/td[1]/input[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//body[@id='body']/div[@id='content']/div[5]/table[@id='id_table_cases']/tbody[1]/tr[1]/td[1]/input[1]")
        for i in range(60):
            try:
                if "Status" == sel.get_text("//form[@id='id_form_case_runs']/div/div[2]/div[2]/span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Status", sel.get_text("//form[@id='id_form_case_runs']/div/div[2]/div[2]/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link=IDLE"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=IDLE"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=IDLE")
        for i in range(60):
            try:
                if sel.is_element_present("//table[@id='id_table_cases']/tbody/tr[1]/td[11]/img"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//table[@id='id_table_cases']/tbody/tr[1]/td[11]/img"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
