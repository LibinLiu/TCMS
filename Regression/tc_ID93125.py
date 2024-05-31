from selenium import selenium
from env import *
import unittest, time, re, random

class Bug680064(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug680064(self):
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
                if env.testrunName == sel.get_text("display_title"): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(env.testrunName, sel.get_text("display_title"))   ###
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
                if sel.is_element_present("id_product_version"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_product_version"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("add_id_product_version"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("add_id_product_version"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("add_id_product_version")
        sel.wait_for_pop_up("id_product_version", "30000")
        sel.select_window("id_product_version")
        for i in range(60):
            try:
                if sel.is_element_present("id_value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_value"))
        except AssertionError, e: self.verificationErrors.append(str(e))
	rdm=random.uniform(1, 1000)
        sel.type("id_value", rdm)
	time.sleep(10)
        for i in range(60):
            try:
                if sel.is_element_present("_save"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("_save"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("_save")
	time.sleep(10)
        sel.select_window("null")
        for i in range(60):
            try:
                if sel.is_element_present("id_product_version"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_product_version"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.mouse_down("id_product_version")
	time.sleep(10)
        sel.select("id_product_version", "label="+str(rdm))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
