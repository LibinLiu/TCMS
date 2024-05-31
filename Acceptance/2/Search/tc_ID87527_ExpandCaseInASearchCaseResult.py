from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class ExpandCaseInASearchCaseResult(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ExpandCaseInASearchCaseResult(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#--(A) Prepare test data
	absPath = os.path.abspath(__file__)

	rdm=random.uniform(1, 1000)
	testcaseNameSuffix="["+str(rdm)+"]"

	testplanName = cc().getFormatName(self,sel,absPath,"testplanName")
	testplanId=cc().createTestPlan(self,sel,testplanName)

	testcaseName1=cc().getFormatName(self,sel,absPath,"testcaseName")+testcaseNameSuffix
	testcaseId1=cc().createCustomizedTestCaseFromPlan(self,sel,testplanName,summary=testcaseName1,product=env.product1,component=[env.component12],\
		category=env.category11,manual="off",auto="on",autoproposal="off",defaulttester=env.useremail,priority="P1")

	testcaseName2=cc().getFormatName(self,sel,absPath,"testcaseName")+testcaseNameSuffix
	testcaseId2=cc().createCustomizedTestCaseFromPlan(self,sel,testplanName,summary=testcaseName2,product=env.product1,component=[env.component13],\
		category=env.category11,manual="off",auto="on",autoproposal="off",defaulttester=env.useremail,priority="P1")

	testcaseName3=cc().getFormatName(self,sel,absPath,"testcaseName")+testcaseNameSuffix
	testcaseId3=cc().createCustomizedTestCaseFromPlan(self,sel,testplanName,summary=testcaseName3,product=env.product1,component=[env.component14],\
		category=env.category11,manual="off",auto="on",autoproposal="off",defaulttester=env.useremail,priority="P1")

	#--(B) Execute test
	#(1)Expand a test case
	cc().searchCaseByCaseOptInASearch(self,sel,summary=testcaseNameSuffix,\
		resultIdNames={testcaseId1:testcaseName1,testcaseId2:testcaseName2,testcaseId3:testcaseName3})

	cc().verifyTextNotPresent(self,sel,env.component12)
	cc().verifyTextNotPresent(self,sel,env.component13)
	cc().verifyTextNotPresent(self,sel,env.component14)

	testcaseId=cc().expcolCaseInASearchCaseResult(self,sel,"1","Expand")
	if testcaseId==testcaseId1: cc().verifyText(self,sel,env.component12)
	elif testcaseId==testcaseId2: cc().verifyText(self,sel,env.component13)
	elif testcaseId==testcaseId3: cc().verifyText(self,sel,env.component14)

	#(2)Expand 2 test cases
	cc().searchCaseByCaseOptInASearch(self,sel,summary=testcaseNameSuffix,\
		resultIdNames={testcaseId1:testcaseName1,testcaseId2:testcaseName2,testcaseId3:testcaseName3})

	cc().verifyTextNotPresent(self,sel,env.component12)
	cc().verifyTextNotPresent(self,sel,env.component13)
	cc().verifyTextNotPresent(self,sel,env.component14)

	testcaseId=cc().expcolCaseInASearchCaseResult(self,sel,"1","Expand")
	if testcaseId==testcaseId1: cc().verifyText(self,sel,env.component12)
	elif testcaseId==testcaseId2: cc().verifyText(self,sel,env.component13)
	elif testcaseId==testcaseId3: cc().verifyText(self,sel,env.component14)

	testcaseId=cc().expcolCaseInASearchCaseResult(self,sel,"2","Expand")
	if testcaseId==testcaseId1: cc().verifyText(self,sel,env.component12)
	elif testcaseId==testcaseId2: cc().verifyText(self,sel,env.component13)
	elif testcaseId==testcaseId3: cc().verifyText(self,sel,env.component14)

	#(3)Expand all test cases
	cc().searchCaseByCaseOptInASearch(self,sel,summary=testcaseNameSuffix,\
		resultIdNames={testcaseId1:testcaseName1,testcaseId2:testcaseName2,testcaseId3:testcaseName3})

	cc().verifyTextNotPresent(self,sel,env.component12)
	cc().verifyTextNotPresent(self,sel,env.component13)
	cc().verifyTextNotPresent(self,sel,env.component14)

	testcaseId=cc().expcolCaseInASearchCaseResult(self,sel,"All","Expand")
	cc().verifyText(self,sel,env.component12)
	cc().verifyText(self,sel,env.component13)
	cc().verifyText(self,sel,env.component14)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
