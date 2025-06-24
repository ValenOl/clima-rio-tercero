import requests
from telegram import Bot, Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio
import time
import os
import logging

# 🔐 CONFIGURACIÓN
# Usar variables de entorno para mayor seguridad
API_KEY_OPENWEATHER = os.getenv('API_KEY_OPENWEATHER', '932f1f40d296561a8a6abd67298f1163')
CITY = os.getenv('CITY', 'Río Tercero,AR')
TOKEN_TELEGRAM = os.getenv('TOKEN_TELEGRAM', '8118768924:AAHpxHKEzl7J92zPIE_3GyR_DPMdrPWEPFY')

# 📝 Configurar logging para el servidor
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 📱 LISTA DE PERSONAS QUE RECIBIRÁN EL MENSAJE
# Agregá aquí los CHAT_ID de todas las personas que quieran recibir el clima
CHAT_IDS = [
    5943496771,  # Tu chat_id (el tuyo)
    # Agregá más chat_ids aquí, uno por línea:
    # 1234567890,  # Ejemplo: Juan
    # 9876543210,  # Ejemplo: María
    # 5556667777,  # Ejemplo: Pedro
]

# 🔍 FUNCIÓN PARA PROBAR LA API KEY
def probar_api_key():
    """Prueba si la API key es válida"""
    url = f'https://api.openweathermap.org/data/2.5/weather?q=London&appid={API_KEY_OPENWEATHER}'
    
    try:
        respuesta = requests.get(url, timeout=10)
        datos = respuesta.json()
        
        print(f"🔍 Probando API key...")
        print(f"Status Code: {respuesta.status_code}")
        print(f"Respuesta: {datos}")
        
        if respuesta.status_code == 200:
            print("✅ API key válida!")
            return True
        elif respuesta.status_code == 401:
            print("❌ API key inválida o no activada")
            print("💡 Posibles soluciones:")
            print("   1. Verifica que la API key sea correcta")
            print("   2. Espera 2 horas después de registrarte (activación automática)")
            print("   3. Revisa tu email de confirmación de OpenWeatherMap")
            return False
        else:
            print(f"⚠️ Error inesperado: {respuesta.status_code}")
            return False
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return False

# 🌤️ FUNCIÓN PARA OBTENER EL CLIMA
def obtener_clima():
    url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&units=metric&lang=es&appid={API_KEY_OPENWEATHER}'
    
    try:
        respuesta = requests.get(url, timeout=10)
        datos = respuesta.json()

        # Verificar si hay error
        if respuesta.status_code != 200:
            if respuesta.status_code == 401:
                raise Exception("❌ API key inválida. Verifica tu clave en OpenWeatherMap")
            elif respuesta.status_code == 404:
                raise Exception(f"❌ Ciudad no encontrada: {CITY}")
            else:
                raise Exception(f"❌ Error {respuesta.status_code}: {datos.get('message', 'Error desconocido')}")

        # Verificar que los datos necesarios estén presentes
        if 'main' not in datos or 'weather' not in datos:
            raise Exception(f"❌ Datos incompletos de la API: {datos}")

        temp = datos['main']['temp']
        desc = datos['weather'][0]['description']
        humedad = datos['main'].get('humidity', 'N/A')
        presion = datos['main'].get('pressure', 'N/A')
        sensacion = datos['main'].get('feels_like', temp)
        viento = datos.get('wind', {}).get('speed', 'N/A')
        
        mensaje = f"🌤️ **Clima en {CITY}**\n\n"
        mensaje += f"🌡️ **Temperatura:** {temp}°C\n"
        mensaje += f"🌡️ **Sensación térmica:** {sensacion}°C\n"
        mensaje += f"☁️ **Estado:** {desc.capitalize()}\n"
        mensaje += f"💧 **Humedad:** {humedad}%\n"
        mensaje += f"📊 **Presión:** {presion} hPa\n"
        mensaje += f"💨 **Viento:** {viento} m/s\n\n"

        if temp < 10:
            mensaje += "🥶 **¡Hace frío, abrigate!**"
        elif temp > 30:
            mensaje += "☀️ **¡Mucho calor hoy!**"
        else:
            mensaje += "🙂 **Clima agradable.**"

        return mensaje

    except requests.exceptions.Timeout:
        raise Exception("❌ Timeout: La API tardó demasiado en responder")
    except requests.exceptions.ConnectionError:
        raise Exception("❌ Error de conexión: Verifica tu internet")
    except Exception as e:
        raise Exception(f"❌ Error inesperado: {e}")

