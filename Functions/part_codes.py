
part_code = ('TESLA:123-S')

supplier, part_info = part_code.split(':')
product_code, size = part_info.split('-')


print(f'{supplier}:{part_info}')

