from selenium import selenium
from env import *
import unittest, time, re, random

from CommonUtils import CCommonUtils as cc

class AddCommentForReviewingCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_AddCommentForReviewingCase(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

        cc().openTestPlan(self,sel,env.testplanName)

	#1. change the status of the test case to PROPOSED
	cc().changeCaseStatusInPlan(self,sel,"PROPOSED")
	cc().clickFirstLevelLinkByLabelNameInPlan(self,sel,"Reviewing Cases")

	#add comments
	comString="This is just a comment test at: "+time.strftime('%Y'+'-'+'%m'+'-'+'%d'+' '+'%H'+'-'+'%M'+'-'+'%S')
	cc().addCommentForCaseInPlan(self,sel,env.testcaseName,comString,needRemove=False)
    
	#2. change the status of the test case to CONFIRMED
	cc().changeReviewCaseStatusInPlan(self,sel,"CONFIRMED")
	cc().clickFirstLevelLinkByLabelNameInPlan(self,sel,"Cases")

	#verify the comments exist
	cc().verifyCommentForCaseInPlan(self,sel,env.testcaseName,comString,comExists=True)

	#3. change the status of the test case to PROPOSED
	cc().changeCaseStatusInPlan(self,sel,"PROPOSED")
	cc().clickFirstLevelLinkByLabelNameInPlan(self,sel,"Reviewing Cases")

	#remove the added comments
	cc().removeCommentForCaseInPlan(self,sel,env.testcaseName,comString)
    
	#4. change the status of the test case to CONFIRMED
	cc().changeReviewCaseStatusInPlan(self,sel,"CONFIRMED")
	cc().clickFirstLevelLinkByLabelNameInPlan(self,sel,"Cases")

	#verify the comments do not exist
	cc().verifyCommentForCaseInPlan(self,sel,env.testcaseName,comString,comExists=False)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
