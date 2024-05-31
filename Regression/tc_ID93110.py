from selenium import selenium
from env import *
import unittest, time, re

class Bug658475(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug658475(self):
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
                if env.testcaseName == sel.get_text("display_title"): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(env.testcaseName, sel.get_text("display_title"))   ###
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//body[@id='body']/div[@id='content']/div[5]/ul[@id='contentTab']/li[6]/a[1]")
        for i in range(60):
            try:
                if sel.is_element_present("bug_id"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("bug_id"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("//a[@onclick='addCaseBug(this.up(1))']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//a[@onclick='addCaseBug(this.up(1))']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("bug_id", "5555")
        sel.click("//a[@onclick='addCaseBug(this.up(1))']")
        for i in range(60):
            try:
                if sel.is_text_present("https://bugzilla.redhat.com/show_bug.cgi?id=5555"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("https://bugzilla.redhat.com/show_bug.cgi?id=5555"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//body[@id='body']/div[@id='content']/div[5]/div[@id='bug']/table[1]/tbody[1]/tr[2]/td[4]/a[1]")
        self.failUnless(re.search(r"^Are you sure to remove the bug[\s\S]$", sel.get_confirmation()))
        for i in range(60):
            try:
                if not sel.is_text_present("https://bugzilla.redhat.com/show_bug.cgi?id=5555"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failIf(sel.is_text_present("https://bugzilla.redhat.com/show_bug.cgi?id=5555"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
