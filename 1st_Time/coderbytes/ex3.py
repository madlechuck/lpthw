from string import maketrans

def LetterChanges(str): 
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
	key = "BCDEFGHIJKLMNOPQRSTUVWXYZAbcdefghijklmnopqrstuvwxyza"
	table = maketrans(alphabet, key)
	print(str.translate(table))
    
    

print LetterChanges(raw_input("Enter string to convert:"))  
