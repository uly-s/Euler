# Generate the names of the numbers from 1 to 1000 in English, with each number on a separate line.
# To ensure accuracy, we'll use a library that can convert numbers to words, if available, or implement logic for this conversion.

# Define a function to convert numbers to words, considering special cases for numbers like 11-19, and tens.

def number_to_words(n):
    # First, define the basic words for numbers and special cases.
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand"]

    if n == 0:
        return "zero"

    if n < 10:
        return ones[n]
    elif 10 <= n < 20:
        return teens[n-10]
    elif 20 <= n < 100:
        return tens[n//10] + ("" + ones[n%10] if n%10 != 0 else "")
    elif 100 <= n < 1000:
        return ones[n//100] + "hundred" + (("and" + number_to_words(n%100)) if n%100 != 0 else "")
    elif 1000 <= n < 10000:
        return ones[n//1000] + "thousand" + (("and" + number_to_words(n%1000)) if n%1000 != 0 else "")
    # For simplicity, we handle numbers up to 9999, which covers the required range.
    # Extending this to larger numbers would follow a similar pattern of dividing and conquering.

# Generate the list of number words from 1 to 1000.
number_words = [number_to_words(n) for n in range(1, 1001)]
    
sum = 0 

for number_word in number_words:
    sum += len(number_word)

print(sum)