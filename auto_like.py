import pyautogui
import time
import sys

# === CONFIGURACIÓN ===
TECLA = 'l'           # La tecla que quieres presionar
REPETICIONES = 1000     # Cuántas veces se presionará
VELOCIDAD = 0.1       # Segundos entre cada pulsación (0.1 es rápido)
ESPERA_INICIAL = 10   # Segundos para que te cambies de pestaña
# =====================

def ejecutar_autoclicker():
    print(f"--- SCRIPT INICIADO ---")
    print(f"Tienes {ESPERA_INICIAL} segundos para ir a la pestaña de Chrome...")
    
    # Cuenta regresiva visual
    for i in range(ESPERA_INICIAL, 0, -1):
        print(f"Empezando en... {i}")
        time.sleep(1)

    print(f"\n¡ACCION! Presionando '{TECLA}' {REPETICIONES} veces...")

    try:
        for n in range(1, REPETICIONES + 1):
            pyautogui.press(TECLA)
            print(f"[{n}/{REPETICIONES}] Presionada '{TECLA}'")
            
            # Pequeña pausa entre teclas
            time.sleep(VELOCIDAD)
            
    except KeyboardInterrupt:
        print("\n\n[!] Script detenido manualmente por el usuario.")
    
    print("\n--- TAREA FINALIZADA ---")

if __name__ == "__main__":
    # NOTA DE SEGURIDAD: 
    # Si algo sale mal, mueve el ratón violentamente hacia 
    # una de las esquinas de tu pantalla para abortar.
    ejecutar_autoclicker()