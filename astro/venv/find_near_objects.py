from astroquery.ned import Ned
import astropy.units as u
from astropy import coordinates
from astropy.coordinates import Galactic
import os
import json
import math
from numpy import ma
from astropy.cosmology import FlatLambdaCDM


# check if co is in the co of a big galaxys from benny's table
def near_a_big_galaxy(obj, co, folder_path):
    f = open(folder_path + 'list_of_large_galaxies' + '.txt')
    f.readline()
    for line in f:
        lst_line = line.split()
        g_name = lst_line[0]
        g_center = coordinates.SkyCoord(float(lst_line[1]), float(lst_line[2]), unit='deg')
        dst_from_cet = co.separation(g_center)
        g_radius = coordinates.Angle(float(lst_line[3]) / 2, unit='arcmin')
        if dst_from_cet < g_radius:
            obj['comments'] = obj['comments'] + ',too close to ' + g_name


# check if co is next to the milkyway galaxy
def near_the_milky_way(co, obj, dist_from_the_milkyway):
    co_galactic = co.transform_to(Galactic)
    if co_galactic.b in range(-dist_from_the_milkyway, dist_from_the_milkyway):
        obj['comments'] = 'found in a dist smaller than ' + dist_from_the_milkyway + ' to the millkyway'


def insert_data_from_redshift(obj, closest_obj):
    obj['data']['reply']['redshift'] = closest_obj[6]
    redshift = closest_obj[6]
    cosmo = FlatLambdaCDM(H0=70, Om0=0.3)
    dl = cosmo.luminosity_distance(redshift)
    obj['data']['reply']['luminosity_distance'] = {'value': dl.value, 'unit': dl.unit}
    m_source = obj['data']['reply']['discoverymag'] - 5*(math.log(float(dl.to(u.parsec).to_value()), 10)-1)
    obj['data']['reply']['sourcemag'] = m_source
    distance_modulus_miu = obj['data']['reply']['discoverymag'] - m_source
    obj['data']['reply']['distance_modulus_miu'] = distance_modulus_miu


def search_near_objs(folder_path, hand_events, scd_pry_events, first_radius_search, second_radius_search,
                     dist_from_the_milkyway, lst_of_scd_pry_obj_type):
    for filename in os.listdir(folder_path + 'info'):
        if filename.endswith(".txt"):
            file_path = folder_path+'info/'+filename
            with open(file_path) as json_file:
                obj = json.load(json_file)
                if obj.get('comment', '0') == '0':
                    obj['comments'] = ''
            co = coordinates.SkyCoord(ra=obj['data']['reply']['radeg'], dec=obj['data']['reply']['decdeg'],
                                      unit=(u.deg, u.deg), frame='fk5')
            near_the_milky_way(co, obj, dist_from_the_milkyway)    # if yes add it to the comments
            near_a_big_galaxy(obj, co, folder_path)   # do def near_a_big_galaxy(co) if yes add to a diffrent list.
            near_objs = Ned.query_region(co, radius=first_radius_search * u.deg, equinox='J2000.0')
            if len(near_objs) == 0:
                hand_events.append(obj)
                f = open(folder_path + 'hand_eve/' + str(obj['data']['received_data']['objname']) + '.txt', 'w+')
                json.dump(obj, f)
                os.remove(file_path)
            else:
                min = near_objs[0][9]
                closest_obj = near_objs[0]
                for line in near_objs:
                    if line[9] <= min:
                        min = line[9]
                        closest_obj = line
                # find if the closest obj is from a certian type
                if closest_obj[4] in lst_of_scd_pry_obj_type:
                    scd_pry_events.append(closest_obj)
                    f = open(folder_path+'scd_pry_eve/' + str(obj['data']['received_data']['objname']) + '.txt', 'w+')
                    json.dump(obj, f)
                if closest_obj[9] > second_radius_search:
                    obj['comments'] = obj['comments'] + ',the closest obj far from ' + str(second_radius_search)
                obj['closest_obj'] = []
                obj['closest_obj'].append({'name': closest_obj[1], 'type': closest_obj[4], 'dist': closest_obj[9],
                                      'diameter': {'value': closest_obj[15], 'unit': 'Diameter points'}})
                if closest_obj[6] is not ma.masked:  # there is info about the redshift
                    insert_data_from_redshift(obj, closest_obj)
                os.remove(file_path)
                new = str(obj)
                f = open(folder_path + 'found_near_obj/' + str(obj['data']['received_data']['objname']) + '.txt', 'w+')
                json.dump(new, f)
            continue
        else:
            continue

'''
def add_info_for_events(folder_path):
    for filename in os.listdir(folder_path + 'found_near_obj'):
        if filename.endswith(".txt"):
            file_path = folder_path+'found_near_obj/'+filename
            with open(file_path) as json_file:
                obj = json.load(json_file)
                print(obj)
                print(type(obj))
                closest_obj_name = obj['closest_obj']['name']
                print(closest_obj_name)
            #closest_obj = Ned.query_object(obj['closest_obj']['name'])
            #if closest_obj[6] is not ma.masked:  # there is info about the redshift
             #   insert_data_from_redshift(obj, closest_obj)
'''

'''
table = Ned.query_object('NGC151')
print(table.pprint_all())
print(table[0][11])
 print(near_objs.pprint_all())
'''