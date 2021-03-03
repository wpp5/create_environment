import os
from dotenv import load_dotenv
load_dotenv() #> loads contents of the .env file into the script's environment
print(os.getenv("SECRET_MESSAGE"))
