# # EXAMPLE

# """
# Given a lower and an uppercase word
# It returns a list with the uppercase word
# """
# extract_uppercase("hello WORLD") => ["WORLD"]

# """
# # Given two uppercase words
# It returns a list with both words
# """
# extract_uppercase("HELLO WORLD") => ["HELLO", "WORLD"]

# """
# Given two lowercase words
# It returns an empty list
# """
# extract_uppercase("hello world") => []

# """
# Given a lower and a mixed case word
# It returns an empty list
# """
# extract_uppercase("hello WoRLD") => []

# """
# Given a lowercase word and an uppercase word with an exclamation mark
# It returns a list with the uppercase word, no exclamation mark
# """
# extract_uppercase("hello WORLD!") => ["WORLD"]

# """
# Given an empty string
# It returns an empty list
# """
# extract_uppercase("") => []

# """
# Given a None value
# It throws an error
# """
# extract_uppercase(None) throws an error