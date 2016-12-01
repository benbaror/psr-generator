"Define the classes which represents pulsars"
import numpy as np
from galpy.orbit import Orbit


class Pulsar(Orbit):
    """
    An generic radio pulsar
    """

    def __init__(self, *args, **kargs):
        """
        Crate pulsar(s)

        INPUT:
        ------
        p0: array_like
           spin period
        p1: spin period derivative
        [ra, dec, d, mu_ra, mu_dec, vlos] in [deg,deg,kpc,mas/yr,mas/yr,km/s]
        (all J2000.0; mu_ra = mu_ra * cos dec); can be Quantities
        """

        super().__init__(*args, **kargs)
        self._p0 = kargs.get('p0', None)
        self._p1 = kargs.get('p1', None)

    @property
    def vll(self):
        vll = super().vll()
        try:
            return np.asscalar(vll)
        except ValueError:
            return vll
