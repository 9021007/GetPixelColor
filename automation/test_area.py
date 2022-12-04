import getpixelcolor


def test_area():
    area = getpixelcolor.area(35, 35, 35, 35)
    assert type(getpixelcolor.area(35, 35, 35, 35)) == type([])
    for i in area:
        assert type(i) == type([])
        for j in i:
            assert type(j) == type([])
            for k in j:
                assert type(k) == type(1)
                assert k >= 0
                assert k <= 255