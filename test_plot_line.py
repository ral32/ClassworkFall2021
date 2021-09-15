import pytest

@pytest.mark.parametrize("(x1,y1), (x2,y2), x3, y3, expected", [(1,1), (2,2), 3, 3, True])

def test_plot_line(coord1, coord2, x3, y3, expected):
    from plot_line import line
    input = [(1,1), (2,2), 3, 3, expected]
    expected = True
    answer = line(input)
    assert answer == expected



