import requests
print(requests.__version__)
r = requests.get('https://www.google.com/') 
print(r.text)
r_p = requests.get('https://raw.githubusercontent.com/yixianLu/lab1/main/script.py')
print(r_p.text)
