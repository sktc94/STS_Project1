wc_dict = {}  
file = open("data.txt", 'r')
for line in file:
  words = line.split()
  for word in words:
    word = word.lower()
    if not word in wc_dict:
      wc_dict[word] = 1
    else:
      wc_dict[word] = wc_dict[word] + 1
print(sorted(wc_dict.items(), key=lambda x: x[1], reverse=True))
