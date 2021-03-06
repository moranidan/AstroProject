import json
import requests
import os
from collections import OrderedDict

# API key for Bot
api_key = "abf86f8ae8ea7f24e611fe7ec352eced3d2418e0"
# list that represents json file for search obj
search_obj = [("ra", ""), ("dec", ""), ("radius", ""), ("units", ""),
            ("objname", ""), ("internal_name", "")]
# list that represents json file for get obj
get_obj = [("objname", ""), ("photometry", "0"), ("spectra", "1")]

# url of TNS and TNS-sandbox api
url_tns_api = "https://wis-tns.weizmann.ac.il/api/get"
url_tns_sandbox_api = "https://sandbox-tns.weizmann.ac.il/api/get"

# current working directory
cwd = os.getcwd()
# directory for downloaded files
download_dir = os.path.join(cwd,'downloaded_files')


# function for changing data to json format
def format_to_json(source):
    # change data to json format and return
    parsed = json.loads(source, object_pairs_hook=OrderedDict)
    result = json.dumps(parsed, indent=4)
    return result


# function for search obj
def search(url, json_list):
  try:
    # url for search obj
    search_url = url+'/search'
    # change json_list to json format
    json_file = OrderedDict(json_list)
    # construct the list of (key,value) pairs
    search_data = [('api_key', (None, api_key)),
                 ('data', (None, json.dumps(json_file)))]
    # search obj using request module
    response = requests.post(search_url, files=search_data)
    # return response
    return response
  except Exception as e:
    return [None, 'Error message : \n'+str(e)]


# function for get obj
def get(url, json_list):
  try:
    # url for get obj
    get_url = url+'/object'
    # change json_list to json format
    json_file = OrderedDict(json_list)
    # construct the list of (key,value) pairs
    get_data = [('api_key', (None, api_key)),
                 ('data', (None, json.dumps(json_file)))]
    # get obj using request module
    response = requests.post(get_url, files=get_data)
    # return response
    return response
  except Exception as e:
    return [None, 'Error message : \n'+str(e)]


# function for downloading file
def get_file(url):
  try:
    # take filename
    filename = os.path.basename(url)
    # downloading file using request module
    response = requests.post(url, files=[('api_key',(None, api_key))],stream=True)
    # saving file
    path = os.path.join(download_dir, filename)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in response:
                f.write(chunk)
        print('File : '+filename+' is successfully downloaded.')
    else:
        print('File : '+filename+' was not downloaded.')
        print('Please check what went wrong.')
  except Exception as e:
    print('Error message : \n'+str(e))


response = requests.get("https://sandbox-tns.weizmann.ac.il/api/get/search", )
# print(response.status_code)







