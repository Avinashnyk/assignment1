print('Enter a word:')
word = input()
len_word = len(word) + 1
output= []
for i in range(-1,-len_word,-1):
    output.append(word[i])

print(output)
                