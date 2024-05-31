from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class DeleteAttachmentInCase(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_DeleteAttachmentInCase(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)
	
	#(1)Prepare test data
	attachmentPath = os.path.abspath(__file__)
	attachmentName = os.path.basename(attachmentPath)
	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)
	cc().addAttachmentInCase(self,sel,[attachmentPath])

	#(2)Execute test
	cc().openTestCaseFromPlan(self,sel,env.testplanName,env.testcaseId,env.testcaseName)
	cc().verifyTestCasePageIsReady(self,sel,env.testcaseName,attachmentNameList=[attachmentName])

	#(3)Delete the attachment
	cc().removeAttachmentInCase(self,sel,[attachmentName])

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()