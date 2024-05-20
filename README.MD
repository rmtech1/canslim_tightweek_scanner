# CANSLIM Tight Week Scanner

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Getting Started](#getting-started)
- [Functionality](#functionality)
- [CANSLIM Criteria](#canslim-criteria)
- [3 Weeks Tight Pattern](#3-weeks-tight-pattern)
- [License](#license)

## Introduction
The CANSLIM Tight Week Scanner is designed to help investors identify potential stock buy opportunities based on the CANSLIM method popularized by William O'Neil. This tool combines traditional CANSLIM criteria with additional pattern recognition for the Cup and Handle and 3 Weeks Tight (3WT) patterns, providing a comprehensive analysis of stocks.

## Features
- **Market Cap Filtering**: Analyze stocks based on market capitalization categories (Micro Cap, Small Cap, Mid Cap, Large Cap).
- **Price Range Filtering**: Focus on stocks within specific price ranges.
- **3WT Pattern Recognition**: Identify stocks that meet the 3 Weeks Tight criteria.
- **Cup and Handle Pattern Detection**: Analyze stocks for the Cup and Handle pattern.
- **CANSLIM Criteria Analysis**: Evaluate stocks based on the CANSLIM method.
- **Progress Indicator**: Visual progress bar to track the analysis process.
- **Detailed Stock Information**: Fetches and displays EPS data, ETF holdings, and more.

## Installation
To install and run the CANSLIM Tight Week Scanner, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/canslim_tightweek_scanner.git
    cd canslim_tightweek_scanner
    ```

2. **Install Dependencies**:
    Make sure you have Python 3.7 or later installed. Then, install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To use the CANSLIM Tight Week Scanner:

1. **Run the Script**:
    ```bash
    python canslim.py
    ```

2. **Follow the Prompts**:
    - Select a market cap category.
    - Select a price range for stocks.
    - Select the 3WT percentage range.
    - The script will analyze the stocks and display the results.

## Getting Started
The CANSLIM Tight Week Scanner was created to address the need for a comprehensive and automated way to analyze stocks based on the CANSLIM method. It simplifies the process of identifying potential buy opportunities by integrating various stock analysis criteria and patterns into a single tool.

### What It Is
This tool is a Python script that leverages web scraping and financial data APIs to fetch and analyze stock data. It evaluates stocks against the CANSLIM criteria, detects Cup and Handle patterns, and checks for the 3 Weeks Tight pattern.

### Why It Was Created
Investors often struggle with manually analyzing stocks to identify potential buy opportunities. This tool automates the process, providing a faster and more efficient way to screen stocks based on well-established criteria and patterns.

## Functionality
### Market Cap Filtering
The script allows users to filter stocks based on their market capitalization:
- Micro Cap
- Small Cap
- Mid Cap
- Large Cap

### Price Range Filtering
Users can specify the price range for stocks they want to analyze:
- Under $5
- Under $10
- $10 to $20
- $20 to $50
- Over $50

### 3 Weeks Tight Pattern
The tool identifies stocks that meet the 3 Weeks Tight (3WT) criteria, where the stock's weekly closing prices stay within a tight range for three consecutive weeks.

### Cup and Handle Pattern
The script detects the Cup and Handle pattern, a bullish continuation pattern that signals a potential upward move.

## CANSLIM Criteria
The CANSLIM method screens stocks based on the following seven characteristics:
1. **C=Current Earnings**: Quarterly earnings per share are up 25% or more.
2. **A=Annual Earnings**: Five-year average compounded earnings growth rate is greater than 24%.
3. **N=New Highs**: The stock is within 15% of making a new 52-week high and is breaking out of a period of consolidation.
4. **S=Shares Outstanding**: The number of shares outstanding is less than 50 million shares, and there has been a recent increase in trading volume.
5. **L=Leading Stocks**: The company is a market leader reflected by a Relative Strength Value (RSV) of 80 or higher.
6. **I=Institutional Ownership**: Institutional sponsorship should be minimal, but there should be at least one major institution with a sizeable position in the stock.
7. **M=Market Conditions**: The market posture should be bullish.

### Example CANSLIM Scoring
The script evaluates stocks against the CANSLIM criteria and assigns a score. Stocks that meet at least 60% of the criteria are highlighted.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Please contribute and fork. I was able to find a significant amount of stocks that have given a good 10% Return. 
---

