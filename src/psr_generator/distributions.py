"Define the virus distribution functions"
import numpy as np
from numpy import cos
from numpy import pi
from numpy import sin
from numpy import sqrt
from numpy.random import rand
from scipy.stats import expon
from scipy.stats import gamma


class GalacticDistribution(object):
    """
    Notes
    -----
    The galactic distribution (x, y, z) are centered at the galactic center.

    R = sqrt(x**2 + y**2)

    f(r) ~ (R/R0)**beta exp(-q*(R-R0)/R0)

    f(z) = exp(-|z|/z0)
    """

    def __init__(self, R0, beta, z0):
        self.R0 = R0
        self.beta = beta
        self.z0 = z0

    def pdf(self, x, y, z, **params):
        """The galactic distribution"""
        self.set_params(params)
        r2d = sqrt(x**2 + y**2)/self.R0
        return (self._r_dist.pdf(r2d) *
                self._z_dist.pdf(abs(z)/self.z0) /
                self.R0 / self.z0)

    def rvs(self, size=1, **params):
        """
        Sample the galactic distribution

        Parameters
        ----------
        size : int or tuple of ints, optional
        Defining number of random variates (default is 1).
        """
        self.set_params(params)
        size = np.atleast_1d(size)
        r_rand = self._r_dist.rvs(size=size)*self.R0
        z_rand = self._z_dist.rvs(size=size)*self.z0
        phi = rand(*size)*2*pi
        return np.array([r_rand*cos(phi), r_rand*sin(phi), z_rand]).squeeze()

    @property
    def _r_dist(self):
        "The radial component of the distribution"
        return gamma(a=self.beta + 1)

    @property
    def _z_dist(self):
        "The vertical component of the distribution"
        return expon()

    def set_params(self, params):
        "Set the distribution parameters"
        self.__dict__.update(params)
