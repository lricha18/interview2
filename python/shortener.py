######## Shortener

# Given two strings s, t, determine if string s can be changed into string t using the following rule:

# Remove any number of lowercase letters from s (or none at all), then capitalize all remaining letters of s.

# Example of the rule:
# s = AAbcD
# Possible outputs using the rule:
# Remove none, capitalize -> AABCD
# Remove c, capitalize -> AABD
# Remove b, capitalize -> AACD
# Remove b and c, capitalize -> AAD

# If it is possible to create the string t by processing s using the rule, then the function should return True, otherwise return False.

def shortener(s, t):
	#Base cases for recursion
	if(len(t) > len(s)): # if there is a substring of T that needs to be found once S is empty, then T cannot be made from S
		return False
	elif(len(t) == 0): 
		if(len(s) == 0): # if substring of t has been reduced to empty, but s is also empty, this substring will work
			return True
		elif(not(s.islower())): # If t has been found in substring but there are still capitals in s, then by rule, this string won't work
			return False
		else:
			return True # If t has been found and remaining s is only lowercase, then substring is valid

	# Will find first occurence of capital letter from T that also in S and split on this letter and check each half 
	for i in range(0, len(t)): 
		index_of_i = s.find(t[i])
		if(index_of_i != -1):
			
			if(index_of_i==0):
				left = shortener(s[0:index_of_i],t[0:i])
			else:
				left = True

			right = shortener(s[index_of_i + 1: len(s)], t[i+1:len(t)])
			return (left and right)

	# This will check if remaining values in S can be found in correct order to match remaining T
	s = s.upper()
	check = 0
	for i in range(0, len(t)):
		check = s[check:len(s)].find(t[i])
		if(check == -1):
			return False
	

	return True

# Test Cases
test_cases = [
	("", "", True),
	("", "B", False),
	("a", "", True),
    ("daBccd", "ABC", True),
    ("sYOCa", "YOCN", False),
    ("aaaaaa", "AAAAAAA", False),
    ("SVAHHHMVIIDYIcOSHMDUAVJRIBxBZQSUBIVEBHfVTZVSHATUYDJGDRRUBQFHEEEUZLQGXTNKFWUYBAeFKUHSFLZEUINBZYRIXOPYYXAEZZWELUPIEIWGZHEIYIROLQLAVHhMKRDSOQTJYYLTCTSIXIDAnPIHNXENWFFZFJASRZRDAPVYPAViVBLVGRHObnwlcyprcfhdpfjkyvgyzpovsgvlqbhtwrucvszaqinbgeafuswkjrcexvyzq","SVAHHHMVIIDYIOSHMDUAVJRIBBZQSUBIVEBHVTZVSHATUYDJGDRRUBQFHEEEUZLQGXTNKFWUYBAFKUHSFLZEUINBZYRIXOPYYXAEZZWELUPIEIWGZHEIYIROLQLAVHMKRDSOQTJYYLTCTSIXIDAPIHNXENWFFZFJASRZRDAPVYPAVVBLVGRHO", True),
    ("a", "AA", False),
    ("UZJMUCYHpfeoqrqeodznwkxfqvzktyomkrVyzgtorqefcmffauqhufkpptaupcpxguscmsbvolhorxnjrheqhxlgukjmgncwyastmtgnwhrvvfgbhybeicaudklkyrwvghpxbtpyqioouttqqrdhbinvbywkjwjkdiynvultxxxmwxztglbqitxmcgiusfewmsvxchkryzxipbmgrnqhfmlghomfbsKjglimxuobomfwutwfcmklzcphbbfohnaxgbaqbgocghaaizyhlctupndmlhwwlxxvighhjjrctcjBvxtagxbhrbrWwsyiiyebdgyfrlztoycxpjcvmzdvfeYqaxitkfkkxwybydcwsbdiovrqwkwzbgammwslwmdesygopzndedsbdixvi","UZJMUCYH", False)
]

for case in test_cases:
    s, t, output = case
    print(shortener(s, t) == output)