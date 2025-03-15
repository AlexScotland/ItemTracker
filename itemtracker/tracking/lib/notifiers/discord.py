import apprise

class DiscordNotifier():

    def __init__(self, webhook_id, webhook_token):
        self.apobj = apprise.Apprise()
        self.apobj.add(f'discord://{webhook_id}/{webhook_token}')
    
    def notify(self, title, message):
        self.apobj.notify(title=title, body=message)
