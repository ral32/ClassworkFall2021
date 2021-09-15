import pytest
@pytest.mark.parametrize("answer, expected", [(1,1), (2,2), 3, 3])

def test_plot_line(answer, expected):
    from plot_line import line
    answer = line((1,1), (2,2), 3)
    expected = 3
    assert answer == expected
    


