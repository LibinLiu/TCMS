from selenium import selenium
from env import *
import unittest, time, re

from CommonUtils import CCommonUtils as cc

class EditRunFromMyRuns(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_EditRunFromMyRuns(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#Prepare test data
	absPath = os.path.abspath(__file__)
	testplanName = cc().getFormatName(self,sel,absPath,"testplanName")
	cc().createTestPlan(self,sel,testplanName)

	testcaseName1=cc().getFormatName(self,sel,absPath,"testcaseName")
	testcaseId1 = cc().createTestCaseFromPlan(self,sel,testplanName,testcaseName1)

	testrunName=cc().getFormatName(self,sel,absPath,"testrunName")
	testrunId = cc().createTestRunFromPlan(self,sel,testplanName,testrunName)

	#Open Test Run From My Runs
	cc().openSearchMyRunPage(self,sel)
	cc().clickLink(self,sel,testrunId)

	#Change some test run info
	runNameNew=testrunName + " - Changed Run Name"
	cc().editTestRun(self,sel,testrunName,summary=runNameNew,product=env.product2,prodversion=env.prodversion2,build=env.build2,notes=env.longstring)

	#Restore the test run info
	cc().editTestRun(self,sel,runNameNew,summary=testrunName,product=env.product1,prodversion=env.prodversion11,build=env.build11,notes="")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
