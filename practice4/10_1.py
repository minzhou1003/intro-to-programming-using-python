# minzhou@bu.edu

def get_grades():
    grades = list(map(int,(input('Enter scores:').split())))
    best = max(grades)
    
    for student, score in enumerate (grades):
        if score >= best - 10:
            print('Student {} score is {} and grade is A'.format(student, score))
            
        elif score >= best - 20:
            print('Student {} score is {} and grade is B'.format(student, score))
             
        elif score >= best - 30:
            print('Student {} score is {} and grade is C'.format(student, score))
            
        elif score >= best - 40:
            print('Student {} score is {} and grade is D'.format(student, score))
           
        else:
            print('Student {} score is {} and grade is F'.format(student, score))
            return  

get_grades()          
            

