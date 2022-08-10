
memory = 0


def calculator(x, operator, y):
	if x.isalpha() or y.isalpha():
		print("Do you even know what numbers are? Stay focused!")
	elif operator not in "+-*/":
		print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
	else:
		match operator:
			case "+":
				if "." in x or "." in y:
					calculated_result = float(x) + float(y)
					return calculated_result
				else:
					calculated_result = int(x) + int(y)
					return calculated_result
			case "-":
				if "." in x or "." in y:
					calculated_result = float(x) - float(y)
					return calculated_result
				else:
					calculated_result = int(x) - int(y)
					return calculated_result
			case "*":
				if "." in x or "." in y:
					calculated_result = float(x) * float(y)
					return calculated_result
				else:
					calculated_result = int(x) * int(y)
					return calculated_result
			case "/":
				try:
					if "." in x or "." in y:
						calculated_result = float(x) / float(y)
						return calculated_result
					else:
						calculated_result = int(x) / int(y)
						return calculated_result
				except ZeroDivisionError:
					print("Yeah... division by zero. Smart move...")


def store_to_memory(number):
	print("Do you want to store the result? (y / n):")
	decision = input()
	if decision == "y":
		return number
	else:
		pass


def keep_going():
	print("Do you want to continue calculations? (y / n):")
	decision = input()
	if decision == "y":
		return True
	else:
		return False


def main():

	while True:
		global memory
		print("Enter an equation")
		calc = input()
		x, oper, y = calc.split(" ")
		if x == "M":
			x = memory
		elif y == "M":
			y = memory
		result = calculator(x, oper, y)
		print(result)
		memory = str(store_to_memory(result))
		if keep_going():
			continue
		else:
			break


if __name__ == "__main__":
	main()
