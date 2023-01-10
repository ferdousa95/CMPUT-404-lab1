import requests

"""
Leaving commented code for TA if they needs to check earlier examples. 
"""

url = 'https://raw.githubusercontent.com/ferdousa95/CMPUT-404-lab1/main/lab1_work.py'
print(requests.get(url).text)
