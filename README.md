# SuccessFactors API Documentation Generator Script Explanation

This document provides a detailed explanation of the `generate_sf_api_doc.py` Python script. This script is designed to automate the creation of technical documentation for SuccessFactors OData APIs by extracting metadata, querying endpoints, and compiling the results into a standardized Excel format.

## Overview

The script performs three main functions:
1.  **Authentication**: Handles OAuth 2.0 authentication (via SAML assertion) to securely connect to SuccessFactors.
2.  **Metadata Extraction**: Downloads OData `$metadata` schemas for configured entities to understand field attributes (types, keys, lengths, labels).
3.  **Documentation Generation**: Queries specific API endpoints defined in a master list, parses the JSON responses, and generates a multi-sheet Excel file detailing the fields, paths, and sample values, enriched with the extracted metadata.

## Prerequisites & Configuration

The script relies on a configuration file `config_SF.py` located in the same directory. This file stores:
*   **Authentication Config**: `SF_CLIENT_ID`, `SF_USER_ID`, `SF_COMPANY_ID`, `SF_PRIVATE_KEY`, etc.
*   **Target Entities**: `ENTITY_SETS` list defining which API entities to process (e.g., "User", "EmpEmployment").
*   **File Paths**: Locations for input templates and output files.

### dependencies
The script uses the following Python libraries:
*   `requests`: For making HTTP API calls.
*   `openpyxl`: For reading and writing Excel files.
*   `pandas`: For data manipulation and sorting.
*   `xml.etree.ElementTree`: For parsing XML metadata from OData services.

## Script Workflow

The `main()` function coordinates the execution flow:

### 1. Authentication
*   **Goal**: Obtain a valid Bearer Token for API requests.
*   **Process**:
    1.  Calls `get_assertion()` to generate a SAML assertion signed with the private key.
    2.  Calls `get_access_token(assertion)` to exchange the assertion for an OAuth 2.0 access token.
    3.  Stores the token in `DYNAMIC_ACCESS_TOKEN` for use in subsequent requests.
    4.  **Fallback**: If dynamic auth fails, it falls back to a hardcoded `BEARER_TOKEN` or Basic Authentication (`USERNAME`/`PASSWORD`) from config.

### 2. Metadata Extraction (`extract_ec_odata_api_dictionary`)
*   **Goal**: Build a dictionary of all possible fields for the target entities.
*   **Process**:
    1.  Iterates through `ENTITY_SETS` (from config).
    2.  Fetches `https://<server>/odata/v2/<entity>/$metadata`.
    3.  Parses the XML response to find `EntityType` and `Property` definitions.
    4.  Extracts attributes: `Name`, `Type`, `MaxLength`, `Label` (sap:label), `required`, `creatable`, `plicklist`, etc.
    5.  Distinguishes between standard fields and navigation properties.
    6.  **Output**: Saves this raw metadata to `3.SF EC Field API Attribute.xlsx` (Sheet: "Simple EC Data API Dictionary") and returns a DataFrame.

### 3. API Query & Sheet Generation
*   **Goal**: Create the final documentation based on a "Master Table List" of required endpoints.
*   **Process**:
    1.  **Load Template**: Opens `2.SF Query Integration Standard API TemplateV1.xlsx`.
    2.  **Read Master List**: Reads the "SF Master Table List" sheet to find rows where:
        *   System is "SuccessFactors"
        *   Category is "API Resource"
    3.  **Execute Queries**: For each matching row:
        *   Constructs the full API endpoint URL (replacing placeholders like `{{Test_API-Server}}`).
        *   Executes the GET request.
        *   **Parse Response**: Uses `parse_api_response` to flatten the JSON result into a list of fields, including their JSON paths (e.g., `d.results[0].userId`) and sample values.
    4.  **Generate Sheet**:
        *   Copies the "API Template" sheet.
        *   Renames it to the "API Name" (truncated to 31 chars).
        *   Fills header info (Trigger Point, Data Flow, Endpoint URL).
        *   Fills the Sample Response block (truncated to top 3 items for brevity).
    5.  **Enrich Data**:
        *   Iterates through the parsed fields.
        *   Fills Excel columns for Field Name, Path, Entity, and Sample Value.
        *   **Lookup**: Searches the metadata dictionary (from Step 2) to fill in technical details like **Label**, **Type**, **Length**, **Picklist**, and **Required** status.

### 4. Cleanup & Final Save
*   **Goal**: Remove unused data to keep the documentation clean.
*   **Process**:
    *   Scans "SF Master Data Dictionary" and "SF DropdownList Mapping" sheets (if they exist).
    *   Deletes rows that were not referenced by any of the queried endpoints in the current run.
    *   Saves the final workbook as `SF_API_Documentation_Generated.xlsx`.

## Key Functions

| Function | Description |
| :--- | :--- |
| `get_assertion()` | Generates the SAML assertion payload for OAuth. |
| `get_access_token()` | Exchanges SAML assertion for an access token via POST request. |
| `make_request()` | Wrapper for HTTP requests; handles auth headers and fallbacks. |
| `extract_ec_odata_api_dictionary()` | Downloads and transforms OData XML metadata into a structured DataFrame. |
| `parse_api_response()` | Recursively traverses JSON API responses to flatten nested structures and capture JSON paths. |

## Output Files

1.  **`SF_API_Documentation_Generated.xlsx`**: The main output. Contains:
    *   **SF Master Table List**: Updated with sample JSON responses.
    *   **[API Name] Sheets**: One sheet per endpoint, detailing every field's path, type, and description.
2.  **`3.SF EC Field API Attribute.xlsx`**: Intermediate file containing the raw dictionary of all fields and their attributes for the configured entities.
