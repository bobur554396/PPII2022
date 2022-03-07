import re
import csv # comma seperated value

with open('row.txt', 'r') as f:
  text = f.read()


# bin_pattern = r'БИН(?P<BIN>.+)'
# ndc_pattern = r'НДС Серия(.+)'
# BIN = re.search(bin_pattern, text)
# if BIN:
#   BIN = BIN.group('BIN').strip()

# NDC = re.search(ndc_pattern, text)
# if NDC:
#   NDC = NDC.group(1).strip()


bin_ndc_pattern = r'БИН(?P<BIN>.+)\nНДС Серия(?P<NDC>.+)'

res = re.search(bin_ndc_pattern, text)
if res:
  BIN = res.group('BIN').strip()
  NDC = res.group('NDC').strip()


bill_num = re.search(r'Порядковый номер чека(?P<bill_number>.+)', text)
bill_num = bill_num.group('bill_number').strip()

products_pattern = r'(?P<name>.+)\n(?P<count>.+)x(?P<price>.+)\n(?P<total>.+)\nСтоимость\n(?P<total2>.+)'

data = [['БИН', 'НДС', 'номер чека', 'name', 'count', 'price', 'total', 'total2']]

products_res = re.finditer(products_pattern, text)
for res in products_res:
  data.append([
      BIN, 
      NDC, 
      bill_num, 
      res.group('name').strip(),
      res.group('count').strip(),
      res.group('price').strip(),
      res.group('total').strip(),
      res.group('total2').strip()
  ])

with open('products.csv', 'w') as f:
  writer = csv.writer(f)
  writer.writerows(data)
  
