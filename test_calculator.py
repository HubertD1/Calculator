from calculator import add, subtract, multiply, divide, CircleArea

def test_add():
	assert add(2,3) == 5

def test_subtract():
        assert subtract(8,5) == 3

def test_divide():
        assert divide(6,2) == 3

def test_multiply():
        assert multiply(4,3) == 12

def test_negative_addition():
	#arrange
	a, b = -4, -7
	#act
	result = add(a,b)
	#assert
	assert result == -11

def test_circleArea():
	assert CircleArea(-4) == "Error"
