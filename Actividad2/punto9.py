students = [
    {"name": " Ana García ", "grade": "8", "status": "aprobado"},
    {"name": "pedro lópez", "grade": "4", "status": "DESAPROBADO"},
    {"name": "MARÍA FERNÁNDEZ", "grade": "10", "status": "Aprobado"},
    {"name": "ana garcía", "grade": "9", "status": "aprobado"},
    {"name": None, "grade": "7", "status": "aprobado"},
    {"name": "Luis Martínez ", "grade": None, "status": "aprobado"},
    {"name": " carlos RUIZ", "grade": "6", "status": "aprobado"},
    {"name": "PEDRO LÓPEZ ", "grade": "3", "status": "desaprobado"},
    {"name": " ", "grade": "5", "status": "aprobado"},
    {"name": "María Fernández", "grade": "7", "status": "APROBADO"},
    {"name": "Sofía Torres", "grade": "9", "status": "Aprobado"},
    {"name": " sofía torres ", "grade": "8", "status": "aprobado"},
    {"name": "Carlos Ruiz", "grade": "6", "status": "APROBADO"},
    {"name": "Roberto Díaz", "grade": "absent", "status": "ausente"},
    {"name": "roberto díaz", "grade": "", "status": "Ausente"},
    {"name": None, "grade": None, "status": None},
    {"name": "Laura Méndez", "grade": "7", "status": "aprobado"},
    {"name": " laura méndez", "grade": "8", "status": "Aprobado"},
    {"name": "GABRIELA RÍOS", "grade": "5", "status": "aprobado"},
    {"name": "gabriela ríos ", "grade": "4", "status": "Desaprobado"},
]



def fix_list(students):
    new_list = []
    for student in students:
        if(student["name"] == None or student["name"] == " " or student["name"] == ""):
            #print(student) anda
            continue
        else:
            if(student["name"].istitle() != True):
                student["name"] = student["name"].title().strip()
                #print(student) anda
            if(student["grade"] == None or student["grade"].isdigit() != True):
                continue
            else:
                if(student["status"] == None or student["status"] == " " or student["status"] == ""):
                    continue
                elif(student["status"].istitle() != True):
                    student["status"] = student["status"].title()
                    #print(student) anda
        es=False
        if(student["name"].strip().lower() in [estudiante["name"].strip().lower() for estudiante in new_list]):
            for estudiante in new_list:
                if (estudiante["name"].strip().lower() == student["name"].strip().lower()):
                    if(estudiante["grade"] > student["grade"]):
                        continue
                    else:
                        if(int(student["grade"]) >= 5):
                            estudiante["status"] = "Aprobado"
                        estudiante["grade"] = student["grade"]
                        es = True
            if(es):
                continue
            else:
                es = False
        else:
            new_list.append(student)
    students_ordenados = sorted(new_list, key=lambda s: s["name"].strip().lower(), reverse = False)
    return students_ordenados


new_list=fix_list(students)
for st in new_list:
    print(st)
    print("\n")