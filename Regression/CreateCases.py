from selenium import selenium
from env import *
import unittest, time, re

class CreateCases(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def get_testcaseId(self,sel):  ###

	sel.click("link=HOME")
	sel.wait_for_page_to_load("30000")

        for i in range(60):
            try:
                if "TESTING" == sel.get_text("link=TESTING"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("TESTING", sel.get_text("link=TESTING"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.mouse_over("link=TESTING")
        for i in range(60):
            try:
                if sel.is_element_present("link=Search Cases"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("link=Search Cases"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("link=Search Cases")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
                if sel.is_element_present("id_summary"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("id_summary"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.type("id_summary", env.testcaseName)  ###
        for i in range(60):
            try:
                if sel.is_element_present("//input[@name='a' and @value='search']"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.failUnless(sel.is_element_present("//input[@name='a' and @value='search']"))
        except AssertionError, e: self.verificationErrors.append(str(e))
        sel.click("//input[@name='a' and @value='search']")
        sel.wait_for_page_to_load("30000")
        for i in range(60):
            try:
               if sel.is_element_present("link="+env.testcaseName):   ###
			sel.click("link="+env.testcaseName)  ###
        		sel.wait_for_page_to_load("30000")

			#Get the case id number
			title = sel.get_title()
			t1=title.find("Test case - ")
			t2=title.find(": ")
			env.testcaseId = title[t1+12:t2]
			break

            except: pass
            time.sleep(1)

	sel.click("link=HOME")
	sel.wait_for_page_to_load("30000")

    def test_create_cases(self):
        sel = self.selenium
        sel.open("/accounts/"+env.user+"/recent/")	###

        for i in range(60):
            try:
                if "Nitrate" == sel.get_title(): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        try: self.assertEqual("Nitrate", sel.get_title())
        except AssertionError, e: self.verificationErrors.append(str(e))

	self.get_testcaseId(sel)

	if env.testcaseId=="":   ###

		print "The testcase '%s' does not exist, begin to create new one..." % env.testcaseName	###

		#open the test plan
		for i in range(60):
		    try:
		        if sel.is_element_present("link="+env.testplanName): break	###
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("link="+env.testplanName))	###
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.click("link="+env.testplanName)	###
		sel.wait_for_page_to_load("30000")

		#create a test case added into the test plan
		for i in range(60):
		    try:
		        if "Case" == sel.get_text("//div[@id='testcases']/form/div/div[1]/ul/li[1]/span"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.assertEqual("Case", sel.get_text("//div[@id='testcases']/form/div/div[1]/ul/li[1]/span"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.mouse_over("//div[@id='testcases']/form/div/div[1]/ul/li[1]/span")
		for i in range(60):
		    try:
		        if "Write new case" == sel.get_value("//div[@id='testcases']/form/div/div[1]/ul/li[1]/ul/li[1]/input"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.assertEqual("Write new case", sel.get_value("//div[@id='testcases']/form/div/div[1]/ul/li[1]/ul/li[1]/input"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.click("//div[@id='testcases']/form/div/div[1]/ul/li[1]/ul/li[1]/input")
		sel.wait_for_page_to_load("30000")
		for i in range(60):
		    try:
		        if "Add new case" == sel.get_title(): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.assertEqual("Add new case", sel.get_title())
		except AssertionError, e: self.verificationErrors.append(str(e))

		#type summary of new test case
		for i in range(60):
		    try:
		        if sel.is_element_present("id_summary"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("id_summary"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.type("id_summary", env.testcaseName)   ###

		#add component
		for i in range(60):
		    try:
		        if sel.is_element_present("id_component_input"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("id_component_input"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		for i in range(60):
		    try:
		        if "TCMS" == sel.get_text("//option[@value='57736']"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.assertEqual("TCMS", sel.get_text("//option[@value='57736']"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.add_selection("id_component_from", "label=TCMS")
		for i in range(60):
		    try:
		        if sel.is_element_present("link=Add"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("link=Add"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.click("link=Add")

		#select category
		for i in range(60):
		    try:
		        if sel.is_element_present("id_category"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("id_category"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		for i in range(60):
		    try:
		        if "Functional" == sel.get_text("//option[@value='182']"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.assertEqual("Functional", sel.get_text("//option[@value='182']"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.select("id_category", "label=Functional")

		#save the test case
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

		#open the test plan
		sel.click("link=HOME")
		sel.wait_for_page_to_load("30000")
		for i in range(60):
		    try:
		        if sel.is_element_present("link="+env.testplanName): break	###
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("link="+env.testplanName))	###
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.click("link="+env.testplanName)	###
		sel.wait_for_page_to_load("30000")

		#change the status of just created test case from reviewing to confirmed
		sel.click("//body[@id='body']/div[@id='content']/div[@id='plan_detail']/div[1]/ul[@id='contentTab']/li[@id='tab_reviewcases']/a[1]")
		for i in range(60):
		    try:
		        if "Status" == sel.get_text("//div[@id='reviewcases']/form/div[1]/div[1]/ul/li[6]/span"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.assertEqual("Status", sel.get_text("//div[@id='reviewcases']/form/div[1]/div[1]/ul/li[6]/span"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.mouse_over("//div[@id='reviewcases']/form/div[1]/div[1]/ul/li[6]/span")
		for i in range(60):
		    try:
		        if sel.is_element_present("//input[@value='Set CONFIRMED']"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("//input[@value='Set CONFIRMED']"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.click("//input[@value='Set CONFIRMED']")
		self.failUnless(re.search(r"^Are you sure you want to change the status[\s\S]$", sel.get_confirmation()))
		sel.click("//body[@id='body']/div[@id='content']/div[@id='plan_detail']/div[1]/ul[@id='contentTab']/li[@id='tab_reviewcases']/a[1]")
		sel.refresh()

		#Get the case id number
		self.get_testcaseId(sel)
		print "Newly created testcase: name[%s],id[%s]"%(env.testcaseName,env.testcaseId)   ###

	else: print "The testcase 'name[%s],id[%s]' exists, no need to create!" %(env.testcaseName,env.testcaseId)	###

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
