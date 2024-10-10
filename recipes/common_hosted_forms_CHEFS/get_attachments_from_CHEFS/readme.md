# Name
Read me for get_chefs_submissions_json.py

# Author
Brian Mang
WLRS, GeoBC, AVA GS

# Description

Derived from Lawrence Perry's [get_chefs_submissions_json.py](https://github.com/bcgov/gis-pantry/tree/master/recipes/common_hosted_forms_CHEFS/response_pull_down_from_CHEFS_api)

Goes through the JSON response recieved through the Common Hosted Forms (CHEFS) API and downloads any submitted attachments. Parameters are handled through a constants.py / .env file but other methods could be used.

# Parameters

* form_id (str): The ID of your form. The form ID is the alphanumberic string located at the end of your form's URL when viewed it in a browser <span>ht</span>tps://submit.digital.gov.bc.ca/app/form/submit?f=[form_id]
* api_token (str): The [API key](https://developer.gov.bc.ca/docs/default/component/chefs-techdocs/Capabilities/Data-Management/Generating-API-keys/) for your form.
* version (int): The version of the form.
* component_name (str): The Property Name of the form's [File Upload component](https://developer.gov.bc.ca/docs/default/component/chefs-techdocs/Components/Form-Builder/BC-Government/#file-upload) accessed from the File Upload Component's API tab from the Form Builder.
* out_folder (str): The folder location to save the attachments

# Dependencies/Requirements/Environments

* Requests
* Base64
* Constants / dotenv (optional)
* Logging

# Known Bugs/Limitations

None known

# Update Log

Uploaded - 2024-09-26
