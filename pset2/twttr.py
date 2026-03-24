def main():
	default_text = input("Input: ")
	convert(default_text)
		
def convert(default):
	vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
	print("Output: ", end="")
	for letter in default:
		if letter not in vowels:
			print(letter, end="")
						
main()
