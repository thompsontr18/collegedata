d={}
if (0,0) in d:
    print("already there")
else:
    d[(0,0)]=["hi","wassup"]
print("Second time")
if (0,0) in d:
    print("already there")
    print(d[(0,0)])
else:
    d[(0,0)]=["hi","wassup"]