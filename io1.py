with open("Poems.txt") as f:
    c=f.read()
    if("sheets" in c):
        print("SHeets is Present")
    else:
        print("Not present")