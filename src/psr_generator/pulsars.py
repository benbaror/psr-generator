"Define the classes which represents pulsars"
from __future__ import division
from __future__ import print_function
from builtins import super

from astropy.coordinates import SkyCoord


class Pulsar(SkyCoord):
    """
    An generic radio pulsar
    """

    def __init__(self, *args, **kargs):
        """
        Crate pulsar(s)

        Arguments:
        ------
        p0: array_like
           spin period
        p1: spin period derivative

        Example:
        -------
        >>> p = pulsars.Pulsar(1e-3, 0, 8.3, unit=['deg','deg','kpc'],
                               frame='galactic')
        >>> print(p.galactocentric.cartesian.xyz.round(2))
        [0., 0., 0.] kpc
        """

        super().__init__(*args, **kargs)
        self._p0 = kargs.get('p0', None)
        self._p1 = kargs.get('p1', None)
