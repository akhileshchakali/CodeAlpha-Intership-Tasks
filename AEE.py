import re

with open('input.txt','r') as file:
    text=file.read()

emails=re.findall(r'[\w\.-]+@[\w\.-]+\.\w+',text)

with open('output.txt','w') as file:
    for i in emails:
        file.write(i+'\n')

print('Email addresses extracted sucessfully!')