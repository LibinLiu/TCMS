from selenium import selenium
from env import *
import unittest, time, re

class Bug638476(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug638476(self):
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
                if sel.is_element_present("link=ENVIRONMENT"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=ENVIRONMENT"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.mouse_over("link=ENVIRONMENT")
        for i in range(60):
            try:
                if sel.is_element_present("link=Groups"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=Groups"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=Groups")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if sel.is_element_present("link=AM-QA (DEV0)"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=AM-QA (DEV0)"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=AM-QA (DEV0)")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if sel.is_element_present("//div[@id='content']/form/table/tbody/tr[1]/td[1]/label"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//div[@id='content']/form/table/tbody/tr[1]/td[1]/label"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "Enabled" == sel.get_table("//div[@id='content']/form/table.0.1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Enabled", sel.get_table("//div[@id='content']/form/table.0.1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("//input[@name='name' and @value='AM-QA (DEV0)' and @type='text']", "AM-QA (DEV011)")
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
                if sel.is_element_present("//input[@value='Back']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@value='Back']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='Save']")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "Environment group saved successfully." == sel.get_table("//div[@id='content']/form/table.2.0"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Environment group saved successfully.", sel.get_table("//div[@id='content']/form/table.2.0"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='Back']")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if sel.is_element_present("link=AM-QA (DEV011)"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=AM-QA (DEV011)"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=AM-QA (DEV011)")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "Enabled" == sel.get_table("//div[@id='content']/form/table.0.1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Enabled", sel.get_table("//div[@id='content']/form/table.0.1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("//input[@name='name' and @value='AM-QA (DEV011)' and @type='text']", "AM-QA (DEV0)")
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
                if sel.is_element_present("//input[@value='Back']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@value='Back']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='Back']")
        sel.wait_for_page_to_load("30000")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
