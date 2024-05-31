from selenium import selenium
import unittest, time, re

from env import *
import CommonElements

class CCommonPages(CommonElements.CCommonElements):


	# ========================================================================================================
	# 	Test Case pages related functions
	# ========================================================================================================


	#-----------------------------------------------------------------------
	#-------------------- (1) Test Case 'Create' page ----------------------
	#-----------------------------------------------------------------------

	def verifyCreateTestCasePageIsReady(self,myself,sel,chosenComponentIdNames="<default>",notChosenComponentIdNames="<default>"):
		''' Verify create test case page is ready. '''

		time.sleep(env.t)
		self.verifyText(myself,sel,"Create new case")
		self.verifyElement(myself,sel,"//input[@type='submit' and @value='Save']")

		if chosenComponentIdNames!="<default>":
			for cId,cName in chosenComponentIdNames.items():
				self.verifyElement(myself,sel,"//select[@id='id_component_to']/option[@value='"+cId+"']")
				self.verifyTargetText(myself,sel,cName,"//select[@id='id_component_to']/option[@value='"+cId+"']")

		if notChosenComponentIdNames!="<default>":
			for cId,cName in notChosenComponentIdNames.items():
				self.verifyElementNotPresent(myself,sel,"//select[@id='id_component_to']/option[@value='"+cId+"']")

				self.verifyElement(myself,sel,"//select[@id='id_component_from']/option[@value='"+cId+"']")
				self.verifyTargetText(myself,sel,cName,"//select[@id='id_component_from']/option[@value='"+cId+"']")

	def fillDataForTestCase(self,myself,sel,summary="<default>",product="<default>",component="<default>",category="<default>",manual="<default>",\
		auto="<default>",autoproposal="<default>",requirement="<default>",script="<default>",alias="<default>",defaulttester="<default>",\
		estdays="<default>",esthours="<default>",estmins="<default>",estsecs="<default>",priority="<default>",arguments="<default>",notes="<default>"):

		''' Fill the data for for a new case with provided data. '''

		#input summary of new test case
		if summary!="<default>": self.inputText(myself,sel,"id_summary", summary)

		#select product
		if product!="<default>": 
			if not self.isSelectedLabel(myself,sel,product,"product"):
				self.selectOptionInDropDownList(myself,sel,"product",product)

		self.clickActionInCreateCase(myself,sel,"Refresh component/category")

		#add component
		if component != "<default>": #Example to set this para: component=[env.component11,env.component12]
			for i in range(len(component)):
				self.selectOptionInList(myself,sel,"id_component_from",component[i])
				self.clickActionInCreateCase(myself,sel,"Add")

		#select category
		if category!="<default>": 
			if not self.isSelectedLabel(myself,sel,category,"category"):
				self.selectOptionInDropDownList(myself,sel,"category",category)

		#Set Automated - Note: The value of the paras 'manual' and 'auto' and 'autoproposal' just involve: 'on', 'off'
		if manual!="<default>": self.clickCheckBox(myself,sel,"is_automated","0",onoff=manual)
		if auto!="<default>": self.clickCheckBox(myself,sel,"is_automated","1",onoff=auto)
		if autoproposal!="<default>": self.clickCheckBox(myself,sel,"is_automated_proposed","",onoff=autoproposal)

		#input requirement
		if requirement!="<default>": self.inputText(myself,sel,"id_requirement", requirement)

		#input script
		if script!="<default>": self.inputText(myself,sel,"id_script", script)

		#input alias
		if alias!="<default>": self.inputText(myself,sel,"id_alias", alias)

		#input Default Tester
		if defaulttester!="<default>": self.inputText(myself,sel,"id_default_tester", defaulttester)

		#add estimated days
		if estdays!="<default>": 
			if not self.isSelectedLabel(myself,sel,estdays,'estimated_time_days'):
				self.selectOptionInDropDownList(myself,sel,"estimated_time_days",estdays)
		#add estimated hours
		if esthours!="<default>": 
			if not self.isSelectedLabel(myself,sel,esthours,'estimated_time_hours'):
				self.selectOptionInDropDownList(myself,sel,"estimated_time_hours",esthours)
		#add estimated minutes
		if estmins!="<default>": 
			if not self.isSelectedLabel(myself,sel,estmins,'estimated_time_minutes'):
				self.selectOptionInDropDownList(myself,sel,"estimated_time_minutes",estmins)
		#add estimated seconds
		if estsecs!="<default>": 
			if not self.isSelectedLabel(myself,sel,estsecs,'estimated_time_seconds'):
				self.selectOptionInDropDownList(myself,sel,"estimated_time_seconds",estsecs)

		#select priority
		if priority!="<default>": #Example to set this para: priority="P1"
			if not self.isSelectedLabel(myself,sel,priority,'priority'):
				self.selectOptionInDropDownList(myself,sel,"priority",priority)

		#input arguments
		if arguments!="<default>": self.inputText(myself,sel,"id_arguments", arguments)

		#add notes
		if notes!="<default>": self.inputText(myself,sel,"id_notes", notes)

	def clickActionInCreateCase(self,myself,sel,ActionName):
		''' Click Action in new test case including button or link. '''

		if ActionName == "Save": self.clickBtnAndWait(myself,sel,"submit","Save")
		elif ActionName == "Save and continue editing": self.clickBtnAndWait(myself,sel,"submit","Save and continue editing")
		elif ActionName == "Save and add another": self.clickBtnAndWait(myself,sel,"submit","Save and add another")
		elif ActionName == "Save and return to plan": self.clickBtnAndWait(myself,sel,"submit","Save and return to plan")
		elif ActionName == "Cancel": self.clickBtnAndWait(myself,sel,"button","Cancel")
		elif ActionName == "Refresh component/category": self.clickBtn(myself,sel,"button","Refresh component/category")

		if ActionName == "Add": self.clickLink(myself,sel,"Add")
		elif ActionName == "Remove": self.clickLink(myself,sel,"Remove")

	def addComponentInCreateCase(self,myself,sel,componentIdNames,wayToAdd="Click Add",needSearchComp=False):
		''' Add component in new test case. 

		    'wayToAdd's value involves: 'Click Add','Double Click','Choose all'.
		    'componentIdNames' is a 'dict' type para. Note: if wayToAdd=="Choose all", the value of 'componentIdNames' should be 'All'.
		 '''

		if wayToAdd=="Click Add":
			for cId,cName in componentIdNames.items():
				if needSearchComp: self.inputText(myself,sel,"id_component_input", cName)

				self.selectOptionInList(myself,sel,"id_component_from",cName)
				self.clickActionInCreateCase(myself,sel,"Add")

				self.verifyElementNotPresent(myself,sel,"//select[@id='id_component_from']/option[@value='"+cId+"']")

				self.verifyElement(myself,sel,"//select[@id='id_component_to']/option[@value='"+cId+"']")
				self.verifyTargetText(myself,sel,cName,"//select[@id='id_component_to']/option[@value='"+cId+"']")

		elif wayToAdd=="Double Click":
			for cId,cName in componentIdNames.items():
				if needSearchComp: self.inputText(myself,sel,"id_component_input", cName)

				self.selectOptionInList(myself,sel,'id_component_from',cName)
				sel.double_click("//select[@id='id_component_from']/option[@value='"+cId+"']")

				self.verifyElementNotPresent(myself,sel,"//select[@id='id_component_from']/option[@value='"+cId+"']")

				self.verifyElement(myself,sel,"//select[@id='id_component_to']/option[@value='"+cId+"']")
				self.verifyTargetText(myself,sel,cName,"//select[@id='id_component_to']/option[@value='"+cId+"']")

		elif wayToAdd=="Choose all" and componentIdNames=="All":
			compfrom = sel.get_text("//select[@id='id_component_from']")
			self.clickLink(myself,sel,"Choose all")

			compto = sel.get_text("//select[@id='id_component_to']")
			try: myself.assertEqual(compfrom, compto)
			except AssertionError, e: myself.verificationErrors.append(str(e))

			compfrom = sel.get_text("//select[@id='id_component_from']")
			try: myself.assertEqual(compfrom, "")
			except AssertionError, e: myself.verificationErrors.append(str(e))

	def removeComponentInCreateCase(self,myself,sel,componentIdNames,wayToRemove="Click Remove"):
		''' Remove component in new test case. 

		    'wayToRemove's value involves: 'Click Remove','Double Click','Clear all'.
		    'componentIdNames' is a 'dict' type para.
		 '''

		if wayToRemove=="Click Remove":
			for cId,cName in componentIdNames.items():
				self.selectOptionInList(myself,sel,"id_component_to",cName)
				self.clickActionInCreateCase(myself,sel,"Remove")

				self.verifyElementNotPresent(myself,sel,"//select[@id='id_component_to']/option[@value='"+cId+"']")

				self.verifyElement(myself,sel,"//select[@id='id_component_from']/option[@value='"+cId+"']")
				self.verifyTargetText(myself,sel,cName,"//select[@id='id_component_from']/option[@value='"+cId+"']")

		elif wayToRemove=="Double Click":
			for cId,cName in componentIdNames.items():
				self.selectOptionInList(myself,sel,'id_component_to',cName)
				sel.double_click("//select[@id='id_component_to']/option[@value='"+cId+"']")

				self.verifyElementNotPresent(myself,sel,"//select[@id='id_component_to']/option[@value='"+cId+"']")

				self.verifyElement(myself,sel,"//select[@id='id_component_from']/option[@value='"+cId+"']")
				self.verifyTargetText(myself,sel,cName,"//select[@id='id_component_from']/option[@value='"+cId+"']")

		elif wayToRemove=="Clear all":
			if componentIdNames=="All":
				compto = sel.get_text("//select[@id='id_component_to']")
				self.clickLink(myself,sel,"Clear all")

				compfrom = sel.get_text("//select[@id='id_component_from']")
				try: myself.assertEqual(compfrom, compto)
				except AssertionError, e: myself.verificationErrors.append(str(e))

				compto = sel.get_text("//select[@id='id_component_to']")
				try: myself.assertEqual(compto, "")
				except AssertionError, e: myself.verificationErrors.append(str(e))

			else:
				self.clickLink(myself,sel,"Clear all")
				for cId,cName in componentIdNames.items():
					self.verifyElementNotPresent(myself,sel,"//select[@id='id_component_to']/option[@value='"+cId+"']")

					self.verifyElement(myself,sel,"//select[@id='id_component_from']/option[@value='"+cId+"']")
					self.verifyTargetText(myself,sel,cName,"//select[@id='id_component_from']/option[@value='"+cId+"']")


	#---------------------------------------------------------------------
	#-------------------- (2) Test Case 'Edit' page ----------------------
	#---------------------------------------------------------------------

	def verifyEditTestCasePageIsReady(self,myself,sel,testcaseName):
		''' Verify edit test case page is ready. '''

		time.sleep(env.t)
		self.verifyPageTitle(myself,sel,"Edit test case - "+testcaseName)
		self.verifyText(myself,sel,"Created")
		self.verifyText(myself,sel,"Last Modified")
		self.verifyElement(myself,sel,"//input[@type='submit' and @value='Save']")
		self.verifyElement(myself,sel,"//input[@type='reset' and @value='Reset']")
		self.verifyElement(myself,sel,"//input[@type='button' and @value='Back']")

	def isEditTestCasePageOpen(self,myself,sel,testcaseName):
		''' Verify if the current page is test run page in edit status. '''

		t1 = self.isPageTitle(myself,sel, "Edit test case - "+testcaseName)
		t2 = self.isLink(myself,sel,"Edit History")
		t3 = self.isBtn(myself,sel,"submit","Save")

		if t1 and t2 and t3: return True
		else: return False

	def fillDataForEditCase(self,myself,sel,summary="<default>",product="<default>",category="<default>",defaulttester="<default>",\
		estdays="<default>",esthours="<default>",estmins="<default>",estsecs="<default>",status="<default>",\
		arguments="<default>",notes="<default>",manual="<default>",auto="<default>",autoproposal="<default>",\
		requirement="<default>",script="<default>",alias="<default>",priority="<default>"):

		''' Fill the data for for a new case with provided data. '''

		#input summary of new test case
		if summary!="<default>": self.inputText(myself,sel,"id_summary", summary)

		#select product
		if product!="<default>": 
			if not product == sel.get_selected_label("//select[@name='product']"):
				self.selectOptionInDropDownList(myself,sel,"product",product)

		#select category
		if category!="<default>": 
			if not self.isSelectedLabel(myself,sel,category,'category'):
				self.selectOptionInDropDownList(myself,sel,"category",category)

		#input Default Tester
		if defaulttester!="<default>": self.inputText(myself,sel,"id_default_tester", defaulttester)

		#add estimated days
		if estdays!="<default>": 
			if not self.isSelectedLabel(myself,sel,estdays,'estimated_time_days'):
				self.selectOptionInDropDownList(myself,sel,"estimated_time_days",estdays)
		#add estimated hours
		if esthours!="<default>": 
			if not self.isSelectedLabel(myself,sel,esthours,'estimated_time_hours'):
				self.selectOptionInDropDownList(myself,sel,"estimated_time_hours",esthours)
		#add estimated minutes
		if estmins!="<default>": 
			if not self.isSelectedLabel(myself,sel,estmins,'estimated_time_minutes'):
				self.selectOptionInDropDownList(myself,sel,"estimated_time_minutes",estmins)
		#add estimated seconds
		if estsecs!="<default>": 
			if not self.isSelectedLabel(myself,sel,estsecs,'estimated_time_seconds'):
				self.selectOptionInDropDownList(myself,sel,"estimated_time_seconds",estsecs)

		#select status as one of below values: "PROPOSED", "CONFIRMED", "DISABLED", "NEED_UPDATE"
		if status!="<default>": 
			if not self.isSelectedLabel(myself,sel,status,"id_case_status"):
				self.selectOptionInDropDownList(myself,sel,"id_case_status",status)

		#input arguments
		if arguments!="<default>": self.inputText(myself,sel,"id_arguments", arguments)

		#add notes
		if notes!="<default>": self.inputText(myself,sel,"id_notes", notes)

		#Set Automated - Note: The value of the paras 'manual' and 'auto' and 'autoproposal' just involve: 'on', 'off'
		if manual!="<default>": self.clickCheckBox(myself,sel,"is_automated","0",onoff=manual)
		if auto!="<default>": self.clickCheckBox(myself,sel,"is_automated","1",onoff=auto)
		if autoproposal!="<default>": self.clickCheckBox(myself,sel,"is_automated_proposed","",onoff=autoproposal)

		#input requirement
		if requirement!="<default>": self.inputText(myself,sel,"id_requirement", requirement)

		#input script
		if script!="<default>": self.inputText(myself,sel,"id_script", script)

		#input alias
		if alias!="<default>": self.inputText(myself,sel,"id_alias", alias)

		#select priority
		if priority!="<default>": #Example to set this para: priority="P1"
			if not self.isSelectedLabel(myself,sel,priority,'priority'):
				self.selectOptionInDropDownList(myself,sel,"priority",priority)

	def editTestCase(self,myself,sel,testcaseName,summary="<default>",product="<default>",category="<default>",\
		defaulttester="<default>",estdays="<default>",esthours="<default>",estmins="<default>",estsecs="<default>",\
		status="<default>",arguments="<default>",notes="<default>",manual="<default>",auto="<default>",\
		autoproposal="<default>",requirement="<default>",script="<default>",alias="<default>",priority="<default>"):
		''' Edit a test case from an opened test case. '''

		self.clickActionInCase(myself,sel,"Edit")
		self.verifyEditTestCasePageIsReady(myself,sel,testcaseName)

		#Fill the data for the edit test case with provided data.
		self.fillDataForEditCase(myself,sel,summary,product,category,defaulttester,\
		estdays,esthours,estmins,estsecs,status,arguments,notes,manual,auto,autoproposal,\
		requirement,script,alias,priority)

		self.clickActionInEditCase(myself,sel,"Save")

		#Verify if test case is saved as expected
		if self.isEditTestCasePageOpen(myself,sel,testcaseName):
			self.verifyEditTestCasePageIsReady(myself,sel,testcaseName)
		else: 
			if summary!="<default>": testcaseName=summary

			#automated's value should just involve: "Manual", "Auto", "Manual(Autoproposed)", "Auto(Autoproposed)", "Both(Autoproposed)"
			automated="<default>"
			if manual=="on" and auto=="off" and autoproposal=="off": automated="Manual"
			elif manual=="off" and auto=="on" and autoproposal=="off": automated="Auto"
			elif manual=="on" and auto=="off" and autoproposal=="on": automated="Manual(Autoproposed)"
			elif manual=="off" and auto=="on" and autoproposal=="on": automated="Auto(Autoproposed)"
			elif manual=="on" and auto=="on" and autoproposal=="on": automated="Both(Autoproposed)"

			self.verifyTestCasePageIsReady(myself,sel,testcaseName,defaulttester,product,category,estdays,\
				esthours,estmins,estsecs,priority,status,notes,automated,requirement,script,alias,arguments)

	def clickActionInEditCase(self,myself,sel,ActionName):
		''' Click Action in new test case including button or link. '''

		if ActionName == "Save": self.clickBtnAndWait(myself,sel,"submit","Save")
		elif ActionName == "Save and continue editing": self.clickBtnAndWait(myself,sel,"submit","Save and continue editing")
		elif ActionName == "Save and edit next enabled case in plan": self.clickElementAndWait(myself,sel,"//input[@type='submit' and @name='_continuenext']")
		elif ActionName == "Reset": self.clickBtnAndWait(myself,sel,"reset","Reset")
		elif ActionName == "Back": self.clickBtnAndWait(myself,sel,"button","Back")

	def verifyErrWarningMsgInEditTestCase(self,myself,sel,errType):
		''' Verify the error warning message when edit test case. '''

		if errType == "Blank Summary":
			self.verifyTargetText(myself,sel,"This field is required.","css=ul.errorlist")


	#---------------------------------------------------------------------
	#-------------------- (3) Test Case 'Read' page ----------------------
	#---------------------------------------------------------------------

	def verifyTestCasePageIsReady(self,myself,sel,testcaseName,defaulttester="<default>",product="<default>",\
		category="<default>",estdays="<default>",esthours="<default>",estmins="<default>",estsecs="<default>",\
		priority="<default>",status="<default>",notes="<default>",author="<default>",\
		automated="<default>",requirement="<default>",script="<default>",alias="<default>",arguments="<default>",\
		attachmentNameList="<default>",componentIdNames="<default>",noComponentIdNames="<default>",\
		taglist="<default>",notaglist="<default>",caserunnamelist="<default>"):
		''' Verify test case page is ready. '''

		time.sleep(env.t)   #Wait some more time to make sure all elements in page have been loaded
		self.verifyTargetText(myself,sel,testcaseName,"display_title")

		if defaulttester!="<default>": #The value of 'author' should be in email format
			if defaulttester=="": defaulttester="No default tester"
			self.verifyTargetText(myself,sel,defaulttester,"css=div.name > span")

		if product!="<default>": self.verifyTargetText(myself,sel,product,"//div[@id='content']/div[4]/fieldset/div/div[2]/div[2]/span")

		if category!="<default>": self.verifyTargetText(myself,sel,category,"//span[@id='display_category']")

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

		#priority's value should just involve: 'P1', 'P2', 'P3', 'P4', 'P5'
		if priority!="<default>": self.verifyTargetText(myself,sel,priority,"//span[@id='display_priority']")

		#status's value should just involve: "PROPOSED", "CONFIRMED", "DISABLED", "NEED_UPDATE"
		if status!="<default>": self.verifyTargetText(myself,sel,status,"//div[@id='content']/div[4]/fieldset/div/div[6]/div[2]/span")

		if notes!="<default>": 
			self.verifyTargetText(myself,sel,notes,"//div[@id='content']/div[4]/fieldset/div/div[7]/div[2]/span")

		if author!="<default>": #The value of 'author' should be in email format
			self.verifyTargetText(myself,sel,author,"css=span.name > a")

		#automated's value should just involve: 'Manual', 'Auto', 'Manual(Autoproposed)', 'Auto(Autoproposed)', 'Both(Autoproposed)'
		if automated!="<default>": self.verifyTargetText(myself,sel,automated,"//div[@id='content']/div[4]/fieldset/div[2]/div[3]/div[2]")

		if requirement!="<default>": 
			if requirement=="": requirement="None"
			self.verifyTargetText(myself,sel,requirement,"//span[@id='display_requirement']")
		if script!="<default>": 
			if script=="": script="None"
			self.verifyTargetText(myself,sel,script,"//span[@id='display_script']")
		if alias!="<default>": 
			if alias=="": alias="None"
			self.verifyTargetText(myself,sel,alias,"//div[@id='content']/div[4]/fieldset/div[2]/div[6]/div[2]/span")
		if arguments!="<default>": 
			if arguments=="": arguments="None"
			self.verifyTargetText(myself,sel,arguments,"//div[@id='content']/div[4]/fieldset/div[2]/div[7]/div[2]/span")

		##-------------------------------------------------------------------------

		if attachmentNameList!="<default>":
			self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Attachments")
			if attachmentNameList!="":
				for i in range(len(attachmentNameList)): 
					self.verifyLink(myself,sel,attachmentNameList[i])
			else:
				self.verifyTargetText(myself,sel,"No attachments","css=span.grey")

		if componentIdNames!="<default>":
			self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Components")
			for cId,cName in componentIdNames.items():
				self.verifyText(myself,sel,cName)
				self.verifyCheckBox(myself,sel,"off","component",cId)

		if noComponentIdNames!="<default>":
			self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Components")
			for cId,cName in noComponentIdNames.items():
				self.isElementNotPresent(myself,sel,"//input[@name='component' and @value='"+cId+"']")

		if taglist!="<default>":
			self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Tags")
			for i in range(len(taglist)): 
				self.verifyText(myself,sel,taglist[i])
		
		if notaglist!="<default>":
			self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Tags")
			for i in range(len(notaglist)): 
				self.verifyTextNotPresent(myself,sel,notaglist[i])

		if caserunnamelist!="<default>":
			self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Case Runs")
			for i in range(len(caserunnamelist)): 
				self.verifyText(myself,sel,caserunnamelist[i])
		
	def isTestCasePageOpen(self,myself,sel,testcaseName):
		''' Verify if the current page is test case page. '''

		title = sel.get_title()
		t11=title.find("Test case - ")
		t12=title.find(": "+testcaseName)

		t2 = self.isTargetText(myself,sel,testcaseName,"display_title")
		t3 = self.isElement(myself,sel,"//input[@type='button' and @value='Clone case']")

		if (t11!=-1) and (t12!=-1) and t2 and t3: return True
		else: return False

	def clickActionInCase(self,myself,sel,ActionName):
		''' Click Action in a test case including button or link. '''

		if ActionName == "Edit": self.clickBtnAndWait(myself,sel,"button","Edit")
		elif ActionName == "Clone case": self.clickBtnAndWait(myself,sel,"button","Clone case")

	def clickFirstLevelLinkInCase(self,myself,sel,linkId):
		''' Click the first level link in test case. '''

		self.clickElement(myself,sel,"//body/div[@id='content']/div[@class='Detailform border-1']/ul/li[@id='"+linkId+"']/a")
		time.sleep(env.ts)

	def clickFirstLevelLinkByLabelNameInCase(self,myself,sel,labelName):
		''' Click the first level link in test case. '''

		if labelName=="Document": self.clickFirstLevelLinkInCase(myself,sel,"tab_document")
		elif labelName=="Attachments": self.clickFirstLevelLinkInCase(myself,sel,"tab_attachment")
		elif labelName=="Test Plans": self.clickFirstLevelLinkInCase(myself,sel,"tab_case_plan")
		elif labelName=="Components": self.clickFirstLevelLinkInCase(myself,sel,"tab_component")
		elif labelName=="Tags": self.clickFirstLevelLinkInCase(myself,sel,"tab_case_tag")
		elif labelName=="Bugs": self.clickFirstLevelLinkInCase(myself,sel,"tab_case_bug")
		elif labelName=="Case Runs": self.clickFirstLevelLinkInCase(myself,sel,"tab_case_run")
		elif labelName=="Change Logs": self.clickFirstLevelLinkInCase(myself,sel,"tab_case_log")


	### ----------------------------------------- Begin of 'Document' Label Part ----------------------------------------- ###

	def viewCaseHistory(self,myself,sel):
		''' To view Case History. '''

		self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Document")

		self.clickLinkAndWait(myself,sel,"View edit history(Current in version 1)")

		self.verifyCaseHistoryPageIsReady(myself,sel)


	### ----------------------------------------- Begin of 'Attachments' Label Part ----------------------------------------- ###

	def addAttachmentInCase(self,myself,sel,attachmentPathList):
		''' Add attachment for test case. '''

		self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Attachments")

		self.clickLink(myself,sel,"add")
		self.verifyTargetText(myself,sel,"Upload New Attachment","css=span.tit")

		for i in range(len(attachmentPathList)):
			self.inputText(myself,sel,"upload_file", attachmentPathList[i])
			self.clickBtn(myself,sel,"submit","Upload")

			self.verifyLink(myself,sel,os.path.basename(attachmentPathList[i]))

	def removeAttachmentInCase(self,myself,sel,attachmentNameList):
		''' Remove attachments for test case. '''

		self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Attachments")

		for i in range(len(attachmentNameList)):

			self.verifyLink(myself,sel,attachmentNameList[i])

			for r in range(1,1000):
				if self.isTargetText(myself,sel,attachmentNameList[i],"//tr["+str(r)+"]/td[1]/a"):

					self.clickElement(myself,sel,"//tr["+str(r)+"]/td[5]/a[2]") #click "Delete" link
					myself.failUnless(re.search(r"^Arey you sure to delete the attachment[\s\S]$", sel.get_confirmation()))
					time.sleep(env.ts)

					self.verifyLinkNotPresent(myself,sel,attachmentNameList[i])
					break


	### ----------------------------------------- Begin of 'Test plans' Label Part ----------------------------------------- ###

	def addTestPlanInCase(self,myself,sel,testplanIdNames="",invalidTestPlanIds=""):
		''' Add Test Plan in test case.

		    The para 'testplanIdNames' is 'dict' type, it's value is like: {testplanId1:testplanName1,testplanId2:testplanName2}
		    The para 'invalidTestPlanIds' is 'list' type. it's value is like: [testplanId1,testplanId2]
		'''

		self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Test Plans")

		if testplanIdNames!="":
			testplanIdStr=""
			for tpId,tpName in testplanIdNames.items():
				testplanIdStr+=tpId+","
			self.inputText(myself,sel,"pk__in", testplanIdStr[:-1])

			self.clickElement(myself,sel,"//input[@value='Add']")

			for tpId,tpName in testplanIdNames.items():
				self.verifyCheckBox(myself,sel,"on","id_preview_plan_"+tpId,tpId)
				self.verifyText(myself,sel,"["+tpId+"] "+tpName)
			self.clickBtn(myself,sel,"submit","Submit")

			for tpId,tpName in testplanIdNames.items():
				self.verifyLink(myself,sel,tpId)
				self.verifyLink(myself,sel,tpName)

		elif invalidTestPlanIds!="":
			invalidtestplanIdStr=""
			for i in range(len(invalidTestPlanIds)):
				invalidtestplanIdStr+=invalidTestPlanIds[i]+","

			self.inputText(myself,sel,"pk__in", invalidtestplanIdStr[:-1])
			self.clickElement(myself,sel,"//input[@value='Add']")

			self.verifyTargetText(myself,sel,"The plan you specific does not exist in database.","//div[@id='dialog']/form")
			self.clickBtn(myself,sel,"button","Cancel")

	def removeTestPlanInCase(self,myself,sel,testplanIds,testcaseId):
		''' Remove Test Plan in test case. '''

		self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Test Plans")

		for i in range(len(testplanIds)):
			self.clickElement(myself,sel,"//input[@onclick='removePlanFromCase(this.up(4), "+testplanIds[i]+", "+testcaseId+")']")
		        myself.failUnless(re.search(r"^Are you sure to remove the case from this plan[\s\S]$", sel.get_confirmation()))
			time.sleep(env.ts)

			self.verifyLinkNotPresent(myself,sel,testplanIds[i])


	### ----------------------------------------- Begin of 'Components' Label Part ----------------------------------------- ###

	def addComponentInCase(self,myself,sel,product,componentList,AddOrCancel="Add"):
		''' Add one component in test case. AddOrCancel's value involves:'Add','Cancel' '''

		self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Components")

		self.clickBtn(myself,sel,"button","Add Component")

		if not self.isSelectedLabel(myself,sel,product,"product"):
			self.selectOptionInList(myself,sel,"product",product)

		for i in range(len(componentList)):
			self.selectOptionInList(myself,sel,"o_component",componentList[i])

		if AddOrCancel == "Add":
			self.clickElement(myself,sel,"//div[@id='dialog']/form/label/input[2]")
			time.sleep(env.ts)

			self.verifyText(myself,sel,product)
			for i in range(len(componentList)):
				self.verifyText(myself,sel,componentList[i])

		elif AddOrCancel == "Cancel":
			self.clickElement(myself,sel,"//div[@id='dialog']/form/input")

			for i in range(len(componentList)):
				self.verifyTextNotPresent(myself,sel,componentList[i])

	def removeComponentInCase(self,myself,sel,componentIdList):
		''' Add one component in test case. '''

		self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Components")

		if componentIdList!="":
			for i in range(len(componentIdList)):
				self.clickCheckBox(myself,sel,"component",componentIdList[i],onoff="on")

			self.clickBtn(myself,sel,"submit","Remove")
			myself.failUnless("^Are you sure you want to delete these component\\(s\\)[\\s\\S]\nYou cannot undo\\.$")
			time.sleep(env.ts)

			for i in range(len(componentIdList)):
				self.verifyTextNotPresent(myself,sel,componentIdList[i])
		else:
			self.clickBtn(myself,sel,"submit","Remove")
			time.sleep(env.ts)


	### ----------------------------------------- Begin of 'Tags' Label Part ----------------------------------------- ###

	def addTagInCase(self,myself,sel,tagName):
		''' Add tag in test case. '''

		self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Tags")
		self.inputText(myself,sel,"id_tags", tagName)
		self.clickElement(myself,sel,"//a[@onclick='addTag(this.up(6))']")

		if tagName!="":
			#To handle serveral tags by comma
			tagNameList=[]
			t=tagName.find(",")
			while t!=-1:
				tagNameList.append(tagName[:t])
				tagName=tagName[t+1:]
				t=tagName.find(",")
			tagNameList.append(tagName)

			for tagItem in tagNameList:
				self.verifyText(myself,sel,tagItem)

		else:
			self.verifyText(myself,sel,"No tag found")

	def removeTagInCase(self,myself,sel,tagName):
		''' Remove tag in test case. '''

		self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Tags")

		#To handle serveral tags by comma
		tagNameList=[]
		t=tagName.find(",")
		while t!=-1:
			tagNameList.append(tagName[:t])
			tagName=tagName[t+1:]
			t=tagName.find(",")
		tagNameList.append(tagName)

		for tagItem in tagNameList:
			self.clickElement(myself,sel,"//a[@onclick=\"removeTag(this.up(5), '"+tagItem+"')\"]")
			self.verifyTextNotPresent(myself,sel,tagItem)

	def editTagInCase(self,myself,sel,tagName,tagNameNew):
		''' Add tag in test case. '''

		self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Tags")

		sel.answer_on_next_prompt(tagNameNew)
		self.clickElement(myself,sel,"//a[@onclick=\"editTag(this.up(5), '"+tagName+"')\"]")
		myself.assertEqual("Please type your new tag", sel.get_prompt())
		time.sleep(env.ts)
		self.verifyText(myself,sel,tagNameNew)


	### ----------------------------------------- Begin of 'Bugs' Label Part ----------------------------------------- ###

	def addBugInCase(self,myself,sel,bugNo,bugURL):
		''' Add bug in test case. '''

		self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Bugs")

		self.inputText(myself,sel,"bug_id", bugNo)
		self.clickElement(myself,sel,"//a[@onclick='addCaseBug(this.up(1))']")
		self.verifyLink(myself,sel,bugURL)

	def removeBugInCase(self,myself,sel,testcaseId,bugNo,bugURL):
		''' Remove bug in test case. '''

		self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Bugs")

        	self.clickElement(myself,sel,"//a[@onclick=\"removeCaseBug('"+bugNo+"', '"+testcaseId+"')\"]")
		myself.failUnless(re.search(r"^Are you sure to remove the bug[\s\S]$", sel.get_confirmation()))
		time.sleep(env.ts)
		self.verifyLinkNotPresent(myself,sel,bugURL)

	def addInvalidBugInCase(self,myself,sel,bugNo):
		''' Try to add a invalid bug in test case. '''

		self.clickFirstLevelLinkByLabelNameInCase(myself,sel,"Bugs")

		self.inputText(myself,sel,"bug_id", bugNo)
		self.clickElement(myself,sel,"//a[@onclick='addCaseBug(this.up(1))']")

		myself.assertEqual("Please input a valid bug id.", sel.get_alert())


	#----------------------------------------------------------------------
	#------------------- (4) Test Case 'Add Case' page --------------------
	#----------------------------------------------------------------------

	def verifyAddCasesFromOtherPlansPageIsReady(self,myself,sel,testplanName,testcaseIdNames="<default>"):
		''' Verify the page 'Add cases from other plans' is ready. '''

		time.sleep(env.t)
		self.verifyPageTitle(myself,sel,"Add cases from other plans")

		self.verifyText(myself,sel,"Add cases from other plans")
		self.verifyTargetText(myself,sel,testplanName,"css=h2")
		self.verifyTargetText(myself,sel,"Search cases to add into this test plan.","css=div.grey.tit")

		self.verifyElement(myself,sel,"//input[@type='submit' and @value='Search']")
		self.verifyElement(myself,sel,"//input[@type='reset' and @value='Reset']")

		if testcaseIdNames!="<default>":
			
			if testcaseIdNames!="":
				for tId,tName in testcaseIdNames.items():
					self.verifyLink(myself,sel,tId)
					self.verifyLink(myself,sel,tName)

			else: self.verifyTargetText(myself,sel,"No test cases found.","css=lable.grey")

	def fillDataForAddCasesFromOtherPlansPage(self,myself,sel,summary="<default>",author="<default>",product="<default>",plan="<default>",\
			priority="<default>",automated="<default>",autoproposed="<default>",category="<default>",\
			status="<default>",component="<default>",bugID="<default>",tag="<default>"):
		''' Fill data in 'Add Cases From Other Plans' page. '''

		self.fillDataForSearchCase(myself,sel,summary,author,product,plan,\
			priority,automated,autoproposed,category,status,component,bugID,tag)

	def clickActionInAddCasesFromOtherPlansPage(self,myself,sel,ActionName):
		''' Click Action in 'Add Cases From Other Plans' Page including button or link. '''

		if ActionName == "Search": self.clickBtnAndWait(myself,sel,"submit","Search")
		elif ActionName == "Reset": self.clickBtn(myself,sel,"reset","Reset")
		elif ActionName == "Add selected cases": self.clickBtnAndWait(myself,sel,"submit","Add selected cases")

	def selectCaseInAddCasesFromOtherPlansPage(self,myself,sel,testcaseIds):
		''' Select a test case in 'Add Cases From Other Plans' Page. The para 'testcaseIds' is 'list' type.
		    Especially, if testcaseIds == 'all', it means to select all test cases, if testcaseIds == '', it means select no any test case. '''

		if testcaseIds == "All":
			self.clickCheckBox(myself,sel,"id_checkbox_all_cases","",onoff="off")
			self.clickCheckBox(myself,sel,"id_checkbox_all_cases","",onoff="on")
		elif testcaseIds == "":
			self.clickCheckBox(myself,sel,"id_checkbox_all_cases","",onoff="on")
			self.clickCheckBox(myself,sel,"id_checkbox_all_cases","",onoff="off")
		else:
			for i in range(len(testcaseIds)):
				self.clickCheckBox(myself,sel,"case",testcaseIds[i],onoff="on")

	
	#----------------------------------------------------------------------
	#-------------------- (5) Test Case 'Other' page ----------------------
	#----------------------------------------------------------------------

	def verifyCaseHistoryPageIsReady(self,myself,sel):
		''' Verify test case history page is ready. '''

		time.sleep(env.t)
		self.verifyPageTitle(myself,sel, "Case History")
		self.verifyTargetText(myself,sel,"Test Case History","css=h2")


