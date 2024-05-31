from selenium import selenium
from env import *
import unittest, time, re

class Bug597132(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug597132(self):
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
                if env.testrunName == sel.get_text("display_title"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(env.testrunName, sel.get_text("display_title"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link=Add Property"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=Add Property"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=Add Property")
        for i in range(60):
            try:
                if sel.is_element_present("//div[@id='dialog']/div/div[3]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//div[@id='dialog']/div/div[3]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("id_add_env_property"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_add_env_property"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("//div[@id='dialog']/div/div[4]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//div[@id='dialog']/div/div[4]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("id_add_env_value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_add_env_value"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("id_env_add"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_env_add"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='Cancel']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@value='Cancel']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "storage" == sel.get_text("//option[@value='37']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("storage", sel.get_text("//option[@value='37']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("id_add_env_property", "label=storage")
        for i in range(60):
            try:
                if sel.is_element_present("id_add_env_value"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_add_env_value"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "file" == sel.get_text("//select[@id='id_add_env_value']/option[3]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("file", sel.get_text("//select[@id='id_add_env_value']/option[3]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("id_add_env_value", "label=file")
        sel.click("id_env_add")
        for i in range(60):
            try:
                if sel.is_element_present("//div[@id='content']/div[4]/div[1]/div[2]/div[7]/div[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//div[@id='content']/div[4]/div[1]/div[2]/div[7]/div[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "storage: file" == sel.get_text("//form[@id='id_form_value_146']/span[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("storage: file", sel.get_text("//form[@id='id_form_value_146']/span[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
