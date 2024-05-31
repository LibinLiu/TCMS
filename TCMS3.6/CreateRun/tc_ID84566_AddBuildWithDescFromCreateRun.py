from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class AddBuildWithDescFromCreateRun(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddBuildWithDescFromCreateRun(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openCreateTestRunFromPlan(self,sel,env.testplanName4,caseSummary=env.testcaseName41,\
		testcaseResultIdNames={env.testcaseId41:env.testcaseName41},\
		testcaseResultNoIdNames={env.testcaseId42:env.testcaseName42})

	rdmNum=random.uniform(1, 10000)
	buildName="Auto"+(str(rdmNum))
        descriptionStr="Just for auto test."

	cc().clickActionInCreateRun(self,sel,"Add Build")
	cc().verifyAddBuildPageIsReady(self,sel)

	cc().fillDataForAddBuildPage(self,sel,build=buildName,product=env.product1,description=descriptionStr)

	cc().clickActionInAddBuildPage(self,sel,"Save")
	cc().verifyCreateTestRunPageIsReady(self,sel,build=buildName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
