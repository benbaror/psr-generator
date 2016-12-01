"Test"
from click.testing import CliRunner
from psr_generator.cli import main
from psr_generator.pulsars import Pulsar


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
