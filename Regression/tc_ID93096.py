from selenium import selenium
from env import *
import unittest, time, re

class Bug618710(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug618710(self):
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
                if "Environment :" == sel.get_text("//div[@id='content']/div[4]/div[1]/div[2]/div[7]/div[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Environment :", sel.get_text("//div[@id='content']/div[4]/div[1]/div[2]/div[7]/div[1]"))
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
                if sel.is_text_present("Property"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("Property"))
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
                if "TCMS_Testing" == sel.get_text("//option[@value='103']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("TCMS_Testing", sel.get_text("//option[@value='103']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("id_add_env_property", "label=TCMS_Testing")
	time.sleep(10)
        for i in range(60):
            try:
                if "Nitrate 3.1.1-3" == sel.get_text("//option[@value='490']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Nitrate 3.1.1-3", sel.get_text("//option[@value='490']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("id_env_add"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_env_add"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("id_env_add")
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
                if sel.is_text_present("Environment :"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("Environment :"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_text_present("TCMS_Testing: Nitrate 3.1.1-3"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("TCMS_Testing: Nitrate 3.1.1-3"))
        except AssertionError, e: self.verificationErrors.append(str(e))
	time.sleep(5)
        for i in range(60):
            try:
                if sel.is_element_present("//body[@id='body']/div[@id='content']/div[4]/div[1]/div[2]/div[7]/div[2]/ul[1]/li[2]/form[1]/span[2]/a[2]/img[1]"): break #//img[@onclick=\"removeProperty('22012','490')\"]
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//body[@id='body']/div[@id='content']/div[4]/div[1]/div[2]/div[7]/div[2]/ul[1]/li[2]/form[1]/span[2]/a[2]/img[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//body[@id='body']/div[@id='content']/div[4]/div[1]/div[2]/div[7]/div[2]/ul[1]/li[2]/form[1]/span[2]/a[2]/img[1]")
	time.sleep(5)
        self.failUnless(re.search(r"^Are you sure to remove this porperty[\s\S]$", sel.get_confirmation()))
	time.sleep(5)
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
