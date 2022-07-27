import requests
import json
import argparse
import os
import sys
import colors as c
from datetime import datetime

my_parser = argparse.ArgumentParser(description='List the content of a folder')
my_parser.add_argument('API_TOKEN',
                       metavar='API_TOKEN',
                       type=str,
                       help='City to show the forecast for (eg. Paris)')
my_parser.add_argument('City',
                       metavar='city',
                       type=str,
                       help='City to show the forecast for (eg. Paris)')

args = my_parser.parse_args()
token = args.API_TOKEN
city = args.City

now = datetime.now()
current_time = now.strftime("%Y-%m-%d %H")
current_time += ':00'


parameters = {
    "key": f"{token}",
    "q": f"{city}",
    "days": "1"
}

response = requests.get("http://api.weatherapi.com/v1/forecast.json", parameters)


for obj in response.json()["forecast"]["forecastday"]:
	for t in obj['hour']:
		if t['time'] == current_time:
			length = len(f"{t['time']} {c.LIGHT_GREEN}{t['temp_c']}°C{c.END}")
			print(f"{c.YELLOW}-{c.END}" * length)
			print(f"{t['time']} {c.LIGHT_GREEN}{t['temp_c']}°C {c.YELLOW}CURRENT{c.END}")
			print(f"{c.YELLOW}-{c.END}" * length)
		else:
			print(f"{t['time']} {c.LIGHT_GREEN}{t['temp_c']}°C{c.END}")



