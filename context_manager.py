from contextlib import contextmanager
from datetime import datetime

def create_cook_book():
	with open ('cook_book_f.txt', encoding='utf8') as f:
		cook_book = {}
		for line in f:
			dish = line.strip()
			amount_of_ingredients = int(f.readline())
			ingredints_list = []
			while amount_of_ingredients != 0:
				ingredient = f.readline().strip().split(' | ')
				ingredient_dict = {}
				ingredient_dict['ingridient_name'] = ingredient[0]
				ingredient_dict['quantity'] = ingredient[1]
				ingredient_dict['measure'] = ingredient[2]
				ingredints_list.append(ingredient_dict)
				amount_of_ingredients -= 1
			cook_book[dish] = ingredints_list
			f.readline()
	return cook_book


def get_shop_list_by_dishes(dishes, person_count):
	cook_book = create_cook_book()
	products = {}
	for dish in dishes:
		for product in cook_book[dish]:
			products_key = product['ingridient_name']
			product_info = {}
			if products_key not in products.keys():
				product_info['measure'] = product['measure']
				product_info['quantity'] = int(product['quantity']) * int(person_count)
				products[products_key] = product_info
			else:
				product_info['measure'] = product['measure']
				product_info['quantity'] = products[products_key]['quantity'] + int(product['quantity']) * int(person_count)
				products[products_key] = product_info
	print(products)


@contextmanager
def working_time(file_path):
	try:
		file = open(file_path, 'w', encoding='utf')
		start = datetime.now()
		file.write(f'Начало выполнения: {str(start)}\n')
		yield file
		
	finally:
		end = datetime.now()
		delta = end - start
		file.write(f'Конец выполнения: {str(end)}\n')
		file.write(f'Время выполнения программы: {delta}')
		file.close()

with working_time('working_time.txt') as file:
	print(create_cook_book())
	print()
	get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)