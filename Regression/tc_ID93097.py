from selenium import selenium
from env import *
import unittest, time, re

class Bug634218(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug634218(self):
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
                if sel.is_text_present("Test Runs"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("Test Runs"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link="+env.testrunName): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link="+env.testrunName))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link="+env.testrunName)
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
                if sel.is_element_present("//body[@id='body']/div[@id='content']/div[5]/table[@id='id_table_cases']/tbody[1]/tr[1]/td[2]/img[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//body[@id='body']/div[@id='content']/div[5]/table[@id='id_table_cases']/tbody[1]/tr[1]/td[2]/img[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//body[@id='body']/div[@id='content']/div[5]/table[@id='id_table_cases']/tbody[1]/tr[1]/td[2]/img[1]")
        for i in range(60):
            try:
                if sel.is_element_present("id_comment"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_comment"))
        except AssertionError, e: self.verificationErrors.append(str(e))
	cmt="Add Test Comments aaaaa at: "+ time.strftime('%Y%m%d%H%M%S')
        sel.type("id_comment", cmt)
        for i in range(60):
            try:
                if "" == sel.get_table("//table[@id='id_table_cases']/tbody/tr[2]/td/table/tbody/tr[4]/td/form/table.1.0"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("", sel.get_table("//table[@id='id_table_cases']/tbody/tr[2]/td/table/tbody/tr[4]/td/form/table.1.0"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='Submit' and @type='submit']")
        for i in range(60):
            try:
                if sel.is_text_present(cmt): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present(cmt))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='Delete Comment']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@value='Delete Comment']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='Delete Comment']")
	time.sleep(5)
	self.failUnless(re.search(r"^Are you sure to delete the comment[\s\S]$", sel.get_confirmation()))
	time.sleep(10)
        sel.click("link=Home")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
