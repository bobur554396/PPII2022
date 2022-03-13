#     - [ ] open method (read - r / append - a / write - w / create - x)

f = open('input3.txt', 'x')

f.write('new line')
# f.writelines(['\nline1', '\nline2'])


f.close()
