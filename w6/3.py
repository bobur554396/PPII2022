#     - [ ] open method (read - r / append - a / write - w / create - x)

f = open('input2.txt', 'w')

f.write('new line')
f.write('\nnew line 2')

# f.writelines(['\nline1', '\nline2'])


f.close()
