def main():
	x, y = get_fuel("Fraction: ")
	print_percentage(x, y)
		
def get_fuel(prompt):
	while True:
		fuel_fraction = (input(prompt))
		try:
			x, y = fuel_fraction.split("/")
			x, y = int(x), int(y)	
		except ValueError:
			pass
		else:
			if x < 0 or x > y or y <= 0:
				continue
			return x, y

def print_percentage(x, y):
	fuel_percent = round(x / y *100)
	if fuel_percent <= 1:
		print("E")
	elif fuel_percent >= 99:
		print("F")
	else:
		print(f"{fuel_percent}%")
			
main()
