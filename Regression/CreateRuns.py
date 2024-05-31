from selenium import selenium
from env import *
import unittest, time, re

class CreateRuns(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium("localhost", 4444, "*chrome", env.domain)   ###
        self.selenium.start()
    
    def test_create_runs(self):
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

	#Check the test run and get the run id number
        for i in range(60):
		try:
			if sel.is_element_present("link="+env.testrunName):	###
				sel.click("link="+env.testrunName)  ###
				sel.wait_for_page_to_load("30000")

				title = sel.get_text("css=div.sprites.crumble")
				t1=title.find('[')
				t2=title.find(']')		
				env.testrunId = title[t1+1:t2]

				print "The testrun 'name[%s],id[%s]' exists, no need to create!" %(env.testrunName,env.testrunId)	###
				break
		except: pass
		time.sleep(1)
        else:
		print "The testrun '%s' does not exist, begin to create new one..." % env.testrunName	###

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
		for i in range(60):
		    try:
		        if sel.is_element_present("//div[@id='testcases']/form/div/div[1]/ul/li[2]/span"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("//div[@id='testcases']/form/div/div[1]/ul/li[2]/span"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.click("//div[@id='testcases']/form/div[1]/div[1]/ul/li[2]/span")
		sel.wait_for_page_to_load("30000")
		time.sleep(10)
		for i in range(60):
		    try:
		        if sel.is_element_present("id_build"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		for i in range(60):
		    try:
		        if "Create new test run" == sel.get_title(): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.assertEqual("Create new test run", sel.get_title())
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.type("id_summary", env.testrunName)   ###

		#add Build
		for i in range(60):
		    try:
		        if sel.is_element_present("id_build"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("id_build"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.select("id_build", "label=TCMS-3.0.3-1.svn2841")

		for i in range(60):
		    try:
		        if sel.is_element_present("css=div.submit-row. > input[type=submit]"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("css=div.submit-row. > input[type=submit]"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.click("css=div.submit-row. > input[type=submit]")
		sel.wait_for_page_to_load("30000")

		#add one property
		for i in range(60):
		    try:
		        if sel.is_element_present("link=Add Property"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("link=Add Property"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.click("link=Add Property")
		#sel.wait_for_page_to_load("30000")
		time.sleep(10)
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
		        if sel.is_element_present("id_add_env_property"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("id_add_env_property"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		for i in range(60):
		    try:
		        if "Arch" == sel.get_text("//option[@value='10']"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.assertEqual("Arch", sel.get_text("//option[@value='10']"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.select("id_add_env_property", "label=Arch")
		for i in range(60):
		    try:
		        if sel.is_element_present("id_add_env_value"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("id_add_env_value"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		for i in range(60):
		    try:
		        if "i386" == sel.get_text("//select[@id='id_add_env_value']/option[2]"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.assertEqual("i386", sel.get_text("//select[@id='id_add_env_value']/option[2]"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.select("id_add_env_value", "label=i386")
		for i in range(60):
		    try:
		        if sel.is_element_present("id_env_add"): break
		    except: pass
		    time.sleep(1)
		else: self.fail("time out")
		try: self.failUnless(sel.is_element_present("id_env_add"))
		except AssertionError, e: self.verificationErrors.append(str(e))
		sel.click("id_env_add")
		sel.wait_for_page_to_load("30000")

		sel.click("link=HOME")
		sel.wait_for_page_to_load("30000")

		#Check the test run and get the run id number
		for i in range(60):
			try:
				if sel.is_element_present("link="+env.testrunName):	###
					sel.click("link="+env.testrunName)  ###
					sel.wait_for_page_to_load("30000")

					title = sel.get_text("css=div.sprites.crumble")
					t1=title.find('[')
					t2=title.find(']')		
					env.testrunId = title[t1+1:t2]

					print "Newly created testrun: name[%s],id[%s]"%(env.testrunName,env.testrunId)   ###
					break
			except: pass
			time.sleep(1)
		sel.click("link=HOME")
		sel.wait_for_page_to_load("30000")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
