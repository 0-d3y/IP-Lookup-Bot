import os 
try:
    import telebot
except:
    os.system("pip install pyTelegramBotAPI")
    import telebot
try:
    from ip_info_ye import ip_info
except:
    os.system("pip install ip-info-ye")
    from ip_info_ye import ip_info
BOT_TOKEN = '8030685005:AAF5gsmU1iZcVv50QOdWMET5xLOdgURdqDg'

bot = telebot.TeleBot(BOT_TOKEN, parse_mode='Markdown')

def escape_markdown(text):
    escape_chars = r'\_*[]()~`>#+-=|{}.!'
    for ch in escape_chars:
        text = text.replace(ch, '\\' + ch)
    return text

def create_table(title, data_dict):
    if not any(data_dict.values()):
        return ""
    
    table = f"*{escape_markdown(title)}*\n"
    table += "```\n"
    max_key_length = max(len(str(key)) for key in data_dict.keys())
    border = "+" + "-" * (max_key_length + 2) + "+" + "-" * 30 + "+\n"
    
    table += border
    for key, value in data_dict.items():
        if value:
            key_str = escape_markdown(str(key)).ljust(max_key_length)
            value_str = escape_markdown(str(value))[:28].ljust(28)  # Limit value length
            table += f"| {key_str} | {value_str} |\n"
    table += border
    table += "```"
    return table

@bot.message_handler(commands=['start'])
def start_cmd(message):
    welcome = (
        "*👋 Welcome to IP Info Bot!*\n\n"
        "This bot provides detailed information about any public IP address.\n"
        "Example:\n"
        "`/ip 8.8.8.8`\n\n"
        "Type /help for available commands."
    )
    bot.reply_to(message, welcome)

@bot.message_handler(commands=['help'])
def help_cmd(message):
    help_text = (
        "*🆘 Help Guide:*\n\n"
        "`/ip <IP_address>` - Get information about an IP\n"
        "`/start` - Show welcome message\n"
        "`/help` - Show this help message\n\n"
        "Example: `/ip 1.1.1.1`"
    )
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['ip'])
def ip_lookup(message):
    parts = message.text.strip().split()
    if len(parts) != 2:
        bot.reply_to(message, "❗️Usage: `/ip <IP_address>`")
        return

    ip = parts[1]
    try:
        data = ip_info(ip)
        if not data or data.get("status") != "success":
            bot.reply_to(message, "❌ No information found or invalid response.")
            return

        info = data.get("response", {})
        
        general_info = {
            "IP": info.get('IP Address'),
            "Network": info.get('Network'),
            "Version": info.get('Version'),
            "Organization": info.get('Organization'),
            "ASN": info.get('ASN Number')
        }
        
        location_info = {
            "City": info.get('City'),
            "Region": f"{info.get('Region')} ({info.get('Region Code')})",
            "Country": info.get('Country'),
            "ISO Code": info.get('Country ISO Code'),
            "Postal Code": info.get('Postal Code')
        }
        
        coordinates_info = {
            "Latitude": info.get('Latitude'),
            "Longitude": info.get('Longitude')
        }
        
        time_info = {
            "Timezone": info.get('Timezone'),
            "UTC Offset": info.get('UTC Offset')
        }
        
        country_info = {
            "Capital": info.get('Country Capital'),
            "Calling Code": info.get('Country Calling Code'),
            "Currency": info.get('Currency'),
            "Population": info.get('Country Population')
        }
        
        msg = f"*🔍 IP Lookup Results for {ip}*\n\n"
        msg += create_table("📊 GENERAL INFORMATION", general_info) + "\n"
        msg += create_table("📍 GEOLOCATION", location_info) + "\n"
        msg += create_table("🗺 COORDINATES", coordinates_info) + "\n"
        msg += create_table("🕒 TIMEZONE", time_info) + "\n"
        msg += create_table("🌍 COUNTRY INFO", country_info) + "\n\n"
        map_url = f"🌐 Map: [Google Maps](https://maps.google.com/?q={info.get('Latitude')},{info.get('Longitude')})\n\n"
        msg += map_url
        msg += f"*🔖 Source: {info.get('code')}*\n"
        msg += "*👤 Powered by Mr.SaMi*"
        
        bot.reply_to(message, msg)

    except Exception as e:
        bot.reply_to(message, f"⚠️ Error:\n`{str(e)}`")

print("Bot is Started - Code By Mr.SaMi")
bot.infinity_polling()
