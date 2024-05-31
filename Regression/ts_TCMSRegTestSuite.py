from selenium import selenium
import unittest, time, re

from env import *

import tc_ID93086, tc_ID93087, tc_ID93089, tc_ID93090, tc_ID93091, tc_ID93092, tc_ID93094, tc_ID93095, tc_ID93096, tc_ID93097, tc_ID93098, tc_ID93099
import tc_ID93106, tc_ID93109, tc_ID93110, tc_ID93113, tc_ID93114, tc_ID93115, tc_ID93116, tc_ID93125, tc_ID93141, tc_ID93647

def suite():

	suite = unittest.TestSuite()

	suite.addTest(tc_ID93086.Bug584838("test_bug584838"))
	suite.addTest(tc_ID93087.Bug590809("test_bug590809"))
	suite.addTest(tc_ID93089.Bug594566("test_bug594566"))
	suite.addTest(tc_ID93090.Bug595680("test_bug595680"))
	suite.addTest(tc_ID93091.Bug597132("test_bug597132"))
	suite.addTest(tc_ID93092.Bug599313("test_bug599313"))
	suite.addTest(tc_ID93094.Bug601756("test_bug601756"))
	suite.addTest(tc_ID93095.Bug612797("test_bug612797"))
	suite.addTest(tc_ID93096.Bug618710("test_bug618710"))
	suite.addTest(tc_ID93097.Bug634218("test_bug634218"))
	suite.addTest(tc_ID93098.Bug638476("test_bug638476"))
	suite.addTest(tc_ID93099.Bug635549("test_bug635549"))
	suite.addTest(tc_ID93106.Bug578717("test_bug578717"))
	suite.addTest(tc_ID93109.Bug658160("test_bug658160"))
	suite.addTest(tc_ID93110.Bug658475("test_bug658475"))
	suite.addTest(tc_ID93113.Bug672231("test_bug672231"))
	suite.addTest(tc_ID93114.Bug672622("test_bug672622"))
	suite.addTest(tc_ID93115.Bug680315("test_bug680315"))
	suite.addTest(tc_ID93116.Bug681156("test_bug681156"))
	suite.addTest(tc_ID93125.Bug680064("test_bug680064"))
	suite.addTest(tc_ID93141.Bug705975("test_bug705975"))
	suite.addTest(tc_ID93647.Bug702393("test_bug702393"))

	return suite

if __name__ == "__main__":
   unittest.main(defaultTest = 'suite')
