import requests
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc."

AV_API_KEY = "MOXWHU20F3I5F19L"
STOCK_URL = "https://www.alphavantage.co/query"
NEWS_API_KEY = "33abbe7bf28a425cbf4af27391819924"
NEWS_API_URL = "https://newsapi.org/v2/everything"

stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AV_API_KEY
}

news_api_params = {
    "q": COMPANY_NAME,
    "apikey": NEWS_API_KEY
}
## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
response = requests.get(url=STOCK_URL, params=stock_parameters)
response.raise_for_status()
# print(response.status_code)
daily_stock_data = response.json()["Time Series (Daily)"]
daily_stock_data_list = [value for (key, value) in daily_stock_data.items()]

yesterday_closing = float(daily_stock_data_list[0]["4. close"])
day_before_closing = float(daily_stock_data_list[1]["4. close"])

percent_change = round((day_before_closing - yesterday_closing) * 100 / yesterday_closing, 2)

# print(yesterday_closing, day_before_closing, percent_change)


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if abs(percent_change) > 0:
    news_response = requests.get(url=NEWS_API_URL, params=news_api_params)
    news_response.raise_for_status()
    news_articles = news_response.json()
    top_articles = news_articles["articles"][:3]
    # print(top_articles)
    if percent_change >= 0:
        up_down_image = "🔺"
    else:
        up_down_image = "🔻"

    for article in top_articles:
        message = f"{STOCK}:{up_down_image}{abs(percent_change)}%\nHeadline: {article['title']}\nBrief: {article['description']}"
        print(message)

#Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