"""class TNSClient {
/// TNS's API URL
protected static $baseAPIUrl = 'https://wis-tns.weizmann.ac.il/api/’;
}


{"id_code": 401, "id_message": "Unauthorized", "data": {"received_data": {"api_key": null}}}


{"id_code": 200, "id_message": "OK", "data": {"at_types": ["Other", "PSN", "PNV", "AGN", "NUC", "FRB"],
                                              "object_types": {"23": "Afterglow", "29": "AGN", "1003": "Computed-Ia",
                                                               "1014": "Computed-IIb", "1011": "Computed-IIP",
                                                               "1020": "Computed-PISN", "27": "CV", "130": "FRB",
                                                               "30": "Galaxy", "60": "Gap", "61": "Gap I",
                                                               "62": "Gap II", "25": "ILRT", "99": "Impostor-SN",
                                                               "70": "Kilonova", "24": "LBV", "210": "M dwarf",
                                                               "26": "Nova", "0": "Other", "31": "QSO", "18": "SLSN-I",
                                                               "19": "SLSN-II", "20": "SLSN-R", "1": "SN", "2": "SN I",
                                                               "15": "SN I-faint", "16": "SN I-rapid", "3": "SN Ia",
                                                               "103": "SN Ia-91bg-like", "104": "SN Ia-91T-like",
                                                               "106": "SN Ia-CSM", "100": "SN Ia-pec",
                                                               "102": "SN Ia-SC", "105": "SN Iax[02cx-like]",
                                                               "4": "SN Ib", "8": "SN Ib-Ca-rich", "107": "SN Ib-pec",
                                                               "6": "SN Ib\/c", "9": "SN Ibn", "5": "SN Ic",
                                                               "7": "SN Ic-BL", "108": "SN Ic-pec", "10": "SN II",
                                                               "110": "SN II-pec", "14": "SN IIb", "12": "SN IIL",
                                                               "13": "SN IIn", "112": "SN IIn-pec", "11": "SN IIP",
                                                               "50": "Std-spec", "120": "TDE", "28": "Varstar",
                                                               "200": "WR", "202": "WR-WC", "201": "WR-WN",
                                                               "203": "WR-WO"},
                                              "spectra_types": {"1": "Object", "2": "Host", "3": "Sky", "4": "Arcs",
                                                                "5": "Synthetic"},
                                              "units": ["Other", "ABMag", "STMag", "VegaMag", "erg cm(-2) sec(-1)",
                                                        "erg cm(-2) sec(-1) Hz(-1)", "erg cm(-2) sec(-1) Ang(-1)",
                                                        "counts sec(-1)", "Jy", "mJy", "Neutrino events", "Angstrom",
                                                        "Nanometre", "Micrometre", "Millimetre", "Centimetre", "Hz",
                                                        "GHz", "eV", "keV", "GeV", "mJy sec"],
                                              "groups": {"0": "None", "1": "PESSTO", "2": "iPTF", "3": "ASAS-SN",
                                                         "4": "Pan-STARRS1", "5": "SkyMapper", "6": "POSS", "7": "BOSS",
                                                         "8": "LOSS", "9": "DAO_OTS", "10": "XOSS", "11": "LCOGT SN-KP",
                                                         "12": "RANSSP", "13": "CRTS", "14": "SNHunt", "15": "DES",
                                                         "16": "Padova-Asiago", "17": "OGLE", "18": "ATLAS",
                                                         "19": "TAROT", "20": "LSQ", "21": "KEGS", "22": "PTSS",
                                                         "23": "XTSS", "24": "GaiaAlerts", "25": "TNTS", "26": "ATS",
                                                         "27": "ISSP", "28": "NUTS", "29": "OOICLE", "30": "DLT40",
                                                         "31": "EHSSP", "32": "CSP", "33": "PIKA", "34": "SUNBIRD",
                                                         "35": "HSC", "36": "MASTER", "37": "ePESSTO",
                                                         "38": "Global SN Project", "39": "PSH", "40": "GREAT",
                                                         "41": "SKYS", "42": "MUSSES", "43": "TexSNs", "44": "JWST-ERS",
                                                         "45": "Swope SN Survey", "46": "STARGATE", "47": "HETH",
                                                         "48": "ZTF", "50": "ASO", "51": "SCAT", "52": "AZTEC",
                                                         "53": "CSNS", "54": "BraTS", "55": "GSNST", "56": "GWAC-ToP",
                                                         "57": "POTS", "58": "CRAFT", "59": "GOTO", "60": "BlackGEM",
                                                         "61": "MeerLICHT", "62": "KSP", "63": "ePESSTO+",
                                                         "64": "Tomo-e", "65": "TCD", "66": "SAGUARO", "67": "Gattini",
                                                         "68": "DECam-GROWTH", "69": "TMTS", "70": "FDST",
                                                         "71": "DESGW", "72": "C-SNAILS", "73": "BTDG", "74": "ALeRCE",
                                                         "75": "GRAWITA"},
                                              "instruments": {"157": "AAT - RGO", "115": "ANU-2.3m - WiFeS",
                                                              "141": "APO-3.5m - APO-TSPEC", "70": "APO-3.5m - DIS",
                                                              "153": "ASASSN-1 - Brutus", "154": "ASASSN-2 - Cassius",
                                                              "191": "ASASSN-3 - Paczynski",
                                                              "192": "ASASSN-4 - Leavitt",
                                                              "195": "ASASSN-5 - Payne-Gaposchkin",
                                                              "169": "AST3 - AST3-Cam", "159": "ATLAS1 - ACAM1",
                                                              "160": "ATLAS2 - ACAM2", "167": "BAO-0.6m - BATC",
                                                              "77": "BAO-0.85m - CCD", "80": "BAO-2.16m - Cassegrain",
                                                              "55": "BAO-2.16m - Phot-spec",
                                                              "215": "BG2 - BlackGEM-Cam2",
                                                              "216": "BG3 - BlackGEM-Cam3",
                                                              "217": "BG4 - BlackGEM-Cam4", "68": "Bok - BC-Bok",
                                                              "131": "BTA-6 - SCORPIO", "48": "CA-2.2m - CAFOS",
                                                              "60": "CA-3.5m - MOSCA", "81": "CA-3.5m - PMAS",
                                                              "176": "CA-3.5m - TWIN", "202": "CFHT - MegaCam",
                                                              "161": "CNEOST - STA1600", "204": "CrAO - AZT-8",
                                                              "79": "Crossley - PNS",
                                                              "205": "CTIO-0.41 - CTIO-Photomultiplier",
                                                              "88": "CTIO-0.9 - CASS-DI",
                                                              "206": "CTIO-1.0 - CTIO-Other", "86": "CTIO-1.5m - LORAL",
                                                              "73": "CTIO-1.5m - RC-Spec-1.5",
                                                              "173": "CTIO-4m - ARCoIRIS", "174": "CTIO-4m - COSMOS",
                                                              "172": "CTIO-4m - DECAM", "87": "CTIO-4m - IR-Spec",
                                                              "72": "CTIO-4m - RC-Spec-4", "45": "Danish-1.54m - DFOSC",
                                                              "143": "DCT - Deveny-LMI", "53": "DDO - Cass",
                                                              "37": "Ekar - AFOSC", "38": "Ekar - BC-Ekar",
                                                              "201": "ESO-1.5m - ARCES", "54": "ESO-1.5m - BC-ESO",
                                                              "158": "ESO-1m - QUEST", "33": "ESO-2.2m - EFOSC-2.2",
                                                              "210": "ESO-2.2m - GROND", "32": "ESO-3.6m - EFOSC2-3.6",
                                                              "31": "ESO-NTT - EFOSC2-NTT", "30": "ESO-NTT - EMMI",
                                                              "34": "ESO-NTT - Sofi", "44": "FLWO-1.5m - FAST",
                                                              "144": "FLWO-1.5m - TRES", "110": "FTN - EM01",
                                                              "108": "FTN - FLOYDS-N", "112": "FTN - FS02",
                                                              "125": "FTS - FLOYDS-S", "105": "FTS - FS01",
                                                              "162": "Gaia - Gaia-astrometric",
                                                              "163": "Gaia - Gaia-photometric",
                                                              "164": "Gaia - Gaia-RVS", "102": "GALEX - GALEX",
                                                              "93": "Galileo - AVI", "57": "Galileo - BC-Asi",
                                                              "133": "GAO-0.65m - GCS", "65": "GAO-1.5m - GLOWS",
                                                              "220": "Gattini - Gattini-camera", "6": "Gemini-N - GMOS",
                                                              "166": "Gemini-N - GNIRS",
                                                              "197": "Gemini-S - Flamingos-2", "9": "Gemini-S - GMOS-S",
                                                              "218": "GOTO-N - GOTO-1", "101": "GTC - OSIRIS",
                                                              "89": "Harlan-Smith - ES2",
                                                              "171": "Harlan-Smith - IDS-McDonald",
                                                              "91": "Harlan-Smith - LCS", "46": "HCT-2m - HFOSC",
                                                              "123": "HET - HET-HRS", "43": "HET - HET-LRS",
                                                              "124": "HET - HET-MRS", "83": "HST - STIS",
                                                              "194": "HST - WFC3", "184": "IGO - IFOSC",
                                                              "67": "INT-2.5m - FOS", "19": "INT-2.5m - IDS",
                                                              "122": "IRTF - SpeX", "94": "IUE - IUE",
                                                              "188": "JWST - MIRI", "185": "JWST - NIRCam",
                                                              "187": "JWST - NIRISS", "186": "JWST - NIRSpec",
                                                              "203": "KAIT - KAITCam", "138": "Kanata - HOWPol",
                                                              "142": "KAO - LOSA-F2", "82": "Keck1 - HIRES",
                                                              "3": "Keck1 - LRIS", "130": "Keck1 - MOSFIRE",
                                                              "4": "Keck2 - DEIMOS", "100": "Keck2 - ESI",
                                                              "212": "KPNO-2.1m - IDS-KPNO", "128": "LBT - LUCI",
                                                              "120": "LBT - MODS1", "121": "LBT - MODS2",
                                                              "63": "LCO-duPont - BC-duPont",
                                                              "64": "LCO-duPont - Mod-spec", "62": "LCO-duPont - WFCCD",
                                                              "208": "LCO1m - Sinistro", "209": "LCO2m - Spectral",
                                                              "10": "Lick-3m - KAST", "198": "Lick-3m - ShARCS",
                                                              "99": "Lick-3m - UV-Schmidt", "199": "Lick-3m - VNIRIS",
                                                              "39": "Lick1m - Nickel-Spec",
                                                              "107": "Lijiang-2.4m - YFOSC", "95": "LT - FRODOspec",
                                                              "156": "LT - SPRAT",
                                                              "151": "Magellan-Baade - BC-Magellan",
                                                              "116": "Magellan-Baade - FIRE",
                                                              "75": "Magellan-Baade - IMACS",
                                                              "137": "Magellan-Baade - MagE",
                                                              "69": "Magellan-Clay - LDSS-2",
                                                              "78": "Magellan-Clay - LDSS-3",
                                                              "84": "Magellan-Clay - MIKE", "200": "Mayall - KOSMOS",
                                                              "5": "Mayall - RC-Spec", "59": "MDM-2.4 - BC-OSU",
                                                              "85": "MDM-2.4 - MARK-III", "135": "MDM-2.4 - modspec",
                                                              "150": "MDM-2.4 - OSMOS", "170": "MDM-2.4 - TIFKAM",
                                                              "145": "Mercator - HERMES", "214": "ML1 - MeerLICHT-Cam",
                                                              "213": "MLO-1.5m - ITS-MLO", "113": "MLO-1m - CCD-MLO",
                                                              "221": "MMT - BINOSPEC", "96": "MMT - Hectospec",
                                                              "180": "MMT - MMIRS", "58": "MMT - MMT-Blue",
                                                              "98": "MMT - MMT-Red", "132": "MSO-74in - BC-MSO",
                                                              "165": "Mt-Abu - Abu-NICS", "49": "Nayuta - MALLS",
                                                              "41": "NOT - ALFOSC", "207": "NOT - StanCam",
                                                              "139": "OAO-188 - KOOLS", "190": "OGLE-1.3m - OGLEIV-Cam",
                                                              "106": "OHP-1.93m - Carelec", "0": "Other - Other",
                                                              "92": "Otto-Struve - IGS", "1": "P200 - DBSP",
                                                              "2": "P200 - LFC", "109": "P200 - P200-TSPEC",
                                                              "103": "P48 - CFH12k", "196": "P48 - ZTF-Cam",
                                                              "104": "P60 - P60-Cam", "149": "P60 - SEDM",
                                                              "146": "Plaskett - Plaskett", "155": "PS1 - GPC1",
                                                              "119": "SAAO - G-Spec", "118": "SALT - HRS-SALT",
                                                              "117": "SALT - RSS", "152": "SkyMapper - SM-WFCam",
                                                              "140": "Sloan - SDSS-Spec", "127": "SOAR - Goodman",
                                                              "136": "SOAR - SOAR-OSIRIS", "126": "SPM15 - RATIR",
                                                              "61": "SSO-2.3m - DBS", "193": "SST - IRAC",
                                                              "66": "SST - IRS", "71": "Subaru - FOCAS",
                                                              "175": "Subaru - HDS", "177": "Subaru - HSC",
                                                              "178": "Subaru - IRCS", "50": "Swift-UVOT - UV-grism",
                                                              "52": "Swift-UVOT - UVOT-Imager",
                                                              "51": "Swift-UVOT - V-grism", "219": "TMT - CCD-TMT",
                                                              "15": "TNG - DOLORES", "147": "TNG - HARPS-N",
                                                              "40": "TNG - NICS", "134": "TNG - SARG",
                                                              "11": "UH88 - SNIFS", "47": "UKIRT - CGS4",
                                                              "8": "VLT-UT1 - FORS1", "7": "VLT-UT1 - FORS2",
                                                              "76": "VLT-UT2 - FORS1-UT2", "148": "VLT-UT2 - UVES",
                                                              "12": "VLT-UT2 - X-Shooter", "35": "VLT-UT3 - ISAAC",
                                                              "168": "VLT-UT3 - VIMOS", "182": "VLT-UT4 - MUSE",
                                                              "183": "VLT-UT4 - SINFONI", "97": "WHT-4.2m - ACAM",
                                                              "18": "WHT-4.2m - FOS-1", "17": "WHT-4.2m - FOS-2",
                                                              "16": "WHT-4.2m - ISIS", "129": "WHT-4.2m - LIRIS",
                                                              "114": "Wise-C18 - C18-Cam", "22": "Wise1m - FOSC",
                                                              "20": "Wise1m - Laiwo", "21": "Wise1m - PI",
                                                              "74": "WIYN - Hydra", "56": "XLT - BFOSC",
                                                              "181": "XLT - HRS-XLT", "179": "XLT - OMR"},
                                              "telescopes": {"0": "Other-Other", "1": "P48-Palomar 1.2m Oschin",
                                                             "2": "P60-Palomar 1.5m", "3": "P200-Palomar 5.1m Hale",
                                                             "4": "Keck1-Keck I 10m", "5": "Keck2-Keck II 10m",
                                                             "6": "Mayall-4m Ncholas U. Mayall Telescope",
                                                             "7": "HET-Hobby-Eberly Telescope",
                                                             "8": "WHT-4.2m-William Herschel Telescope",
                                                             "9": "Lick1m-Lick 1m Nickel Reflector",
                                                             "10": "Lick-3m-3m Lick  Shane Reflector",
                                                             "11": "MDM-2.4-MDM 2.4m Hiltner",
                                                             "12": "NOT-Nordic Optical Telescope",
                                                             "13": "PAIRITEL-Peters Automated Infrared Imaging Telescope",
                                                             "14": "TNG-Telescopio Nazionale Galileo",
                                                             "15": "Gemini-N-Gemini North",
                                                             "16": "Gemini-S-Gemini South", "17": "UH88-UH 88inch",
                                                             "18": "Wise1m-Wise 1m", "19": "Wise-C18-Wise 18 inch",
                                                             "20": "VLT-UT1-The Very Large Telescope - UT1",
                                                             "21": "VLT-UT2-The Very Large Telescope - UT2",
                                                             "22": "VLT-UT3-The Very Large Telescope - UT3",
                                                             "23": "VLT-UT4-The Very Large Telescope - UT4",
                                                             "30": "ESO-NTT-The ESO New Technology Telescope",
                                                             "31": "ESO-2.2m-The ESO 2.2m at La Silla",
                                                             "32": "ESO-3.6m-The ESO 3.6m at La Silla",
                                                             "33": "INT-2.5m-Isaac Newton Telescope 2.5m",
                                                             "34": "Ekar-Asiago Ekar Telescope",
                                                             "36": "FLWO-1.5m-FLWO 1.5m Tillinghast",
                                                             "37": "Danish-1.54m-The Danish 1.54-m Telescope at La Silla",
                                                             "38": "HCT-2m-The 2-m Himalayan Chandra Telescope (IAO)",
                                                             "39": "UKIRT-United Kingdom Infra-Red Telescope",
                                                             "40": "CA-2.2m-Calar Alto 2.2m Telescope",
                                                             "41": "Nayuta-NHAO Nayuta 2m Telescope",
                                                             "42": "Swift-UVOT-UV\/Optical Telescope on Swift",
                                                             "43": "DDO-David Dunlap Observatory",
                                                             "44": "ESO-1.5m-ESO 1.5-m Telescope",
                                                             "45": "BAO-2.16m-2.16m Beijing Astronomical Observatory Telescope",
                                                             "46": "Galileo-Asiago Galileo Telescope",
                                                             "47": "MMT-MMT Observatory 6.5m",
                                                             "48": "CA-3.5m-Calar Alto 3.5m Telescope",
                                                             "49": "SSO-2.3m-Siding Spring Observatory 2.3-m Telescope",
                                                             "50": "LCO-duPont-Las Campanas Observatory du Pont telescope",
                                                             "51": "GAO-1.5m-Gunma Astronomical Observatory 150cm reflector",
                                                             "52": "SST-The Spitzer Space Telescope",
                                                             "53": "Bok-Bok Telescope",
                                                             "54": "Magellan-Baade-Walter Baade Magellan 6.5-m telescope (LCO)",
                                                             "55": "APO-3.5m-3.5m Astrophysical Reaserch Consortium",
                                                             "56": "Subaru-Subaru",
                                                             "57": "CTIO-4m-CTIO - 4-m Victor M. Blanco Telescope",
                                                             "58": "CTIO-1.5m-CTIO - 1.5-Meter Telescope (SMARTS Consortium)",
                                                             "59": "WIYN-Wisconsin-Indiana-Yale-NOAO Telescope",
                                                             "60": "BAO-0.85m-0.85m Beijing Astronomical Observatory Telescope",
                                                             "61": "Crossley-Crossley Reflector",
                                                             "62": "HST-Hubble Space Telescope",
                                                             "63": "Magellan-Clay-Landon T. Clay Magellan 6.5-m telescope (LCO)",
                                                             "65": "CTIO-0.9-CTIO 0.9 Meter (SMARTS Consortium)",
                                                             "66": "copernico-Copernico Teliscope",
                                                             "67": "Harlan-Smith-2.7m Harlan J Smith Telescope",
                                                             "68": "Otto-Struve-2.1m-Otto Struve Tellescope",
                                                             "69": "IUE-International Ultraviolet Explorer",
                                                             "70": "LT-Liverpool Telescope",
                                                             "71": "GTC-Gran Telescopio Canarias",
                                                             "72": "Sloan-Sloan Digital Sky Survey",
                                                             "73": "GALEX-Galaxy Evolution Explorer 50 cm",
                                                             "74": "FTN-Faulkes Telescope North",
                                                             "75": "FTS-Faulkes Telescope South",
                                                             "76": "OHP-1.93m-Haute-Provence Observatory",
                                                             "77": "Lijiang-2.4m-Lijiang 2.4m telescope - Yunnan Obsvervatories",
                                                             "78": "MLO-1m-Mount Laguna Observatory 1m",
                                                             "79": "ANU-2.3m-ANU 2.3m Advanced Technology Telescope",
                                                             "80": "KAIT-Katzman Automatic Imaging Telescope",
                                                             "81": "SAAO-South African Astronomical Observatory",
                                                             "82": "SALT-Southern African Large Telescope",
                                                             "83": "LBT-Large Binocular Telescope",
                                                             "84": "IRTF-NASA Infrared Telescope Facility",
                                                             "85": "SPM15-SPM 1.5-meter Johnson telescope",
                                                             "86": "SOAR-Southern Astrophysical Research Telescope",
                                                             "87": "BTA-6-Big Telescope Alt-azimuth",
                                                             "88": "MSO-74in-74-inch Reflector - Mount Stromlo Observatory",
                                                             "89": "GAO-0.65m-Gunma 0.65m",
                                                             "90": "Kanata-KANATA 1.5-m Optical and Near-Infrared telescope",
                                                             "91": "OAO-188-Okayama Astrophysical Observatory 188cm",
                                                             "92": "KAO-Koyama Astronomical Observatory - Araki Telescope",
                                                             "93": "DCT-Discovery Channel Telescope",
                                                             "94": "Alvan-Clark-Boyden Refractor",
                                                             "95": "Plaskett-Dominion AStrophysical Observatory",
                                                             "96": "Mercator-Roque de los Muchachos Observatory",
                                                             "97": "SkyMapper-SkyMapper wide-field survey telescope",
                                                             "98": "PS1-Pan-STARRS", "99": "ASASSN-1-ASASSN-Brutus",
                                                             "100": "ASASSN-2-ASASSN-Cassius",
                                                             "101": "AAT-Anglo-Australian Telescope",
                                                             "102": "ESO-1m-ESO 1-m Schmidt telescope",
                                                             "103": "ATLAS1-ATLAS Haleakala",
                                                             "104": "ATLAS2-ATLAS Mauna Loa",
                                                             "105": "XLT-XingLong telescope",
                                                             "106": "CNEOST-Chinese Near Earth Object Survey Telescope",
                                                             "107": "Gaia-Gaia Spacecraft",
                                                             "108": "Mt-Abu-Mount Abu Infrared Observatory",
                                                             "109": "BAO-0.6m-0.6m Beijing Astronomical Observatory Telescope",
                                                             "110": "AST3-The Antarctic Schmidt\/Survey Telescopes",
                                                             "111": "IGO-IUCAA Girawali Observatory",
                                                             "112": "JWST-James Webb Space Telescope",
                                                             "113": "OGLE-1.3m-The 1.3 m OGLE Warsaw Telescope",
                                                             "114": "ASASSN-3-ASASSN-Paczynski",
                                                             "115": "ASASSN-4-ASASSN-Leavitt",
                                                             "116": "ASASSN-5-ASASSN-Payne-Gaposchkin",
                                                             "117": "CFHT-Canada-France-Hawaii Telescope",
                                                             "118": "CrAO-Crimean Astrophysical Observatory",
                                                             "119": "CTIO-0.41-CTIO 0.41 Meter (PROMPT)",
                                                             "120": "CTIO-1.0-CTIO 1.0 Meter (SMARTS)",
                                                             "121": "LCO1m-LCO 1m", "122": "LCO2m-LCO 2m",
                                                             "123": "KPNO-2.1m-KPNO 2.1m", "124": "MLO-1.5m-MLO 1.5m",
                                                             "125": "ML1-MeerLICHT-1", "126": "BG2-BlackGEM- 2",
                                                             "127": "BG3-BlackGEM- 3", "128": "BG4-BlackGEM- 4",
                                                             "129": "GOTO-N-GOTO-North",
                                                             "130": "TMT-Tsinghua Ma-huateng Telescope",
                                                             "131": "Gattini-Palomar Gattini-IR"},
                                              "archives": {"2": "DSS", "0": "Other", "1": "SDSS"},
                                              "filters": {"0": "Other", "1": "Clear", "10": "U-Johnson",
                                                          "11": "B-Johnson", "12": "V-Johnson", "13": "R-Cousins",
                                                          "14": "I-Cousins", "15": "J-Bessel", "16": "H-Bessel",
                                                          "17": "K-Bessel", "18": "L", "19": "M", "20": "U-Sloan",
                                                          "21": "g-Sloan", "22": "r-Sloan", "23": "i-Sloan",
                                                          "24": "z-Sloan", "25": "y-PS1", "26": "w-PS1",
                                                          "30": "NUV-Galex", "31": "FUV-Galex", "32": "U-Swift-UVOT",
                                                          "33": "B-Swift-UVOT", "34": "V-Swift-UVOT",
                                                          "35": "uvm2-Swift-UVOT", "36": "uvw2-Swift-UVOT",
                                                          "37": "uvw1-Swift-UVOT", "40": "3.6-Spitzer IRAC",
                                                          "41": "4.5-Spitzer IRAC", "42": "5.8-Spitzer IRAC",
                                                          "43": "8.0-Spitzer IRAC", "45": "3.4-WISE", "46": "4.6-WISE",
                                                          "47": "12-WISE", "48": "22-WISE", "50": "R-PTF",
                                                          "51": "g-PTF", "52": "I-PTF", "55": "V-crts-CRTS",
                                                          "60": "g-SM-SkyMapper", "61": "r-SM-SkyMapper",
                                                          "62": "i-SM-SkyMapper", "63": "z-SM-SkyMapper",
                                                          "64": "u-SM-SkyMapper", "65": "v-SM-SkyMapper",
                                                          "70": "gr-LSQ", "71": "cyan-ATLAS", "72": "orange-ATLAS",
                                                          "75": "G-Gaia", "80": "VR-DECAM", "81": "Y-DECAM", "90": "Ha",
                                                          "91": "g-HSC", "92": "r2-HSC", "93": "i2-HSC", "94": "z-HSC",
                                                          "95": "y-HSC", "100": "F200W-JWST", "101": "F444W-JWST",
                                                          "110": "g-ZTF", "111": "r-ZTF", "112": "i-ZTF",
                                                          "113": "BG-u-BlackGem", "114": "BG-g-BlackGem",
                                                          "115": "BG-r-BlackGem", "116": "BG-i-BlackGem",
                                                          "117": "BG-z-BlackGem", "118": "BG-q-BlackGem",
                                                          "120": "L-GOTO", "121": "R-GOTO", "122": "G-GOTO",
                                                          "123": "B -GOTO"}}}"""