import getpixelcolor

def test_pixel():
    pixel = getpixelcolor.pixel(35, 35)
    assert type(getpixelcolor.pixel(35, 35)) == type((1, 1, 1))
    for i in pixel:
        assert type(i) == type(1)
        assert i >= 0
        assert i <= 255

