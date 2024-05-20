import requests
from bs4 import BeautifulSoup
import yfinance as yf
import pandas as pd
from tqdm import tqdm  # Import tqdm for progress bar

# Market cap categories and their URLs
cap_categories = ['Micro Cap', 'Small Cap', 'Mid Cap', 'Large Cap']
urls = {
    'Micro Cap': 'https://stockanalysis.com/list/micro-cap-stocks/',
    'Small Cap': 'https://stockanalysis.com/list/small-cap-stocks/',
    'Mid Cap': 'https://stockanalysis.com/list/mid-cap-stocks/',
    'Large Cap': 'https://stockanalysis.com/list/large-cap-stocks/'
}


def select_market_cap():
    print("Select a market cap category to start analysis:")
    for i, category in enumerate(cap_categories, start=1):
        print(f"{i}. {category}")
    choice = input("Enter your choice (1-4): ")
    return cap_categories[int(choice) - 1] if choice.isdigit() and 1 <= int(choice) <= 4 else cap_categories[0]


def get_price_range(choice):
    ranges = {
        '1': (0, 5),
        '2': (0, 10),
        '3': (10, 20),
        '4': (20, 50),
        '5': (50, float('inf'))
    }
    return ranges.get(choice, (0, 5))  # Default to 'Under $5'


def select_price_range():
    print("Select a price range for the stocks:")
    price_ranges = {
        '1': 'Under $5',
        '2': 'Under $10',
        '3': '$10 to $20',
        '4': '$20 to $50',
        '5': 'Over $50'
    }
    for key, value in price_ranges.items():
        print(f"{key}. {value}")
    choice = input("Enter your choice (1-5): ")
    return choice


def select_3wt_range():
    print("Select the 3WT percentage range:")
    percentage_ranges = {
        '1': '1% - 5%',
        '2': '5% - 10%',
        '3': '10% - 15%',
        '4': '15% - 20%',
        '5': 'Over 20%'
    }
    for key, value in percentage_ranges.items():
        print(f"{key}. {value}")
    choice = input("Enter your choice (1-5): ")
    return choice


def get_3wt_range(choice):
    ranges = {
        '1': (1, 5),
        '2': (5, 10),
        '3': (10, 15),
        '4': (15, 20),
        '5': (20, float('inf'))
    }
    return ranges.get(choice, (1, 5))  # Default to '1% - 5%'


def fetch_tickers(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'id': 'main-table'})
    data = []
    for row in table.find_all('tr')[1:]:
        cols = row.find_all('td')
        ticker_info = {
            'No.': cols[0].text,
            'Symbol': cols[1].text,
            'Company Name': cols[2].text,
            'Market Cap': cols[3].text,
            'Stock Price': cols[4].text,
            '% Change': cols[5].text,
            'Revenue': cols[6].text
        }
        data.append(ticker_info)
    return data


def fetch_eps_data(ticker):
    url = f"https://stockanalysis.com/stocks/{ticker}/financials/?p=quarterly"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    eps_rows = soup.find_all('div', class_='row')[1:]
    eps_data = {}
    for row in eps_rows[:4]:
        columns = row.find_all('div')
        quarter = columns[0].text.strip()
        eps = columns[2].text.strip()
        eps_data[f'EPS {quarter}'] = eps
    return eps_data


def fetch_etf_count(ticker):
    url = f"https://www.etf.com/{ticker}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    etf_div = soup.find('div', class_="stock-information__data--main")
    etf_count = int(etf_div.text) if etf_div else 0
    return etf_count


def analyze_stock(ticker, price_choice, wt_choice):
    try:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="2y", interval="1wk")
        current_price = hist['Close'].iloc[-1]
        price_range = get_price_range(price_choice)
        wt_range = get_3wt_range(wt_choice)

        if not (price_range[0] <= current_price <= price_range[1]):
            return False, 0  # Price not in selected range

        # Calculate weekly percentage changes
        hist['PriceChange'] = hist['Close'].pct_change()
        hist['InRange'] = hist['PriceChange'].apply(lambda x: wt_range[0] / 100 <= abs(x) <= wt_range[1] / 100)
        percent_3wt = (hist['InRange'].rolling(window=3).sum() == 3).mean() * 100  # Calculate the percentage

        # Conditions for Cup and Handle detection (simplified for this example)
        is_cup = hist['PriceChange'].rolling(window=13).sum() < 0.1  # 3 months for cup
        is_handle = hist['PriceChange'].rolling(window=3).sum() < 0.02  # 3 weeks for handle

        # Check for uptrend after the handle
        uptrend_post_handle = hist['PriceChange'].rolling(window=4).sum() > 0.05

        meets_cup_handle_criteria = is_cup.iloc[-1] and is_handle.iloc[-1] and uptrend_post_handle.iloc[-1]
        return meets_cup_handle_criteria, percent_3wt
    except Exception as e:
        print(f"Error analyzing {ticker}: {e}")
        return False, 0


def format_price(price):
    return f"${price:,.2f}"


def format_volume(volume):
    if volume >= 1_000_000_000:
        return f"{volume / 1_000_000_000:.1f}B"
    elif volume >= 1_000_000:
        return f"{volume / 1_000_000:.1f}M"
    elif volume >= 1_000:
        return f"{volume / 1_000:.1f}K"
    else:
        return f"{volume}"


def format_market_cap(cap):
    if cap >= 1_000_000_000:
        return f"${cap / 1_000_000_000:.1f}B"
    elif cap >= 1_000_000:
        return f"${cap / 1_000_000:.1f}M"
    elif cap >= 1_000:
        return f"${cap / 1_000:.1f}K"
    else:
        return f"${cap}"


def format_3wt(percent_3wt):
    return f"{percent_3wt:.2f}%"


def main():
    selected_cap = select_market_cap()
    price_choice = select_price_range()
    wt_choice = select_3wt_range()
    tickers = fetch_tickers(urls[selected_cap])
    analysis_results = []

    with tqdm(total=len(tickers), desc="Analyzing stocks") as pbar:
        for ticker_info in tickers:
            ticker_symbol = ticker_info['Symbol'].upper()  # Extract and convert the ticker symbol to uppercase
            if '.' in ticker_info['Symbol']:  # Skip tickers with periods
                continue
            meets_cup_handle_criteria, percent_3wt = analyze_stock(ticker_symbol, price_choice, wt_choice)  # Updated to handle 3WT
            if meets_cup_handle_criteria:  # If the stock meets Cup & Handle and 3WT criteria
                eps_data = fetch_eps_data(ticker_symbol)
                etf_count = fetch_etf_count(ticker_symbol)
                stock_info = yf.Ticker(ticker_symbol).info
                analysis_results.append({
                    'Ticker': ticker_symbol,
                    'Company Name': ticker_info['Company Name'],
                    'Stock Price': format_price(float(ticker_info['Stock Price'].replace('$', '').replace(',', ''))),
                    'Market Cap': format_market_cap(float(ticker_info['Market Cap'].replace('$', '').replace('B', '').replace('M', '').replace(',', ''))),
                    '3WT %': format_3wt(percent_3wt),
                    '# ETFs Holding': etf_count,
                    'Link': f"[View Ticker](https://stockanalysis.com/stocks/{ticker_symbol.lower()}/)",
                    **eps_data
                })
            pbar.update(1)

    df = pd.DataFrame(analysis_results)
    if not df.empty:
        print(df.to_string(index=False))
    else:
        print("No stocks met the criteria.")


if __name__ == "__main__":
    main()
