# Test Requirements for functions in Roman.py

1) toRoman should return the Roman numeral representation for all integers 1 to 3999.

2) toRoman should fail when given an integer outside the range 1 to 3999.

3) toRoman should fail when given a non-integer number.

4) fromRoman should take a valid Roman numeral and return the number that it represents.

5) fromRoman should fail when given an invalid Roman numeral.

6) If you take a number, convert it to Roman numerals, then convert that back to a number, you should end up with the number you started with. So fromRoman(toRoman(n)) == n for all n in 1..3999.

7) toRoman should always return a Roman numeral using uppercase letters.

8) fromRoman should only accept uppercase Roman numerals (i.e. it should fail when given lowercase input).
