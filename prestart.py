import subprocess
import sys

from alembic import command
from alembic.config import Config

from app.core.config import ROOT

alembic_cfg = Config(ROOT.parent / "alembic.ini")

subprocess.run([sys.executable, "./app/backend_pre_start.py"])
command.upgrade(alembic_cfg, "head")
subprocess.run([sys.executable, "./app/initial_data.py"])
