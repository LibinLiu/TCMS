from selenium import selenium
import unittest, time, re

from env import *
import CommonElements

class CCommonPages(CommonElements.CCommonElements):


	# ========================================================================================================
	# 	Home page related functions
	# ========================================================================================================
  

	#-----------------------------------------------------------------------
	#--------------------- (1) 'Home -> Recent' page -----------------------
	#-----------------------------------------------------------------------

	def verifyHomePageIsReady(self,myself,sel):
		''' Verify home page is ready. '''

		time.sleep(env.ts)
		self.verifyPageTitle(myself,sel, "Nitrate")
		self.verifyTargetText(myself,sel,"Test Runs","//div[@id='content']/div[2]/div[1]/table/tbody/tr[1]/th/div/div[1]")
		self.verifyTargetText(myself,sel,"Test Plans","//div[@id='content']/div[2]/div[2]/table/tbody/tr[1]/th[1]/div/div")

	def isHomePageOpen(self,myself,sel):
		''' Verify if the current page is home page. '''

		t1 = self.isPageTitle(myself,sel, "Nitrate")
		t2 = self.isTargetText(myself,sel,"Test Runs","//div[@id='content']/div[2]/div[1]/table/tbody/tr[1]/th/div/div[1]")
		t3 = self.isTargetText(myself,sel,"Test Plans","//div[@id='content']/div[2]/div[2]/table/tbody/tr[1]/th[1]/div/div")

		if t1 and t2 and t3: return True
		else: return False

	def clickMenu(self,myself,sel,menuName,submenuName):
		''' Moveover the menu named as the value of menuName like "PLANNING", 
		and then click the submenu named as the value of submenuName, such as "New Plan". '''
		
		self.verifyLink(myself,sel,menuName)
		sel.mouse_over("link="+menuName)

		self.clickLinkAndWait(myself,sel,submenuName)

	def clickActionLinkInHomePage(self,myself,sel,linkName):
		''' Click a button or link in the home page. '''

		if linkName == "Bookmark this page": self.clickElement(myself,sel,"//input[@type='submit' and @value='Bookmark this page']")

		if linkName == "Advanced Search": self.clickLinkAndWait(myself,sel,"Advanced Search")

		if linkName == "Recent": self.clickLinkAndWait(myself,sel,"Recent")
		elif linkName == "Bookmarks": self.clickLinkAndWait(myself,sel,"Bookmarks")
		elif linkName == "Basic Information": self.clickLinkAndWait(myself,sel,"Basic Information")

		if linkName == "Contact developers": self.clickLinkAndWait(myself,sel,"Contact developers")
		elif linkName == "Request permissions": self.clickLinkAndWait(myself,sel,"Request permissions")
		elif linkName == "Report bug": self.clickLinkAndWait(myself,sel,"Report bug")
		elif linkName == "User guide": self.clickLinkAndWait(myself,sel,"User guide")
		elif linkName == "Satisfaction Survey": self.clickLinkAndWait(myself,sel,"Satisfaction Survey")
		elif linkName == "Release schedule": self.clickLinkAndWait(myself,sel,"Release schedule")
		elif linkName == "XML-RPC service": self.clickLinkAndWait(myself,sel,"XML-RPC service")

	def quickSearch(self,myself,sel,searchType,searchText):
		''' search test plan/case/run in top right of home page. '''

		self.selectOptionInDropDownList(myself,sel,"search_type",searchType)

		self.inputText(myself,sel,"search_content",searchText)

		self.clickBtnAndWait(myself,sel,"button","Go")


	#-----------------------------------------------------------------------
	#-------------------- (2) 'Home -> Bookmarks' page ---------------------
	#-----------------------------------------------------------------------

	def verifyBookmarksPageIsReady(self,myself,sel):
		''' Verify home page is ready. '''

		time.sleep(env.ts)
		self.verifyPageTitle(myself,sel, "Bookmarks - "+env.user)
		self.verifyElement(myself,sel,"//input[@type='submit' and @value='Delete']")

	def addBookmark(self,myself,sel,bookmarkName="<default>",bookmarkDesc="<default>",submitOrCancel="Submit"):
		''' click 'Bookmark this page' in home page to add a bookmark for current page. '''

		self.clickActionLinkInHomePage(myself,sel,"Bookmark this page")

		cururl = sel.get_location()
		self.verifyValue(myself,sel,cururl,"id_url")

		if bookmarkName!="<default>":
			if bookmarkName != sel.get_value("id_name"):
				self.inputText(myself,sel,"id_name",bookmarkName)
		else: 
			bookmarkName = sel.get_value("id_name")

		if bookmarkDesc!="<default>": self.inputText(myself,sel,"id_description",bookmarkDesc)

		if submitOrCancel=="Submit":
			self.clickBtn(myself,sel,"submit",submitOrCancel)
			time.sleep(env.ts)

			myself.assertEqual("Bookmark added.", sel.get_alert())
			time.sleep(env.ts)

		elif submitOrCancel=="Cancel":
			self.clickBtn(myself,sel,"button",submitOrCancel)
			time.sleep(env.ts)

	def deleteBookmarks(self,myself,sel,bookmarkNameList,delete=True):
		''' click Delete In Bookmarks Page to delete Bookmarks. '''

		self.clickCheckBox(myself,sel,"id_check_all_bookmark","",onoff="on")
		self.clickCheckBox(myself,sel,"id_check_all_bookmark","",onoff="off")
		if delete:
			self.clickCheckBox(myself,sel,"id_check_all_bookmark","",onoff="on")

			for i in range(len(bookmarkNameList)):
				self.verifyLink(myself,sel,bookmarkNameList[i])

			self.clickElement(myself,sel,"//input[@type='submit' and @value='Delete']")
			myself.failUnless(re.search(r"^Are you sure you wish to delete these bookmarks[\s\S]$", sel.get_confirmation()))
			time.sleep(env.ts)

			for i in range(len(bookmarkNameList)):
				self.verifyLinkNotPresent(myself,sel,bookmarkNameList[i])

		else:
			self.clickElement(myself,sel,"//input[@type='submit' and @value='Delete']")
			myself.failUnless(re.search(r"^Are you sure you wish to delete these bookmarks[\s\S]$", sel.get_confirmation()))
			time.sleep(env.ts)

			myself.assertEqual("No bookmark selected.", sel.get_alert())
			time.sleep(env.ts)

			for i in range(len(bookmarkNameList)):
				self.verifyLink(myself,sel,bookmarkNameList[i])


	#-----------------------------------------------------------------------
	#--------------- (3) 'Home -> Basic information' page ------------------
	#-----------------------------------------------------------------------

	def verifyBasicInformationPageIsReady(self,myself,sel,firstName="<default>",lastName="<default>",phoneNumber="<default>",\
		IMType="<default>",IMValue="<default>",webURL="<default>",address="<default>",notes="<default>", isSaved=False,isInvalidWebURL=False):
		''' Verify Basic information page is ready. '''

		time.sleep(env.ts)

		#(1)Verify basic info
		self.verifyPageTitle(myself,sel,"Profile - "+env.user)
		self.verifyText(myself,sel,"Username")
		self.verifyText(myself,sel,env.user)
		self.verifyText(myself,sel,"Email")
		self.verifyText(myself,sel,env.useremail)
		self.verifyElement(myself,sel,"//input[@value='Save Change']")

		#(2)Verify the specific info
		if firstName!="<default>": self.verifyValue(myself,sel, firstName,"id_first_name")
		if lastName!="<default>": self.verifyValue(myself,sel, lastName,"id_last_name")
		if phoneNumber!="<default>": self.verifyValue(myself,sel, phoneNumber,"id_phone_number")

		#select IM Type: 'IRC', 'Jabber', 'MSN', 'Yahoo', 'messenger', 'ICQ'
		if IMType!="<default>": self.verifySelectedLabel(myself,sel,IMType,"id_im_type_id")

		if IMValue!="<default>": self.verifyValue(myself,sel, IMValue,"id_im")
		if webURL!="<default>": self.verifyValue(myself,sel, webURL,"id_url")
		if address!="<default>": self.verifyValue(myself,sel, address,"id_address")
		if notes!="<default>": self.verifyValue(myself,sel, notes,"id_notes")

		if isSaved:
			self.verifyText(myself,sel,"Information successfully updated.")
		elif isInvalidWebURL:
			self.verifyTargetText(myself,sel,"urlEnter a valid URL.","css=ul.errorlist > li")

	def fillDataForBasicinfoPage(self,myself,sel,firstName="<default>",lastName="<default>",phoneNumber="<default>",\
		IMType="<default>",IMValue="<default>",webURL="<default>",address="<default>",notes="<default>"):

		''' Fill the data for Basic information form with provided data. '''

		if firstName!="<default>": self.inputText(myself,sel,"id_first_name", firstName)
		if lastName!="<default>": self.inputText(myself,sel,"id_last_name", lastName)
		if phoneNumber!="<default>": self.inputText(myself,sel,"id_phone_number", phoneNumber)

		#select IM Type: 'IRC', 'Jabber', 'MSN', 'Yahoo', 'messenger', 'ICQ'
		if IMType!="<default>": 
			if not self.isSelectedLabel(myself,sel,IMType,"id_im_type_id"):
				self.selectOptionInDropDownList(myself,sel,"id_im_type_id",IMType)

		if IMValue!="<default>": self.inputText(myself,sel,"id_im", IMValue)
		if webURL!="<default>": self.inputText(myself,sel,"id_url", webURL)
		if address!="<default>": self.inputText(myself,sel,"id_address", address)
		if notes!="<default>": self.inputText(myself,sel,"id_notes", notes)

	def clickActionInBasicinfo(self,myself,sel,ActionName):
		''' Click Action in Basic information page including button or link. '''

		if ActionName == "Save Change": self.clickBtnAndWait(myself,sel,"submit","Save Change")


