import requests
import json
from datetime import date

Pincode = "175018"
District_code = "215"
Date =  date.today().strftime(format='%d-%m-%Y')
# FOR PINCODE
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(Pincode,Date)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}

data = requests.get(url,headers=headers)

resp = json.loads(data.text)

avail = False

for centers in resp['centers']:
    for sess in centers['sessions']:
        if int(sess["min_age_limit"])==18:
            print(centers)
            avail = True

url  = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(District_code,Date)
data = requests.get(url,headers=headers)

resp = json.loads(data.text)

for centers in resp['centers']:
    for sess in centers['sessions']:
        if int(sess["min_age_limit"])==18:
            print(centers)
            avail = True


if not avail:
    print('No Slots available')