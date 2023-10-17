def square(num):
    return ( num * num )

# Test case 1
def test_cal_square_1( ):
    result = square(5)
    assert result == 25
 
 
# Test case 2
def test_cal_square_2( ):
    result = square(6)
    assert result == 36
 
 
# Test case 3
def test_cal_square_3( ):
    result = square(7)
    assert result == 49
 
 
# Test case 4
def test_cal_square_4( ):
    result = square(8)
    assert result == 64