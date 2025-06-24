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
- **☁️ Hosting 24/7** en Render

## 📱 Comandos Disponibles

- `/start` - Iniciar el bot y ver mensaje de bienvenida
- `/clima` - Obtener información del clima actual
- `/ayuda` - Ver ayuda y comandos disponibles
- `/info` - Información del bot y datos técnicos

## 🛠️ Tecnologías Utilizadas

- **Python 3.11**
- **python-telegram-bot** - Para la API de Telegram
- **requests** - Para consultar la API del clima
- **OpenWeatherMap API** - Datos meteorológicos
- **Render** - Hosting gratuito 24/7

## ⚙️ Instalación Local

1. **Clona el repositorio:**
```bash
git clone https://github.com/ValenOl/clima-rio-tercero.git
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

## ☁️ Despliegue en Render (24/7)

### Opción 1: Despliegue Automático (Recomendado)

1. **Fork este repositorio** en tu cuenta de GitHub
2. **Ve a [Render.com](https://render.com)** y crea una cuenta
3. **Click en "New +" → "Web Service"**
4. **Conecta tu repositorio de GitHub**
5. **Configura el servicio:**
   - **Name:** `clima-rio-tercero-bot`
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python clima_bot.py`
6. **Agrega las variables de entorno:**
   - `API_KEY_OPENWEATHER` = tu API key de OpenWeatherMap
   - `TOKEN_TELEGRAM` = tu token de bot de Telegram
   - `CITY` = `Río Tercero,AR` (o la ciudad que quieras)
7. **Click en "Create Web Service"**

### Opción 2: Despliegue Manual

1. **Crea una cuenta en [Render.com](https://render.com)**
2. **Crea un nuevo Web Service**
3. **Conecta tu repositorio de GitHub**
4. **Configura las variables de entorno** como se muestra arriba
5. **Deploy automático**

## 🔧 Configuración

### Variables de Entorno (para servidor)

```bash
API_KEY_OPENWEATHER=tu-api-key-aqui
TOKEN_TELEGRAM=tu-token-de-bot-aqui
CITY=Río Tercero,AR
```

### Configuración Local

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

## 🔍 Monitoreo

El bot incluye logging detallado para monitorear:
- Usuarios que interactúan con el bot
- Consultas exitosas al clima
- Errores y problemas
- Estado del servicio

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

**ValenOl** - [@ValenOl](https://github.com/ValenOl)

## 🙏 Agradecimientos

- [OpenWeatherMap](https://openweathermap.org/) por proporcionar los datos meteorológicos
- [python-telegram-bot](https://python-telegram-bot.org/) por la excelente librería
- [Render](https://render.com/) por el hosting gratuito
- La comunidad de Python por el soporte

---

⭐ Si te gustó este proyecto, ¡dale una estrella en GitHub! 