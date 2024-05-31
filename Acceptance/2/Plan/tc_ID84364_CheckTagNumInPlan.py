from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CheckTagNumInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CheckTagNumInPlan(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	cc().openTestPlan(self,sel,env.testplanName)
	
	#Add 3 new tags
	tagName1 = "mytag1@xx"
	tagName2 = "mytag2@xx"
	tagName3 = "mytag3@xx"
	tagName = tagName1+","+tagName2+","+tagName3

	cc().addTagInPlan(self,sel,tagName,needRemove=False)

	#Verify that the number is interconsistency with the real number of tags.
	cc().verifyTagInfoInPlan(self,sel,tagNum=3)

	#Remove the tag
	cc().removeTagInPlan(self,sel,[tagName1,tagName2,tagName3])

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
