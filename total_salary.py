def total_salary(path):
	try:
		with open(path, 'r', encoding='utf-8') as file:
			salaries = []
			for line in file:
				line = line.strip()
				if not line:
					continue
				try:
					_, salary_str = line.split(',')
					salary = float(salary_str.strip())
					salaries.append(salary)
				except ValueError:
					print(f'Ошибка в строке {line}')

			# if not salaries:
			# 	return (0, 0)
			total = sum(salaries)
			average = total / len(salaries)

			return (total, average)
		
	except FileNotFoundError:
		print(f'Файл: {path} - не найден')
		return (0, 0)
	except Exception as e:
		print(f'Ошибка: {e}')
		return (0, 0)


total, average = total_salary("salary_file.txt")
print(f"Общая сумма заработной платы: {total:.2f}, Средняя заработная плата: {average:.2f}")