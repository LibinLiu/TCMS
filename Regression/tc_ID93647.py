from selenium import selenium
from env import *
import unittest, time, re

class Bug702393(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug702393(self):
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
                if sel.is_element_present("link=Advanced Search"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=Advanced Search"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=Advanced Search")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "Advanced Search" == sel.get_title(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Advanced Search", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.add_selection("r_product", "label=TCMS")
        for i in range(60):
            try:
                if "TCMS" == sel.get_text("//select[@id='r_product']/option[178]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("TCMS", sel.get_text("//select[@id='r_product']/option[178]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
	time.sleep(10)
	sel.add_selection("r_version", "label=3.4")
        for i in range(60):
            try:
                if "3.4" == sel.get_text("//option[@value='1066']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("3.4", sel.get_text("//option[@value='1066']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("btnSearchRun"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("btnSearchRun"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("btnSearchRun")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "Advanced Search Results" == sel.get_title(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Advanced Search Results", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='Clone']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@value='Clone']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='Clone']")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "INFO - At least one run is required" == sel.get_title(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("INFO - At least one run is required", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "At least one run is required" == sel.get_text("//div[@id='content']/div/div/p"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("At least one run is required", sel.get_text("//div[@id='content']/div/div/p"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link=Continue"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=Continue"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
