
import requests

mbox = requests.get('http://www.py4inf.com/code/mbox.txt').text

all_lines = mbox.split('\n')
print(all_lines)