# 📩 ENVIAR MENSAJE POR TELEGRAM (FUNCIÓN ASÍNCRONA)
async def enviar_mensaje_async(chat_id, mensaje):
    try:
        bot = Bot(token=TOKEN_TELEGRAM)
        await bot.send_message(chat_id=chat_id, text=mensaje)
        print(f"✅ Mensaje enviado a chat_id: {chat_id}")
        return True
    except Exception as e:
        print(f"❌ Error enviando mensaje a chat_id {chat_id}: {e}")
        return False

# 📩 ENVIAR MENSAJE A TODAS LAS PERSONAS
async def enviar_mensaje_a_todos_async(mensaje):
    bot = Bot(token=TOKEN_TELEGRAM)
    exitosos = 0
    fallidos = 0
    
    print(f"📤 Enviando mensaje a {len(CHAT_IDS)} personas...")
    
    for chat_id in CHAT_IDS:
        try:
            await bot.send_message(chat_id=chat_id, text=mensaje)
            print(f"✅ Enviado a chat_id: {chat_id}")
            exitosos += 1
        except Exception as e:
            print(f"❌ Error enviando a chat_id {chat_id}: {e}")
            fallidos += 1
        # Pequeña pausa para no sobrecargar la API de Telegram
        await asyncio.sleep(0.5)
    
    print(f"\n📊 Resumen: {exitosos} enviados, {fallidos} fallidos")
    return exitosos, fallidos

# 📩 ENVIAR MENSAJE A TODAS LAS PERSONAS (WRAPPER)
def enviar_mensaje_a_todos(mensaje):
    return asyncio.run(enviar_mensaje_a_todos_async(mensaje))

# 🔧 FUNCIÓN PARA OBTENER CHAT_ID
def obtener_chat_id():
    """Función para ayudar a obtener el chat_id de una persona"""
    print("🔧 Para obtener el chat_id de una persona:")
    print("1. La persona debe buscar tu bot en Telegram")
    print("2. Enviar /start al bot")
    print("3. Enviar cualquier mensaje al bot")
    print("4. El bot responderá con su chat_id")
    print("\n💡 También podés usar @userinfobot para obtener tu chat_id")

# 📱 COMANDO /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /start - Mensaje de bienvenida"""
    user = update.effective_user
    mensaje = f"👋 ¡Hola {user.first_name}!\n\n"
    mensaje += "🌤️ Soy tu bot del clima para **Río Tercero**\n\n"
    mensaje += "📋 **Comandos disponibles:**\n"
    mensaje += "• `/clima` - Ver el clima actual\n"
    mensaje += "• `/ayuda` - Ver esta ayuda\n"
    mensaje += "• `/info` - Información del bot\n\n"
    mensaje += "💡 También podés escribir cualquier mensaje y te diré el clima actual."
    
    await update.message.reply_text(mensaje, parse_mode='Markdown')
    logger.info(f"Usuario {user.id} ({user.first_name}) inició el bot")

