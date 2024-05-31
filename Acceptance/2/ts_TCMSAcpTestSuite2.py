from selenium import selenium
import unittest, time, re

from env import *

#(Total: 55)
#Plan related test cases (total: 21)
import Plan.tc_ID84261_CreatePlanToAddClassification, Plan.tc_ID84263_CreatePlan, Plan.tc_ID84267_CreatePlanWithInvalidPlanDoc, Plan.tc_ID84275_ClonePlan, Plan.tc_ID84304_AlterPlanName, Plan.tc_ID84313_DisablePlan, Plan.tc_ID84314_EnablePlan, Plan.tc_ID84340_PrintPlan, Plan.tc_ID84347_CheckDocumentInfoInPlan, Plan.tc_ID84360_AddTagInPlan, Plan.tc_ID84361_AddTagWithChiSpechrNameInPlan, Plan.tc_ID84364_CheckTagNumInPlan, Plan.tc_ID84365_CheckCaseNumWithTagInPlan, Plan.tc_ID84366_CheckPlanNumWithTagInPlan, Plan.tc_ID84367_CheckRunNumWithTagInPlan, Plan.tc_ID84368_EditTagInPlan, Plan.tc_ID84369_RemoveTagInPlan, Plan.tc_ID84379_CheckMyPlans, Plan.tc_ID84380_CheckMyPlanAuthor, Plan.tc_ID86752_AddMoreTagInPlan, Plan.tc_ID99073_CheckRunProgBarInPlan

#Search related test cases (total: 34)
import Search.tc_ID84335_SearchPlanBySomeOpts, Search.tc_ID84336_SearchPlanByTag, Search.tc_ID84338_PrintCopyInSearchPlanResult, Search.tc_ID84342_ExportNonePlanInSearchPlanResult, Search.tc_ID84619_SearchRunToEditRun, Search.tc_ID84627_SearchRunByAll, Search.tc_ID86691_QuickSearchCaseById, Search.tc_ID86695_QuickSearchPlanById, Search.tc_ID86696_QuickSearchRunById, Search.tc_ID86697_QuickSearchRunByName, Search.tc_ID86698_QuickSearchCaseByName, Search.tc_ID86699_QuickSearchPlanByName, Search.tc_ID86753_CreatePlanInSearchResult, Search.tc_ID86755_OpenPlanInSearchPlanResult, Search.tc_ID87466_SearchPlanByAllOptInASearch, Search.tc_ID87471_SearchPlanByFAutInASearch, Search.tc_ID87473_SearchCaseRunByPlanItemInASearch, Search.tc_ID87489_SearchCaseByAllOptInASearch, Search.tc_ID87494_SearchCaseByMAutTesterInASearch, Search.tc_ID87496_SearchPlanRunByCaseItemInASearch, Search.tc_ID87510_SearchRunByFMgrTesterInASearch, Search.tc_ID87512_SearchPlanCaseByRunItemInASearch, Search.tc_ID87516_ClickCaseNumInASearchPlanResult, Search.tc_ID87517_ClickRunNumInASearchPlanResult, Search.tc_ID87518_CreatePlanInASearchPlanResult, Search.tc_ID87519_CloneInASearchPlanResult, Search.tc_ID87520_PrintCopyInASearchPlanResult, Search.tc_ID87527_ExpandCaseInASearchCaseResult, Search.tc_ID87532_CloneInASearchCaseResult, Search.tc_ID87533_PrintCopyInASearchCaseResult, Search.tc_ID87538_CloneInASearchRunResult, Search.tc_ID92889_SearchPlanByProdVerInASearch, Search.tc_ID92890_SearchCaseByCaseProdInASearch, Search.tc_ID92891_SearchRunByProdVerInASearch

