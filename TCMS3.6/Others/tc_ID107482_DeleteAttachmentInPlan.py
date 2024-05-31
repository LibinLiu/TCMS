from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class DeleteAttachmentInPlan(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_DeleteAttachmentInPlan(self):
        sel = self.selenium
        sel.open(env.openurl)
        cc().verifyHomePageIsReady(self,sel)

	#(1)Prepare test data
	attachmentPath = os.path.abspath(__file__)
	attachmentName = os.path.basename(attachmentPath)
	cc().openTestPlan(self,sel,env.testplanName)
	cc().addAttachmentInPlan(self,sel,[attachmentPath])

	#(2)Execute test
	cc().openTestPlan(self,sel,env.testplanName)
	cc().verifyTestPlanPageIsReady(self,sel,env.testplanName,attachmentNameList=[attachmentName])

	#(3)Delete the attachment
	cc().removeAttachmentInPlan(self,sel,[attachmentName])
	
    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
