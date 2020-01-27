from connect_to_TNS import *
import json


# API key for Bot
api_key = "abf86f8ae8ea7f24e611fe7ec352eced3d2418e0"
# list that represents json file for search obj
search_obj = [("ra", ""), ("dec", ""), ("radius", ""), ("units", ""), ("objname", ""), ("internal_name", "")]
# list that represents json file for get obj
get_obj = [("objname", ""), ("photometry", "0"), ("spectra", "1")]

# url of TNS and TNS-sandbox api
url_tns_api = "https://wis-tns.weizmann.ac.il/api/get"
url_tns_sandbox_api = "https://sandbox-tns.weizmann.ac.il/api/get"


def check_the_response(response):
    if None not in response:
        # Here we just display the full json data as the response
        json_data = format_to_json(response.text)
        return json_data
    else:
        print(response[1])


'''
this function called by add_new_event function (in main model) and connect to the tns website 
     and get the events that happend in the date requested
input: datetime sdate - a time to start the looking for a new event
       datetime fdate - a time to stop the looking for a new event
       datetime day_delta - the amount of time between the start and final date
output: list - lst of all the object that were found
'''
# go over the dates and per day give a list of obj


def find_new_events(sdate, fdate, day_delta):
    # do a loop on days and get the info
    for i in range((fdate - sdate).days+1):
        date = sdate + i*day_delta
        search_obj.append(('public_timestamp', str(date)))
        response = search(url_tns_api, search_obj)
        json_data = check_the_response(response)
        dy = json.loads(json_data)
        # a list oa all the objects from that date
        lst_of_obj = dy['data']['reply']
        # go over the objects per day
        for obj in lst_of_obj:
            # print("name  "+obj['objname'])
            response = get(url_tns_api, obj)
            json_data = check_the_response(response)
            ob = json.loads(json_data)
            lst_of_obj[lst_of_obj.index(obj)] = ob
            # print(ob)
        return lst_of_obj

