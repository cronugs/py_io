f = open('newfile.txt', 'a')
f.write("Hello\n")
f.close()


f = open('newfile.txt', 'a')
lines = ['Hello', 'World', 'Welcome', 'To', 'File io \n']
text = ' '.join(lines)
f.writelines(text)
f.close()