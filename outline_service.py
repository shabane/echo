#!/usr/bin/env python3
import sqlite3
from datetime import datetime
from outline.core.outline import Outline
import logging
from time import sleep


while True:

    date = datetime.today().date()

    db = sqlite3.connect('db.sqlite3')
    keys = db.execute(f'select * from outline_link where exp_date="{str(date)}"').fetchall()

    for key in keys:
        apiUrl = db.execute(f'select * from outline_server where id={key[10]}').fetchone()[2]
        outline_server = Outline(apiUrl)
        if outline_server.set_date_limit(key[11], 1_000_000):
            # db.execute(f'delete from outline_link where id={key[0]}')
            db.execute(f'update outline_link set max_size=1000000, enabled=0 where id={key[0]}')
            db.commit()
            logging.info(f'{key[1]}')
        else:
            logging.error(f'the key {key} did not deleted from server')

    db.close()
    sleep(3600)
