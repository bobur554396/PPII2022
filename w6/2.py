#     - [ ] open method (read - r / append - a / write - w / create - x)

f = open('input4.txt', 'a')

# f.write('new line')
# f.write('\nnew line')

f.writelines(['\nline1', '\nline2'])


f.close()

