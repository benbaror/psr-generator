"Define the classes which represents pulsars"
from __future__ import division
from __future__ import print_function
from builtins import super
from astropy.coordinates import SkyCoord
from . distributions import GalacticDistribution


class Pulsar(SkyCoord):
    """
    An generic radio pulsar
    """

    def __init__(self, *args, **kwargs):
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

        super().__init__(*args, **kwargs)
        self._p0 = kwargs.pop('p0', None)
        self._p1 = kwargs.pop('p1', None)


class RandomPulsar(Pulsar, GalacticDistribution):
    """
    An generic radio pulsar
    """

    def __init__(self, *args, **kwargs):
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
        self.R0 = kwargs.pop('R0', None)
        self.beta = kwargs.pop('beta', None)
        self.z0 = kwargs.pop('z0', None)
        self.size = kwargs.pop('size', None)
        self.unit = kwargs.get('unit', 'kpc')

        try:
            super().__init__(*args, **kwargs)
        except ValueError:
            x, y, z = super().sampler_position(size=self.size)
            super().__init__(x=x, y=y, z=z, unit=self.unit,
                             frame='galactocentric')
