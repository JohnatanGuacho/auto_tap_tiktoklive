# Improved README

```markdown
# TikTok Live Auto-Tap 🚀

Un script sencillo en Python para automatizar los "likes" (tap-tap) en transmisiones en vivo de TikTok Web utilizando emulación de teclado.

## 📋 Requisitos

- Python 3.6+
- Las bibliotecas listadas en `requirements.txt`

### Instalar dependencias

```bash
pip install pyautogui
```

## 🚀 Cómo usarlo

1. Abre el Live de TikTok en tu navegador (Chrome/Edge/Firefox)
2. Ejecuta el script:
   ```bash
   python auto_like.py
   ```
3. Tienes **10 segundos** para cambiar a la ventana del navegador y hacer clic dentro del Live
4. El script empezará a presionar la tecla 'L' automáticamente para generar los likes

## ⚙️ Configuración

Edita estas variables al inicio de `auto_like.py`:

- **REPETICIONES**: Cuántos likes quieres dar (por defecto: 1000)
- **VELOCIDAD**: Segundos entre cada pulsación (por defecto: 0.1)
- **ESPERA_INICIAL**: Segundos de margen para cambiar de ventana (por defecto: 10)

## 🛑 Botón de pánico

Para detener el script en emergencia:

- **Opción A**: Mueve el ratón violentamente hacia cualquiera de las 4 esquinas de la pantalla
- **Opción B**: Presiona `Ctrl + C` en la terminal

## ⚠️ Disclaimer

Usa este script con responsabilidad. El abuso de automatizaciones puede causar bloqueos temporales en tu cuenta de TikTok.
