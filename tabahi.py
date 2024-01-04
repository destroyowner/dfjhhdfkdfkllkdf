import os
from telethon import TelegramClient, events
from telethon.tl.custom import Button

api_id = int(os.environ["api_id"])
api_hash = os.environ["api_hash"]
bot_token = os.environ["bot_token"]

tabahi = TelegramClient("tabahi", api_id, api_hash).start(bot_token=bot_token)

@tabahi.on(events.NewMessage(pattern=r'\/start'))
async def start_tabahi(event):
    try:
        if event.is_private:
            message_location = event.peer_id.user_id
            reply_message_location = event.id
            one = "https://telegra.ph/file/1a8e9ec3c9d79e560e135.png"
            two = "https://telegra.ph/file/81245fadb3ed275817e14.png"
            tabahi_contact = [
                [
                    Button.url("Contact 🇳Δ𝐖𝔸𝐁 𝐓𝐀𝐁𝐀𝐇𝐈 ࿐", url="https://t.me/TABAHI_ALONE")
                ]
                ]
            await tabahi.send_file(message_location, one)
            await tabahi.send_file(message_location, two)
            await tabahi.send_message(message_location, "Hey there,\nMy name is Divyansh, my name on Telegram is 🇳Δ𝐖𝔸𝐁 𝐓𝐀𝐁𝐀𝐇𝐈 ࿐ (@TABAHI_ALONE) and I am a transgender male. If anyone wants to fuck my ass, please call me. I earn money from sexting to feed my family; please call me for sex.\n📞 Mobile Number:\n+919058075506\n+919870952006", buttons=tabahi_contact)
        else:
            message_location = event.to_id
            reply_message_location = event.id
            await tabahi.send_message(message_location, "DM me if you want to take advantage of my service and click on the Start button.", reply_to=reply_message_location)
    except:
        pass

@tabahi.on(events.NewMessage(pattern=r"\/send"))
async def send_information(event):
    try:
        if event.is_private:
            sender = event.peer_id.user_id
            owner = 6696970488
            target_group = -1002079437826
            if sender == owner:
                get_message = event.message.text
                validate = get_message.replace("/send ", "")
                message = validate
                await tabahi.send_message(target_group, message)
            else:
                pass
        else:
            pass
    except AttributeError:
        pass

@tabahi.on(events.NewMessage(pattern=r"\/reply"))
async def reply_information(event):
    try:
        if event.is_private:
            sender = event.peer_id.user_id
            owner = 6696970488
            target_group = -1002079437826
            if sender == owner:
                get_message_id = event.message.raw_text.split()
                message_id = get_message_id[1]
                get_data = event.message.text
                convert_data_type = get_data.split()
                validate = convert_data_type[2:]
                validate_message = " ".join(validate)
                get_message = validate_message.splitlines()
                message = get_message[0]
                await tabahi.send_message(target_group, message, reply_to=int(message_id))
            else:
                pass
        else:
            pass
    except AttributeError:
        pass

print("Tabahi Started")
tabahi.run_until_disconnected()