def suite():

	suite = unittest.TestSuite()

	#Plan related test cases (total: 21)
	suite.addTest(Plan.tc_ID84261_CreatePlanToAddClassification.CreatePlanToAddClassification("test_CreatePlanToAddClassification"))
	suite.addTest(Plan.tc_ID84263_CreatePlan.CreatePlan("test_CreatePlan"))
	suite.addTest(Plan.tc_ID84267_CreatePlanWithInvalidPlanDoc.CreatePlanWithInvalidPlanDoc("test_CreatePlanWithInvalidPlanDoc"))
	suite.addTest(Plan.tc_ID84275_ClonePlan.ClonePlan("test_ClonePlan"))
	suite.addTest(Plan.tc_ID84304_AlterPlanName.AlterPlanName("test_AlterPlanName"))
	suite.addTest(Plan.tc_ID84313_DisablePlan.DisablePlan("test_DisablePlan"))
	suite.addTest(Plan.tc_ID84314_EnablePlan.EnablePlan("test_EnablePlan"))
	suite.addTest(Plan.tc_ID84340_PrintPlan.PrintPlan("test_PrintPlan"))
	suite.addTest(Plan.tc_ID84347_CheckDocumentInfoInPlan.CheckDocumentInfoInPlan("test_CheckDocumentInfoInPlan"))
	suite.addTest(Plan.tc_ID84360_AddTagInPlan.AddTagInPlan("test_AddTagInPlan"))
	suite.addTest(Plan.tc_ID84361_AddTagWithChiSpechrNameInPlan.AddTagWithChiSpechrNameInPlan("test_AddTagWithChiSpechrNameInPlan"))
	suite.addTest(Plan.tc_ID84364_CheckTagNumInPlan.CheckTagNumInPlan("test_CheckTagNumInPlan"))
	suite.addTest(Plan.tc_ID84365_CheckCaseNumWithTagInPlan.CheckCaseNumWithTagInPlan("test_CheckCaseNumWithTagInPlan"))
	suite.addTest(Plan.tc_ID84366_CheckPlanNumWithTagInPlan.CheckPlanNumWithTagInPlan("test_CheckPlanNumWithTagInPlan"))
	suite.addTest(Plan.tc_ID84367_CheckRunNumWithTagInPlan.CheckRunNumWithTagInPlan("test_CheckRunNumWithTagInPlan"))
	suite.addTest(Plan.tc_ID84368_EditTagInPlan.EditTagInPlan("test_EditTagInPlan"))
	suite.addTest(Plan.tc_ID84369_RemoveTagInPlan.RemoveTagInPlan("test_RemoveTagInPlan"))
	suite.addTest(Plan.tc_ID84379_CheckMyPlans.CheckMyPlans("test_CheckMyPlans"))
	suite.addTest(Plan.tc_ID84380_CheckMyPlanAuthor.CheckMyPlanAuthor("test_CheckMyPlanAuthor"))
	suite.addTest(Plan.tc_ID86752_AddMoreTagInPlan.AddMoreTagInPlan("test_AddMoreTagInPlan"))
	suite.addTest(Plan.tc_ID99073_CheckRunProgBarInPlan.CheckRunProgBarInPlan("test_CheckRunProgBarInPlan"))

	#Search related test cases (total: 34)
	suite.addTest(Search.tc_ID84335_SearchPlanBySomeOpts.SearchPlanBySomeOpts("test_SearchPlanBySomeOpts"))
	suite.addTest(Search.tc_ID84336_SearchPlanByTag.SearchPlanByTag("test_SearchPlanByTag"))
	suite.addTest(Search.tc_ID84338_PrintCopyInSearchPlanResult.PrintCopyInSearchPlanResult("test_PrintCopyInSearchPlanResult"))
	suite.addTest(Search.tc_ID84342_ExportNonePlanInSearchPlanResult.ExportNonePlanInSearchPlanResult("test_ExportNonePlanInSearchPlanResult"))
	suite.addTest(Search.tc_ID84619_SearchRunToEditRun.SearchRunToEditRun("test_SearchRunToEditRun"))
	suite.addTest(Search.tc_ID84627_SearchRunByAll.SearchRunByAll("test_SearchRunByAll"))
	suite.addTest(Search.tc_ID86691_QuickSearchCaseById.QuickSearchCaseById("test_QuickSearchCaseById"))
	suite.addTest(Search.tc_ID86695_QuickSearchPlanById.QuickSearchPlanById("test_QuickSearchPlanById"))
	suite.addTest(Search.tc_ID86696_QuickSearchRunById.QuickSearchRunById("test_QuickSearchRunById"))
	suite.addTest(Search.tc_ID86697_QuickSearchRunByName.QuickSearchRunByName("test_QuickSearchRunByName"))
	suite.addTest(Search.tc_ID86698_QuickSearchCaseByName.QuickSearchCaseByName("test_QuickSearchCaseByName"))
	suite.addTest(Search.tc_ID86699_QuickSearchPlanByName.QuickSearchPlanByName("test_QuickSearchPlanByName"))
	suite.addTest(Search.tc_ID86753_CreatePlanInSearchResult.CreatePlanInSearchResult("test_CreatePlanInSearchResult"))
	suite.addTest(Search.tc_ID86755_OpenPlanInSearchPlanResult.OpenPlanInSearchPlanResult("test_OpenPlanInSearchPlanResult"))
	suite.addTest(Search.tc_ID87466_SearchPlanByAllOptInASearch.SearchPlanByAllOptInASearch("test_SearchPlanByAllOptInASearch"))
	suite.addTest(Search.tc_ID87471_SearchPlanByFAutInASearch.SearchPlanByFAutInASearch("test_SearchPlanByFAutInASearch"))
	suite.addTest(Search.tc_ID87473_SearchCaseRunByPlanItemInASearch.SearchCaseRunByPlanItemInASearch("test_SearchCaseRunByPlanItemInASearch"))
	suite.addTest(Search.tc_ID87489_SearchCaseByAllOptInASearch.SearchCaseByAllOptInASearch("test_SearchCaseByAllOptInASearch"))
	suite.addTest(Search.tc_ID87494_SearchCaseByMAutTesterInASearch.SearchCaseByMAutTesterInASearch("test_SearchCaseByMAutTesterInASearch"))
	suite.addTest(Search.tc_ID87496_SearchPlanRunByCaseItemInASearch.SearchPlanRunByCaseItemInASearch("test_SearchPlanRunByCaseItemInASearch"))
	suite.addTest(Search.tc_ID87510_SearchRunByFMgrTesterInASearch.SearchRunByFMgrTesterInASearch("test_SearchRunByFMgrTesterInASearch"))
	suite.addTest(Search.tc_ID87512_SearchPlanCaseByRunItemInASearch.SearchPlanCaseByRunItemInASearch("test_SearchPlanCaseByRunItemInASearch"))
	suite.addTest(Search.tc_ID87516_ClickCaseNumInASearchPlanResult.ClickCaseNumInASearchPlanResult("test_ClickCaseNumInASearchPlanResult"))
	suite.addTest(Search.tc_ID87517_ClickRunNumInASearchPlanResult.ClickRunNumInASearchPlanResult("test_ClickRunNumInASearchPlanResult"))
	suite.addTest(Search.tc_ID87518_CreatePlanInASearchPlanResult.CreatePlanInASearchPlanResult("test_CreatePlanInASearchPlanResult"))
	suite.addTest(Search.tc_ID87519_CloneInASearchPlanResult.CloneInASearchPlanResult("test_CloneInASearchPlanResult"))
	suite.addTest(Search.tc_ID87520_PrintCopyInASearchPlanResult.PrintCopyInASearchPlanResult("test_PrintCopyInASearchPlanResult"))
	suite.addTest(Search.tc_ID87527_ExpandCaseInASearchCaseResult.ExpandCaseInASearchCaseResult("test_ExpandCaseInASearchCaseResult"))
	suite.addTest(Search.tc_ID87532_CloneInASearchCaseResult.CloneInASearchCaseResult("test_CloneInASearchCaseResult"))
	suite.addTest(Search.tc_ID87533_PrintCopyInASearchCaseResult.PrintCopyInASearchCaseResult("test_PrintCopyInASearchCaseResult"))
	suite.addTest(Search.tc_ID87538_CloneInASearchRunResult.CloneInASearchRunResult("test_CloneInASearchRunResult"))
	suite.addTest(Search.tc_ID92889_SearchPlanByProdVerInASearch.SearchPlanByProdVerInASearch("test_SearchPlanByProdVerInASearch"))
	suite.addTest(Search.tc_ID92890_SearchCaseByCaseProdInASearch.SearchCaseByCaseProdInASearch("test_SearchCaseByCaseProdInASearch"))
	suite.addTest(Search.tc_ID92891_SearchRunByProdVerInASearch.SearchRunByProdVerInASearch("test_SearchRunByProdVerInASearch"))

	return suite

if __name__ == "__main__":   unittest.main(defaultTest = 'suite')