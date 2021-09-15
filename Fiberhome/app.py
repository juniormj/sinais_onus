#!/bin/env python3
# -*- coding: utf-8 -*-

import os
from datetime import datetime
from sys import argv

from dotenv import find_dotenv, load_dotenv
from easysnmp import Session
from influxdb import InfluxDBClient
from telebot import TeleBot

load_dotenv(find_dotenv())

IP_SERVER = os.environ.get("IP_SERVER")
ID_SALA = os.environ.get("ID_SALA")
TOKEN = os.environ.get("TOKEN")
bot = TeleBot(TOKEN)
ip_olt = argv[1]
cidade = argv[2]

session = Session(hostname=ip_olt, community="adsl", version=2)


def main():

    try:
        pon_name = session.walk("1.3.6.1.4.1.5875.800.3.9.3.3.1.2")
        onu_sinal = session.walk("1.3.6.1.4.1.5875.800.3.9.3.3.1.6")

        insert_json = []
        count = 0

        for sinal in onu_sinal:
            for name_pon in pon_name:

                if int(sinal.value) < -2400:
                    if sinal.oid_index == name_pon.oid_index:
                        insert_json.append(
                            {
                                "measurement": cidade,
                                "time": datetime.now(),
                                "fields": {
                                    "onu": name_pon.value.split()[1],
                                    "sinal": sinal.value,
                                    "ip": ip_olt,
                                },
                            }
                        )
                        count += 1

        save(insert_json)
        msg = f"Encontradas {count} onus anormais em {cidade}"
        bot.send_message(ID_SALA, msg)
    except SystemError:
        bot.send_message(ID_SALA, f"Timeout OLT: {ip_olt} {cidade} ")


def save(insert_json):
    client = InfluxDBClient(IP_SERVER, 8086, "grafana", "grafana", "sinais_fiberhome")
    client.write_points(insert_json)
    client.close()


main()
