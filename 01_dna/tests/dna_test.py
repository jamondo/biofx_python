""" Tests for dna.py """

import os
import platform
from subprocess import getstatusoutput

PRG = './dna_v2.py'
RUN = f'python {PRG}' if platform.system() == 'Windows' else f'python3 {PRG}'
TEST1 = ('./tests/inputs/input1.txt', '1 2 3 4')
TEST2 = ('./tests/inputs/input2.txt', '20 12 17 21')
TEST3 = ('./tests/inputs/input3.txt', '196 231 237 246')
TEST4 = ('./tests/inputs/input4.txt', '1 2 3 4')


# --------------------------------------------------
def test_exists() -> None:
    """ Program exists """

    assert os.path.exists(PRG)


# --------------------------------------------------
def test_usage() -> None:
    """ Prints usage """

    for flag in ['-h']:
        rv, out = getstatusoutput(f'{RUN} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_dies_no_args() -> None:
    """ Dies with no arguments """

    rv, out = getstatusoutput(RUN)
    assert rv != 0
    assert out.lower().startswith('usage:')


# --------------------------------------------------
def test_arg() -> None:
    """ Uses command-line arg """

    for file, expected in [TEST1, TEST2, TEST3]:
        dna = open(file).read()
        retval, out = getstatusoutput(f'{RUN} {dna}')
        assert retval == 0
        assert out == expected


# --------------------------------------------------
def test_file() -> None:
    """ Uses file arg """

    for file, expected in [TEST1, TEST2, TEST3]:
        retval, out = getstatusoutput(f'{RUN} {file}')
        assert retval == 0
        assert out == expected


# --------------------------------------------------
def test_lower() -> None:
    """ Uses file arg """

    for file, expected in [TEST1, TEST2, TEST3, TEST4]:
        retval, out = getstatusoutput(f'{RUN} {file}')
        assert retval == 0
        assert out == expected
