#!/usr/bin/env python
# "*" coding: utf"8 "*"

"""
SuccessFactors EC API Toolkit " Configuration File

This file contains all configuration variables for the SuccessFactors EC API Toolkit.
Keep this file secure and do not share it with the script.
"""

import os

# =============================================================================
# API Connection Settings
# =============================================================================

# 1.1 Production Authentication
# IMPORTANT: Use environment variables for credentials. See .env.example for template
API_SERVER = os.getenv('API_SERVER', 'api44.sapsf.com')
USERNAME = os.getenv('USERNAME', 'YOUR_USERNAME')
PASSWORD = os.getenv('PASSWORD', 'YOUR_PASSWORD')
BEARER_TOKEN = os.getenv('BEARER_TOKEN', 'YOUR_BEARER_TOKEN')  # Set in environment
ZH_BEARER_TOKEN = os.getenv('ZH_BEARER_TOKEN', 'YOUR_ZH_BEARER_TOKEN')  # Set in environment

# 1.2 Testing Authentication
# IMPORTANT: Use environment variables for credentials. See .env.example for template
TEST_API_SERVER = os.getenv('TEST_API_SERVER', 'api44.sapsf.com')
API_USERNAME = os.getenv('API_USERNAME', 'YOUR_TEST_USERNAME')
API_PASSWORD = os.getenv('API_PASSWORD', 'YOUR_TEST_PASSWORD')
Test_BEARER_TOKEN = os.getenv('TEST_BEARER_TOKEN', 'YOUR_TEST_BEARER_TOKEN')  # Set in environment
ZH_Test_BEARER_TOKEN = os.getenv('ZH_TEST_BEARER_TOKEN', 'YOUR_ZH_TEST_BEARER_TOKEN')  # Set in environment

# Fixed postman authentication information
# AUTH_TYPE = "Basic"
AUTH_TYPE = os.getenv('AUTH_TYPE', 'Bearer')
AUTH_VALUE = os.getenv('AUTH_VALUE', 'YOUR_AUTH_VALUE')  # Set in environment

# =============================================================================
# Employee Data for Testing
# =============================================================================

EMPLOYEE_ID = "00002005170"  # Used for filtering API results
TEST_EMPLOYEE_ID = "APITEST00002005170"  # Used for testing API requests in Upsert
POSITION = "Test0018225"
EVENT_REASON = "HIR"
REHIRE_REASON = "REHIRE"
HIRE_DATE = "/Date(1763626277000)/"
NOSHOW_DATE = "/Date(1763626277000)/"
TER_EVENT_REASON = "NS"
RELATED_PERSONIDEXTERNAL = "APITEST00002005170_01"
BACKGROUND_ID = "0"

# =============================================================================
# API Endpoints and Entity Sets
# =============================================================================

# API Endpoints
API_ENDPOINT = f"https://{TEST_API_SERVER}/odata/v2/upsert?$format=json"

# Entity Sets for API Operations
ENTITY_SETS = [
"User", "PerPerson", "EmpEmployment", "EmpJob", "PerPersonal", 
    #"PerGlobalInfoCHN","PerGlobalInfoCAN","PerGlobalInfoUSA","PerGlobalInfoIND","PerGlobalInfoMYS","PerGlobalInfoPHL","PerGlobalInfoSGP","PerGlobalInfoTHA","PerGlobalInfoGBR","PerGlobalInfoVNM","PerGlobalInfoKHM",
    #"EmpJobRelationships", "EmpCompensation", "EmpPayCompRecurring", "EmpPayCompNonRecurring", "EmpWorkPermit",  
    "PerNationalId", 
    #"PerEmail", "PerPhone", "PerPersonRelationship", "PerAddressDEFLT", "PerEmergencyContacts",
    "PaymentInformationV3", "PaymentInformationDetailV3","cust_PaymentInformationDetailV3CHN",
    #"EmpCostDistribution","EmpCostDistributionItem",
    #"Background_OutsideWorkExperience", "Background_Education", "Background_Certificates", "Background_Languages","Background_Memberships","Background_Awards",
    "EmpEmploymentTermination",
    #"Photo",
    "Position", "FODepartment", "PickListValueV2","FOJobCode",
    #"HireDateChange",
    #"cust_PayResult","cust_PayResult_item",
    #"cust_globalPayresult","cust_globalPayresult_item",
    #"cust_TimeAccount","cust_TimeAccount_item","cust_LeaveOfAbsence","cust_LeaveOfAbsence_item",
    "cust_LOA","cust_LOAItem",
    #"cust_onb_Education_Main","cust_onb_Education",
    #"cust_onb_LanguageSkills_main","cust_onb_LanguageSkills",
    #"cust_onb_ProfessionalQualification_main","cust_onb_ProfessionalQualification",
    #"cust_onb_PriorWorkExperience_main","cust_onb_PriorWorkExperience",
    #"cust_Membership","cust_onb_Membership",
    #"cust_onb_LastSalaryPackage_main","cust_onb_LastSalaryPackage_item",
    #"cust_GroupMedicalInsurance","cust_GroupMedicalInsurance_item",
    #"cust_PhysicalExam","cust_PhysicalExam_item",
    #"cust_RetirementScheme","cust_RetirementScheme_item",
    #"cust_ExternalLearningHistory_Parent","cust_ExternalLearningHistory_Child"
]
GOListENTITY_SETS = [
    "FOLocation", "FOEventReason", "FOPayComponent", "FOPayGroup", "FOFrequency", "Bank"
]

# =============================================================================
# File Paths
# =============================================================================

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
EC_TABLE_ATTRIBUTE = os.path.join(SCRIPT_DIR, "1.SF EC Table API Attribute.xlsx")
INTEGRATION_FILE = os.path.join(SCRIPT_DIR, "2.SF Query Integration Standard API TemplateV1.xlsx")
EXCEL_OUTPUT_PATH = os.path.join(SCRIPT_DIR, "3.SF EC Field API Attribute.xlsx")
EXCEL_FILE = os.path.join(SCRIPT_DIR, "4.SF New Hire Sample API Upsert.xlsx")
OUTPUT_FILE = os.path.join(SCRIPT_DIR, "5.SF New Hire API Post Preview.xlsx")
PICKLIST_OUTPUT_PATH = os.path.join(SCRIPT_DIR, "6.SF Dropdown CodeValue Table.xlsx")
NEW_FILE = os.path.join(SCRIPT_DIR, "7.SF Standard New Hire API DocumentV1.xlsx")
POSTMAN_EXCEL_OUTPUT = os.path.join(SCRIPT_DIR, "8.SF New Hire Postman_Collection Excel.xlsx")
POSTMAN_COLLECTION_OUTPUT = os.path.join(SCRIPT_DIR, "9.SF New Hire Postman_Collection.json")

# =============================================================================
# Constants
# =============================================================================

MAX_SHEETNAME_LEN = 31

# XML Namespaces for Metadata Parsing
ns = {
    'edmx': 'http://schemas.microsoft.com/ado/2007/06/edmx',
    'm': 'http://schemas.microsoft.com/ado/2007/08/dataservices/metadata',
    '': 'http://schemas.microsoft.com/ado/2008/09/edm',
    'sap': 'http://www.successfactors.com/edm/sap'
}