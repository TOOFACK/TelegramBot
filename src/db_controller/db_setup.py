import pyrootutils

pyrootutils.setup_root(__file__, indicator=".project", pythonpath=True)
from conf.config import Configurator_yml
from src.service.service import ContentController


def setup_db():
    my_conf = Configurator_yml()
    content_table_controller = ContentController()
    db_congif_data = my_conf.db_config.data
    for k in db_congif_data:
        content_table_controller.insert_data(
            data={"content_name": k, "content_value": db_congif_data[k]}
        )


if __name__ == "__main__":
    setup_db()
