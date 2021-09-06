import requests

url = "http://127.0.0.1:5000/data"

new_data_1 = {'id':'1',  'name':'smriti'}
new_data_2 = {'id':'2',  'name':'mithali'}
new_data_3 = {'id':'3',  'name':'harmanpreet'}

post_resp = requests.post(url, data=new_data_1)
get_resp = requests.get(url)

