from search_new_event import *
from find_near_objects import *
import datetime

# if i=1 it shows that this is isnt the first run of the code
i = 0
# list for all the events
main_lst = []
# list for events that we dont know their type
unk_events = []
# list of events that have no near objs
hand_events = []
# list of events that the closest obj to them is one from the list
scd_pry_events = []
lst_of_scd_pry_obj_type = [b'PN', b'V*', b'Cl']
folder_path = 'C:/Users/user/Documents/astro/'
first_radius_search = 0.003    # in deg
second_radius_search = 0.001   # in deg
dist_from_the_milkyway = 5     # in deg


def __main__():
    sdate = datetime.datetime(2020, 1, 25, hour=2, minute=20, second=35)
    fdate = datetime.datetime(2020, 1, 25, hour=2, minute=20, second=37)
    day_delta = datetime.timedelta(days=1)
    add_new_events(sdate, fdate, day_delta)
    # sdate = datetime.datetime.today()
    print("the start date:")
    print(sdate)


'''
this function add new events from the tns database into the new_events folder
input: datetime start_date - a time to start the looking for a new event
       datetime final_date - a time to stop the looking for a new event
       datetime day_delta - the amount of time between the start and final date
output: void, added events to new_events folder  
'''


def add_new_events(start_date, final_date, day_delta):
    lst = find_new_events(start_date, final_date, day_delta)
    for obj in lst:
        if obj not in main_lst:
            main_lst.append(obj)
    print("The main list is:")
    print(main_lst)
    # print(len(main_lst))


'''
this function find out if the events in the  new_events folder have been given a type (were discover)
input: null
output: unk_events list, added events to unk_events folder  
'''


def find_if_discoverd():
    for obj in main_lst:
        if obj['data']['reply']['type'] == None:
            if obj not in unk_events:
                f = open(folder_path+'/info/'+str(obj['data']['received_data']['objname'])+'.txt', 'w+')
                # print(obj)
                json.dump(obj, f)
                unk_events.append(obj)
    return (unk_events)


__main__()
find_if_discoverd()
print("the unk_event list len "+str(len(unk_events)))
search_near_objs(folder_path, hand_events, scd_pry_events, first_radius_search, second_radius_search,
                 dist_from_the_milkyway, lst_of_scd_pry_obj_type)
# add_info_for_events(folder_path)