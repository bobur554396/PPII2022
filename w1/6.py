a = 2
b = 3

print('a = ' + str(a) + ', b = ' + str(b))
print('a = %s, b = %s' % a, b)
print('a = {}, b = {}'.format(a, b))
print('a = {0}, b = {1}'.format(a, b))
print('a = {1}, b = {0}'.format(a, b))
print('a = {foo}, b = {bar}'.format(foo=a, bar=b))
print(f'a = {a}, b = {b}')
