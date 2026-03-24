def main():
	coke = 50
	while coke > 0:
		pay = int(input("Insert Coin: "))
		if pay == 5 or pay == 10 or pay == 25:
			coke -= pay
			if coke > 0: 
				print(f"Amount Due: {coke}")
		else:
			print(f"Amount Due: {coke}")
	
	if coke == 0:
		print(f"Change Owed: {0}")
	elif coke < 0:
		print(f"Change Owed: {0 - coke}")
		
main()
