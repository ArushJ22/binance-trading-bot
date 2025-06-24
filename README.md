# 🔁 Binance Testnet Trading Bot

A simplified crypto trading bot built in **Python** for the **Binance SPOT Testnet**.

> 💼 Submitted as part of the hiring task for **Junior Python Developer – Crypto Trading Bot**

---

## ✅ Features

- ✅ Place **Market**, **Limit**, and **Stop-Limit** orders  
- ✅ Supports both **BUY** and **SELL** orders  
- ✅ Interactive CLI using `questionary` (dropdowns, clean prompts)  
- ✅ Input validation and comprehensive error handling  
- ✅ Logs all API actions and errors to `logs/bot.log`  
- ✅ Modular and clean codebase:  
  - `bot/` – Core trading logic  
  - `cli/` – Command-line interface  
  - `utils/` – Helper functions and configurations  

---

## 📦 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/binance-trading-bot.git
cd binance-trading-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your API Keys

Create a `config.py` file in the project root with the following content:

```python
API_KEY = "your_api_key_here"
API_SECRET = "your_api_secret_here"
```

> 🧪 Get your API keys from: [https://testnet.binance.vision](https://testnet.binance.vision)

---

## 🚀 Running the Bot

```bash
python main.py
```

---

## 🛠 Tech Stack

- **Python 3**
- **[python-binance](https://github.com/sammchardy/python-binance)** – Binance API wrapper  
- **[questionary](https://github.com/tmbo/questionary)** – User-friendly CLI prompts  
- **logging** – Python’s built-in logging module for error and activity logs  

---

## 👤 Author

**Arush John**  
📧 Email: [arushjohn22@gmail.com](mailto:arushjohn22@gmail.com)  
🐙 GitHub: [https://github.com/ArushJ22](https://github.com/ArushJ22)
