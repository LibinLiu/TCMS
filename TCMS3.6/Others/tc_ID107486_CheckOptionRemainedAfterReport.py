from selenium import selenium
import unittest, time, re

from env import *
from CommonUtils import CCommonUtils as cc

class CheckOptionRemainedAfterReport(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()

    def test_CheckOptionRemainedAfterReport(self):
        sel = self.selenium
        sel.open(env.openurl)
	cc().verifyHomePageIsReady(self,sel)

	cc().openTestingReportPage(self,sel)

	cc().generateTestingReport(self,sel,product=env.product1,prodversionList=[env.prodversion11,env.prodversion12],\
		buildList=[env.build11,env.build12],executeDateAfter="2000-01-01",\
		executeDateBefore=time.strftime('%Y'+'-'+'%m'+'-'+'%d'),reportType="By Case-Run Tester",\
		verifyOptions=True)

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
