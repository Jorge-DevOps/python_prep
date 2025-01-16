from collections import namedtuple

if __name__ == '__main__':
    rows = int(input())  
    #Crear un namedtuple llamado 'Student' con campos: que recibe en input
    Student = namedtuple('Student', input())
    data_list = [input().split() for i in range(rows)]
    #Crear un agrega los valores al tuple, con un for, y accede a al valor de marks (puntjae) lo convierte a entere, lo suma y saca el promedio
    print(sum([int(Student(data[0], data[1], data[2], data[3]).MARKS) for data in data_list])/rows)
    print(Student.MARKS)


#5
#MARKS      CLASS      NAME       ID        
#92         2          Calum      1         
#82         5          Scott      2         
#94         2          Jason      3         
#55         8          Glenn      4         
#82         2          Fergus     5