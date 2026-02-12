# 🤖 Crypto Trader Bot

Automated cryptocurrency trading bot for Binance that generates buy/sell signals based on price movements and manages profit/loss automatically.

## 📋 Features

✅ **Automated Trading** - Automatically buys and sells cryptocurrencies based on market signals
✅ **Profit/Loss Tracking** - Monitors and logs all trades with detailed P&L calculations
✅ **Risk Management** - Automatic stop-loss and profit-taking at configured levels
✅ **Multi-Pair Support** - Can trade any cryptocurrency pair available on Binance
✅ **Real-time Monitoring** - Continuously monitors market prices and executes trades

## 📁 Project Structure

```
Crypto-trader/
├── config.py           # Configuration and settings
├── binance_api.py      # Binance API integration
├── trading_logic.py    # Buy/Sell signal generation and trade execution
├── bot.py              # Main bot application
├── requirements.txt    # Python dependencies
└── README.md           # This file
```

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- Binance API Keys (from your Binance account)

### Steps

1. **Clone the repository:**
```bash
git clone https://github.com/ya32420-debug/Crypto-trader.git
cd Crypto-trader
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Configure your API keys:**
Edit `config.py` and add your Binance API credentials:
```python
BINANCE_API_KEY = 'your_api_key_here'
BINANCE_API_SECRET = 'your_api_secret_here'
```

## ⚙️ Configuration

Edit `config.py` to customize:

```python
TRADING_PAIR = 'BTCUSDT'      # Which pair to trade
TRADE_AMOUNT = 0.01           # Amount per trade
STOP_LOSS = 0.02              # 2% stop loss
PROFIT_TARGET = 0.05          # 5% profit target
USE_TRAILING_STOP = True      # Enable trailing stop
```

## 🚀 Running the Bot

```bash
python bot.py
```

The bot will:
1. Connect to Binance API
2. Monitor the configured trading pair
3. Generate buy/sell signals automatically
4. Execute trades based on your settings
5. Track profits and losses

## 📊 Trading Logic

- **Buy Signal**: Price increases by 1%
- **Sell Signal**: Either profit target reached OR stop loss triggered
- **Risk Management**: Automatic exits prevent large losses

## 📈 Expected Behavior

The bot will continuously:
- Check current price vs previous price
- Generate signals when thresholds are met
- Execute trades automatically
- Log all transactions with P&L

## ⚠️ Important Notes

1. **Test First**: Use small amounts initially
2. **Monitor Regularly**: Don't leave it running unattended
3. **API Security**: Keep your API keys private
4. **Restrictions**: Ensure your Binance account allows API trading

## 📝 Example Output

```
[BUY] BTCUSDT at $45000
[SELL] BTCUSDT at $47250 | Profit/Loss: 5.00%
Total Profit: $2250
```

## 🤝 Contributing

Feel free to fork and improve this bot!

## 📄 License

MIT License - Feel free to use this project for personal and commercial purposes.

## ⚡ Quick Start

```bash
# 1. Clone
git clone https://github.com/ya32420-debug/Crypto-trader.git

# 2. Install
pip install -r requirements.txt

# 3. Configure
# Edit config.py with your API keys

# 4. Run
python bot.py
```

---

**Made with ❤️ by ya32420-debug**

For support or questions, open an issue on GitHub!