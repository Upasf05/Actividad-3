import random #Librería random
import tkinter as tk #Librería Tkinter para interfaces gráficas

class JuegoPPT: #Clase principal que convierte el código en uno con POO, los objetos serán las funciones (def), que interactuan entre sí
    def __init__(self, root): #Función init que define las variables y los ajustes de la interfaz gráfica en el objeto root
        #Configurar la interfaz gráfica
        self.root = root #Configurar la ventana
        self.root.title("Piedra, Papel o Tijera") #Título de la apliación
        self.root.geometry("320x480") #Resolución de la pantalla
        self.root.configure(bg="lightblue") #Color de fondo

        #Configurar campos de resultados
        self.resultado_usuario = tk.StringVar() #Resultado del usuario
        self.resultado_computadora = tk.StringVar() #Resultado del programa
        self.resultado = tk.StringVar() #Para 'ganaste' o 'perdiste'

        self.crear_interfaz() #Invocar la siguiente función u objeto.

    def crear_interfaz(self): #Método que crea todos los botones y cuadros de texto
        #Mensajes de texto
        tk.Label(self.root, text="¡Bienvenido a Piedra, Papel o Tijera!", bg="lightblue").pack(pady=10) #Mensaje de bienvenida
        tk.Label(self.root, text="Elige una opción", bg="lightblue").pack(pady=5) #Mensaje de selección de opciones, debajo del de bienvenida 

        # Botones de opciones de piedra, papel o tijera. Cada uno es un objeto individual.
        tk.Button(self.root, text="Piedra", bg="blue", command=lambda: self.jugar(1)).pack(pady=5) #Para piedra
        tk.Button(self.root, text="Papel", bg="blue", command=lambda: self.jugar(2)).pack(pady=5) #Para papel
        tk.Button(self.root, text="Tijera", bg="blue", command=lambda: self.jugar(3)).pack(pady=5) #Para tijera

        # Etiquetas de texto para mostrar resultados a través de mensajes. Cada una es un ibjeto individual. 
        tk.Label(self.root, textvariable=self.resultado_usuario, bg="lightblue").pack(pady=5) #Resultado del usuario
        tk.Label(self.root, textvariable=self.resultado_computadora, bg="lightblue").pack(pady=5) #Resultado del programa
        tk.Label(self.root, textvariable=self.resultado, bg="lightblue").pack(pady=10) #Para 'ganaste' o 'perdiste'

        tk.Button(self.root, text="Jugar de nuevo", bg="blue", command=self.reiniciar).pack(pady=10) #Botón para reiniciar

    def jugar(self, opcion): #Método donde se ejecuta el juego
        opciones = {1: "Piedra", 2: "Papel", 3: "Tijera"} #Opciones numéricas de piedra papel o tijera
        njgd = opcion #Número del jugador, se escoge en base al botón que este pulsa
        nadv = random.randint(1, 3) #Número del programa, lo escoge aleatoriamente gracias a la librería Random

        # Mostrar las opciones elegidas
        self.resultado_usuario.set(f"Has escogido: {opciones[njgd]}") #Opción del usuario
        self.resultado_computadora.set(f"Opción de la computadora: {opciones[nadv]}") #Opción del programa

        # Determinar el resultado
        if njgd == nadv: #Empate si los valores del jugador y el programa son iguales
            self.resultado.set("Es un empate!")
        elif (njgd == 1 and nadv == 2) or (njgd == 2 and nadv == 3) or (njgd == 3 and nadv == 1): #Implementar la lógica de piedra papel o tijera
            self.resultado.set("Perdiste")
        else: #Incoporar automáticamente las lógicas invertidas con else
            self.resultado.set("¡Has ganado!")

    def reiniciar(self): #Método para reiniciar el programa
        self.resultado_usuario.set("") #Mostrar resultado del jugador
        self.resultado_computadora.set("") #Mostrar resultado del programa
        self.resultado.set("") #Mostrar si se ganó o perdió

if __name__ == "__main__": #Estructura para ejecutar la clase dentro del programa
    root = tk.Tk() #Crea y ejecuta la interfaz gráfica
    app = JuegoPPT(root) #Incopora en la ventana la clase como un objeto con todas sus funciones
    root.mainloop() #Permite la ejecución continua de la ventana

     
