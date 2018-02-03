def multiply(a, b):
	res = 0;
	while (b != 0):
		if (b & 1):
			 res = add(res, a); # if b is odd, add a to result
		a <<= 1
		b >>= 1
	}
	return res;
}