# 🌤️ COMANDO /clima
async def clima_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /clima - Obtener el clima actual"""
    await update.message.reply_text("🌤️ Consultando el clima...")
    
    try:
        clima = obtener_clima()
        await update.message.reply_text(clima, parse_mode='Markdown')
        logger.info(f"Clima consultado exitosamente por usuario {update.effective_user.id}")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")
        logger.error(f"Error obteniendo clima: {e}")

# 📖 COMANDO /ayuda
async def ayuda_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /ayuda - Mostrar ayuda"""
    mensaje = "📖 **Ayuda del Bot del Clima**\n\n"
    mensaje += "🌤️ Este bot te da información del clima en **Río Tercero, Córdoba**\n\n"
    mensaje += "📋 **Comandos:**\n"
    mensaje += "• `/start` - Iniciar el bot\n"
    mensaje += "• `/clima` - Ver clima actual\n"
    mensaje += "• `/ayuda` - Esta ayuda\n"
    mensaje += "• `/info` - Información del bot\n\n"
    mensaje += "💡 **Tip:** También podés escribir cualquier mensaje y te diré el clima."
    
    await update.message.reply_text(mensaje, parse_mode='Markdown')

# ℹ️ COMANDO /info
async def info_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Comando /info - Información del bot"""
    mensaje = "ℹ️ **Información del Bot**\n\n"
    mensaje += "🤖 **Bot del Clima - Río Tercero**\n"
    mensaje += "📍 **Ciudad:** Río Tercero, Córdoba, Argentina\n"
    mensaje += "🌤️ **Datos:** OpenWeatherMap API\n"
    mensaje += "📱 **Desarrollado con:** Python + python-telegram-bot\n"
    mensaje += "☁️ **Hosting:** Render (24/7)\n\n"
    mensaje += "🕐 **Última actualización:** Datos en tiempo real\n"
    mensaje += "🌡️ **Unidades:** Celsius, métrico\n\n"
    mensaje += "💬 Para usar el bot, escribí `/clima` o cualquier mensaje."
    
    await update.message.reply_text(mensaje, parse_mode='Markdown')

# 💬 MANEJAR MENSAJES DE TEXTO
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Manejar mensajes de texto - responder con el clima"""
    message_type = update.message.chat.type
    text = update.message.text
    user = update.effective_user
    
    logger.info(f'Usuario {user.id} ({user.first_name}) en {message_type}: "{text}"')
    
    # Si es un comando, no hacer nada (ya se maneja con los handlers)
    if text.startswith('/'):
        return
    
    # Para cualquier otro mensaje, mostrar el clima
    await update.message.reply_text("🌤️ Consultando el clima...")
    
    try:
        clima = obtener_clima()
        await update.message.reply_text(clima, parse_mode='Markdown')
        logger.info(f"Clima enviado exitosamente a usuario {user.id}")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: {e}")
        logger.error(f"Error enviando clima a usuario {user.id}: {e}")

# ❌ MANEJAR ERRORES
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Manejar errores del bot"""
    logger.error(f'Error: {context.error}')
    if update:
        await update.message.reply_text("❌ Ocurrió un error. Intentá de nuevo más tarde.")

# 🚀 FUNCIÓN PRINCIPAL
def main():
    """Función principal del bot"""
    logger.info("🚀 Iniciando bot del clima...")
    
    # Crear la aplicación
    app = Application.builder().token(TOKEN_TELEGRAM).build()
    
    # Agregar handlers para comandos
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('clima', clima_command))
    app.add_handler(CommandHandler('ayuda', ayuda_command))
    app.add_handler(CommandHandler('info', info_command))
    
    # Agregar handler para mensajes de texto
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # Agregar handler de errores
    app.add_error_handler(error_handler)
    
    logger.info("✅ Bot iniciado correctamente!")
    logger.info("📱 El bot está listo para recibir mensajes...")
    
    # Iniciar el bot
    app.run_polling(poll_interval=1)

# ▶️ EJECUCIÓN
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.info("🛑 Bot detenido por el usuario")
    except Exception as e:
        logger.error(f"❌ Error al iniciar el bot: {e}")