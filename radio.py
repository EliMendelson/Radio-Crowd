import soundcloud
import rumps

client = soundcloud.Client(client_id = 081fb28bc6c3af772cd32e5724348ec7)

class Radio(rumps.App):
    def __init__(self):
        super(Radio, self).__init__("RaCr", "./RaCr_logo.png")
        self.menu = [