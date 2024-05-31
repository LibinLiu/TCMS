from selenium import selenium
from env import *
import unittest, time, re

class Bug705975(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug705975(self):
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
                if sel.is_element_present("link=Search Plans"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=Search Plans"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=Search Plans")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if sel.is_element_present("id_product"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_product"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.select("id_product", "label=TCMS")
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='Search']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@value='Search']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='Search']")
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
        sel.click("//input[@name='plan' and @value='"+env.testplanId+"']")   ###
        for i in range(60):
            try:
                if sel.is_element_present("//input[@value='Printable copy']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@value='Printable copy']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@value='Printable copy']")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "Printable copy for test cases" == sel.get_title(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Printable copy for test cases", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
	time.sleep(10)
        for i in range(60):
            try:
                if env.testplanName == sel.get_text("//b"): break   ###
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual(env.testplanName, sel.get_text("//b"))   ###
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
