from astroquery.ned import Ned
import astropy.units as u
from astropy import coordinates
from astropy.coordinates import Galactic
import os
import json
import math
from numpy import ma
from astropy.cosmology import FlatLambdaCDM

folder_path ='C:/Users/user/Documents/astro/'
obj_name = "2019vab"
file_path = folder_path + "found_near_obj/" + obj_name+ ".txt"
with open(file_path) as json_file:
    obj = json.load(json_file)
    print(type(obj))
    print(str(obj['closest_obj']['name']))
    result_table = Ned.query_object(obj['closest_obj']['name'])
    print(result_table.pprint_all())