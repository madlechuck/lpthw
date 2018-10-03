formatter = "%r %r %r %r"  # defines the variable named formatter as a 4 format string
# this replaces the %r in formatter variable with numbrs
print formatter % (1, 2, 3, 4)  
# this replaces the %r in formatter with text numbers
print formatter % ("one", "two", "three", "Four")  
# this replaces the %r with True or false
print formatter % (True, False, False, True) 
# this replaces the %r with a print of the variable formatter... 
print formatter % (formatter, formatter, formatter, formatter)  
# this replaces the %r of formatter with text.
print formatter % ("I had this thing.", "That you could type up right.", "But it didn't sing.", "So I said goodnight.")  