[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/THAVASIGTI/pycovid_india)
[![PyPI](https://img.shields.io/pypi/v/pycovid-india)](https://pypi.org/project/pycovid-india)

### india_covid

Indian COVID-19 Vaccine and Cases Status
Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus. Most people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment.

## import package

``` python
Python 3.6.9 (default, Jan 26 2021, 15:33:00) 
[GCC 8.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pycovid_india
>>> inCovid = pycovid_india.CovidInfo()
>>> 
>>> 
```

## Get State id
- this `id` state code. return value dict format.

``` python
>>>
>>> inCovid.get_state_id
```
output:
``` json
{
    "0": "Andaman and Nicobar",
    "1": "Andhra Pradesh", 
    "2": "Arunachal Pradesh", 
    "3": "Assam", 
    "4": "Bihar", 
    "5": "Chandigarh", 
    "6": "Chhattisgarh", 
    "7": "Dadra and Nagar Haveli and Daman and Diu", 
    "8": "Delhi", 
    "9": "Goa", 
    "10": "Gujarat", 
    "11": "Haryana", 
    "12": "Himachal Pradesh", 
    "13": "Jammu and Kashmir", 
    "14": "Jharkhand", 
    "15": "Karnataka", 
    "16": "Kerala", 
    "17": "Ladakh", 
    "18": "Lakshadweep", 
    "19": "Maharashtra", 
    "20": "Manipur", 
    "21": "Meghalaya", 
    "22": "Mizoram", 
    "23": "Madhya Pradesh", 
    "24": "Nagaland", 
    "25": "Odisha", 
    "26": "Puducherry", 
    "27": "Punjab", 
    "28": "Rajasthan", 
    "29": "Sikkim", 
    "30": "Tamil Nadu", 
    "31": "Telengana", 
    "32": "Tripura", 
    "33": "Uttar Pradesh", 
    "34": "Uttarakhand", 
    "35": "West Bengal"
}
```

## india covid vaccine last update infomation

``` python
>>>
>>> inCovid.get_covid_vaccine_last_update()
```
output:
``` json
{
    "day": "2021-05-29",
    "india_dose1": 167617477, 
    "india_dose2": 44449137, 
    "india_total_doses": 212066614, 
    "india_last_dose1": 164779253, 
    "india_last_dose2": 44123192, 
    "india_last_total_doses": 208902445
}

```

## get state covid cases infomation and covid acivity 

input id is state code `16` 

``` python
>>> inCovid.get_state_covid_info(16)
```
output:
``` json
{
    "Name of State / UT": "Kerala", 
    "state_code": "32", 
    "abbreviation_code": "KL", 
    "state_helpline": "0471-2552056", 
    "covid_portal_url": "http://dhs.kerala.gov.in/public-health-2019-n-corona-virus/", 
    "covid_facilities": "http://arogyakeralam.gov.in/2020/03/25/guidelines/", 
    "state_donation_url": "https://donation.cmdrf.kerala.gov.in/", 
    "Total Confirmed cases": "2494385", 
    "Active": "233425", 
    "Cured/Discharged/Migrated": "2252505", 
    "Death": "8455", 
    "whatsapp_chatbot_url": "https://wa.me/919072220183?text=Hi", 
    "fb_chatbot_url": "", 
    "epass_url": "https://covid19jagratha.kerala.nic.in/home/addDomestic", 
    "last_confirmed_covid_cases": "2470872", 
    "last_cured_discharged": "2224405", 
    "last_death": "8257", 
    "last_active_covid_cases": "238210", 
    "diff_confirmed_covid_cases": "23513", 
    "diff_cured_discharged": "28100", 
    "diff_death": "198", 
    "diff_active_covid_cases": "-4785"
}

```
## get state covid vaccine activity

this id state code `30`

``` python
>>> inCovid.get_state_covid_vaccine_info(30)
```
output
``` json
{
    "st_name": "Tamil Nadu", 
    "state_id": "31", 
    "covid_state_name": "Tamil Nadu", 
    "covid_state_id": "33", 
    "dose1": "6782968", 
    "dose2": "2013165", 
    "total_doses": "8796133", 
    "last_dose1": "6523932", 
    "last_dose2": "1995551", 
    "last_total_doses": "8519483"
}
```