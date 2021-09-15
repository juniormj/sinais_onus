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

session = Session(hostname=ip_olt, community="public", version=2)


def main():

    try:
        insert_json = []
        count = 0

        pon_name = session.walk("ifName")
        onu_sinal = session.walk("1.3.6.1.4.1.2011.6.128.1.1.2.51.1.4")

        for name_pon in pon_name:
            for sinal in onu_sinal:

                if int(sinal.value) < -2400:
                    if sinal.oid.split(".")[10] == name_pon.oid_index:
                        onu_filter = name_pon.value.split()[1]
                        onu_split = (
                            onu_filter.split("/")[1] + "/" + onu_filter.split("/")[2]
                        )
                        onu = onu_split + "/" + sinal.oid.split(".")[11]
                        insert_json.append(
                            {
                                "measurement": cidade,
                                "time": datetime.now(),
                                "fields": {
                                    "onu": onu,
                                    "sinal": sinal.value,
                                    "ip": ip_olt,
                                },
                            }
                        )
                        count += 1
                        break

        save(insert_json)
        msg = f"Encontradas {count} onus anormais em {cidade}"
        bot.send_message(ID_SALA, msg)
    except SystemError:
        bot.send_message(ID_SALA, f"Timeout OLT: {ip_olt} {cidade} ")


def save(insert_json):
    client = InfluxDBClient(IP_SERVER, 8086, "grafana", "grafana", "sinais_huawei")
    client.write_points(insert_json)
    client.close()


main()
