
<h1 align="center">
  <br>
  <a href="http://www.amitmerchant.com/electron-markdownify"><img src="https://avatars.githubusercontent.com/u/33784865?s=280&v=4" alt="Markdownify" width="200"></a>
  <br>
  AIO Bot
  <br>
</h1>

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
![Stable Version](https://img.shields.io/pypi/v/poetry?label=stable)
![Python Versions](https://img.shields.io/pypi/pyversions/poetry)
![Python Versions](https://camo.githubusercontent.com/d91ed7ac7abbd5a6102cbe988dd8e9ac21bde0a73d97be7603b891ad08ce3479/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f64652532307374796c652d626c61636b2d3030303030302e737667)
![Python Versions](https://camo.githubusercontent.com/fe4a658dd745f746410f961ae45d44355db1cc0e4c09c7877d265c1380248943/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f253230696d706f7274732d69736f72742d2532333136373462313f7374796c653d666c6174266c6162656c436f6c6f723d656638333336)

# TelegramBot
Telegram bot for self representation

## Docker
Разработка велась в devcontainer, Dockerfile.dev лежит в /docker
для сборки образа для разработки:
```commandline
bash docker/docker_build_dev.sh Poetry version, Image Name
```
## Poetry 
В качестве менеджера зависимостей использовался poetry 1.5.1,
все зависмости можно найти в requirements.txt, либо pypropject.toml

## Inforamtion
Для сокрытия личных данных, использовались yaml конфиги и класс Configurator_yml, все содержится в /conf. В качестве бд использовался PostgreSQL, для миграции использовался alembic, деплой производится с помощью docker compose.

UPD. Не успел до дедлайна реализовать webhook, проблемы с настройкой nginx конфигурации. 



