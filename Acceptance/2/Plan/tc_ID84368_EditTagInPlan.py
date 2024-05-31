from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class EditTagInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_EditTagInPlan(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().openTestPlan(self,sel,env.testplanName)

	#Add a new tag
	tagName = "mytag@xx"
	cc().addTagInPlan(self,sel,tagName,needRemove=False)

	#Edit the newly added tag
	tagNameNew = tagName + "New"
	cc().editTagInPlan(self,sel,tagName,tagNameNew)

	#Remove the changed tag
	cc().removeTagInPlan(self,sel,[tagNameNew])

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
