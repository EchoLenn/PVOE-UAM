print("Numero de alumnos en la lista: ")
numero=int(input())
ueas=["Calculo integral","Calculo diferencial","Diseño logico","Fisica","Quimica"]

matriculas=[]

def solicitar_calificaciones(num):
    caliA=[]
    for i in range(num):
        print(f"Ingresa la matricula del alumno {i+1}:")
        matricula=input()
        matriculas.append(matricula)
        for j in range(5):
             print("Alumno:")
             alumnoM = input()

             print(f"Calificación de {ueas[j]}:")
             uea=int(input())
             caliA.append(uea)
    
    return caliA

def calcular_promedios(arreglo):
        pos=0
        listaP=[]
        for i in range(numero):
            suma=0
            promedio=0
            cont=0

            while cont<5:
                suma+=arreglo[pos]
                pos+=1
                cont+=1

            promedio=suma/5
            listaP.append(promedio)
        return listaP

def imprimir_lista():
     arr= solicitar_calificaciones(numero)
     prom=calcular_promedios(arr)

     print("Alumno\tCI\tCD \tDL\tFis\tQuim \tPromedio")
     for i in range(numero):
          print(matriculas[i],f"\t{arr[i*5]}\t{arr[i*5+1]}\t{arr[i*5+2]}\t{arr[i*5+3]}\t{arr[i*5+4]}\t{prom[i]}")
    
imprimir_lista()
