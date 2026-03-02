TikTok Live Auto-Tap 🚀
Un script sencillo en Python para automatizar los "likes" (tap-tap) en transmisiones en vivo de TikTok Web utilizando emulación de teclado.

REQUISITOS
Para usar este script, necesitas tener instalado Python y la biblioteca pyautogui.

Instalar dependencias:
pip install pyautogui

CÓMO USARLO
Abre el Live de TikTok en tu navegador Chrome/Edge/Firefox.

Ejecuta el script: python auto_like.py

Tienes 10 SEGUNDOS para cambiar a la ventana del navegador y hacer clic dentro del Live.

El script empezará a presionar la tecla 'L' automáticamente para generar los likes.

CONFIGURACIÓN
Puedes editar estas variables al inicio del archivo auto_like.py:

REPETICIONES: Cuántos likes quieres dar (por defecto 1000).

VELOCIDAD: Segundos entre cada pulsación (0.1 es rápido y seguro).

ESPERA_INICIAL: Segundos de margen para que cambies de ventana.

SEGURIDAD (BOTÓN DE PÁNICO)
Si el script se vuelve loco o quieres detenerlo de emergencia:

OPCIÓN A: Mueve el puntero del ratón violentamente hacia cualquiera de las 4 ESQUINAS de tu pantalla. Esto activará el sistema de seguridad de PyAutoGUI y detendrá el proceso de inmediato.

OPCIÓN B: Presiona Ctrl + C en la terminal donde se está ejecutando el script.

Nota: Usa este script con responsabilidad. El abuso de automatizaciones puede causar bloqueos temporales en tu cuenta de TikTok.
