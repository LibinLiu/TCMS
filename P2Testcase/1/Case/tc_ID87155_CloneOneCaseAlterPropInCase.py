from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CloneOneCaseAlterPropInCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CloneOneCaseAlterPropInCase(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	#(1)Prepare test data
	absPath = os.path.abspath(__file__)
	testplanName = cc().getFormatName(self,sel,absPath,"testplanName")
	testplanId = cc().createTestPlan(self,sel,testplanName)

	testcaseName1=cc().getFormatName(self,sel,absPath,"testcaseName")
	testcaseId1 = cc().createTestCaseFromPlan(self,sel,testplanName,testcaseName1)

	cc().openTestPlan(self,sel,testplanName)

	#(2)Execute test
	cc().clickCaseActionInPlan(self,sel,"Clone")
	cc().verifyCloneTestCasePageIsReady(self,sel,{testcaseId1:testcaseName1})

	cc().saveCloneTestCase(self,sel,selectPlan="Use Sameplan",keepOriginalAuthor="off",\
			keepOriginalDefaultTester="off",copyComponentToNewProduct="off")

	cc().verifyTestCasePageIsReady(self,sel,testcaseName1,defaulttester=env.useremail,\
		author=env.useremail,noComponentIdNames={env.componentId11:env.component11})

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
