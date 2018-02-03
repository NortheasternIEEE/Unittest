import roman
import unittest
class SanityCheck(unittest.TestCase):
	def testSanity(self):
		"""fromRoman(toRoman(n))==n for all n"""
		for integer in range(1, 5000):
			numeral = roman.toRoman(integer)
			result = roman.fromRoman(numeral)
			self.assertEqual(integer, result)

class CaseCheck(unittest.TestCase):
	def testToRomanCase(self):
		"""toRoman should always return uppercase"""
		for integer in range(1, 5000):
			numeral = roman.toRoman(integer)
			self.assertEqual(numeral, numeral.upper())

	def testFromRomanCase(self):
		"""fromRoman should only accept uppercase input"""
		for integer in range(1, 5000):
			numeral = roman.toRoman(integer)
			roman.fromRoman(numeral.upper())
			self.assertRaises(roman.InvalidRomanNumeralError,
							  roman.fromRoman, numeral.lower())
