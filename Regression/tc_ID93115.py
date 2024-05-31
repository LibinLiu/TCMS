from selenium import selenium
from env import *
import unittest, time, re

class Bug680315(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_bug680315(self):
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
                if sel.is_element_present("link=REPORTING"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=REPORTING"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.mouse_over("link=REPORTING")
        for i in range(60):
            try:
                if sel.is_element_present("link=Overall"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=Overall"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=Overall")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "Reporting" == sel.get_title(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Reporting", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "Product" == sel.get_text("//div[@id='content']/h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Product", sel.get_text("//div[@id='content']/h1"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if sel.is_element_present("link=ACK Viewer"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=ACK Viewer"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=ACK Viewer")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if "Reporting - ACK Viewer" == sel.get_title(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Reporting - ACK Viewer", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "ACK Viewer" == sel.get_text("//div[@id='content']/div[2]/span"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("ACK Viewer", sel.get_text("//div[@id='content']/div[2]/span"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "Testing Runs" == sel.get_text("//div[@id='content']/div[3]/div/table/tbody/tr[1]/td"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Testing Runs", sel.get_text("//div[@id='content']/div[3]/div/table/tbody/tr[1]/td"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        for i in range(60):
            try:
                if "Testing Cases" == sel.get_text("//div[@id='content']/div[3]/div/table/tbody/tr[4]/td"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Testing Cases", sel.get_text("//div[@id='content']/div[3]/div/table/tbody/tr[4]/td"))
        except AssertionError, e: self.verificationErrors.append(str(e))
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
