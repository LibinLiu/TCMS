from selenium import selenium
from env import *
import unittest, time, re

class Bug601756(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug601756(self):
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
                if "Test Plans" == sel.get_text("//div[@id='content']/div[2]/div[2]/table/tbody/tr[1]/th[1]/div/div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Test Plans", sel.get_text("//div[@id='content']/div[2]/div[2]/table/tbody/tr[1]/th[1]/div/div"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if env.testplanName == sel.get_text("link="+env.testplanName): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(env.testplanName, sel.get_text("link="+env.testplanName))   ###
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link="+env.testplanName)   ###
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
                if "Test case - %s: %s"%(env.testcaseId,env.testcaseName) == sel.get_title(): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Test case - %s: %s"%(env.testcaseId,env.testcaseName), sel.get_title())   ###
        except AssertionError, e: self.verificationErrors.append(str(e))

	for i in range(60):
	    try:
	        if sel.is_element_present("//body[@id='body']/div[@id='content']/div[5]/ul[1]/li[4]/a[1]"): break
	    except: pass
	    time.sleep(1)
	else: self.fail("time out")
	try: self.failUnless(sel.is_element_present("//body[@id='body']/div[@id='content']/div[5]/ul[1]/li[4]/a[1]"))
	except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//body[@id='body']/div[@id='content']/div[5]/ul[1]/li[4]/a[1]")

        for i in range(60):
            try:
                if "TCMS" == sel.get_text("//form[@id='id_form_case_component']/table/tbody/tr[1]/td[2]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("TCMS", sel.get_text("//form[@id='id_form_case_component']/table/tbody/tr[1]/td[2]"))
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
                if "Edit test case - %s"%env.testcaseName == sel.get_title(): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Edit test case - %s"%env.testcaseName, sel.get_title())   ###
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
                if sel.is_element_present("//body[@id='body']/div[@id='content']/div[5]/ul[1]/li[4]/a[1]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//body[@id='body']/div[@id='content']/div[5]/ul[1]/li[4]/a[1]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//body[@id='body']/div[@id='content']/div[5]/ul[1]/li[4]/a[1]")

        for i in range(60):
            try:
                if "TCMS" == sel.get_text("//form[@id='id_form_case_component']/table/tbody/tr[1]/td[2]"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("TCMS", sel.get_text("//form[@id='id_form_case_component']/table/tbody/tr[1]/td[2]"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
