# Sentify

!!! success "Financial Analysis"
    Leveraging Sentiment Analysis on News for Stock Market Insights.

## Overview

This project focuses on analyzing the sentiment of news articles to predict stock trends. It features a Flask-based web application designed to provide real-time financial data analysis and sentiment tracking.

## How It Works

!!! tip "Analysis Process"
    - **Input**: Users can enter a company name or ticker symbol to retrieve relevant news articles.
    - **Process**: Each news article is analyzed for sentiment, with scores generated to gauge the article's impact on stock trends.
    - **Output**: The application delivers actionable insights and confidence indices based on the sentiment analysis, helping investors make informed decisions about their investments.

## Features

!!! example "Key Capabilities"
    - **Real-time Sentiment Analysis**: Process news articles as they are published
    - **Market Correlation**: Link sentiment scores to market movements
    - **Trading Signals**: Generate buy/sell recommendations based on sentiment
    - **News Aggregation**: Collect and analyze news from multiple sources
    - **Historical Analysis**: Track sentiment trends over time
    - **Web Interface**: Flask-based application for easy access

## Technology Stack

- **Backend**: Flask web application
- **Language**: Python 3.11+
- **Data Processing**: Natural Language Processing (NLP)
- **News Sources**: Financial news APIs
- **Analysis**: Machine learning models for sentiment classification
- **Deployment**: Local development server

## Installation & Setup

!!! info "Prerequisites"
    - Python (version 3.11 or higher)
    - Poetry (recommended) or pip

### Using Poetry (recommended)

```shell
git clone https://github.com/LifeAdventurer/sentify.git
cd sentify
poetry install
poetry env activate
```

### Using pip

```shell
git clone https://github.com/LifeAdventurer/sentify.git
cd sentify
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## Usage

To serve the Flask app locally, run:

```shell
poetry run python3 src/main.py
```

## Configuration

The application can be configured by updating the `config.py` file in the `src/config` directory:

!!! tip "Key Configuration Parameters"
    - **TOP_COMPANIES_COUNT**: Number of top companies ranked by market cap to search (default: 10000)
    - **TIMESTAMP_FORMAT**: Format for timestamps used in the application (default: "%Y-%m-%dT%H:%M:%SZ")
    - **UTC_DIFFERENCE**: Difference in hours between local time and UTC (default: 8)
    - **MAX_NEWS_LOOKBACK_DAYS**: Maximum days to look back when fetching news (default: 60)
    - **CPU_COUNT**: Number of CPUs used for multiprocessing (default: 2)

## Use Cases

!!! example "Perfect For"
    - **Individual Investors**: Make data-driven investment decisions
    - **Trading Firms**: Enhance algorithmic trading strategies
    - **Financial Analysts**: Supplement traditional analysis methods
    - **Market Researchers**: Understand market sentiment trends
    - **Risk Management**: Identify potential market volatility

## Repository

!!! link "Source Code"
    View the project on [GitHub](https://github.com/LifeAdventurer/sentify)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](https://github.com/LifeAdventurer/sentify/blob/main/LICENSE) file for details.
