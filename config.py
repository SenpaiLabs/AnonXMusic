from os import getenv
from dotenv import load_dotenv

load_dotenv()


class Config:
    def init(self):
        self.API_ID = 32076000
        self.API_HASH = "22adb8c3d3f905d09fe41cf4ae805b71"

        self.BOT_TOKEN = "9160938427:AAGrX0KSGSThbx3wh1ibGHUrFVCS6CjvavY"
        self.MONGO_URL = "mongodb+srv://public:abishnoimf@cluster0.rqk6ihd.mongodb.net/?retryWrites=true&w=majority"

        self.LOGGER_ID = 5436045769
        self.OWNER_ID = 8516736963

        self.DURATION_LIMIT = 60 * 60
        self.QUEUE_LIMIT = 20
        self.PLAYLIST_LIMIT = 20

        self.SESSION1 = "BAFRwgAAKtH4gBQ2_eG4yLIm5aJhje4AwPvDWbfXKjKZ4vvUI6W5fuh_HTbj9giinPy-9rKrjifsIzmGO_zS9Q1So_AFqZKyH5yOcGChpUZvbHDEfmEOBY2kH2qqooUPGioAz47XKcOtuEy8idGp-JQv-hBawR1fStyNuYliNBlrQ_L9vUjX8Cs0CaYbvIhiyytkoGnTfmGdOO_2eNb9PJh_b2u2ye3kvDAHta-R4UKZjILaRQ3NV2T_D4uPUJQa0Ezk8Y7yMVUo02q6JzLbJgsS30qTGTI5viRr2wXfCZmH0sc7upb3mtAkIC41HglF_-TXAeHp4OOqP7kHNv7bEEDl6gAAAAIJ678XAA"
        self.SESSION2 = None
        self.SESSION3 = None

        self.SUPPORT_CHANNEL = "https://t.me/fallenx"
        self.SUPPORT_CHAT = "https://t.me/DevilsHeavenMF"

        self.AUTO_LEAVE = False
        self.AUTO_END = False

        self.THUMB_GEN = True
        self.VIDEO_PLAY = True

        self.LANG_CODE = "en"

        self.COOKIES_URL = []

        self.DEFAULT_THUMB = "https://te.legra.ph/file/3e40a408286d4eda24191.jpg"
        self.PING_IMG = "https://files.catbox.moe/haagg2.png"
        self.START_IMG = "https://files.catbox.moe/zvziwk.jpg"

    def check(self):
        missing = [
            var
            for var in [
                "API_ID",
                "API_HASH",
                "BOT_TOKEN",
                "MONGO_URL",
                "LOGGER_ID",
                "OWNER_ID",
                "SESSION1",
            ]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(
                f"Missing required environment variables: {', '.join(missing)}"
            )
