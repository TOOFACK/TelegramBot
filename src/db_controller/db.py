import os

import pyrootutils
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

pyrootutils.setup_root(__file__, indicator=".project", pythonpath=True)
from conf.config import Configurator_yml

engine = create_engine(url=Configurator_yml().get_uri_db())
# engine_test = create_engine(url=os.environ.get('TEST_DB'))


Session = sessionmaker(bind=engine)


# TEST_DB=postgresql://maxim:maxim@test_db:5432/maxim
# VENDOR__DATABASE__DSN="postgresql+asyncpg://maxim:maxim@test_db:5432/maxim"
