# 🏛️ The Fed-Speak Decoder

**Quantifying Central Bank Sentiment using NLP.**

## 🎯 Objective
In financial markets, the tone of the Federal Reserve (FOMC) dictates liquidity and volatility. This project automates the retrieval of FOMC Minutes and applies a Lexicon-based NLP analysis to generate a "Sentiment Score."

**Current Analysis Result:**
- **Meeting Date:** Latest Available
- **Sentiment Score:** -79 (Highly Bearish/Risk-Averse)
- **Top Keywords:** Board, Inflation, Rate.

## 🛠️ Tech Stack
- **Python 3.12**
- **Web Scraping:** `requests`, `BeautifulSoup`
- **NLP:** Custom Loughran-McDonald Financial Dictionary
- **Data Engineering:** Automated path handling and text cleaning

## 🚀 How to Run

Copy and paste these commands in your terminal:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the Scraper (Fetch latest minutes)
python scraper.py

# 3. Run the Analyzer (Calculate sentiment)
python analyzer.py
📊 Methodology
The algorithm filters "Stop Words" to isolate financial terminology. It then maps the remaining tokens against a weighted dictionary:

Positive (+1): growth, strong, recovery...

Negative (-1): inflation, risk, weak, decline...

🔮 Next Steps
Visualize sentiment evolution over time (Matplotlib).

Correlate sentiment score with S&P 500 (SPY) daily returns.
