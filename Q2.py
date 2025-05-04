#Task-2
T={"name":["prince","Seema","Tamanna","Sarthak"],"age":[20,21,20,19],"roll":[198,240,292,235]}
 
student = []

for i in range(len(T["name"])):
    info = (T["roll"][i], T["name"][i], T["age"][i]) 
    student.append(info)
    
    
for p in student:
 print("name:{},roll:{},age:{}".format(p[1],p[0],p[2]))    
 