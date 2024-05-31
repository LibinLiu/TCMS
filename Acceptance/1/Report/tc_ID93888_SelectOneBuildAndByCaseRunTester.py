from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class SelectOneBuildAndByCaseRunTester(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_SelectOneBuildAndByCaseRunTester(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openTestingReportPage(self,sel)

	cc().generateTestingReport(self,sel,product=env.product1,prodversionList=[env.prodversion11],\
			buildList=[env.build11],reportType="By Case-Run Tester")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
