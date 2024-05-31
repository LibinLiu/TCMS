from selenium import selenium
import unittest, time, re
import os, sys, inspect

from env import *
from CommonUtils import CCommonUtils as cc

class CreatePlanWithInvalidPlanDoc(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.selenium = selenium(env.host, env.port, env.browser, env.domain)
        self.selenium.start()
    
    def test_CreatePlanWithInvalidPlanDoc(self):
        sel = self.selenium
        sel.open(env.openurl)

        cc().verifyHomePageIsReady(self,sel)

	#(1)Check invalid doc - an application file
	cc().clickMenu(self,sel,"PLANNING","New Plan")
	cc().verifyCreateTestPlanPageIsReady(self,sel)

	planName = "New Test plan1 xxxxxx11 for Auto"

	planDocName = os.path.dirname(os.path.abspath(__file__)) + os.sep + "testdata"

	cc().fillDataForTestPlan(self,sel,planname=planName,product=env.product1,prodversion=env.prodversion11,\
		typename=env.plantype11,uploadPlanDocName=planDocName)

	cc().clickActionInCreateTestPlan(self,sel,"Create test plan")

	#Verify if a red warning for the error will appear
	cc().verifyErrWarningMsgInEditTestPlan(self,sel,"Upload Invalid Plan Document1")

	#(2)Check invalid doc - an .sh file
	cc().clickMenu(self,sel,"PLANNING","New Plan")
	cc().verifyCreateTestPlanPageIsReady(self,sel)

	planName = "New Test plan2 xxxxxx11 for Auto"

	planDocName = os.path.dirname(os.path.abspath(__file__)) + os.sep + "testdata.sh"

	cc().fillDataForTestPlan(self,sel,planname=planName,product=env.product1,prodversion=env.prodversion11,\
		typename=env.plantype11,uploadPlanDocName=planDocName)

	cc().clickActionInCreateTestPlan(self,sel,"Create test plan")

	#Verify if a red warning for the error will appear
	cc().verifyErrWarningMsgInEditTestPlan(self,sel,"Upload Invalid Plan Document2")

    def tearDown(self):
        self.selenium.stop()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
