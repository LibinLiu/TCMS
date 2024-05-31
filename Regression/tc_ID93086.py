from selenium import selenium
from env import *
import unittest, time, re

class Bug584838(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug584838(self):
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
                if env.testrunName == sel.get_text("link="+env.testrunName): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(env.testrunName, sel.get_text("link="+env.testrunName))   ###
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link="+env.testrunName)   ###
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if env.testrunName == sel.get_title(): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(env.testrunName, sel.get_title())   ###
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("btn_edit"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("btn_edit"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("btn_edit")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "Edit Test Run" == sel.get_text("//div[@id='content']/h2"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Edit Test Run", sel.get_text("//div[@id='content']/h2"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "Summary" == sel.get_text("//div[@id='content']/form/div[3]/table/tbody/tr[1]/td[1]/label"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Summary", sel.get_text("//div[@id='content']/form/div[3]/table/tbody/tr[1]/td[1]/label"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("id_summary"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_summary"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("id_product"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_product"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("id_product_version"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_product_version"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("id_build"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_build"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("id_manager"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_manager"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("id_default_tester"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_default_tester"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("estimated_time_days"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("estimated_time_days"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("estimated_time_hours"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("estimated_time_hours"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("estimated_time_minutes"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("estimated_time_minutes"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("estimated_time_seconds"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("estimated_time_seconds"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("id_notes"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_notes"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='Save']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@value='Save']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='Reset']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@value='Reset']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='Back']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@value='Back']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_summary", "Test run for Copy of test create new test plan on Unknown environment_testplan")
        sel.select("id_product", "label=TCMS")
        for i in range(60):
            try:
                if "Devel" == sel.get_text("//option[@value='885']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Devel", sel.get_text("//option[@value='885']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("id_product_version", "label=3.3")
        for i in range(60):
            try:
                if "tcms_testing" == sel.get_text("//option[@value='703']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("tcms_testing", sel.get_text("//option[@value='703']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("id_build", "label=TCMS 3.0.3-2.svn2859")
        sel.select("estimated_time_days", "label=3")
        sel.select("estimated_time_hours", "label=16")
        sel.select("estimated_time_minutes", "label=25")
        sel.select("estimated_time_seconds", "label=35")
        sel.type("id_notes", "test plan test")
        sel.click("//input[@value='Save']")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "Test run for Copy of test create new test plan on Unknown environment_testplan" == sel.get_text("display_title"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Test run for Copy of test create new test plan on Unknown environment_testplan", sel.get_text("display_title"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_text_present("Product"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("Product"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "TCMS" == sel.get_text("link=TCMS"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("TCMS", sel.get_text("link=TCMS"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "Build :" == sel.get_text("//div[@id='content']/div[4]/div[1]/div[3]/div[2]/div[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Build :", sel.get_text("//div[@id='content']/div[4]/div[1]/div[3]/div[2]/div[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "TCMS 3.0.3-2.svn2859" == sel.get_text("link=TCMS 3.0.3-2.svn2859"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("TCMS 3.0.3-2.svn2859", sel.get_text("link=TCMS 3.0.3-2.svn2859"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "Estimated Time :" == sel.get_text("//div[@id='content']/div[4]/div[1]/div[2]/div[4]/div[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Estimated Time :", sel.get_text("//div[@id='content']/div[4]/div[1]/div[2]/div[4]/div[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "3 days, 16:25:35" == sel.get_text("//div[@id='content']/div[4]/div[1]/div[2]/div[4]/div[2]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("3 days, 16:25:35", sel.get_text("//div[@id='content']/div[4]/div[1]/div[2]/div[4]/div[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "Note :" == sel.get_text("//div[@id='content']/div[4]/div[1]/div[4]/div[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Note :", sel.get_text("//div[@id='content']/div[4]/div[1]/div[4]/div[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "test plan test" == sel.get_text("//div[@id='content']/div[4]/div[1]/div[4]/div[2]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("test plan test", sel.get_text("//div[@id='content']/div[4]/div[1]/div[4]/div[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("btn_edit"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("btn_edit"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("btn_edit")
        sel.wait_for_page_to_load("30000")
        sel.type("id_summary", env.testrunName)   ###
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='Save']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@value='Save']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='Save']")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
