
# 🌦️ Telegram Weather Bot (Selenium + PyTelegramBotAPI)

Simple Telegram bot that gets weather data using Selenium and sends it to users.

---

## 🚀 Features

- Telegram bot with PyTelegramBotAPI
- Weather scraping using Selenium
- City input from user
- Headless Chrome automation
- Secure `.env` token storage

---

## 🧠 How it works

User sends a city name → bot opens Google → searches weather → extracts temperature → sends result back.

---

## 🛠️ Tech Stack

- Python
- PyTelegramBotAPI
- Selenium
- WebDriver Manager
- python-dotenv

---

## 📦 Installation

### 1. Clone repo
```bash
git clone https://github.com/your-username/weather-bot.git
cd weather-bot
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Create `.env`

```env
TELEGRAM_TOKEN=your_token_here
```

---

## ▶️ Run project

```bash
python bot.py
```

---

## 📁 Project structure

```
weather_bot/
│
├── bot.py
├── parser.py
├── config.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Usage

* `/start` → start bot
* Send city name → get weather

Example:

```
Yerevan
Moscow
Paris
```

---

## ⚠️ Notes

* Selenium depends on Google UI (may break if layout changes)
* Use headless Chrome for server
* For production better use Weather API

---

## 🔐 Security

Add `.env` to `.gitignore`:

```
.env
__pycache__/
```

Never expose your bot token.

---

## 🚀 Improvements

* Switch Selenium → Weather API (OpenWeather)
* Add inline buttons
* Docker support
* Webhook mode
* Caching results

---

## 👨‍💻 Author

Built for learning and practice 🚀


