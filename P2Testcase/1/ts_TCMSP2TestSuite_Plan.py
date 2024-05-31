from selenium import selenium
import unittest, time, re

from env import *

#(Total: 49)
#Plan related test cases (total: 49)
import Plan.tc_ID84262_CreatePlanWithExistingName, Plan.tc_ID84269_AddProduct, Plan.tc_ID84270_AddProductInVersion, Plan.tc_ID84271_AddVersion, Plan.tc_ID84272_AddExistProduct, Plan.tc_ID84274_ClonePlanWithCancelBtn, Plan.tc_ID84276_ClonePlanWithCreateCaseLink, Plan.tc_ID84280_ClonePlanWithoutCase, Plan.tc_ID84281_ClonePlanWithAttach, Plan.tc_ID84282_ClonePlanWithDocument, Plan.tc_ID84283_ClonePlanWithEnvironment, Plan.tc_ID84285_ClonePlanWithMeAsAuthor, Plan.tc_ID84286_ClonePlanWithMeAsTester, Plan.tc_ID84287_ClonePlanWithNewName, Plan.tc_ID84288_ClonePlanWithNewProduct, Plan.tc_ID84289_ClonePlanWithNewProductVersion, Plan.tc_ID84290_ClonePlanWithOriginalAuthor, Plan.tc_ID84291_ClonePlanWithOriginalTester, Plan.tc_ID84292_ClonePlanWithoutAttach, Plan.tc_ID84293_ClonePlanWithoutDocument, Plan.tc_ID84294_ClonePlanWithoutEnvironment, Plan.tc_ID84295_SetActive, Plan.tc_ID84296_SetInActive, Plan.tc_ID84302_SetEnvironment, Plan.tc_ID84305_SetParentId, Plan.tc_ID84306_SetProduct, Plan.tc_ID84307_SetProductVersion, Plan.tc_ID84308_SetPlanType, Plan.tc_ID84309_SetReferenceLink, Plan.tc_ID84310_SavePlanWithoutChange, Plan.tc_ID84316_ResetSearchPlan, Plan.tc_ID84320_SearchPlanByAuthor, Plan.tc_ID84332_SearchPlanByType, Plan.tc_ID84333_SearchPlanByProduct, Plan.tc_ID84337_PrintableNoPlans, Plan.tc_ID84349_NewCaseCheckRemoveComponent, Plan.tc_ID84352_RemoveAllComponent, Plan.tc_ID84353_RemoveOneComponent, Plan.tc_ID84354_UpdateMultiComponent, Plan.tc_ID84355_UpdateOneComponent, Plan.tc_ID84358_CheckAttachList, Plan.tc_ID84362_AddTagsByMultiTimesInCase, Plan.tc_ID84363_AddTagsToCases, Plan.tc_ID84376_RemoveChildNode, Plan.tc_ID86744_ClonePlanWithAllCases, Plan.tc_ID86750_RemoveTagFromCases, Plan.tc_ID86757_ClickCaseNumInSearchPlanResult, Plan.tc_ID86758_ClickRunNumInSearchPlanResult, Plan.tc_ID86759_ClickEditInSearchPlanResult

