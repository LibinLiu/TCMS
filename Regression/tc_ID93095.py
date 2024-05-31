from selenium import selenium
from env import *
import unittest, time, re

class Bug612797(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug612797(self):
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
                if env.testrunName == sel.get_title(): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(env.testrunName, sel.get_title())   ###
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_text_present("Environment"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("Environment"))
        except AssertionError, e: self.verificationErrors.append(str(e))
	time.sleep(10)
        for i in range(60):
            try:
                if sel.is_text_present("Arch: i386"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("Arch: i386"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("//img[@title='Remove this property']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//img[@title='Remove this property']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//img[@title='Remove this property']")
        self.failUnless(re.search(r"^Are you sure to remove this porperty[\s\S]$", sel.get_confirmation()))
	time.sleep(15)

        for i in range(60):
            try:
                if sel.is_element_present("link=Add Property"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=Add Property"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=Add Property")
        sel.click("//div[@onclick='this.up(1).hide()']")
        for i in range(60):
            try:
                if "Arch" == sel.get_text("//option[@value='10']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Arch", sel.get_text("//option[@value='10']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("id_add_env_property", "label=Arch")
        for i in range(60):
            try:
                if "i386" == sel.get_text("//select[@id='id_add_env_value']/option[2]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("i386", sel.get_text("//select[@id='id_add_env_value']/option[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("id_add_env_value", "label=i386")
        for i in range(60):
            try:
                if sel.is_element_present("id_env_add"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_env_add"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id_env_add")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
