from webbrowser import get

import pyrootutils
from omegaconf import OmegaConf

pyrootutils.setup_root(__file__, indicator=".project", pythonpath=True)


class Configurator_yml:
    def __init__(self) -> None:
        self._bot_config = OmegaConf.load("conf/bot.yaml")
        self._db_config = OmegaConf.load("conf/db.yaml")

    db_config = property()
    bot_config = property()

    @db_config.getter
    def db_config(self):
        return self._db_config

    @bot_config.getter
    def bot_config(self):
        return self._bot_config

    def get_uri_db(self):
        info = self._db_config.base
        return f"{info.schema}://{info.user}:{info.password}@{info.ip}:{info.port}/{info.bd_name}"

    def get_bot_token(self):
        return self._bot_config.base.token

    def get_domen(self):
        return self._bot_config.base.domen


if __name__ == "__main__":
    my_conf = Configurator_yml()
    print(my_conf.db_config)
    for k in my_conf.db_config.data:
        print(k)
        print(my_conf.db_config.data[k])
