import datetime, time
import urllib.request

#일리아스 24장을 키워드로 분류해 손쉽게 요약할 수 있습니다
url = "http://classics.mit.edu/Homer/iliad.24.xxiv.html"

f = urllib.request.urlopen(url)
data = f.read().decode('utf-8')

begin = data.find("The assembly now broke up and the people went their ways each to his")
end = data.find("></A>horses")
end += len("></A>horses")

speech = data[begin:end]
speech = speech.replace("<A", " ")
speech = speech.replace(",", " ")
speech = speech.replace("\"", " ")
speech = speech.replace("></A>", " ")
speech = speech.replace("NAME", " ")
speech = speech.replace("=", " ")
speech = speech.split()

analyze = {}
for word in speech:
    analyze[word] = analyze.get(word, 0) + 1

flist = sorted(analyze.items(), key=lambda kv: kv[1], reverse=True)
print("number of words is ", len(flist))

cnt = 0
for k, v in flist:
    print(k, v)
    if cnt > 100: break
    cnt += 1
