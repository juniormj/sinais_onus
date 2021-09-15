#!/bin/bash
echo "
##############################################################
###############   INSTALANDO DOCKER COMPOSER   ###############
##############################################################"
apt update
apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common gcc python3-dev python3-pip libsnmp-dev snmp-mibs-downloader software-properties-common -y
add-apt-repository "deb http://ftp.de.debian.org/debian $(lsb_release -cs) main non-free"
add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -
apt update

curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose

chmod +x /usr/local/bin/docker-compose
docker-compose --version

echo "
#############################################################
###################   INSTALANDO DOCKER   ###################
#############################################################"
apt-cache policy docker-ce
apt install docker-ce
systemctl status docker


echo "
###########################################################
###################   COMANDOS DOCKER   ###################
###########################################################"
docker-compose up -d