def suite():

	suite = unittest.TestSuite()

	#Plan related test cases (total: 49)
	suite.addTest(Plan.tc_ID84262_CreatePlanWithExistingName.CreatePlanWithExistingName("test_CreatePlanWithExistingName"))
	suite.addTest(Plan.tc_ID84269_AddProduct.AddProduct("test_AddProduct"))
	suite.addTest(Plan.tc_ID84270_AddProductInVersion.AddProductInVersion("test_AddProductInVersion"))
	suite.addTest(Plan.tc_ID84271_AddVersion.AddVersion("test_AddVersion"))
	suite.addTest(Plan.tc_ID84272_AddExistProduct.AddExistProduct("test_AddExistProduct"))
	suite.addTest(Plan.tc_ID84274_ClonePlanWithCancelBtn.ClonePlanWithCancelBtn("test_ClonePlanWithCancelBtn"))
	suite.addTest(Plan.tc_ID84276_ClonePlanWithCreateCaseLink.ClonePlanWithCreateCaseLink("test_ClonePlanWithCreateCaseLink"))
	suite.addTest(Plan.tc_ID84280_ClonePlanWithoutCase.ClonePlanWithoutCase("test_ClonePlanWithoutCase"))
	suite.addTest(Plan.tc_ID84281_ClonePlanWithAttach.ClonePlanWithAttach("test_ClonePlanWithAttach"))
	suite.addTest(Plan.tc_ID84282_ClonePlanWithDocument.ClonePlanWithDocument("test_ClonePlanWithDocument"))
	suite.addTest(Plan.tc_ID84283_ClonePlanWithEnvironment.ClonePlanWithEnvironment("test_ClonePlanWithEnvironment"))
	suite.addTest(Plan.tc_ID84285_ClonePlanWithMeAsAuthor.ClonePlanWithMeAsAuthor("test_ClonePlanWithMeAsAuthor"))
	suite.addTest(Plan.tc_ID84286_ClonePlanWithMeAsTester.ClonePlanWithMeAsTester("test_ClonePlanWithMeAsTester"))
	suite.addTest(Plan.tc_ID84287_ClonePlanWithNewName.ClonePlanWithNewName("test_ClonePlanWithNewName"))
	suite.addTest(Plan.tc_ID84288_ClonePlanWithNewProduct.ClonePlanWithNewProduct("test_ClonePlanWithNewProduct"))
	suite.addTest(Plan.tc_ID84289_ClonePlanWithNewProductVersion.ClonePlanWithNewProductVersion("test_ClonePlanWithNewProductVersion"))
	suite.addTest(Plan.tc_ID84290_ClonePlanWithOriginalAuthor.ClonePlanWithOriginalAuthor("test_ClonePlanWithOriginalAuthor"))
	suite.addTest(Plan.tc_ID84291_ClonePlanWithOriginalTester.ClonePlanWithOriginalTester("test_ClonePlanWithOriginalTester"))
	suite.addTest(Plan.tc_ID84292_ClonePlanWithoutAttach.ClonePlanWithoutAttach("test_ClonePlanWithoutAttach"))
	suite.addTest(Plan.tc_ID84293_ClonePlanWithoutDocument.ClonePlanWithoutDocument("test_ClonePlanWithoutDocument"))
	suite.addTest(Plan.tc_ID84294_ClonePlanWithoutEnvironment.ClonePlanWithoutEnvironment("test_ClonePlanWithoutEnvironment"))
	suite.addTest(Plan.tc_ID84295_SetActive.SetActive("test_SetActive"))
	suite.addTest(Plan.tc_ID84296_SetInActive.SetInActive("test_SetInActive"))
	suite.addTest(Plan.tc_ID84302_SetEnvironment.SetEnvironment("test_SetEnvironment"))
	suite.addTest(Plan.tc_ID84305_SetParentId.SetParentId("test_SetParentId"))
	suite.addTest(Plan.tc_ID84306_SetProduct.SetProduct("test_SetProduct"))
	suite.addTest(Plan.tc_ID84307_SetProductVersion.SetProductVersion("test_SetProductVersion"))
	suite.addTest(Plan.tc_ID84308_SetPlanType.SetPlanType("test_SetPlanType"))
	suite.addTest(Plan.tc_ID84309_SetReferenceLink.SetReferenceLink("test_SetReferenceLink"))
	suite.addTest(Plan.tc_ID84310_SavePlanWithoutChange.SavePlanWithoutChange("test_SavePlanWithoutChange"))
	suite.addTest(Plan.tc_ID84316_ResetSearchPlan.ResetSearchPlan("test_ResetSearchPlan"))
	suite.addTest(Plan.tc_ID84320_SearchPlanByAuthor.SearchPlanByAuthor("test_SearchPlanByAuthor"))
	suite.addTest(Plan.tc_ID84332_SearchPlanByType.SearchPlanByType("test_SearchPlanByType"))
	suite.addTest(Plan.tc_ID84333_SearchPlanByProduct.SearchPlanByProduct("test_SearchPlanByProduct"))
	suite.addTest(Plan.tc_ID84337_PrintableNoPlans.PrintableNoPlans("test_PrintableNoPlans"))
	suite.addTest(Plan.tc_ID84349_NewCaseCheckRemoveComponent.NewCaseCheckRemoveComponent("test_NewCaseCheckRemoveComponent"))
	suite.addTest(Plan.tc_ID84352_RemoveAllComponent.RemoveAllComponent("test_RemoveAllComponent"))
	suite.addTest(Plan.tc_ID84353_RemoveOneComponent.RemoveOneComponent("test_RemoveOneComponent"))
	suite.addTest(Plan.tc_ID84354_UpdateMultiComponent.UpdateMultiComponent("test_UpdateMultiComponent"))
	suite.addTest(Plan.tc_ID84355_UpdateOneComponent.UpdateOneComponent("test_UpdateOneComponent"))
	suite.addTest(Plan.tc_ID84358_CheckAttachList.CheckAttachList("test_CheckAttachList"))
	suite.addTest(Plan.tc_ID84362_AddTagsByMultiTimesInCase.AddTagsByMultiTimesInCase("test_AddTagsByMultiTimesInCase"))
	suite.addTest(Plan.tc_ID84363_AddTagsToCases.AddTagsToCases("test_AddTagsToCases"))
	suite.addTest(Plan.tc_ID84376_RemoveChildNode.RemoveChildNode("test_RemoveChildNode"))
	suite.addTest(Plan.tc_ID86744_ClonePlanWithAllCases.ClonePlanWithAllCases("test_ClonePlanWithAllCases"))
	suite.addTest(Plan.tc_ID86750_RemoveTagFromCases.RemoveTagFromCases("test_RemoveTagFromCases"))
	suite.addTest(Plan.tc_ID86757_ClickCaseNumInSearchPlanResult.ClickCaseNumInSearchPlanResult("test_ClickCaseNumInSearchPlanResult"))
	suite.addTest(Plan.tc_ID86758_ClickRunNumInSearchPlanResult.ClickRunNumInSearchPlanResult("test_ClickRunNumInSearchPlanResult"))
	suite.addTest(Plan.tc_ID86759_ClickEditInSearchPlanResult.ClickEditInSearchPlanResult("test_ClickEditInSearchPlanResult"))

	return suite

if __name__ == "__main__":
   unittest.main(defaultTest = 'suite')
