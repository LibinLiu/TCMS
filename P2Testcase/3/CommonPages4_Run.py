from selenium import selenium
import unittest, time, re

from env import *
import CommonElements

class CCommonPages(CommonElements.CCommonElements):


	# ========================================================================================================
	# 	Test Run related functions
	# ========================================================================================================


	#----------------------------------------------------------------------
	#-------------------- (1) Test Run 'Create' page ----------------------
	#----------------------------------------------------------------------

	def verifyCreateTestRunPageIsReady(self,myself,sel,prodversion="<default>",build="<default>",envGroup="<default>",\
		envGPPropOnoffs="<default>"):
		''' Verify create test run page is ready. '''

		time.sleep(env.t)
		sel.select_window("null")
		self.verifyTargetText(myself,sel,"Create New Test Run","css=h2")
		self.verifyElement(myself,sel,"//input[@type='submit' and @value='Save']")

		if prodversion!="<default>": self.verifySelectedLabel(myself,sel,prodversion,"product_version")
		if build!="<default>": self.verifySelectedLabel(myself,sel,build,"id_build")

		if envGroup!="<default>":
			self.verifyTargetText(myself,sel,"Environment Group: "+envGroup,"css=legend")

		#The 'envGPPropOnoffs' is a 'dict' type para
		if envGPPropOnoffs!="<default>":
			for tProp,tOnoff in envGPPropOnoffs.items():
				self.verifyText(myself,sel,tProp)
				for r in range(1,1000):
					if self.isTargetText(myself,sel,tProp,"//div[@id='content']/form/div[3]/table/tbody/tr[9]/td[2]/fieldset/ul/li["+str(r)+"]/label"):

						self.verifyCheckBox(myself,sel,tOnoff,"","",\
							fieldTarget="//div[@id='content']/form/div[3]/table/tbody/tr[9]/td[2]/fieldset/ul/li["+str(r)+"]/input")
						break

	def verifyCaseOrder(self,myself,sel,sortType,sortDataList):
		''' Verify the order of the test case in the create run page is correct. 
		    Note: the value of 'sortDataList' should be a list of data sorted as 'ascendent', an example here:

				dataList=[env.testcaseName41,env.testcaseName42]
				dataList.sort()
				CCommonUtils().verifyCaseOrder(self,sel,"By Test Case Summary",dataList)

		'''

		if sortType=="By Test Case Summary": tdcell="3"
		elif sortType=="By Author": tdcell="4"
		elif sortType=="By Created Date": tdcell="5"
		elif sortType=="By Category": tdcell="6"
		elif sortType=="By Priority": tdcell="7"
		elif sortType=="By Action": tdcell="8"

		datalength=len(sortDataList)

		#To check & get the start lint of all the cases in the table - due to hiden line exists in the table
		startline=1
		if not self.isElement(myself,sel,"//body/div[@id='testcases_selected']/table/tbody/tr["+str(startline)+"]/td["+tdcell+"]"):
			startline+=datalength

		#When cases are sorted as 'ascendent'
		if self.isElement(myself,sel,"//table[@id='testcases']/thead/tr/th[@class='sortcol sortasc']"):
			for r in range(datalength):
				self.verifyTargetText(myself,sel,sortDataList[r],"//body/div[@id='testcases_selected']/table/tbody/tr["+str(startline+r)+"]/td["+tdcell+"]")

		#When cases are sorted as 'descendent'
		elif self.isElement(myself,sel,"//table[@id='testcases']/thead/tr/th[@class='sortcol sortdesc']"):

			for r in range(datalength):
				self.verifyTargetText(myself,sel,sortDataList[datalength-1-r],"//body/div[@id='testcases_selected']/table/tbody/tr["+str(startline+r)+"]/td["+tdcell+"]")

	def fillDataForTestRun(self,myself,sel,summary="<default>",product="<default>",prodversion="<default>",\
		build="<default>",runmanager="<default>",defaulttester="<default>",estdays="<default>",\
		esthours="<default>",estmins="<default>",estsecs="<default>",notes="<default>",envGPPropOnoffs="<default>",\
		envGPPropValues="<default>",finished="<default>"):
		''' Fill the data for a new test run form with provided data. 
		    Note: this function is applicable for both create-run and edit-run, and the para 'finished' is just used for edit-run. '''

		#input summary of new test run
		if summary!="<default>": self.inputText(myself,sel,"id_summary", summary)

		#select product
		if product!="<default>": 
			if not self.isSelectedLabel(myself,sel,product,"id_product"):
				self.selectOptionInDropDownList(myself,sel,"id_product",product)

		#select product version
		if prodversion!="<default>": 
			if not self.isSelectedLabel(myself,sel,prodversion,"id_product_version"):
				self.selectOptionInDropDownList(myself,sel,"id_product_version",prodversion)

		#add Build
		if build!="<default>": 
			if not self.isSelectedLabel(myself,sel,build,"id_build"):
				self.selectOptionInDropDownList(myself,sel,"id_build",build)

		#add Run Manager
		if runmanager!="<default>": self.inputText(myself,sel,"id_manager", runmanager)

		#add Default Tester
		if defaulttester!="<default>": self.inputText(myself,sel,"id_default_tester", defaulttester)

		#add estimated days
		if estdays!="<default>": 
			if not estdays == sel.get_selected_label("//select[@name='estimated_time_days']"):
				self.selectOptionInDropDownList(myself,sel,"estimated_time_days",estdays)
		#add estimated hours
		if esthours!="<default>": 
			if not estdays == sel.get_selected_label("//select[@name='estimated_time_hours']"):
				self.selectOptionInDropDownList(myself,sel,"estimated_time_hours",esthours)
		#add estimated minutes
		if estmins!="<default>": 
			if not estdays == sel.get_selected_label("//select[@name='estimated_time_minutes']"):
				self.selectOptionInDropDownList(myself,sel,"estimated_time_minutes",estmins)
		#add estimated seconds
		if estsecs!="<default>": 
			if not estdays == sel.get_selected_label("//select[@name='estimated_time_seconds']"):
				self.selectOptionInDropDownList(myself,sel,"estimated_time_seconds",estsecs)

		#add notes
		if notes!="<default>": self.inputText(myself,sel,"id_notes", notes)

		#The 'envGPPropOnoffs' is a 'dict' type para: the key should be the property name and the value of should be: 'on' or 'off'
		if envGPPropOnoffs!="<default>":
			for tProp,tOnoff in envGPPropOnoffs.items():
				self.verifyText(myself,sel,tProp)
				for r in range(1,1000):
					if self.isTargetText(myself,sel,tProp,"//div[@id='content']/form/div[3]/table/tbody/tr[9]/td[2]/fieldset/ul/li["+str(r)+"]/label"):

						self.clickCheckBox(myself,sel,"","",fieldTarget="//div[@id='content']/form/div[3]/table/tbody/tr[9]/td[2]/fieldset/ul/li["+str(r)+"]/input",\
							onoff=tOnoff)
						break

		#The 'envGPPropValues' is a 'dict' type para: the key should be the property name and the value of should be: 'on' or 'off'
		if envGPPropValues!="<default>":
			for tProp,tValue in envGPPropValues.items():
				self.verifyText(myself,sel,tProp)
				for r in range(1,1000):
					if self.isTargetText(myself,sel,tProp,"//div[@id='content']/form/div[3]/table/tbody/tr[9]/td[2]/fieldset/ul/li["+str(r)+"]/label"):

						if not self.isSelectedLabel(myself,sel,tValue,"",fieldTarget="//div[@id='content']/form/div[3]/table/tbody/tr[9]/td[2]/fieldset/ul/li["+str(r)+"]/select"):
							self.selectOptionInDropDownList(myself,sel,"//div[@id='content']/form/div[3]/table/tbody/tr[9]/td[2]/fieldset/ul/li["+str(r)+"]/select",tValue)
						break

		#Note: The para 'finished' is just applicable to edit test run, an example to set this para: finished="on",or finished="off"
		if finished!="<default>":
			self.clickCheckBox(myself,sel,"id_finished","",onoff=finished)

	def clickActionInCreateRun(self,myself,sel,ActionName,ActionValue="<default>"):
		''' Click Action in new test run including button or link. '''

		if ActionName == "Save": self.clickBtnAndWait(myself,sel,"submit","Save")
		elif ActionName == "Cancel": self.clickBtnAndWait(myself,sel,"button","cancel")

		if ActionName == "Add Product Version":
			self.clickLink(myself,sel,"Add Product Version")
			sel.wait_for_pop_up("id_product_version", "30000")
			time.sleep(env.ts)

		elif ActionName == "Add Build":
			self.clickLink(myself,sel,"Add Build")
			sel.wait_for_pop_up("id_build", "30000")
			time.sleep(env.ts)

		if ActionName == "Test Plan Name": self.clickLinkAndWait(myself,sel,ActionValue)

		if ActionName == "Title Test Case Summary": self.clickAt(myself,sel,"//table[@id='testcases']/thead/tr/th[3]")
		elif ActionName == "Title Author": self.clickAt(myself,sel,"//table[@id='testcases']/thead/tr/th[4]")
		elif ActionName == "Title Created Date": self.clickAt(myself,sel,"//table[@id='testcases']/thead/tr/th[5]")
		elif ActionName == "Title Category": self.clickAt(myself,sel,"//table[@id='testcases']/thead/tr/th[6]")
		elif ActionName == "Title Priority": self.clickAt(myself,sel,"//table[@id='testcases']/thead/tr/th[7]")
		elif ActionName == "Title Action": self.clickAt(myself,sel,"//table[@id='testcases']/thead/tr/th[8]")

	def removeCaseInCreateRun(self,myself,sel,testcaseNameList):
		'''Remove Case In Create Run form. '''

		for tName in testcaseNameList:
			for r in range(1,1000):
				if self.isTargetText(myself,sel,tName,"link_"+str(r)):

					#click 'remove' link to remove the test case
					self.clickElement(myself,sel,"//tr[@id='row_"+str(r)+"']/td[8]/a")

					self.verifyLinkNotPresent(myself,sel,tName)
					break

	def verifyErrWarningMsgInCreateTestRun(self,myself,sel,errType,wrongUser=""):
		''' Verify the error warning message when create test run. '''

		if errType == "Blank Summary":
			self.verifyTargetText(myself,sel,"This field is required.","css=ul.errorlist > li")
		elif errType == "Blank Build":
			self.verifyTargetText(myself,sel,"buildThis field is required.","css=ul.errorlist > li")
		elif errType == "Other Build":
			self.verifyTargetText(myself,sel,"Select a valid choice. That choice is not one of the available choices.","css=ul.errorlist > li")
		elif errType == "Blank Run Manager":
			self.verifyTargetText(myself,sel,"A user name is required.","css=ul.errorlist > li")
		elif errType == "Invalid Run Manager":
			self.verifyTargetText(myself,sel,"Unknown user: \""+wrongUser+"\"","css=ul.errorlist > li")
		elif errType == "Invalid Default Tester":
			self.verifyTargetText(myself,sel,"Unknown user: \""+wrongUser+"\"","css=ul.errorlist > li")


	#---------------------------------------------------------------------
	#-------------------- (2) Test Run 'Edit' page -----------------------
	#---------------------------------------------------------------------

	def verifyEditTestRunPageIsReady(self,myself,sel,testrunName,summary="<default>",product="<default>",prodversion="<default>",\
		build="<default>",runmanager="<default>",defaulttester="<default>",estdays="<default>",\
		esthours="<default>",estmins="<default>",estsecs="<default>",notes="<default>",finished="<default>"):
		''' Verify edit test run page is ready. '''

		time.sleep(env.t) #Wait some more time to make sure all elements in page have been loaded
		self.verifyPageTitle(myself,sel,testrunName)
		self.verifyTargetText(myself,sel,"Edit Test Run","css=h2")
		self.verifyElement(myself,sel,"//input[@value='Save']")
		self.verifyElement(myself,sel,"//input[@value='Reset']")
		self.verifyElement(myself,sel,"//input[@value='Back']")

		if summary!="<default>": self.verifyValue(myself,sel,summary,"id_summary")
		if product!="<default>": self.verifySelectedLabel(myself,sel,product,"product")
		if prodversion!="<default>": self.verifySelectedLabel(myself,sel,prodversion,"product_version")
		if build!="<default>": self.verifySelectedLabel(myself,sel,build,"id_build")
		if runmanager!="<default>": self.verifyValue(myself,sel,runmanager,"id_manager")
		if defaulttester!="<default>": self.verifyValue(myself,sel,defaulttester,"id_default_tester")

		#verify estimated days
		if estdays!="<default>": self.verifySelectedLabel(myself,sel,estdays,"estimated_time_days")
		#verify estimated hours
		if esthours!="<default>": self.verifySelectedLabel(myself,sel,esthours,"estimated_time_hours")
		#verify estimated minutes
		if estmins!="<default>": self.verifySelectedLabel(myself,sel,estmins,"estimated_time_minutes")
		#verify estimated seconds
		if estsecs!="<default>": self.verifySelectedLabel(myself,sel,estsecs,"estimated_time_seconds")

		if notes!="<default>": self.verifyValue(myself,sel,notes,"id_notes")

		if finished!="<default>": self.verifyCheckBox(myself,sel,finished,"id_finished","")

	def isEditTestRunPageOpen(self,myself,sel,testrunName):
		''' Verify if the current page is test run page in edit status. '''

		t1 = self.isPageTitle(myself,sel, testrunName)
		t2 = self.isTargetText(myself,sel,"Edit Test Run","css=h2")
		t3 = self.isElement(myself,sel,"//input[@value='Save']")

		if t1 and t2 and t3: return True
		else: return False

	def editTestRun(self,myself,sel,testrunName,summary="<default>",product="<default>",prodversion="<default>",\
		build="<default>",runmanager="<default>",defaulttester="<default>",estdays="<default>",\
		esthours="<default>",estmins="<default>",estsecs="<default>",notes="<default>",finished="<default>"):
		''' Edit a test run from an opened test run. '''

		self.clickActionInRun(myself,sel,"Edit")
		self.verifyEditTestRunPageIsReady(myself,sel,testrunName)

		#Fill the data for the edit test run with provided data.
		self.fillDataForTestRun(myself,sel,summary,product,prodversion,build,runmanager,\
		defaulttester,estdays,esthours,estmins,estsecs,notes,finished)

		self.clickActionInEditRun(myself,sel,"Save")

		#Verify if test run is saved as expected
		if self.isEditTestRunPageOpen(myself,sel,testrunName):
			self.verifyEditTestRunPageIsReady(myself,sel,testrunName)
		else: 
			if summary=="<default>":
				self.verifyTestRunPageIsReady(myself,sel,testrunName,summary,product,prodversion,build,runmanager,\
				defaulttester,estdays,esthours,estmins,estsecs,notes,finished)
			else:
				self.verifyTestRunPageIsReady(myself,sel,summary,summary,product,prodversion,build,runmanager,\
				defaulttester,estdays,esthours,estmins,estsecs,notes,finished)

	def clickActionInEditRun(self,myself,sel,ActionName):
		''' Click Action in a edit test run including button or link. '''

		if ActionName == "Save": self.clickBtnAndWait(myself,sel,"submit","Save")
		elif ActionName == "Reset": self.clickBtn(myself,sel,"reset","Reset")
		elif ActionName == "Back": self.clickBtnAndWait(myself,sel,"button","Back")

	def verifyErrWarningMsgInEditTestRun(self,myself,sel,errType,wrongUser=""):
		''' Verify the error warning message when edit test run. '''

		if errType == "Blank Summary":
			self.verifyTargetText(myself,sel,"This field is required.","css=ul.errorlist > li")
			self.verifyTargetText(myself,sel,"summaryThis field is required.","css=#errors > ul.errorlist > li")
		elif errType == "Blank Build":
			self.verifyTargetText(myself,sel,"buildThis field is required.","css=ul.errorlist > li")
		elif errType == "Other Build":
			self.verifyTargetText(myself,sel,"Select a valid choice. That choice is not one of the available choices.","css=ul.errorlist > li")
		elif errType == "Invalid Run Manager":
			self.verifyTargetText(myself,sel,"Unknown user: \""+wrongUser+"\"","css=ul.errorlist > li")
			self.verifyTargetText(myself,sel,"managerUnknown user: \""+wrongUser+"\"","css=#errors > ul.errorlist > li")
		elif errType == "Invalid Default Tester":
			self.verifyTargetText(myself,sel,"Unknown user: \""+wrongUser+"\"","css=ul.errorlist > li")
			self.verifyTargetText(myself,sel,"default_testerUnknown user: \""+wrongUser+"\"","css=#errors > ul.errorlist > li")


	#--------------------------------------------------------------------
	#-------------------- (3) Test Run 'Read' page ----------------------
	#--------------------------------------------------------------------

	def verifyTestRunPageIsReady(self,myself,sel,testrunName,summary="<default>",product="<default>",prodversion="<default>",\
		build="<default>",runmanager="<default>",defaulttester="<default>",estdays="<default>",\
		esthours="<default>",estmins="<default>",estsecs="<default>",envGPPropOnoffs="<default>",envGPPropValues="<default>",\
		notes="<default>",finished="<default>",caseNum="<default>",\
		testcaseIds="<default>",notestcaseIds="<default>",cclist="<default>",nocclist="<default>",\
		testcaseNameTesters="<default>",testcaseNameAssignees="<default>",testcaseNameStatuses="<default>"):
		''' Verify test run page is ready. 

		    An example of the value of testcaseIds: [testcaseId1,testcaseId2]
		    An example of the value of cclist: 	    [env.useremail,env.useremail2]
		'''

		time.sleep(env.t) #Wait some more time to make sure all elements in page have been loaded
		self.verifyPageTitle(myself,sel,testrunName)
		self.verifyTargetText(myself,sel,testrunName,"display_title")

		if summary!="<default>": self.verifyTargetText(myself,sel,summary,"display_title")
		if product!="<default>": self.verifyLink(myself,sel,product)
		if prodversion!="<default>": self.verifyLink(myself,sel,prodversion)
		if build!="<default>": self.verifyLink(myself,sel,build)
		if runmanager!="<default>": self.verifyTargetText(myself,sel,runmanager,"//div[@id='content']/div[4]/div/div[2]/div[3]/div[2]/a")
		if defaulttester!="<default>": 
			if defaulttester == "": defaulttester="None"
			self.verifyTargetText(myself,sel,defaulttester,"//div[@id='content']/div[4]/div/div[3]/div[3]/div[2]")

		#verify estimated days
		if estdays!="<default>": 
			if estdays == "0": checkesttime = ""
			else: checkesttime = estdays + " day,"
			self.verifyText(myself,sel,checkesttime)

		#verify estimated hours
		if esthours!="<default>": 
			checkesttime = esthours+":"
			self.verifyText(myself,sel,checkesttime)

		#verify estimated minutes
		if estmins!="<default>": 
			if int(estmins) < 10: checkesttime = ":0"+estmins+":"
			elif int(estmins) > 10: checkesttime = ":"+estmins+":"
			self.verifyText(myself,sel,checkesttime)

		#verify estimated seconds
		if estsecs!="<default>": 
			if int(estsecs) < 10: checkesttime = ":0"+estsecs
			elif int(estsecs) > 10: checkesttime = ":"+estsecs
			self.verifyText(myself,sel,checkesttime)

		#The 'envGPPropOnoffs' is a 'dict' type para
		if envGPPropOnoffs!="<default>":
			for tProp,tOnoff in envGPPropOnoffs.items():
				if tOnoff=='on':
					self.verifyText(myself,sel,tProp+": ")
				elif tOnoff=='off':
					self.verifyTextNotPresent(myself,sel,tProp+": ")

		#The 'envGPPropValues' is a 'dict' type para: the key should be the property name and the value of should be: 'on' or 'off'
		if envGPPropValues!="<default>":
			for tProp,tValue in envGPPropValues.items():
				if envGPPropOnoffs!="<default>":
					for tOnoffProp in envGPPropOnoffs.keys():
						if tOnoffProp==tProp:
							self.verifyText(myself,sel,tProp+": ")
							self.verifyText(myself,sel,": "+tValue)
							break
					else:
						self.verifyTextNotPresent(myself,sel,tProp+": ")
						self.verifyTextNotPresent(myself,sel,": "+tValue)

				else:
					self.verifyText(myself,sel,tProp+": ")
					self.verifyText(myself,sel,": "+tValue)

		if notes!="<default>": self.verifyTargetText(myself,sel,notes,"//div[@id='content']/div[5]/div[2]")

		if finished!="<default>": 
			if finished == "on": self.verifyTargetText(myself,sel,"Finished","css=span.pauselink")
			elif finished == "off":
				self.verifyElementNotPresent(myself,sel,"css=span.pauselink")
				self.verifyTargetText(myself,sel,"Running","css=span.runninglink")

		if caseNum!="<default>": self.verifyTargetText(myself,sel,"Cases: "+caseNum,"css=span.tit")

		if testcaseIds!="<default>":
			for i in range(len(testcaseIds)): 
				self.verifyLink(myself,sel,testcaseIds[i])

		if notestcaseIds!="<default>":
			for i in range(len(notestcaseIds)): 
				self.verifyLinkNotPresent(myself,sel,notestcaseIds[i])

		if cclist!="<default>":
			for i in range(len(cclist)): 
				self.verifyElement(myself,sel,"//a[contains(@href, 'mailto:"+cclist[i]+"')]")

		if nocclist!="<default>":
			for i in range(len(nocclist)): 
				self.verifyElementNotPresent(myself,sel,"//a[contains(@href, 'mailto:"+nocclist[i]+"')]")

		if testcaseNameTesters!="<default>":
			for tName,tTester in testcaseNameTesters.items():
				self.verifyCaseRunTester(myself,sel,tName,tTester)

		if testcaseNameAssignees!="<default>":
			for tName,tAsgne in testcaseNameAssignees.items():
				self.verifyCaseRunAssignee(myself,sel,tName,tAsgne)

		if testcaseNameStatuses!="<default>":
			for tName,tStatus in testcaseNameStatuses.items():
				self.verifyCaseRunStatus(myself,sel,tName,tStatus)

	def isTestRunPageOpen(self,myself,sel,testrunName):
		''' Verify if the current page is test run page. '''

		t1 = self.isPageTitle(myself,sel, testrunName)
		t2 = self.isTargetText(myself,sel,testrunName,"display_title")
		t3 = self.isText(myself,sel,"Case Run ID")

		if t1 and t2 and t3: return True
		else: return False

	def verifyReportInfoInRun(self,myself,sel,IDLE="<default>",RUNNING="<default>",PAUSED="<default>",PASSED="<default>",FAILED="<default>",\
				BLOCKED="<default>",ERROR="<default>",WAIVED="<default>",TOTAL="<default>",bugNum="<default>"):
		''' verify report info in run for test case run. '''

		#Verify the link of 'Show All Bugs'
		if bugNum!="<default>": 
			if bugNum!="" and int(bugNum)>0: 
				self.verifyLink(myself,sel,"Show All Bugs ["+bugNum+"]")
			else: 
				self.verifyElementNotPresent(myself,sel,"css=a[title=Show ALl Bugs]")
				self.verifyTargetText(myself,sel,"Show All Bugs [0]","css=div.statu > ul:nth(1) > li:nth(1)")

		#Verify if the status of the case run is correct
		if IDLE!="<default>": self.verifyTargetText(myself,sel,IDLE,"//a[@onclick=\"showCaseRunsWithSelectedStatus($('id_filter'), '1')\"]")
		if PASSED!="<default>": self.verifyTargetText(myself,sel,PASSED,"//a[@onclick=\"showCaseRunsWithSelectedStatus($('id_filter'), '2')\"]")
		if FAILED!="<default>": self.verifyTargetText(myself,sel,FAILED,"//a[@onclick=\"showCaseRunsWithSelectedStatus($('id_filter'), '3')\"]")
		if RUNNING!="<default>": self.verifyTargetText(myself,sel,RUNNING,"//a[@onclick=\"showCaseRunsWithSelectedStatus($('id_filter'), '4')\"]")
		if PAUSED!="<default>": self.verifyTargetText(myself,sel,PAUSED,"//a[@onclick=\"showCaseRunsWithSelectedStatus($('id_filter'), '5')\"]")
		if BLOCKED!="<default>": self.verifyTargetText(myself,sel,BLOCKED,"//a[@onclick=\"showCaseRunsWithSelectedStatus($('id_filter'), '6')\"]")
		if ERROR!="<default>": self.verifyTargetText(myself,sel,ERROR,"//a[@onclick=\"showCaseRunsWithSelectedStatus($('id_filter'), '7')\"]")
		if WAIVED!="<default>": self.verifyTargetText(myself,sel,WAIVED,"//a[@onclick=\"showCaseRunsWithSelectedStatus($('id_filter'), '8')\"]")
		if TOTAL!="<default>": self.verifyTargetText(myself,sel,TOTAL,"//a[@onclick=\"showCaseRunsWithSelectedStatus($('id_filter'), '')\"]")
		
	def verifyCaseRunTester(self,myself,sel,testcaseName,tester):
		''' Check Tester for test case run. '''

		self.verifyLink(myself,sel,testcaseName)

		for r in range(1,1000):
			if self.isTargetText(myself,sel,testcaseName,"link_"+str(r)):
				self.verifyElement(myself,sel,"//table[@id='id_table_cases']/tbody/tr["+str(r)+"]/td[6]/a[@href='/accounts/"+tester+"/profile/']")
				break

	def verifyCaseRunAssignee(self,myself,sel,testcaseName,assignee):
		''' Check Assignee for test case run. '''

		self.verifyLink(myself,sel,testcaseName)

		for r in range(1,1000):
			if self.isTargetText(myself,sel,testcaseName,"link_"+str(r)):
				self.verifyElement(myself,sel,"//table[@id='id_table_cases']/tbody/tr["+str(r)+"]/td[7]/a[@href='/accounts/"+assignee+"/profile/']")
				break

	def verifyCaseRunStatus(self,myself,sel,testcaseName,status):
		''' Check status for test case run. '''

		if status == "IDLE": statusiconClass="icon_status btn_idle"
		elif status == "RUNNING": statusiconClass="icon_status btn_running"
		elif status == "PAUSED": statusiconClass="icon_status btn_paused"
		elif status == "PASSED": statusiconClass="icon_status btn_passed"
		elif status == "FAILED": statusiconClass="icon_status btn_failed"
		elif status == "BLOCKED": statusiconClass="icon_status btn_blocked"
		elif status == "ERROR": statusiconClass="icon_status btn_error"
		elif status == "WAIVED": statusiconClass="icon_status btn_waived"
		
		self.verifyLink(myself,sel,testcaseName)

		#Verify if the status of the case run is correct
		for r in range(1,1000):
			if self.isTargetText(myself,sel,testcaseName,"link_"+str(r)):
				if r==1:self.verifyElement(myself,sel,"//table[@id='id_table_cases']/tbody/tr["+str(r)+"]/td[11]/img[@class='"+statusiconClass+"']")
				else: self.verifyElement(myself,sel,"//table[@id='id_table_cases']/tbody/tr["+str(r+1)+"]/td[11]/img[@class='"+statusiconClass+"']")
				break

	def clickActionInRun(self,myself,sel,ActionName):
		''' Click Action in a test run including button or link. '''

		if ActionName == "Edit": self.clickBtnAndWait(myself,sel,"button","Edit")
		elif ActionName == "Clone": self.clickBtnAndWait(myself,sel,"button","Clone")
		elif ActionName == "Delete": self.clickBtnAndWait(myself,sel,"button","Delete")
		elif ActionName == "Export": self.clickBtnAndWait(myself,sel,"button","Export")

		if ActionName == "Set to Finished": self.clickElement(myself,sel,"//input[@value='Set to Finished']")
		elif ActionName == "Set to Running": self.clickElement(myself,sel,"//input[@value='Set to Running']")

		if ActionName == "EnableAutomatically": self.clickCheckBox(myself,sel,"id_check_box_auto_blinddown","",onoff="on")
		elif ActionName == "DisableAutomatically": self.clickCheckBox(myself,sel,"id_check_box_auto_blinddown","",onoff="off")

		if ActionName == "EnableHighlight": self.clickCheckBox(myself,sel,"id_check_box_highlight","",onoff="on")
		elif ActionName == "DisableHighlight": self.clickCheckBox(myself,sel,"id_check_box_highlight","",onoff="off")

		if ActionName == "Report": self.clickLink(myself,sel,"Report")
		elif ActionName == "Show All Bugs": self.clickElement(myself,sel,"css=a[title=Show ALl Bugs]")

		if ActionName == "Show filter options": self.clickElement(myself,sel,"//a[contains(text(),'Show filter options')]")
		elif ActionName == "Hide filter options": self.clickElement(myself,sel,"//a[contains(text(),'Hide filter options')]")

		if ActionName == "Search": self.clickBtnAndWait(myself,sel,"submit","Search")
		elif ActionName == "Reset": self.clickBtn(myself,sel,"reset","Reset")

	def selectCaseInRun(self,myself,sel,testcaserunIds):
		''' Select a test case in test run.
		    Especially, if testcaserunIds == 'all', it means to select all test case runs, if testcaserunIds == '', it means select no any test case run. '''

		if testcaserunIds == "All":
			self.clickCheckBox(myself,sel,"id_check_all_button","",onoff="off")
			self.clickCheckBox(myself,sel,"id_check_all_button","",onoff="on")
		else:
			self.clickCheckBox(myself,sel,"id_check_all_button","",onoff="on")
			self.clickCheckBox(myself,sel,"id_check_all_button","",onoff="off")
			if testcaserunIds != "":
				for i in range(len(testcaserunIds)):
					self.clickCheckBox(myself,sel,"case_run",testcaserunIds[i],onoff="on")

	def expandCaseInRun(self,myself,sel,testcaseName,testcaserunId=""):
		''' Expand or collapse a test case in test run. In particular, if testcaseName=="All", will expand or collapse all test cases.'''

		if testcaseName=="All":
			self.clickElement(myself,sel,"//img[@id='id_blind_all_img']")
			time.sleep(env.t)
		else:
			if testcaserunId=="":
				self.clickElement(myself,sel,"//a[contains(text(),'"+testcaseName+"')]")
				time.sleep(env.t)
			else: 
				self.clickElement(myself,sel,"//a[contains(text(),'#"+testcaserunId+"')]")
				time.sleep(env.t)


	### ----------------------------------------- Begin of 'Action in Run' Part ----------------------------------------- ###

	def addTagInRun(self,myself,sel,tagName,needRemove=True):
		''' Add a tag in test run '''

	        sel.answer_on_next_prompt(tagName)
		self.clickLink(myself,sel,"Add Tag")
		myself.assertEqual("Please type new tag.", sel.get_prompt())
		time.sleep(env.ts)
		self.verifyText(myself,sel,tagName)

		if needRemove:
			self.clickElement(myself,sel,"css=img[title=remove this tag]")
			self.verifyTextNotPresent(myself,sel,tagName)
			self.verifyElementNotPresent(myself,sel,"css=img[title=remove this tag]")

	def removeTagInRun(self,myself,sel,tagName):
		''' Remove a tag in test run '''

		self.verifyText(myself,sel,tagName)
		self.clickElement(myself,sel,"css=img[title=remove this tag]")

		self.verifyTextNotPresent(myself,sel,tagName)
		self.verifyElementNotPresent(myself,sel,"css=img[title=remove this tag]")

	def addPropertyInRun(self,myself,sel,propertyName,propertyValue,AddOrCancel="Add",needRemove=True):
		''' Add one property in test run. 

		    AddOrCancel's value involves:'Add','Cancel'; needRemove's value involves: True,False '''

		self.clickLink(myself,sel,"Add Property")
		self.selectOptionInDropDownList(myself,sel,"id_add_env_property",propertyName)
		self.selectOptionInDropDownList(myself,sel,"id_add_env_value",propertyValue)
		self.clickBtn(myself,sel,"button",AddOrCancel)
		time.sleep(env.ts)

		if AddOrCancel == "Add":
			self.verifyText(myself,sel,propertyName)
			self.verifyText(myself,sel,propertyValue)

			if needRemove:
				self.removePropertyInRun(myself,sel,propertyName,propertyValue)
	
		elif AddOrCancel == "Cancel":
			self.verifyTextNotPresent(myself,sel,propertyName)
			self.verifyTextNotPresent(myself,sel,propertyValue)

	def editPropertyInRun(self,myself,sel,propertyName,propertyOldValue,propertyNewValue,needRemove=True):
		''' Edit one property in test run. 

		    If need/no need to remove the property, set needRemove's value involving: True,False '''

		self.clickElement(myself,sel,"css=img[title=Edit this value]")
		self.selectOptionInDropDownList(myself,sel,"id_select_value_43",propertyNewValue)
		self.clickBtn(myself,sel,"button","Submit")
		self.verifyText(myself,sel,propertyName)
		self.verifyText(myself,sel,propertyNewValue)
		self.verifyTextNotPresent(myself,sel,propertyOldValue)

		if needRemove:
			self.removePropertyInRun(myself,sel,propertyName,propertyNewValue)

	def removePropertyInRun(self,myself,sel,propertyName,propertyValue):
		''' Remove one property in test run. '''

		self.clickElement(myself,sel,"css=img[title=Remove this property]")
		myself.failUnless(re.search(r"^Are you sure to remove this porperty[\s\S]$", sel.get_confirmation()))
		time.sleep(env.ts)
		self.verifyTextNotPresent(myself,sel,propertyName)
		self.verifyTextNotPresent(myself,sel,propertyValue)
		self.verifyElementNotPresent(myself,sel,"css=img[title=Remove this property]")
	
	def setStatusToFinishedOrRunningInRun(self,myself,sel,actionName):
		''' Set Status To Finished Or Running in test run '''

		self.clickActionInRun(myself,sel,actionName)
		if actionName == "Set to Finished":
			self.verifyTargetText(myself,sel,"Finished","css=span.pauselink")
		elif actionName == "Set to Running":
			self.verifyTargetText(myself,sel,"Running","css=span.runninglink")

	def addCCInRun(self,myself,sel,validUserEmail="",invalidUserEmail="",needRemove=True):
		''' Add a valid or invalid CC user in test run and then check the result, and if needed - that is, needRemove=True, will remove it. '''

		if validUserEmail!="":
			sel.answer_on_next_prompt(validUserEmail)
			self.clickLink(myself,sel,"Add CC")
			myself.assertEqual("Please type new email or username for CC.", sel.get_prompt())
			time.sleep(env.ts)
			self.verifyElement(myself,sel,"//a[contains(@href, 'mailto:"+validUserEmail+"')]")

			if needRemove:
				self.clickElement(myself,sel,"css=img[title=remove this tag]")
				myself.failUnless(re.search(r"^Are you sure to delete this user from CC[\s\S]$", sel.get_confirmation()))
				time.sleep(env.ts)
				self.verifyElementNotPresent(myself,sel,"//a[contains(@href, 'mailto:"+validUserEmail+"')]")
				self.verifyElementNotPresent(myself,sel,"css=img[title=remove this tag]")

		if invalidUserEmail!="":
			sel.answer_on_next_prompt(invalidUserEmail)
			self.clickLink(myself,sel,"Add CC")
			myself.assertEqual("Please type new email or username for CC.", sel.get_prompt())
			myself.assertEqual("The user you typed does not exist in database", sel.get_alert())
			self.verifyElementNotPresent(myself,sel,"//a[contains(@href, 'mailto:"+invalidUserEmail+"')]")

	def editCaseRunSortNumInRun(self,myself,sel,testrunId,testcaserunId,oldSortNum,newSortNum):
		''' Edit sort number of case run in test run. ''' 

		sel.answer_on_next_prompt(newSortNum)
		self.clickElement(myself,sel,"//a[@onclick=\"changeCaseRunOrder('"+testrunId+"', '"+testcaserunId+"', '"+oldSortNum+"')\"]")
		myself.assertEqual("Enter your new order number", sel.get_prompt())
		time.sleep(env.ts)

	def verifyFilterItemDataInRun(self,myself,sel,summary="<default>",defaulttester="<default>",assignee="<default>",\
				bugno="<default>",status="<default>",priority="<default>"):
		''' Verify Filter Item Data In Run. '''

		time.sleep(env.ts)
		if summary!="<default>": self.verifyValue(myself,sel,summary,"id_summary")
		if defaulttester!="<default>": self.verifyValue(myself,sel,defaulttester,"id_default_tester")
		if assignee!="<default>": self.verifyValue(myself,sel,assignee,"id_assignee")
		if bugno!="<default>": self.verifyValue(myself,sel,bugno,"id_bug")
		if status!="<default>": self.verifySelectedLabel(myself,sel,status,"case_run_status__pk")
		if priority!="<default>": self.verifySelectedLabel(myself,sel,priority,"case__priority__pk")

	def fillDataForFilterItemInRun(self,myself,sel,summary="<default>",defaulttester="<default>",assignee="<default>",\
				bugno="<default>",status="<default>",priority="<default>"):

		''' Fill the data for filter items in run with provided data. '''

		#input summary of new test run
		if summary!="<default>": self.inputText(myself,sel,"id_summary", summary)

		#add Default Tester
		if defaulttester!="<default>": self.inputText(myself,sel,"id_default_tester", defaulttester)

		#add assignee
		if assignee!="<default>": self.inputText(myself,sel,"id_assignee", assignee)

		#add bug
		if bugno!="<default>": self.inputText(myself,sel,"id_bug", bugno)

		#select status
		if status!="<default>": 
			if not self.isSelectedLabel(myself,sel,status,'case_run_status__pk'):
				self.selectOptionInDropDownList(myself,sel,"case_run_status__pk",status)

		#select priority
		if priority!="<default>": 
			if not self.isSelectedLabel(myself,sel,priority,'case__priority__pk'):
				self.selectOptionInDropDownList(myself,sel,"case__priority__pk",priority)

	def filterCaseInRun(self,myself,sel,summary="<default>",defaulttester="<default>",assignee="<default>",\
		bugno="<default>",status="<default>",priority="<default>",testcaseResultIdNames="<default>",\
		testcaseResultNoIdNames="<default>"):
		'''Filter test cases with right options in test run.  'testcaseResultIdNames' is a 'dict' type para. '''

		self.clickActionInRun(myself,sel,"Show filter options")

		self.fillDataForFilterItemInRun(myself,sel,summary,defaulttester,assignee,bugno,status,priority)

		#Click the "Search" button
		self.clickActionInRun(myself,sel,"Search")

		if testcaseResultIdNames!="<default>":
			if testcaseResultIdNames!="":
				for tId,tName in testcaseResultIdNames.items():
					self.verifyLink(myself,sel,tId)
					self.verifyLink(myself,sel,tName)
			else:
				#if testcaseResultIdNames=="", it indicates there should be no test case run searched out
				self.verifyTargetText(myself,sel,"No case run found","css=td")

		if testcaseResultNoIdNames!="<default>":
			if testcaseResultNoIdNames!="":
				for tId,tName in testcaseResultNoIdNames.items():
					self.verifyLinkNotPresent(myself,sel,tId)
					self.verifyLinkNotPresent(myself,sel,tName)


	### ----------------------------------------- Begin of 'Cases' Label Part ----------------------------------------- ###

	def selectCaseAction(self,myself,sel,action,removecaseNum=""):
		''' Select action from Cases dropdown list. 
		    The para 'removecaseNum' is simply used for the action 'Remove', 
		    its value, whose format is like:'1','2','10', indicates how many test cases will be removed from run. '''

		self.verifyTargetText(myself,sel,"Cases Add Remove Re-order Update Assignee","//form[@id='id_form_case_runs']/div/div[2]/div")
		self.verifyElement(myself,sel,"//form[@id='id_form_case_runs']/div/div[2]/div/span")
		sel.mouse_over("//form[@id='id_form_case_runs']/div/div[2]/div/span")
		time.sleep(env.ts)

		self.clickLink(myself,sel,action)
		time.sleep(env.t)
		
		if action == "Remove" and removecaseNum!="":
			myself.failUnless(re.search(r"^You are about to delete "+removecaseNum+" case run\(s\)\. Are you sure[\s\S]$", sel.get_confirmation()))
			time.sleep(env.t)


	### ----------------------------------------- Begin of 'Status' Label Part ----------------------------------------- ###

	def alterCaseRunStatus(self,myself,sel,status,selectedCase=True):
		''' Alter status for test case run.

			Note: 'selectedCase=True' indicates there is at least one case selected;
			      'selectedCase=False' indicates there is no case selected.
		'''

		self.verifyTargetText(myself,sel,"Status IDLE PASSED FAILED RUNNING PAUSED BLOCKED ERROR WAIVED","//form[@id='id_form_case_runs']/div/div[2]/div[2]")
		self.verifyElement(myself,sel,"//form[@id='id_form_case_runs']/div/div[2]/div[2]/span")
		sel.mouse_over("//form[@id='id_form_case_runs']/div/div[2]/div[2]/span")

		#Note: the value of 'status' involves: 'IDLE', 'PASSED', 'FAILED', 'RUNNING', 'PAUSED', 'BLOCKED', 'ERROR', 'WAIVED
		self.clickLink(myself,sel,status)
		time.sleep(env.t)

		if selectedCase:
			myself.failUnless(re.search(r"^Are you sure you want to change the status[\s\S]$", sel.get_confirmation()))
			time.sleep(env.t)
		else: myself.assertEqual("No cases selected! Please select at least one case.", sel.get_alert())

	def alterCaseRunStatusByIcon(self,myself,sel,testcaseName,status):
		''' Alter status for test case run by clicking icon in case run. '''

		if status == "IDLE": self.clickElement(myself,sel,"//input[@type='submit' and @title='IDLE']")
		elif status == "RUNNING": self.clickElement(myself,sel,"//input[@type='submit' and @title='RUNNING']")
		elif status == "PAUSED": self.clickElement(myself,sel,"//input[@type='submit' and @title='PAUSED']")
		elif status == "PASSED": self.clickElement(myself,sel,"//input[@type='submit' and @title='PASSED']")
		elif status == "FAILED": self.clickElement(myself,sel,"//input[@type='submit' and @title='FAILED']")
		elif status == "BLOCKED": self.clickElement(myself,sel,"//input[@type='submit' and @title='BLOCKED']")
		elif status == "ERROR": self.clickElement(myself,sel,"//input[@type='submit' and @title='ERROR']")
		elif status == "WAIVED": self.clickElement(myself,sel,"//input[@type='submit' and @title='WAIVED']")

		time.sleep(env.t)


	### ----------------------------------------- Begin of 'Bugs' Label Part ----------------------------------------- ###

	def clickAddBug(self,myself,sel,bugNo,bugNoIsValid=True,selectedCase=True):
		''' Add bug for test case run. '''

		self.verifyElement(myself,sel,"//form[@id='id_form_case_runs']/div/div[2]/div[3]/span")
		sel.mouse_move("//form[@id='id_form_case_runs']/div/div[2]/div[3]/span")
		
		sel.answer_on_next_prompt(bugNo)
		self.clickElement(myself,sel,'''//a[@onclick="updateBugs('add')"]''')
		myself.assertEqual("Specify bug IDs, using comma to seperate multiple IDs.", sel.get_prompt())
		time.sleep(env.ts)

		if not bugNoIsValid:
			try: myself.assertEqual("Please specify only integers for bugs, caseruns(using comma to seperate IDs),                "+\
				"and bug_system. (DEBUG INFO: invalid literal for int(): "+bugNo+")", sel.get_alert())
			except AssertionError, e: myself.verificationErrors.append(str(e))

		#Bug exists, when bug got fixed, below code will need to be repaired accordingly.
		elif not selectedCase:
			try: myself.assertEqual("Please specify only integers for bugs, caseruns(using comma to seperate IDs),                "+\
				"and bug_system. (DEBUG INFO: invalid literal for int(): )", sel.get_alert())
			except AssertionError, e: myself.verificationErrors.append(str(e))

	def clickRemoveBug(self,myself,sel,bugNo,bugNoIsValid=True,selectedCase=True):
		''' Add bug for test case run. '''

		self.verifyElement(myself,sel,"//form[@id='id_form_case_runs']/div/div[2]/div[3]/span")
		sel.mouse_move("//form[@id='id_form_case_runs']/div/div[2]/div[3]/span")
		
		sel.answer_on_next_prompt(bugNo)
		self.clickElement(myself,sel,'''//a[@onclick="updateBugs('remove')"]''')
		myself.assertEqual("Specify bug IDs, using comma to seperate multiple IDs.", sel.get_prompt())
		time.sleep(env.ts)

		if not bugNoIsValid:
			try: myself.assertEqual("Please specify only integers for bugs, caseruns(using comma to seperate IDs),                "+\
				"and bug_system. (DEBUG INFO: invalid literal for int(): "+bugNo+")", sel.get_alert())
			except AssertionError, e: myself.verificationErrors.append(str(e))

		#Bug exists, when bug got fixed, below code will need to be repaired accordingly.
		elif not selectedCase:
			try: myself.assertEqual("Please specify only integers for bugs, caseruns(using comma to seperate IDs),                "+\
				"and bug_system. (DEBUG INFO: invalid literal for int(): )", sel.get_alert())
			except AssertionError, e: myself.verificationErrors.append(str(e))


	### ----------------------------------------- Begin of 'Comments' Label Part ----------------------------------------- ###

	def clickAddComments(self,myself,sel,comText):
		''' Add comments for test case run. '''

		self.verifyElement(myself,sel,"//form[@id='id_form_case_runs']/div/div[2]/div[4]/span")
		sel.mouse_move("//form[@id='id_form_case_runs']/div/div[2]/div[4]/span")
		
		self.clickElement(myself,sel,"//a[@onclick='showCommentForm();']")

		self.inputText(myself,sel,"commentText",comText)
		self.clickElement(myself,sel,"//button[@id='btnComment']")

		time.sleep(env.t)

	def addCommentForCaseInRun(self,myself,sel,testcaserunId,testcaseName,comString,needRemove=True):
		''' Add Comment For Case in test run. 
		    If testcaserunId=="", it means to try to add a comments without case selected, so an error should be shown. '''

		if testcaserunId!="":
			self.selectCaseInRun(myself,sel,[testcaserunId])

			self.clickAddComments(myself,sel,comString)

			self.expandCaseInRun(myself,sel,testcaseName)

			#Verify if the comments have been added successfully
			self.clickLink(myself,sel,"Show All")
			self.verifyText(myself,sel,comString)

			if needRemove:
				#Delete the added comments
				self.clickElement(myself,sel,"//input[@title='Remove Comment']")
				time.sleep(env.ts)
				myself.failUnless(re.search(r"^Are you sure to delete the comment[\s\S]$", sel.get_confirmation()))
				time.sleep(env.ts)

				#Verify the added comments have been deleted
				self.clickLink(myself,sel,"Show All")
				self.verifyTextNotPresent(myself,sel,comString)

		#Bug exists, when bug got fixed, below code will need to be repaired accordingly.
		else:
			self.clickAddComments(myself,sel,comString)
			self.verifyTargetText(myself,sel,"No runs selected.","css=#commentsErr")


	#------------------------------------------------------------------------
	#-------------------- (4) Test Run 'Add case' page ----------------------
	#------------------------------------------------------------------------

	def verifyTestRunAddCasePageIsReady(self,myself,sel,testrunName):
		''' Verify test run Add Case page is ready. '''

		time.sleep(env.ts)
		self.verifyPageTitle(myself,sel,"Assign new test run")
		self.verifyTargetText(myself,sel,testrunName,"//h2[@id='display_title']/a")

	def selectTestCasesInRunAddCasePage(self,myself,sel,testcaseIds,usePlanSortkey="<default>"):
		''' Select part of test cases in the run add case page. The data type of the para testcaseIds is 'list' type. '''

		for i in range(len(testcaseIds)):
			self.clickCheckBox(myself,sel,"case",testcaseIds[i],onoff="on")

		#The value of the para 'usePlanSortkey' should be: 'on' or 'off'
		if usePlanSortkey!="<default>":
			self.clickCheckBox(myself,sel,"id_checkbox_plan_sortkey","",onoff=usePlanSortkey)

	def clickActionInRunAddCasePage(self,myself,sel,ActionName):
		''' Click Action in test run Add Case Page including button or link. '''

		if ActionName == "Update": self.clickBtnAndWait(myself,sel,"submit","Update")
		elif ActionName == "Reset": self.clickBtn(myself,sel,"reset","Reset")


	#----------------------------------------------------------------------
	#-------------------- (5) Test Run 'Other' page -----------------------
	#----------------------------------------------------------------------

	def verifyTestLogReportPageIsReady(self,myself,sel,testrunId,testrunName,caserunStatusList="<default>",bugNoList="<default>"):
		''' Verify test Test Log Report page is ready.

		    An example of the value of caserunStatusList: caserunStatusList=["PASSED","IDLE"]
		    An example of the value of bugNoList: bugNoList=["112233","445566"]
		    Example of call: CCommonUtils().verifyTestLogReportPageIsReady(self,sel,testrunId,testrunName,caserunStatusList=["IDLE","IDLE"],bugNoList=[bugNo1,bugNo2])
		'''

		time.sleep(env.ts)
		self.verifyText(myself,sel,"Test Log Report")
		self.verifyLink(myself,sel,"["+testrunId+"] "+testrunName)

		if caserunStatusList!="<default>":
			for i in range(len(caserunStatusList)):
				self.verifyTargetText(myself,sel,caserunStatusList[i],"//div[@id='content']/table/tbody/tr["+str((i+1)*2)+"]/td[7]/span")

		if bugNoList!="<default>":
			if bugNoList!="":
				bugNoStr=""
				for i in range(len(bugNoList)):
					self.verifyTargetText(myself,sel,"Bugs ID:","css=span.notes_title")
					self.verifyLink(myself,sel,"Bug List:")
					self.verifyText(myself,sel,"View all bugs")

					self.verifyLink(myself,sel,bugNoList[i])
					self.verifyLink(myself,sel,"https://bugzilla.redhat.com/show_bug.cgi?id="+bugNoList[i])
					bugNoStr+=bugNoList[i]+","

				self.verifyLink(myself,sel,"https://bugzilla.redhat.com/buglist.cgi?bugidtype=include&bug_id="+bugNoStr[:-1])
			else:
				self.verifyElementNotPresent(myself,sel,"css=span.notes_title")
				self.verifyLinkNotPresent(myself,sel,"Bug List:")
				self.verifyTextNotPresent(myself,sel,"View all bugs")

	def verifyNoCaseForRunWarningPageIsReady(self,myself,sel):
		''' Verify the warning page is ready and shown correctly when create a run from a plan without a test case selected or save a run without any case exists in it. '''

		time.sleep(env.ts)
		self.verifyPageTitle(myself,sel, "INFO - At least one case is required by a run.")
		self.verifyTargetText(myself,sel,"At least one case is required by a run.","css=P")
		self.verifyLink(myself,sel,"Continue")



