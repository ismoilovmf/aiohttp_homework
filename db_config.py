import os
from dotenv import load_dotenv

load_dotenv()

DSN = f'postgresql+asyncpg://{os.environ.get("PG_USER")}:' \
         f'{os.environ.get("PG_PASS")}@{os.environ.get("PG_HOST")}:' \
         f'{os.environ.get("PG_PORT")}/{os.environ.get("PG_DB")}'

DSN_SYNC = f'postgresql://{os.environ.get("PG_USER")}:' \
         f'{os.environ.get("PG_PASS")}@{os.environ.get("PG_HOST")}:' \
         f'{os.environ.get("PG_PORT")}/{os.environ.get("PG_DB")}'

