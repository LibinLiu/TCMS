from selenium import selenium
from env import *
import unittest, time, re

class Bug672622(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug672622(self):
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
                if sel.is_element_present("link=PLANNING"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=PLANNING"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.mouse_over("link=PLANNING")
        for i in range(60):
            try:
                if sel.is_element_present("link=Search Plans"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=Search Plans"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=Search Plans")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "Search Plan" == sel.get_text("//form[@id='id_search_plan_form']/h2"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Search Plan", sel.get_text("//form[@id='id_search_plan_form']/h2"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("id_product"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_product"))
        except AssertionError, e: self.verificationErrors.append(str(e))
	'''
        for i in range(60):
            try:
                if "TCMS" == sel.get_text("//option[@value='116']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("TCMS", sel.get_text("//option[@value='116']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
	'''
	time.sleep(10)
        sel.select("id_product", "label=TCMS")
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='Search']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@value='Search']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='Search']")
        sel.wait_for_page_to_load("30000")
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
                if env.testplanName == sel.get_title(): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(env.testplanName, sel.get_title())   ###
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
                if "Agilefant" == sel.get_text("//option[@value='104']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Agilefant", sel.get_text("//option[@value='104']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("id_product", "label=Agilefant")
        for i in range(60):
            try:
                if "1.6.2" == sel.get_text("//select[@id='id_default_product_version']/option"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("1.6.2", sel.get_text("//select[@id='id_default_product_version']/option"))
        except AssertionError, e: self.verificationErrors.append(str(e))
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
        for i in range(60):
            try:
                if "Product :" == sel.get_text("//div[@id='content']/div[3]/div[1]/div[3]/div[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Product :", sel.get_text("//div[@id='content']/div[3]/div[1]/div[3]/div[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link=Agilefant"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=Agilefant"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "Version :" == sel.get_text("//div[@id='content']/div[3]/div[1]/div[4]/div[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Version :", sel.get_text("//div[@id='content']/div[3]/div[1]/div[4]/div[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "1.6.2" == sel.get_text("display_product_version"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("1.6.2", sel.get_text("display_product_version"))
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
                if sel.is_element_present("id_product"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_product"))
        except AssertionError, e: self.verificationErrors.append(str(e))
	time.sleep(10)
        sel.select("id_product", "label=TCMS")
        time.sleep(10)
	sel.select("id_default_product_version", "label=1.0")
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
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
