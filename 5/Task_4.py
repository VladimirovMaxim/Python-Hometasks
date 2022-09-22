def rle_encode(data):
    final_code = ''
    prev_char = ''
    count = 1
    if not data: return ''
    for char in data:
        if char != prev_char:
            if  prev_char:
                final_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        final_code += str(count) + prev_char
        return final_code



def rle_decode(new_data):
    final_decode = ""
    count = ""
    for char in new_data:
        if char.isdigit():
            count += char
        else:
            final_decode += char * int(count)
            count = ""
    return final_decode



text_3 = open("text_3.txt","w")
text_3.write("aaagggyuyiiiwwnnn")
text_3.close()

text_3 = open("text_3.txt","r")
data = text_3.read()
print(data)
text_3.close()

text_4 = open("text_4.txt","w")
coded = rle_encode(data)  
text_4.write(coded)
text_4.close()

text_5 = open("text_5.txt","w")

text_5.write(rle_decode(coded))
text_5.close()