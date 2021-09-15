#!/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import sys
from time import sleep

from rich.console import Console

vendor_olt = sys.argv[1]
console = Console()


def execute(vendor):
    drop_database = f"drop database sinais_{vendor.lower()}"
    create_database = f"create database sinais_{vendor.lower()}"

    subprocess.getstatusoutput(f"docker exec influxdb influx -execute {drop_database}")
    subprocess.getstatusoutput(
        f"docker exec influxdb influx -execute {create_database}"
    )

    ips = open(f"{vendor}/IPs")
    for ip in ips:
        ip = ip.split("\n")[0]
        subprocess.getstatusoutput(f"{vendor}/./app.py {ip.split()[0]} {ip.split()[1]}")
        print(f"{vendor}/./app.py {ip}")
        sleep(5)
        console.log(f"OLT {ip} Finalizada")
    ips.close()


with console.status("[green] Executando Tarefa... [/]") as task:
    execute(vendor_olt)
