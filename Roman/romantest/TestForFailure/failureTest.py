import roman
import unittest
class ToRomanBadInput(unittest.TestCase):
	def testTooLarge(self):
		"""toRoman should fail with large input"""
		self.assertRaises(roman.OutOfRangeError, roman.toRoman, 5000)

	def testZero(self):
		"""toRoman should fail with 0 input"""
		self.assertRaises(roman.OutOfRangeError, roman.toRoman, 0)

	def testNegative(self):
		"""toRoman should fail with negative input"""
		self.assertRaises(roman.OutOfRangeError, roman.toRoman, -1)

	def testDecimal(self):
		"""toRoman should fail with non-integer input"""
		self.assertRaises(roman.NotIntegerError, roman.toRoman, 0.5)

class FromRomanBadInput(unittest.TestCase):
	def testTooManyRepeatedNumerals(self):
		"""fromRoman should fail with too many repeated numerals"""
		for s in ('MMMMM', 'DD', 'CCCC', 'LL', 'XXXX', 'VV', 'IIII'):
			self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, s)

	def testRepeatedPairs(self):
		"""fromRoman should fail with repeated pairs of numerals"""
		for s in ('CMCM', 'CDCD', 'XCXC', 'XLXL', 'IXIX', 'IVIV'):
			self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, s)

	def testMalformedAntecedent(self):
		"""fromRoman should fail with malformed antecedents"""
		for s in ('IIMXCC', 'VX', 'DCM', 'CMM', 'IXIV',
				  'MCMC', 'XCX', 'IVI', 'LM', 'LD', 'LC'):
			self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, s)

	def testBlank(self):
		"""fromRoman should fail with blank string"""
		self.assertRaises(roman.InvalidRomanNumeralError, roman.fromRoman, "")
