from selenium import selenium
from env import *
import unittest, time, re

class Bug681156(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug681156(self):
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
                if sel.is_element_present("link="+env.testplanName): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link="+env.testplanName))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link="+env.testplanName)
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if env.testplanName == sel.get_text("display_title"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(env.testplanName, sel.get_text("display_title"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link="+env.testcaseId): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link="+env.testcaseId))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("//a[@id='id_blind_all_link']/img"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//a[@id='id_blind_all_link']/img"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//div[@id='testcases']/table/thead/tr/th[2]/input")
        sel.click("//a[@id='id_blind_all_link']/img")
        for i in range(60):
            try:
                if sel.is_text_present("Setup:"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("Setup:"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_text_present("Actions:"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("Actions:"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_text_present("Expected Results:"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("Expected Results:"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_text_present("Breakdown:"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_text_present("Breakdown:"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
