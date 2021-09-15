# Sinais Onus

Sistema desenvolvido para coleta de sinais alto em OLTs da Fiberhome e Huawei via SNMP e apresentado em gráficos pelo Grafana.


## 📋 Pré-requisitos
---

Antes de começar, você vai precisar ter instalado em sua máquina o git: [Git](https://git-scm.com). 
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)


## 🔧 Instalação
---

```bash
# Clone este repositório
$ git clone https://github.com/juniormj/sinais_onus.git
```

#### Acesse o diretório do projeto pelo terminal

```bash
$ cd sinais_onus
```

#### Execute o script ***install-docker*** como root

```bash
./install-docker.sh
```

#### Instalação das dependências

```bash
$ pip3 install -r requirements.txt
```

#### Agendando tarefas no crontab
```bash
26,00,00 01,13,17 * * * python /home/User/sinais_onus/start.py Huawei > /tmp/outputhuawei.log 2>&1
27,00,00 01,13,17 * * * python /home/User/sinais_onus/start.py Fiberhome > /tmp/outputfiberhome.log 2>&1
```

#### 
## 📦 Implementação
---

#### Adicionando endereços das OLTs
Caso a OLT de coleta seja Fiberhome adicione o IP e o nome da cidade dentro do arquivo IPs separado por espaço, um abaixo do outro. exemplo.

```
1.1.1.1 cidade1
2.2.2.2 cidade2
3.3.3.3 cidade3
```

E assim segue o mesmo modelo para OLTs da Huawei.

Após ter executado o script ***install-docker*** você poderá perceber que o docker
e o plugins do influxDB já estarão disponíveis.

<table>
    <tr>
        <td><img src="imgs/login.png" width="400px"></img></td>
        <td><img src="imgs/plugins.png" width="400px"></img></td>
    </tr>
</table>

#### Configuração do datasource:

<table>
    <tr>
        <td><img src="imgs/config_datasource.png" width="400px"></img></td>
        <td><img src="imgs/config_datasource2.png" width="400px"></img></td>
    </tr>
</table>

#### Criação do dashboard:

![dashboard](imgs/config_panel.png)

## 🛠️ Construído com
---

Abaixo as ferramentas utilizadas para o desenvolvimento desse projeto

* [Docker](https://www.docker.com/) - É uma plataforma de software que permite fazer deploy de serviços.
* [Grafana](https://grafana.com/) - É uma solution open source para análise e monitoramento.
* [InfluxDB](https://www.influxdata.com/) - É um banco de dados de código aberto designado para lidar com alto volume de leituras e escritas por segundo sem causar muito impacto.


## 🖇️ Colaborandores
---

<!-- 
<a href="#" title="Tutoriais">✅</a>
<a href="#" title="Documentacao">📖</a>
<a href="#" title="Design">🎨</a>
<a href="#" title="Codigo">💻</a>
<a href="#" title="Bug reports">🐛</a>
<a href="#" title="Testes">⚠️</a>
<a href="#" title="compilacao">📦</a>
<a href="#" title="Ideas, Feedback">🤔</a>
<a href="#" title="Responder questoes">💬</a>
<a href="#" title="#">📝</a>
-->

<table>
  <tr>
    <td align="center">
    <a href="#">
    <img style="border-radius: 50%;" src="https://avatar.skype.com/v1/avatars/live:inaciophd/public?returnDefaultImage=false&size=l" object-fit="cover" width="100px;" height="100px" alt=""/>
    <br /><sub><b>Inacio</b></sub></a><br /> <a href="#" title="Testes">⚠️</a> <a href="#" title="Ideas, Feedback">🤔</a></td>
    <td align="center"><a href="http://audiolion.github.io"><img style="border-radius: 50%;" src="https://avatar.skype.com/v1/avatars/live:mauro.junior/public?returnDefaultImage=false&size=l" width="100px;" alt=""/><br /><sub><b>Mauro</b></sub></a><br /><a href="#" title="Ideas, Feedback">🤔</a><a href="#" title="Bug reports">🐛</a></td>
  </tr>
</table>

Contribuições de qualquer tipo são bem-vindas!

## ✒️ Autores
---

<a href="https://www.linkedin.com/in/messias-manoel-da-silva-junior-15004664/">
 <img style="border-radius: 50%;" src="https://i.ibb.co/VWcJsjm/pp-amarelo.jpg" width="100px;"  alt=""/>
 <br />
 <sub><b>Messias Junior</b></sub></a> 🔞


Entre em contato!

[![Twitter Badge](https://img.shields.io/badge/-@juniormj-1ca0f1?style=flat-square&labelColor=1ca0f1&logo=twitter&logoColor=white&link=https://twitter.com/juniormj1)](https://twitter.com/juniormj1) [![Linkedin Badge](https://img.shields.io/badge/-Messias_Junior-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/messias-manoel-da-silva-junior-15004664/)](https://www.linkedin.com/in/messias-manoel-da-silva-junior-15004664/) 
[![Gmail Badge](https://img.shields.io/badge/-juniormj1@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:juniormj1@gmail.com)](mailto:juniormj1@gmail.com)


## 📄 Licença
---

Este projeto está licenciado sob a Licença [MIT](http://#)

