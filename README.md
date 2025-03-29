# Hilos_Concurrencia
🎰 Tragamonedas - Proyecto Python con MVC

Este proyecto implementa un juego de tragamonedas simple utilizando el patrón Modelo-Vista-Controlador (MVC) con Python y tkinter para la interfaz gráfica.
🚀 Cómo ejecutar el proyecto

    Requisitos previos:

        Python 3.x instalado

        No se requieren librerías adicionales (usa módulos estándar)

    Ejecución:
    bash
    Copy

    python view.py

    El programa iniciará automáticamente la interfaz gráfica.

🧩 Estructura del proyecto

El proyecto sigue una arquitectura MVC (Modelo-Vista-Controlador):
Copy

tragamonedas/
├── view.py        # Vista (Interfaz gráfica)
├── Controlador.py # Controlador (Lógica del juego)
└── modelo.py      # Modelo (Datos y reglas del juego)

🎮 Cómo jugar

    Ingresa el monto de tu apuesta en el campo correspondiente

    Haz clic en el botón "🎰 Girar 🎰"

    Los carretes girarán mostrando una animación

    Al detenerse, verás si ganaste o perdiste

    ¡Puedes volver a jugar cuantas veces quieras!

🔧 Funcionamiento técnico
📦 Modelo (modelo.py)

    Contiene las clases base del juego:

        Symbol: Representa los símbolos del carrete

        Reel: Simula un carrete individual

        SlotMachine: Maneja la lógica principal del juego

        Bet: Maneja las apuestas

🖥️ Vista (view.py)

    Interfaz gráfica con tkinter

    Muestra los carretes y botones interactivos

    Actualiza la pantalla según el estado del juego

🎛️ Controlador (Controlador.py)

    Coordina la interacción entre Vista y Modelo

    Implementa el giro de carretes con animación progresiva

    Usa hilos para no bloquear la interfaz durante las animaciones

🛠️ Características técnicas destacadas

✅ Patrón MVC limpio: Separación clara de responsabilidades
✅ Animación progresiva: Los carretes giran rápido al inicio y se frenan gradualmente
✅ Thread-safe: Usa locks para evitar condiciones de carrera
✅ Interfaz atractiva: Emojis y colores para una experiencia visual agradable
✅ Extensible: Fácil de modificar para añadir más características
📝 Notas adicionales

    El juego actualmente no utiliza el monto de apuesta en los cálculos (es meramente visual)

    Los símbolos disponibles son: 🍒, 🍋, 🔔, 🍉, ⭐, 7️⃣

    La detección de victoria es simple (todos los símbolos iguales)
