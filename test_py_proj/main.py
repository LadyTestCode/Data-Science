
from dotenv import load_dotenv
import os  

def print_author():
	load_dotenv(dotenv_path='../.env')
	author = os.getenv('AUTHOR')
	print(f"The author is: {author}")

print_author()              