import os

def IBW(sexo,altura):
  if (sexo == 1):
    pesoI = round(56.2+1.41*((altura/2.54)-60),1)
    print(f"""
      *+*+*+*+*+*+*+*+*+*+*+*+*+*+**+*++*+*+*+*+**+*+
          {nombre} tu peso ideal es: {pesoI}
      *+*+*+*+*+*+*+*+*+*+*+*+*+*+**+*++*+*+*+*+**+*+
          """)
  elif (sexo == 2):
    pesoI = round(53.1+1.36*((altura/2.54)-60),1)
    print(f"""
      *+*+*+*+*+*+*+*+*+*+*+*+*+*+**+*++*+*+*+*+**+*+
          {nombre} tu peso ideal es: {pesoI}
      *+*+*+*+*+*+*+*+*+*+*+*+*+*+**+*++*+*+*+*+**+*+
          """)
  else:
    print("Sexo no valido.\n Seleccione Masculino o Femenino")

    
def quemCalo(peso):

  op=0
  dur=0
  acc=""
  met=0
  qc = 0
  print(f"""
    *+*+*+*+*+*+*+*+*+*+*+*+*+*+**+*++*+*+*+*+**+*+
              Quemando Calorias
    *+*+*+*+*+*+*+*+*+*+*+*+*+*+**+*++*+*+*+*+**+*+
        """)
  while op != 6:
    print(f"""         {nombre} que actividad deseas realizar?
    *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**+*++*+*+*+*+**+*+
          1. Caminar.
          2. Tenis.
          3. Montar bicicleta.
          4. Correr.
          5. Nadar.
          6. Salir.
    *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**+*++*+*+*+*+**+*+
          """)
    op=int(input())
    if(op==1):
      acc="Caminando"
      met=2
    if(op==2):
      acc="Jugando Tenis"
      met=5
    if(op==3):
      acc="Montando bicicleta"
      met=14
    if(op==4):
      acc="Corriendo"
      met=6
    if(op==5):
      acc="Nadando"
      met=9.8
    if(op==6):
      titulo()
    else:
      "Seleccione una opcion valida"
    

    print(f"""       {nombre} Cuanto tiempo estuviste {acc}? (min)""")
    
    dur = int(input())
    os.system ("clear") 
    
    qc = (dur*met*peso)/200
    print(f""" 
          {nombre} tu quema de calorias fue:
          {qc} cal, por estar {acc} durante {dur} min.
          """)
    op = 6
          

def pGC():
  porcent = 0
  imc= peso/altura
  if(sexo==1):
    porcent= round(1.20*imc+0.23*(edad-16.2),2)
    print(f"""
        {nombre}, tu porcentaje de grasa corporal es: {porcent}%
        """)
  elif(sexo==2):
    porcent= round(1.20*imc+0.23*(edad-5.4),2)
    print(f"""
        {nombre}, tu porcentaje de grasa corporal es:{porcent}% """)

def IMB():
  ind=0
  if(sexo==1):
    ind= round((13397*peso)+(4799*edad)-(5677*altura)+88362,2)
    print(f"""
        {nombre}, tu indice metabolico basal es: {ind}. """)
  elif(sexo==2):
    ind= round((9247*peso)+(3098*edad)-(4330*altura)+47593,2)
    print(f"""
        {nombre}, tu indice metabolico basal es: {ind}. """)
  
def titulo():
  print("""
    *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**+*++*+*+*+*+**+*+
            Calculadora Amigable.
    *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**+*++*+*+*+*+**+*+""")
  

#solicito al usuario que operacion desea realizar
def menuOp():
  op=0
  titulo()
  while op != 5:
    print(f"""           {nombre} que operacion deseas realizar?
    *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**+*++*+*+*+*+**+*+
      1. Peso ideal                    | Resumen: 
      2. Quemando calorias.            |  Nombre: {nombre}. 
      3. Porcentaje de grasa corporal. |  Edad: {edad} años. 
      4. Indice metabolico basal.      |  Estatura: {altura} cm.
      5. Salir                         |  Peso: {peso} kg.
    *+*+*+*+*+*+*+*+*+*+*+*+*+*+*+*+**+*++*+*+*+*+**+*+
          """)

    op=int(input())

    os.system ("clear")  

    if(op) == 1:
      titulo()
      IBW(sexo,altura)
    elif(op) == 2:
      titulo()
      quemCalo(peso)
    elif(op) == 3:
      titulo()
      pGC()
    elif(op) == 4:
      titulo()
      IMB()
    elif(op) == 5:
      print("Saliendo.")
    else:
      print(f"{nombre}, seleccione una opcion valida.")


titulo()
#Solicito los datos al usuario
nombre=input("Cual es tu nombre?\n")
sexo=(int(input(f"""{nombre} cual es tu sexo?\n
    1.Hombre
    2.Mujer\n""")))
edad=int(input(f"{nombre} cual es tu edad? (años)\n"))
peso=int(input(f"{nombre} cual es tu peso? (kg)\n"))
altura=int(input(f"{nombre} cual es tu altura? (cm)\n"))

os.system ("clear")  
menuOp()

