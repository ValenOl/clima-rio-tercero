# 🌤️ Bot del Clima - Río Tercero

Un bot de Telegram que proporciona información del clima en tiempo real para Río Tercero, Córdoba, Argentina.

## 🚀 Características

- **🌡️ Temperatura actual** en grados Celsius
- **🌡️ Sensación térmica** 
- **☁️ Estado del clima** con descripción
- **💧 Humedad** del ambiente
- **📊 Presión atmosférica**
- **💨 Velocidad del viento**
- **🎯 Recomendaciones** según la temperatura

## 📱 Comandos Disponibles

- `/start` - Iniciar el bot y ver mensaje de bienvenida
- `/clima` - Obtener información del clima actual
- `/ayuda` - Ver ayuda y comandos disponibles
- `/info` - Información del bot y datos técnicos

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **python-telegram-bot** - Para la API de Telegram
- **requests** - Para consultar la API del clima
- **OpenWeatherMap API** - Datos meteorológicos

## ⚙️ Instalación

1. **Clona el repositorio:**
```bash
git clone https://github.com/tu-usuario/clima-rio-tercero.git
cd clima-rio-tercero
```

2. **Instala las dependencias:**
```bash
pip install -r requirements.txt
```

3. **Configura las variables:**
   - Obtén tu API key de [OpenWeatherMap](https://openweathermap.org/api)
   - Obtén tu token de bot de [@BotFather](https://t.me/botfather) en Telegram
   - Actualiza las variables en `clima_bot.py`

4. **Ejecuta el bot:**
```bash
python clima_bot.py
```

## 🔧 Configuración

Edita las siguientes variables en `clima_bot.py`:

```python
API_KEY_OPENWEATHER = 'tu-api-key-aqui'
TOKEN_TELEGRAM = 'tu-token-de-bot-aqui'
CITY = 'Río Tercero,AR'  # Puedes cambiar la ciudad
```

## 📊 API Keys Necesarias

### OpenWeatherMap
1. Regístrate en [OpenWeatherMap](https://openweathermap.org/)
2. Ve a "API Keys" en tu perfil
3. Copia tu API key (puede tardar hasta 2 horas en activarse)

### Telegram Bot
1. Habla con [@BotFather](https://t.me/botfather) en Telegram
2. Usa el comando `/newbot`
3. Sigue las instrucciones para crear tu bot
4. Copia el token que te proporciona

## 🎯 Uso

Una vez configurado y ejecutado:

1. Busca tu bot en Telegram
2. Envía `/start` para comenzar
3. Usa `/clima` o escribe cualquier mensaje para ver el clima
4. El bot responderá con información detallada del clima

## 📝 Ejemplo de Respuesta

```
🌤️ Clima en Río Tercero,AR

🌡️ Temperatura: 22°C
🌡️ Sensación térmica: 24°C
☁️ Estado: Cielo claro
💧 Humedad: 45%
📊 Presión: 1013 hPa
💨 Viento: 3.2 m/s

🙂 Clima agradable.
```

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si quieres agregar nuevas características:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

**Tu Nombre** - [@tu-usuario](https://github.com/tu-usuario)

## 🙏 Agradecimientos

- [OpenWeatherMap](https://openweathermap.org/) por proporcionar los datos meteorológicos
- [python-telegram-bot](https://python-telegram-bot.org/) por la excelente librería
- La comunidad de Python por el soporte

---

⭐ Si te gustó este proyecto, ¡dale una estrella en GitHub! 