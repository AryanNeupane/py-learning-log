class school:
    name="abc public school"
    address="st-2 load"
    
    def __init__(self,name,address,level):
        self.name=name
        self.address=address,
        self.level=level

    @staticmethod
    def quality():
        print("good quality Education")



s1=school("parijat","kapilbastu",12)

print(s1.level)
s1.quality()

