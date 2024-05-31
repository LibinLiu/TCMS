from selenium import selenium
from env import *
import unittest, time, re, random

from CommonUtils import CCommonUtils as cc

class RemoveCommentForReviewingCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_RemoveCommentForReviewingCase(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

        cc().openTestPlan(self,sel,env.testplanName)

	#change the status of the test case to PROPOSED
	cc().changeCaseStatusInPlan(self,sel,"PROPOSED")

	cc().clickFirstLevelLinkByLabelNameInPlan(self,sel,"Reviewing Cases")

	comString="This is just a comment test at: "+time.strftime('%Y'+'-'+'%m'+'-'+'%d'+' '+'%H'+'-'+'%M'+'-'+'%S')
	cc().addCommentForCaseInPlan(self,sel,env.testcaseName,comString)
    
	#restore the status of the test case to CONFIRMED
	cc().changeReviewCaseStatusInPlan(self,sel,"CONFIRMED")
    
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
