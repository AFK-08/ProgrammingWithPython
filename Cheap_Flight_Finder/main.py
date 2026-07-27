import requests
import requests_cache
from data_manager import DataManager

Accessing_sheet = DataManager()
sheet_data = Accessing_sheet.get_data()

