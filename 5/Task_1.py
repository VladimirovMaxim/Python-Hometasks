# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text_1 = open("text_1.txt","w")
text_1.write("abcghg try abcaba to do doabc it abcit in English ")
text_1.close()

text_1 = open("text_1.txt","r")
data = text_1.read()
print(data)
text_1.close

text_2= open("text_2.txt","w")
result = " ".join(filter(lambda x: "abc" not in x, data.split()))
print(result)
text_2.writelines(result)
text_2.close()