from selenium import selenium
from env import *
import unittest, time, re

class Bug599313 (unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug599313(self):
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
                if sel.is_element_present("link="+env.testplanName): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link="+env.testplanName))   ###
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link="+env.testplanName)   ###
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "" == sel.get_text("//div[@id='testcases']/table/thead/tr/th[2]/input"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("", sel.get_text("//div[@id='testcases']/table/thead/tr/th[2]/input"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//div[@id='testcases']/table/thead/tr/th[2]/input")
        for i in range(60):
            try:
                if sel.is_element_present("//input[@name='case' and @value='%s']"%env.testcaseId): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@name='case' and @value='%s']"%env.testcaseId))   ###
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@name='case' and @value='%s']"%env.testcaseId)   ###
        for i in range(60):
            try:
                if "Component" == sel.get_value("//div[@id='testcases']/form/div/div[1]/ul/li[6]/input"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Component", sel.get_value("//div[@id='testcases']/form/div/div[1]/ul/li[6]/input"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//div[@id='testcases']/form/div/div[1]/ul/li[6]/input")
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
                if "Database" == sel.get_text("//select[@id='id_o_component']/option[2]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Database", sel.get_text("//select[@id='id_o_component']/option[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.add_selection("id_o_component", "label=Database")
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='Add']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@value='Add']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='Add']")
        sel.select_window("null")
        for i in range(60):
            try:
                if sel.is_element_present("link="+env.testcaseId): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link="+env.testcaseId))   ###
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link="+env.testcaseId)   ###
        for i in range(60):
            try:
                if sel.is_element_present("//body[@id='body']/div[@id='content']/div[5]/ul[1]/li[4]/a[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//body[@id='body']/div[@id='content']/div[5]/ul[1]/li[4]/a[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//body[@id='body']/div[@id='content']/div[5]/ul[1]/li[4]/a[1]")
	time.sleep(10)
        for i in range(60):
            try:
                if "Database" == sel.get_text("//form[@id='id_form_case_component']/table/tbody/tr[1]/td[2]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Database", sel.get_text("//form[@id='id_form_case_component']/table/tbody/tr[1]/td[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
   
	for i in range(60):
            try:
                if sel.is_element_present("link=Remove"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=Remove"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=Remove")
        self.failUnless("^Are you sure you want to delete these component\\(s\\)[\\s\\S]\nThe action will unable to undo\\.$")
        for i in range(60):
            try:
                if "Test case - %s: %s"%(env.testcaseId,env.testcaseName) == sel.get_title(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Test case - %s: %s"%(env.testcaseId,env.testcaseName), sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if not sel.is_text_present("//form[@id='id_form_case_component']/table/tbody/tr[1]/td[2]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failIf(sel.is_text_present("//form[@id='id_form_case_component']/table/tbody/tr[1]/td[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
 
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
