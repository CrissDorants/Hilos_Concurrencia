import tkinter as tk
from tkinter import messagebox
import random

class SlotMachineView:
    def __init__(self, root, reels=3):
        self.root = root
        self.controller = None  # Se inicializa vacío para evitar el import circular
        self.bet_amount = tk.IntVar()
        self.reels = reels

        # Configuración de la ventana
        self.root.title("🎰 Tragamonedas 🎰")
        self.root.configure(bg="black")
        self.create_ui()

    def set_controller(self, controller):
        """Asigna el controlador después de inicializar la vista."""
        self.controller = controller

    def create_ui(self):
        tk.Label(self.root, text="Apuesta:", font=("Arial", 16), fg="white", bg="black").pack()
        tk.Entry(self.root, textvariable=self.bet_amount, font=("Arial", 14)).pack()

        # Área de los carretes con emojis
        self.reel_labels = [tk.Label(self.root, text="❓", font=("Arial", 40), fg="white", bg="black") for _ in range(3)]
        for label in self.reel_labels:
            label.pack(pady=5)

        # Botón de giro (se desactiva hasta que el controlador esté listo)
        self.spin_button = tk.Button(self.root, text="🎰 Girar 🎰", font=("Arial", 16), state=tk.DISABLED, command=self.spin)
        self.spin_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 18), fg="white", bg="black")
        self.result_label.pack()

    def enable_spin_button(self):
        """Activa el botón de giro cuando el controlador está listo."""
        self.spin_button.config(state=tk.NORMAL)

    def spin(self):
        """Método llamado al presionar el botón de girar."""
        if self.controller:
            self.controller.spin_reels()

    def update_reels(self, symbols):
        """Actualiza los carretes con los nuevos símbolos."""
        for i, symbol in enumerate(symbols):
            self.reel_labels[i].config(text=symbol, fg=random.choice(["yellow", "red", "blue", "green"]))

    def show_result_message(self, win):
        """Muestra un mensaje de resultado."""
        if win:
            self.result_label.config(text="🎉 ¡Ganaste! 🎉", fg="gold")
        else:
            self.result_label.config(text="😢 Intenta de nuevo", fg="white")

# --- Importación DIFERIDA del Controlador ---
if __name__ == "__main__":
    from Controlador import SlotMachineController  # Ahora se importa aquí

    root = tk.Tk()
    view = SlotMachineView(root)
    controller = SlotMachineController(root, view)  # Se pasa la vista al controlador
    view.set_controller(controller)  # Asigna el controlador a la vista
    view.enable_spin_button()  # Activa el botón de girar
    root.mainloop()
