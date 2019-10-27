data ="prakash puri puri goswami"
word_list=data.split()
list_len=len(word_list)
word_dict={}

for word in word_list:
    print(f"word in for= {word}")
    print(f"word_list in for = {word_list}")
    if word in word_dict:
        print(f"word in if = {word}")
        print(f"word_dict in if = {word_dict}")
        word_dict[word]+=1
        print(f"word_dict[word]= {word_dict[word]}")

    else:
        word_dict[word]=1
        print(f"word_dict[word in else = {word_dict[word]}]")




print(word_dict)      
print(type(word_dict))     
