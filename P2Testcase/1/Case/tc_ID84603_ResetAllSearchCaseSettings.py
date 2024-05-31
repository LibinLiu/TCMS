from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class ResetAllSearchCaseSettings(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_ResetAllSearchCaseSettings(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)
	
	cc().openSearchCasePage(self,sel)

	#Fill data in Search Case page.
	cc().fillDataForSearchCase(self,sel,summary="Testxxx",author="Testxxx",product=env.product1,plan="Testxxx",\
			priority=[1,2,3,4,5],automated="Auto",autoproposed="on",category=env.category11,\
			status=[1,4],component=env.component11,bugID="Testxxx",tag="Testxxx")

	#Click Reset button and Verify the Default Setting of Search Case page is correct.
	cc().clickActionInSearchCase(self,sel,"Reset")
	cc().verifySearchCasePageDefaultSetting(self,sel)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
