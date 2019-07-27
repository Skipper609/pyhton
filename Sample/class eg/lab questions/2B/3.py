def showInfo(student_dict):
    for key,value in student_dict.items():
        print(f"{key} : {value}")
    
inp = {"N001" : "Rajesh" , "N002" : "Suresh"}
showInfo(inp)