"Test"
import numpy as np
from click.testing import CliRunner

from psr_generator.cli import main
from psr_generator.distributions import GalacticDistribution
from psr_generator.pulsars import Pulsar
from psr_generator.pulsars import RandomPulsar



def test_main():
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == '()\n'
    assert result.exit_code == 0


def test_pulsar():
    tol = 1e-3
    pulsar = Pulsar(1e-3, 0, 8.3, unit=['deg', 'deg', 'kpc'],
                    frame='galactic')
    assert all(abs(pulsar.galactocentric.cartesian.xyz.value) < tol)  # pi/3600/180 * (pc/km) * (s/yr)

def test_random_pulsar():
    tol = 1e-3

    pulsars = RandomPulsar(R0=4, beta=1, z0=0.2, size=10)
    assert len(pulsars) == 10

    x, y, z = pulsars.galactocentric.cartesian.xyz.value
    r = np.sqrt((x + 8.3)**2 + y**2 + z**2)
    assert all(abs(1 - pulsars.galactic.distance.value/r) < tol)

    rpulsars = RandomPulsar(x=x, y=y, z=z, unit='kpc', frame='galactocentric')
    pulsars = Pulsar(x=x, y=y, z=z, unit='kpc', frame='galactocentric')
    assert all(abs(1 - rpulsars.galactic.distance.value/rpulsars.galactic.distance.value) < tol)

def test_galactic_dist():
    galactic_dist = GalacticDistribution(R0=10, beta=2, z0=0.1)
    assert galactic_dist.R0 == 10
    assert galactic_dist.beta == 2
    assert galactic_dist.z0 == 0.1

    pdf = galactic_dist.pdf(*[np.linspace(-1, 1, 10)]*3)
    assert pdf.size == 10

    x, y, z = galactic_dist.rvs(size=[10, 20])
    assert x.shape == (10, 20)

    xyz = galactic_dist.rvs()
    assert xyz.shape == (3,)

    xyz = galactic_dist.rvs(R0=1, beta=0.2, z0=10)
    assert galactic_dist.R0 == 1
    assert galactic_dist.beta == 0.2
    assert galactic_dist.z0 == 10

    pdf = galactic_dist.pdf(*[np.linspace(-1, 1, 10)]*3, R0=10, beta=2, z0=0.1)
    assert galactic_dist.R0 == 10
    assert galactic_dist.beta == 2
    assert galactic_dist.z0 == 0.1
