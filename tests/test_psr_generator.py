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
    tol = 1e-10
    pulsar = Pulsar(vxvv=[25, 25, 1, 1, 0, 0], lb=True)
    assert abs(pulsar.vll - 4.74047) < tol  # pi/3600/180 * (pc/km) * (s/yr)
