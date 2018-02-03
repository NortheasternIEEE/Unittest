# Stage 2

Let's start passing test cases

romanNumeralMap is a tuple of tuples which defines three things:

1) The character representations of the most basic Roman numerals. Note that this is not just the single-character Roman numerals; you're also defining two-character pairs like CM (“one hundred less than one thousand”); this will make the toRoman code simpler later.

2) The order of the Roman numerals. They are listed in descending value order, from M all the way down to I.

3) The value of each Roman numeral. Each inner tuple is a pair of (numeral, value).

Here's where your rich data structure pays off, because you don't need any special logic to handle the subtraction rule. To convert to Roman numerals, you simply iterate through romanNumeralMap looking for the largest integer value less than or equal to the input. Once found, you add the Roman numeral representation to the end of the output, subtract the corresponding integer value from the input, lather, rinse, repeat.
