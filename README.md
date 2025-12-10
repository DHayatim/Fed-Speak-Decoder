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
1. Install dependencies:
   ```bash
   pip install -r requirements.txt