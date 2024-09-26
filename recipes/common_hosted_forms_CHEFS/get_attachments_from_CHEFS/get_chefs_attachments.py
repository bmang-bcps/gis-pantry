# --------------------------------------------------------------------------------------------------
# Author: Brian Mang
# Ministry, Division, Branch: WLRS, GeoBC, AVA GS
# Updated: 2024-09-19
# Description:
#    Derived from Lawrence Perry's get_chefs_submissions_json.py
#    https://github.com/bcgov/gis-pantry/tree/master/recipes/common_hosted_forms_CHEFS/response_pull_down_from_CHEFS_api
#    Pull attachments off submitted forms using the Common Hosted Forms (CHEFS) API.
# --------------------------------------------------------------------------------------------------
import requests
import base64
import logging
import constants

logging.basicConfig(level=logging.INFO, format="%(levelname)s | %(asctime)s | %(message)s", datefmt='%Y-%m-%d %H:%M:%S %z')

def get_chefs_submissions_json(form_id, api_token, version, component_name, out_folder):
    """
    Returns the JSON response from the CHEFS API for the specified form ID, API token, and version.

    Args:
        form_id (str): The form ID. View read me for more information.
        api_token (str): The API token. View read me for more information.
        version (int): The version of the form.
        component_name (str): The name of the form's File Upload component
        out_folder (str): The folder location to save the attachments
    
    Returns:
        dict: The JSON response from the CHEFS API.
    """
    username_password = f'{form_id}:{api_token}'
    base64_encoded_credentials = base64.b64encode(username_password.encode("utf-8")).decode("utf-8")

    headers = {
        "Authorization": f"Basic {base64_encoded_credentials}"
    }
    url = f"https://submit.digital.gov.bc.ca/app/api/v1/forms/{form_id}/export"

    # remove status to grab attachments from all forms 
    # or set to SUBMITTED, ASSIGNED, COMPLETED or REVISED for specific forms
    params = {
        "version": version,
        "format": "json",
        "type": "submissions",
        "status": "SUBMITTED"
    }
    
    # get the submission response
    response = requests.get(url, headers=headers, params=params)
    
    # go through the JSON
    for form in response.json():
        
        # get attachment information from form with name of the File Upload component as key
        attachment = form[f"{component_name}"]
       # iterate through list to get attachment properties
        for att_info in attachment:
            # get attachment id
            data_id = att_info["data"]["id"]
            # get attachment name
            original_name = att_info["originalName"]
            # get attachment URL
            attachment_url = f"https://submit.digital.gov.bc.ca/app/api/v1/files/{data_id}"
            # get attachment response
            att_response = requests.get(attachment_url, headers=headers, stream=True)
            # attempt to download attachments
            if att_response.status_code == 200:
                # save attachments to output folder
                with open(f"{out_folder}/{original_name}", 'wb') as file:
                    # stream the content in chunks to avoid large memory usage
                    for chunk in att_response.iter_content(chunk_size=8192):
                        file.write(chunk)
            else:
                logging.info(f"Failed to download file. Status code: {att_response.status_code}, Message: {att_response.text}")
            
    return response

response = get_chefs_submissions_json(constants.form_id, constants.api_token, constants.version, constants.component_name, constants.out_folder)
