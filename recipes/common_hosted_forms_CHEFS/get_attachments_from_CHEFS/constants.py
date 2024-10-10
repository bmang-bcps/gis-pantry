import os
import dotenv

envPath = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(envPath):
    print("loading dot env...")
    dotenv.load_dotenv()

form_id = os.environ["form_id"]
api_token = os.environ["api_token"]
version = os.environ["version"]
component_name = os.environ["component_name"]
out_folder = os.environ["out_folder"]
