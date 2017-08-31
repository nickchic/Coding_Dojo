word_list = ['hello','world','my','name','is','Anna']
char = 'o'
newList = []

for idx in range(0,len(word_list)):
    if not word_list[idx].find(char) == -1:
        newList.append(word_list[idx])

print newList
