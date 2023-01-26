
class MenuOperBasicas:
    
    def _init_(self):
       pass

    def suma(self, a, b):
         self.n1=a
         self.n2=b
         self.result= self.n1+self.n2
         print("La suma de los dos números es: {}".format(self.result)) 

    def resta(self, a, b):
         self.n1=a
         self.n2=b
         self.result= self.num1-self.num2
         print("La resta de los dos números es: {}".format(self.result)) 

    def multiplicacion(self, a, b):
         self.n1=a
         self.n2=b
         self.result= self.num1*self.num2
         print("La multiplicación de los dos números es: {}".format(self.result)) 
    
    def division(self, a, b):
         self.n1=a
         self.n2=b
         try:
          self.result= self.num1/self.num2
          print("La división de los dos números es: {}".format(self.result))
         except ZeroDivisionError:
          print("¡La división entre cero no es posible!")
         
          

def main():
    
    opcion = 0
    while True:
      
      print(" Menú... 1.-Sumar 2.-Restar 3.-Multiplicar 4.-Dividir")
      
      opcion = int(input("Elige una opción: "))
      obj=MenuOperBasicas()


      if opcion == 1:
        n1= int(input("Ingresa el primer número: "))
        n2= int(input("Ingresa el segundo número: "))        
        obj.suma(n1,n2)
        
      elif opcion == 2:
          n1= int(input("Ingresa el primer número: "))
          n2= int(input("Ingresa el segundo número: "))
          obj.resta(n1,n2)

      elif opcion == 3:
          n1= int(input("Ingresa el primer número: "))
          n2= int(input("Ingresa el segundo número: "))
          obj.multiplicacion(n1,n2)

      elif opcion == 4:
          n1= int(input("Ingresa el primer número: "))
          n2= int(input("Ingresa el segundo número: "))      
        
          obj.division(n1,n2)

    
    
if __name__ == '_main_':
    main()
    

    