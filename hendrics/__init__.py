# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""This is proposed as an Astropy affiliated package."""

# Affiliated packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *

# ----------------------------------------------------------------------------

# For egg_info test builds to pass, put package imports here.
if not _ASTROPY_SETUP_:
    # Workaround: import netCDF4 before everything else. This loads the HDF5
    # library that netCDF4 uses and not something else.

    try:
        import netCDF4 as nc

        HEN_FILE_EXTENSION = ".nc"
        HAS_NETCDF = True
    except ImportError:
        HEN_FILE_EXTENSION = ".p"
        HAS_NETCDF = False
        pass

    import stingray.utils

    # Patch stingray.utils
    def _root_squared_mean(array):
        import numpy as np

        array = np.asarray(array)
        return np.sqrt(np.sum(array ** 2)) / len(array)

    stingray.utils._root_squared_mean = _root_squared_mean
