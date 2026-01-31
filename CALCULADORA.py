#proyecto: "calculadora básica por consola". Lenguaje: Python. Autor: Paleo Sol. Publicado el 31 de Enero del 2026.
print("por favor, ingrese los siguientes datos:")
name=input("nombre:")

#damos la bienvenida e introducimos al usuario
print("¡Bienvenido/a a mi Calculadora básica," + name + "!")
print("En esta calculadora podrás realizar las siguientes operaciones: + para sumar, - para restar, * para multiplicar y / para dividir.")
print("Ingresa la operación que deseas realizar:")

#realizamos la operación según los datos ingresados por el usuario. La función "WHILE TRUE" permite al usuario seguir operando cuantas veces quiera.
while True:
    try:
        num1=float(input("primer número de tu operación:"))
        operation=str(input("operación:"))
        num2=float(input("segundo número de tu operación:"))
        if operation not in ["+","-","*","/"]:
           print("Lo siento, la operación ingresada no es válida. Intentalo otra vez.")
           continue
        if operation=="+":
           result=num1+num2
           print("=" + str(result))
        elif operation=="-":
             result=num1-num2
             print("=" + str(result))
        elif operation=="*":
             result=num1*num2
             print("=" + str(result))
        elif operation=="/":
            if num2==0:
               print("ERROR. no se puede dividir por cero.")
            else: 
                result=num1/num2
                print("=" + str(result))
    except ValueError:
          print("Lo siento, los números ingresados no son válidos. Intentalo otra vez.")
    answer=str(input("¿deseas continuar operando? (si/no):"))
    if answer.lower()=="no":
        print("¡Muchas gracias por usar mi calculadora," + name + "!" "¡Hasta luego! Saliendo...")
        break 


