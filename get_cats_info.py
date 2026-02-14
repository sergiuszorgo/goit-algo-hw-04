def get_cats_info(path: str):
	cats = []
	try:
		with open(path, 'r',encoding='utf-8') as file:
			for line in file:
				line = line.strip()
				if not line:
					continue
				try:
					cat_id, cat_name, cat_age = line.split(',')
					cat_info = {"id": cat_id.strip(), "name": cat_name.strip(), "age": cat_age}
					cats.append(cat_info)

				except ValueError:
					print(f'Ошибка в строке: {line}')
					continue
		return cats
	except FileNotFoundError:
		print(f'Не найден файл: {path}')
	except Exception as e:
		print(f'Ошибка: {e}')

cats_info = get_cats_info("cats_info.txt")
print(cats_info)
