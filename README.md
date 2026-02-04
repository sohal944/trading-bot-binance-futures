# Binance Futures Testnet Trading Bot

## Overview
This project is a CLI-based Python trading bot that places orders on the Binance Futures Testnet (USDT-M).
It demonstrates clean code structure, input validation, logging, and proper error handling.

---

## Setup

### 1. Create Binance Futures Testnet Account
- Register at https://testnet.binancefuture.com
- Enable USDT-M Futures
- Generate API Key and Secret with Futures permissions

### 2. Environment Setup
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Configure Environment Variables
Create a .env file in the project root:
```bash
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```
## Usage
### MARKET Order
```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```
### LIMIT Order
```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 70000
```
### STOP-LIMIT Order (Bonus)
```bash
python cli.py --symbol BTCUSDT --side SELL --order-type STOP_LIMIT --quantity 0.001 --price 69000 --stop-price 69500
```
## Logging
-Logs are written to logs/trading_bot.log
-Logs include API requests, responses, and error details
-The log file contains at least one MARKET order and one LIMIT order as required

## Assumptions & Notes
-Uses Binance Futures Testnet (USDT-M) only
-Binance Testnet may return partial order responses for some order types
-Missing response fields are handled defensively in the code

## Project Structure
```bash
trading_bot/
  bot/
    client.py
    orders.py
    validators.py
    logging_config.py
  cli.py
  README.md
  requirements.txt
  logs/
```

