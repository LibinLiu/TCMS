from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class CheckPlanNumWithTagInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CheckPlanNumWithTagInPlan(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	rdm=random.uniform(1, 1000)
	tagName = "mytag@xx"+str(rdm)

	cc().openTestPlan(self,sel,env.testplanName)
	cc().addTagInPlan(self,sel,tagName,needRemove=False)
	cc().verifyTagInfoInPlan(self,sel,planNum=1,tagName=tagName)

	#Remove the tag from case and plan
	cc().removeTagInPlan(self,sel,[tagName])

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
