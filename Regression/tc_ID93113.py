from selenium import selenium
from env import *
import unittest, time, re

class Bug672231(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug672231(self):
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
                if sel.is_element_present("link=My Plans"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=My Plans"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=My Plans")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "Test plans" == sel.get_title(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Test plans", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link="+env.testplanName): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link="+env.testplanName))   ###
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.open_window(env.domain+"/plan/"+env.testplanName+"/", "")   ###

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
