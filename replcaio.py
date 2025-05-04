

# word="sheets"

# with open("Poems.txt","r") as f:
#     content=f.read()
# newC=content.replace(word,"##########")
# with open("Poems.txt","w") as f:
#     f.write(newC)

words=['sheets','Ipsum']

with open("Poems.txt","r") as f:
    content=f.read()


for i in words:
    newC=content.replace(i,"##########")

with open("Poems.txt","w") as f:
    f.write(newC)   





