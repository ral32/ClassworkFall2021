import pytest
@pytest.mark.parametrize("coord1, coord2, x3, expected", 
                            [((1,1), (2,2), 3, 3)])


def test_line(coord1, coord2, x3, expected):
    from plot_line import line
    answer = line(coord1, coord2, x3)
    assert answer == expected
    