# Enable / disable the airdrop
airdrop_live = True

# API Telegram
api_token = (
    "5096180642:AAEYSun6HRosnvVr-0IiN009lx3-xTk7S68"  
)

host = "157.90.107.94"  

log_channel = 0  # Channel ID. Example: -1001355597767
admins = []  # Telegram User ID's. Admins are able to execute command "/airdroplist"
airdrop_cap = 100  
wallet_changes = 3  

# Database
mysql_host = "localhost"
mysql_db = "TelegramAirdropBot"
mysql_user = "saeed"
mysql_pw = "--------"

texts = {
    "start_1": "Hi {} and welcome to our (Madrid) Airdrop!\n\nGet started by clicking the button below.\n\n",
    "start_2": "Hi {},\n\nYour address has been added to the airdrop list!\n\n",
    "start_captcha": "Hi {},\n\n",
    "airdrop_start": "The airdrop didn't start yet.",
    "airdrop_address": "Type in your address:",
    "airdrop_max_cap": "ℹ️ The airdrop reached its max cap.",
    "airdrop_walletused": "⚠️ That address has already been used. Use a different one.",
    "airdrop_confirmation": "✅ Your address has been added to airdrop list.",
    "airdrop_wallet_update": "✅ Your address has been updated.",
}
