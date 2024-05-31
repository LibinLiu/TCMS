import unittest, time, re
import os, sys, inspect
from optparse import OptionParser

filename=""
title=""
description=""
platform=""
datasuiteno=""

if len(sys.argv) != 6:
	print "Please provide 5 parameters by referring to the usage as below:"
	print """usage: --filename=<filename>  --title=<title> --description=<description>  --platform=<platform> --datasuiteno=<datasuiteno>"""
	print """For example: python TCMSP2TestHTMLRunner.py --filename="my_report.html" --title="My unit test" --description="This demonstrates the report output by HTMLTestRunner." --platform="englab" --datasuiteno="1" """

	sys.exit(1)
else:
	parser = OptionParser()
	parser.add_option("--filename", dest="filename", help="Test result file name")
	parser.add_option("--title", dest="title", help="Test result file title")
	parser.add_option("--description", dest="description", help="Test result file description")
	parser.add_option("--platform", dest="platform", help="Test platform name, it should be 'englab' or 'stage'")
	parser.add_option("--datasuiteno", dest="datasuiteno", help="Test data suite no., like '1', '2', etc.")

	(options, args) = parser.parse_args()

	if options.filename != None: filename=options.filename
	if options.title != None: title=options.title
	if options.description != None: description=options.description
	if options.platform != None: platform=options.platform
	if options.datasuiteno != None: datasuiteno=options.datasuiteno

if platform == "stage":
	import _data.stage.data1 as data1, _data.stage.data2 as data2, _data.stage.data3 as data3, _data.stage.data4 as data4, _data.stage.data5 as data5
elif platform == "englab":
	import _data.englab.data1 as data1, _data.englab.data2 as data2, _data.englab.data3 as data3, _data.englab.data4 as data4, _data.englab.data5 as data5

if datasuiteno == "1": dataSuite = data1
elif datasuiteno == "2": dataSuite = data2
elif datasuiteno == "3": dataSuite = data3
elif datasuiteno == "4": dataSuite = data4
elif datasuiteno == "5": dataSuite = data5


class env:
	'''Save all the global variant values, which are needed for testing, in this class.'''

	host = "localhost"
	port = 4444
	browser = "*chrome"
	if platform == "stage":
		domain = "https://tcms-stage.englab.bne.redhat.com/"
	elif platform == "englab":
		domain = "https://tcms.englab.nay.redhat.com/"
	
	user = "liliu"
	useremail = user+"@redhat.com"
	openurl = "/accounts/"+user+"/recent/"

	user2 = "xtian"
	useremail2 = user2+"@redhat.com"

	ts=10
	t=12
	tl=15


	#----------------------------------------------------------------------
	#------------------- (1) Basic Data Requirements ----------------------
	#----------------------------------------------------------------------

	product1 = "TCMS"
	prodversion11 = "1.0"
	prodversion12 = "2.0"
	build11 = "TCMS-3.0.3-1.svn2841"
	build12 = "TCMS 3.0.3-2.svn2859"
	plantype11 = "Function"
	plantype12 = "Acceptance"
	component11 = "TCMS"
	componentId11 = "57736"
	component12 = "Application"
	componentId12 = "57563"
	component13 = "Database"
	componentId13 = "57564"
	component14 = "Distribution"
	componentId14 = "57565"
	component15 = "Documentation"
	componentId15 = "57566"

	category11 = "Functional"
	category12 = "Regression"

	classification1 = "Red Hat Products"
	classification2 = "Fedora"

	product2 = "Red Hat Enterprise Linux 6"
	prodversion2 = "6.1"
	build2 = "RHEL6-6.1"
	category21 = "RHEL6"

	product3 = "test-product"

	product4 = "Bugzilla" #this product should be no any build exists;

	envgroup1 = "TCMS_Testing"
	envgpproperty11="TCMS_Testing"
	envgppropvalue111="Nitrate 3.1.1-3"
	envgppropvalue112="Nitrate 3.2-2"

	envgroup2 = "RHEL-Virt"
	envgpproperty21="Arch"
	envgppropvalue211="All"
	envgppropvalue212="i386"
	envgppropvalue213="i686"
	envgpproperty22="guest_arch"
	envgppropvalue221="i386"
	envgppropvalue222="x86_64"

	runproperty1 = "Arch"
	runpropvalue11 = "i386"
	runpropvalue12 = "i686"

	#----------------------------------------------------------------------
	#------------ (2) Test Plan/Case/Run Data Requirements ----------------
	#----------------------------------------------------------------------

	''' Requirements For Test Plan/Case/Run 1:
		#Test Plan requirement: sole name; no tag; 1 case; 1 run; name length > 6; Plan Product:TCMS; Product Version:1.0; Plan Type:Function; Active;
		#Test Case requirement: sole name; no tag; name length > 8; Product:TCMS; Category:Functional; Default test: user+"@redhat.com";Component: TCMS; Automated: Auto; Priority: P1
		#Test Run requirement: sole name; add only 1 case into run; name length > 8; Product:TCMS; Product Version:1.0; Manager: user+"@redhat.com"; Default test: user+"@redhat.com"; Status:Running
	'''

	###---(A)Test Plan/Case/Run 1
	testplanName = dataSuite.testplanName
	testplanId = dataSuite.testplanId

	testcaseName = dataSuite.testcaseName
	testcaseId = dataSuite.testcaseId

	testrunName = dataSuite.testrunName
	testrunId = dataSuite.testrunId
	testcaserunId = dataSuite.testcaserunId

	###---(B)Test Plan/Case/Run 2
	testplanName2 = dataSuite.testplanName2
	testplanId2 = dataSuite.testplanId2

	testcaseName2 = dataSuite.testcaseName2
	testcaseId2 = dataSuite.testcaseId2

	testrunName2 = dataSuite.testrunName2
	testrunId2 = dataSuite.testrunId2
	testcaserunId2 = dataSuite.testcaserunId2

	###---(C)Test Plan/Case/Run 3
	testplanName3 = dataSuite.testplanName3
	testplanId3 = dataSuite.testplanId3

	testcaseName3 = dataSuite.testcaseName3
	testcaseId3 = dataSuite.testcaseId3

	testrunName3 = dataSuite.testrunName3
	testrunId3 = dataSuite.testrunId3
	testcaserunId3 = dataSuite.testcaserunId3

	###---(D)Test Plan/Case/Run 4
	testplanName4 = dataSuite.testplanName4
	testplanId4 = dataSuite.testplanId4

	testcaseName41 = dataSuite.testcaseName41
	testcaseId41 = dataSuite.testcaseId41
	component41 = component12

	testcaseName42 = dataSuite.testcaseName42
	testcaseId42 = dataSuite.testcaseId42
	component42 = component13

	testrunName4 = dataSuite.testrunName4
	testrunId4 = dataSuite.testrunId4
	testcaserunId41 = dataSuite.testcaserunId41
	testcaserunId42 = dataSuite.testcaserunId42

	testrunName42 = dataSuite.testrunName42
	testrunId42 = dataSuite.testrunId42
	testcaserunId421 = dataSuite.testcaserunId421
	testcaserunId422 = dataSuite.testcaserunId422

	#----------------------------------------------------------------------
	#------------------ (3) Other Data Requirements -----------------------
	#----------------------------------------------------------------------

	longstring =   "wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwxwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwy"
	longURL = "http://baike.baidu.com/taglist?tag=%BF%D5%BC%E4%CE%BB%D6%C3++gis&tagfromview/wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwxwwwwwwwwwwwwww"

	bugno = "711657"
	bugurl = "https://bugzilla.redhat.com/show_bug.cgi?id="+bugno


