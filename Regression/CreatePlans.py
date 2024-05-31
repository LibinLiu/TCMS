from selenium import selenium
from env import *
import unittest, time, re

class CreatePlans(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_create_plans(self):
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
			if sel.is_element_present("link="+env.testplanName):	###
				print "The testplan '%s' exists, no need to create!" % env.testplanName	###
				break
		except: pass
		time.sleep(1)
        else:
		print "The testplan '%s' does not exist, begin to create new one..." % env.testplanName	###

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
			if sel.is_element_present("link=New Plan"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("link=New Plan"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.click("link=New Plan")
		sel.wait_for_page_to_load("30000")
		for i in range(60):
		    try:
			if sel.is_element_present("id_name"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("id_name"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.type("id_name", env.testplanName)   ###
		for i in range(60):
		    try:
			if sel.is_element_present("id_product"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("id_product"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.select("id_product", "label=TCMS")
		time.sleep(10)
		for i in range(60):
		    try:
			if sel.is_element_present("id_default_product_version"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("id_default_product_version"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		for i in range(60):
		    try:
			sel.select("id_default_product_version", "label=1.0")
			break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		for i in range(60):
		    try:
			if sel.is_element_present("id_type"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("id_type"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.select("id_type", "label=Function")
		for i in range(60):
		    try:
			if sel.is_element_present("//input[@value='Create test plan']"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("//input[@value='Create test plan']"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.click("//input[@value='Create test plan']")
		sel.wait_for_page_to_load("30000")
		sel.click("link=HOME")
		sel.wait_for_page_to_load("30000")
		for i in range(60):
			try:
				if sel.is_element_present("link="+env.testplanName):	###
					print "Newly created testplan name: %s"%env.testplanName   ###
					break
			except: pass
			time.sleep(1)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
