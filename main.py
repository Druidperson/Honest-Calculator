memory = float(0)


def take_input():
	print("Enter an equation")
	calc = input()
	x, oper, y = calc.split(" ")
	if x == "M":
		x = memory
	elif y == "M":
		y = memory
	return str(x), str(oper), str(y)


def store_to_memory(number):
	global memory
	print("Do you want to store the result? (y / n):")
	decision = input()
	if decision == "y":
		memory = number
	else:
		pass


def calculator():
	while True:
		x, oper, y = take_input()
		if x.isalpha() or y.isalpha():
			print("Do you even know what numbers are? Stay focused!")
		elif oper not in "+-*/":
			print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
		else:
			match oper:
				case "+":
					if "." in x or "." in y:
						calculated_result = float(x) + float(y)
						print(calculated_result)
						return calculated_result
					else:
						calculated_result = float(x) + float(y)
						print(calculated_result)
						return calculated_result
				case "-":
					if "." in x or "." in y:
						calculated_result = float(x) - float(y)
						print(calculated_result)
						return calculated_result
					else:
						calculated_result = int(x) - int(y)
						print(calculated_result)
						return calculated_result
				case "*":
					if "." in x or "." in y:
						calculated_result = float(x) * float(y)
						print(calculated_result)
						return calculated_result
					else:
						calculated_result = float(x) * float(y)
						print(calculated_result)
						return calculated_result
				case "/":
					try:
						if "." in x or "." in y:
							calculated_result = float(x) / float(y)
							print(calculated_result)
							return calculated_result
						else:
							calculated_result = int(x) / int(y)
							print(calculated_result)
							return calculated_result
					except ZeroDivisionError:
						print("Yeah... division by zero. Smart move...")


def main():
	while True:
		result = calculator()
		store_to_memory(result)
		print("Do you want to continue calculations? (y / n):")
		decision = input()
		if decision == "y":
			continue
		else:
			break


if __name__ == "__main__":
	main()
