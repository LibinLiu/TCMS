from selenium import selenium
from env import *
import unittest, time, re

class Bug594566(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug594566(self):
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
                if sel.is_element_present("link="+env.testcaseId): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link="+env.testcaseId))   ###
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link="+env.testcaseId)   ###
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "Product :" == sel.get_text("//div[@id='content']/div[4]/fieldset/div[1]/div[2]/div[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Product :", sel.get_text("//div[@id='content']/div[4]/fieldset/div[1]/div[2]/div[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "TCMS" == sel.get_text("//div[@id='content']/div[4]/fieldset/div[1]/div[2]/div[2]/span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("TCMS", sel.get_text("//div[@id='content']/div[4]/fieldset/div[1]/div[2]/div[2]/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "" == sel.get_text("btn_edit"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("", sel.get_text("btn_edit"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("btn_edit")
        sel.wait_for_page_to_load("30000")
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
                if sel.is_element_present("id_product"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_product"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "389" == sel.get_text("//option[@value='144']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("389", sel.get_text("//option[@value='144']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("id_product", "label=389")
        for i in range(60):
            try:
                if sel.is_element_present("id_category"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_category"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "test" == sel.get_text("//option[@value='292']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("test", sel.get_text("//option[@value='292']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("id_category", "label=test")
        for i in range(60):
            try:
                if "" == sel.get_text("//input[@value='Save']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("", sel.get_text("//input[@value='Save']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='Save']")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "Test case - %s: %s"%(env.testcaseId,env.testcaseName) == sel.get_title(): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Test case - %s: %s"%(env.testcaseId,env.testcaseName), sel.get_title())   ###
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "Product :" == sel.get_text("//div[@id='content']/div[4]/fieldset/div[1]/div[2]/div[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Product :", sel.get_text("//div[@id='content']/div[4]/fieldset/div[1]/div[2]/div[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_text_present("389"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("389"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "" == sel.get_text("btn_edit"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("", sel.get_text("btn_edit"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("btn_edit")
        sel.wait_for_page_to_load("30000")
        sel.select("id_product", "label=TCMS")
        for i in range(60):
            try:
                if sel.is_element_present("id_category"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_category"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "Functional" == sel.get_text("//select[@id='id_category']/option[4]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Functional", sel.get_text("//select[@id='id_category']/option[4]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("id_category", "label=Functional")
        sel.click("//input[@value='Save']")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
