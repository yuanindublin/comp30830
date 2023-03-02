import config
from sqlalchemy import create_engine,text
import traceback
import glob
import os
from pprint import pprint
import simplejson as json
import requests
import time
# from IPython.display import display


engine = create_engine(
    "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(config.USER, config.PASSWORD, config.URI, config.PORT, config.DB), echo=True)

# Test the database connection
def main() :
    try:
        with engine.connect() as conn:
            res = conn.execute(text("SHOW VARIABLES"))
            print(list(res))
    except:
        print(traceback.format_exc())
    return 

if __name__ == '__main__':
    main()


def create_table():    
    sql = """CREATE DATABASE IF NOT EXISTS dbbikes"""
    engine.execute(sql)

    for res in engine.execute("SHOW VARIABLES"):
        print(res)

    sql = """
    CREATE TABLE IF NOT EXISTS station
    (
    address VARCHAR(256),
    banking INTEGER,
    bike_stands INTEGER,
    bonus INTEGER,
    contract_name VARCHAR(256),
    name VARCHAR(256),
    number INTEGER NOT NULL,
    position_lat REAL,
    position_lng REAL,
    status VARCHAR(256),
    last_update INTEGER UNSIGNED NOT NULL,
    PRIMARY KEY (number, last_update)
    )
    """
    try:
        res = engine.execute("DROP TABLE IF EXISTS station")
        res = engine.execute(sql)
        print(res.fetchall())
    except Exception as e:
        print(e)

    sql = """
    CREATE TABLE IF NOT EXISTS availability
    (
    number INTEGER NOT NULL,
    available_bikes INTEGER,
    available_bike_stands INTEGER,    
    last_update INTEGER UNSIGNED NOT NULL,
    status VARCHAR(256),
    PRIMARY KEY (number, last_update)
    )
    """
    try:
        res = engine.execute("DROP TABLE IF EXISTS availability")
        res = engine.execute(sql)
        print(res.fetchall())
    except Exception as e:
        print(e)

    sql = """
    CREATE TABLE IF NOT EXISTS weather
    (
    station INTEGER NOT NULL,
    last_update INT(11) UNSIGNED NOT NULL,
    temperature REAL,
    weathercode INTEGER,
    windspeed REAL,
    hourly_time VARCHAR(300),
    hourly_temp VARCHAR(180),
    hourly_preci VARCHAR(140),
    hourly_weathercode VARCHAR(140),
    hourly_windspeed VARCHAR(180),
    daily_time VARCHAR(90),
    daily_weathercode VARCHAR(40),
    daily_temp_max VARCHAR(60),
    daily_temp_min VARCHAR(60),
    PRIMARY KEY (station, last_update)
    )
    """

    sql 
    try:
        res = engine.execute("DROP TABLE IF EXISTS weather")
        res = engine.execute(sql)
        print(res.fetchall())
    except Exception as e:
        print(e)

# If need to redesign/delete the table, run this function.
# create_table()