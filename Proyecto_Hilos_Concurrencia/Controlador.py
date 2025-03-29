import threading
import time
from modelo import SlotMachine
import tkinter as tk

class SlotMachineController:
    def __init__(self, root, view):
        self.root = root
        self.slot_machine = SlotMachine(reels=3)  
        self.view = view
        self.lock = threading.Lock()

    def spin_reels(self):
        """Inicia el giro de los carretes en un hilo separado para no bloquear la UI."""
        thread = threading.Thread(target=self._spin, daemon=True)
        thread.start()

    def _spin(self):
        """Simula el giro de los carretes con una animación progresiva."""
        with self.lock:
            
            total_spins = 20  # Cantidad total de iteraciones de la animación
            min_speed = 0.05   # Velocidad mínima (más rápida al inicio)
            max_speed = 0.3    # Velocidad máxima (más lenta al final)
            
            for i in range(total_spins):
                temp_results = self.slot_machine.generate_random_result()
                self.view.update_reels(temp_results)

                # Cálculo de velocidad progresiva (de rápida a lenta)
                speed = min_speed + (max_speed - min_speed) * (i / total_spins)
                time.sleep(speed)

            # Mostrar el resultado final
            results = self.slot_machine.play()
            self.view.update_reels(results)
            self.view.show_result_message(results)

            self.view.enable_spin_button()

