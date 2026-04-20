import re

#task1
text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
res = re.split(r'[.!?]+', text)
for word in res:
    print(word.strip())


#task2
text = "картошка редисок лук огурец редиска, редиску"
res = re.sub(r"редис\w+", "*давайте жить дружно*", text)
print(res)

text = "картошка редисок лук огурец хороший человек хорошего человека "
res = re.sub(r"хорош\w+ челове\w+", "*давайте жить дружно*", text)
print(res)

#task3
date="12-3-1997"

res = re.findall(r'\d\d.\d\d.\d{4}',date)
print(res)