wording = []
word = input("Please type the ssenntence:  ").split()

x = 1
y = (len(word))//2
for i in range(y):
    wording.append(word[x])
    x = x + 2
for i in range(len(wording)):
    word.remove(wording[i])
print(" ".join(word))

