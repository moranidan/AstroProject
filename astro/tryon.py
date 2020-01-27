"""
txt = "welcome to the ,jungle"

pattern= [" ",",","\n"]
x = txt.replace(" ","")
x = x.replace(",","")

print(x)
"""

#how to open fits file with image only
import copy
import numpy
import matplotlib.pyplot as plt
import astropy.io.fits
image_data = astropy.io.fits.getdata("D:/obj/new2.fits")
plt.figure()
plt.imshow(image_data[0])
plt.show()


"""
import numpy
import astropy.io.fits
from astropy.table import Table
lst = astropy.io.fits.open("D:/obj/new2.fits")
lst.info()
evt_data = Table(lst[0].data)

import astropy.io.fits
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style
plt.style.use(astropy_mpl_style)
image_file = "D:/obj/new2.fits"
astropy.io.fits.info("D:/obj/new2.fits")
image_data = astropy.io.fits.getdata(image_file, ext=0)
print(image_data.shape)
plt.figure()
plt.imshow(image_data, cmap='gray')
plt.colorbar()





import copy
data_cube_copy = copy.deepcopy(data_cube)
data_cube_copy_page_3 = data_cube_copy[3]
import matplotlib.pyplot as plt
plt.display(data_cube[3])
data_cube_copy_page_3[90:110,:] = 32000.0
plt.display(data_cube_copy_page_3)
data_cube_copy_page_3[:,20:30] = 32000.0
plt.display(data_cube_copy_page_3)
data_cube_copy_page_3[:,-30:-20] = 32000.0
plt.display(data_cube_copy_page_3)










{
  "id_code": 200,
  "id_message": "OK",
  "data": {
    "received_data": {
      "objname": "1999gy",
      "photometry": 0,
      "spectra": 1
    },
    "reply": {
      "objname": "1999gy",
      "name": "1999gy",
      "redshift": null,
      "hostname": null,
      "host_redshift": null,
      "isTNS_AT": 1,
      "discoverydate": "1999-03-21 11:27:29",
      "discoverymag": 17.88,
      "discmagfilter": {
        "id": 22,
        "name": "r",
        "family": "Sloan"
      },
      "public": 1,
      "end_prop_period": null,
      "sourceid": 1,
      "discovererid": 643,
      "name_prefix": "AT",
      "type": null,
      "discoverer": "Cornen",
      "internal_name": "",
      "spectra": [],
      "ra": "16:19:58.055",
      "radeg": 244.991894009,
      "dec": "-01:10:29.09",
      "decdeg": -1.174747776,
      "object_type": {
        "name": null,
        "id": null
      },
      "source_group": {
        "groupid": 0,
        "group_name": "None"
      }
    }
  }
}


{
  "id_code": 200,
  "id_message": "OK",
  "data": {
    "received_data": {
      "objname": "1999gy",
      "photometry": 1,
      "spectra": 0
    },
    "reply": {
      "objname": "1999gy",
      "name": "1999gy",
      "redshift": null,
      "hostname": null,
      "host_redshift": null,
      "isTNS_AT": 1,
      "discoverydate": "1999-03-21 11:27:29",
      "discoverymag": 17.88,
      "discmagfilter": {
        "id": 22,
        "name": "r",
        "family": "Sloan"
      },
      "public": 1,
      "end_prop_period": null,
      "sourceid": 1,
      "discovererid": 643,
      "name_prefix": "AT",
      "type": null,
      "discoverer": "Cornen",
      "internal_name": "",
      "photometry": [
        {
          "flux": 17.88,
          "fluxerr": null,
          "limflux": null,
          "obsdate": "1999-03-21 11:27:29",
          "jd": 2451258.977419,
          "exptime": null,
          "observer": null,
          "remarks": "",
          "flux_unit": {
            "id": 1,
            "name": "ABMag"
          },
          "instrument": {
            "id": 140,
            "name": "SDSS-Spec"
          },
          "telescope": {
            "id": 72,
            "name": "Sloan"
          },
          "filters": {
            "id": 22,
            "name": "r"
          }
        }
      ],
      "ra": "16:19:58.055",
      "radeg": 244.991894009,
      "dec": "-01:10:29.09",
      "decdeg": -1.174747776,
      "object_type": {
        "name": null,
        "id": null
      },
      "source_group": {
        "groupid": 0,
        "group_name": "None"
      }
    }
  }

"""