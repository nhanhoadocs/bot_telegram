# Telebot

A [Telegram](https://telegram.org/) Bot written in Python (Work-In-Progress)

## Installation

### 1. Clone this repo and install all requirements:

```
git clone https://github.com/nhanhoadocs/bot_telegram.git
cd bot_telegram/check_port
sudo pip3 install -r requirements.txt
```

### 2. Run Setup

```
sudo python3 setup.py install
```

### 3. Edit tele.conf and move to /etc/telebot

```
cd etc/
vi tele.conf
```

```
[DEFAULT]

telegram_token = your_token
```
Save file

```
mkdir /etc/telebot
cp tele.conf /etc/telebot
```

### 4. Install supervisor package

```
sudo yum install -y supervisor
sudo systemctl start supervisord
sudo systemctl enable supervisord
sudo cp bot.conf /etc/supervisord.d/bot.ini
```

### 5. Start BOT

```
sudo supervisorctl update
sudo supervisorctl start bot
```

====================================

## Running with Docker

### 1. Preparing environment

- Install docker on Ubuntu or CentOS

```
curl -fsSL https://get.docker.com | sh
```

### 2. Build image from Dockerfile

```
cd bot_telegram/check_port
build -t bot_image .
```

Work-in-process
