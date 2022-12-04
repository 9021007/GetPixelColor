import getpixelcolor
import numpy as np
def test_average():
    average = getpixelcolor.average(35, 35, 35, 35)
    assert type(getpixelcolor.average(35, 35, 35, 35)) == type((1, 1, 1))
    for i in average:
        
        assert type(i) == type(np.int64(1)) or type(i) == type(np.int32(1)) or type(i) == type(1)
        assert i >= 0
        assert i <= 255