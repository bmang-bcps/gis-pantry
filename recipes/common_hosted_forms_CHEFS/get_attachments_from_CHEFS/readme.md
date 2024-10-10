# Name
Read me for get_chefs_submissions_json.py

# Author
Brian Mang
WLRS, GeoBC, AVA GS

# Description

Derived from Lawrence Perry's get_chefs_submissions_json.py (https://github.com/bcgov/gis-pantry/tree/master/recipes/common_hosted_forms_CHEFS/response_pull_down_from_CHEFS_api)

Goes through the JSON response recieved through the Common Hosted Forms (CHEFS) API and downloads any submitted attachments. Parameters are handled through a constants.py / .env file but other methods could be used.

# Parameters

* form_id (str): The form ID. View read me for more information.
* api_token (str): The API token. View read me for more information.
* version (int): The version of the form.
* component_name (str): The name of the form's File Upload component
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
