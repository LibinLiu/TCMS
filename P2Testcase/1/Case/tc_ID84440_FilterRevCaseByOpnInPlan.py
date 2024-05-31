from selenium import selenium
import unittest, time, re, random

from env import *
from CommonUtils import CCommonUtils as cc

class FilterRevCaseByOpnInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_FilterRevCaseByOpnInPlan(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#Add a tag in test case
	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)

	rdm=random.uniform(1, 1000)
	tagName = "aa@@aa11"+str(rdm)
	cc().addTagInCase(self,sel,tagName)

	#change the status of the test case to 'PROPOSED'
	cc().openTestPlan(self,sel,env.testplanName)
	cc().changeCaseStatusInPlan(self,sel,"PROPOSED")
	cc().clickFirstLevelLinkByLabelNameInPlan(self,sel,"Reviewing Cases")

	#Filter reviewing test case
	cc().filterCaseInPlan(self,sel,caseType="Reviewing Cases",caseSummary=env.testcaseName,author=env.user,defaulttester=env.user,\
			priorityList=[1],automated="Auto",autoproposed="off",category=env.category11,\
			statusList=[1],component=env.component11,tag=tagName,testcaseResultIdNames={env.testcaseId:env.testcaseName})
    
	#restore the status of the test case to 'CONFIRMED'
	cc().changeReviewCaseStatusInPlan(self,sel,"CONFIRMED")
	cc().clickFirstLevelLinkByLabelNameInPlan(self,sel,"Cases")
	cc().verifyLink(self,sel,env.testcaseId)

	#Remove the added tag
	cc().clickLink(self,sel,env.testcaseId)
	cc().removeTagInCase(self,sel,tagName)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
