COMMANDS = {
    "/start": "Start the bot",
    "/help": "Show available commands",
    "/create_account": "Create new Instagram account",
    "/auto_like": "Auto like a post",
    "/auto_comment": "Auto comment on a post"
}

def get_help_text():
    help_text = "Available Commands:\n"
    for command, description in COMMANDS.items():
        help_text += f"{command} - {description}\n"
    return help_text
