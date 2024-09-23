# Florida Real Estate Market Analysis

## Project Overview

This project involves scraping real estate data from Realtor.com for properties listed in Florida and creating dashboards to analyze the performance of brokers, property prices, and geographic trends. The analysis helps real estate agents, buyers, and investors make informed decisions.

## Motivation

The Florida real estate market is diverse and dynamic, making it challenging for stakeholders to stay informed about trends in property listings, prices, and broker performance. This project aims to:
- Provide a comprehensive overview of the market through data visualization.
- Help stakeholders, such as real estate agents, buyers, and investors, make data-driven decisions.
- Leverage web scraping to gather and analyze large datasets in real-time.

## Data Collection

The [data](data/) was scraped from [Realtor.com](https://www.realtor.com/realestateandhomes-search/Florida) using a Python-based web scraper. The scraper collected information such as:
- **Price**: Property prices in USD.
- **Category**: Type of property (e.g., house, condo, land).
- **Beds**: Number of bedrooms.
- **Baths**: Number of bathrooms.
- **Area**: Square footage of the property.
- **Plot Size**: Lot size in square feet.
- **Address**: Location of the property.
- **Broker**: Listing broker.
- **URL**: Direct link to the property listing.

## Data Transformation

After scraping the raw data from Realtor.com, the following data transformation steps were performed to clean and prepare the dataset for analysis:
1. **Handling Missing Values**
2. **Data Type Conversion**
3. **Extracting ZIP Codes from Address**
4. **Handling Property Prices**


The cleaned dataset contains over 8,312 listings and covers a wide range of property types and geographic locations across Florida.

## Key Findings

### 1. **Broker Performance**
   - **Top Brokers**: Lennar, Meritage Homes, and Coldwell Banker Realty dominate the market in terms of the number of listings.
   - **Geographic Presence**: Some brokers have a strong presence in specific areas. For instance, **Coldwell Banker Realty** is most active in **Bradenton**, while **Lennar** performs strongly in **Orlando**.

### 2. **Real Estate Market Overview**
   - **Price Distribution**: The majority of properties are priced between **$0** and **$500,000**, with fewer properties listed above the **$1M** range.
   - **Property Types**: **Houses** make up the majority of the listings (over 66% of the market), followed by **Mobile Homes** and **Condos**.

### 3. **Property Features**
   - **Bedroom and Bathroom Insights**: Homes with **3-5 bedrooms** are the most common, while properties with **2-3 bathrooms** are typical.
   - **Area Analysis**: The average price per square foot varies by property type, with **land** having the highest average at **$647.8/sqft**.

## Observations

- **Geographic Hotspots**: **Parrish** and **Hobe Sound** have the highest concentration of listings, making them key areas of focus for both agents and investors.
- **Price Trends**: The price distribution suggests that Florida offers a range of property options for different budgets, with a majority of listings under **$500K**, making it accessible for average buyers.
- **Broker Strategies**: Brokers like **Lennar** and **Meritage Homes** are leveraging their position to dominate in high-growth areas, which could influence market dynamics.

## Visualizations

Three Tableau dashboards were created from the scraped data:
1. **Broker Performance Dashboard**: Visualizes the performance of top brokers in Florida.
2. **Real Estate Market Overview**: Analyzes the price distribution, property types, and geographic listing trends.
3. **Property Features Dashboard**: Focuses on property attributes like bedrooms, bathrooms, area, and average price per square foot.

## [Dashboards](https://public.tableau.com/views/Realtor_Real_Estate_Data_Anlyasis/Overviewdashoboard?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

### Dashboard 1:

![Real Estate Market Overview](https://github.com/ahmedtanvir47/RealEstate_Florida/blob/main/dashboard/Overview%20dashoboard.png)

### Dashboard 2:

![Broker Performance Dashboard](https://github.com/ahmedtanvir47/RealEstate_Florida/blob/main/dashboard/Broker%20dashboard.png)

### Dashboard 3:

![Property Features Dashboard](https://github.com/ahmedtanvir47/RealEstate_Florida/blob/main/dashboard/Property%20Dashboard.png)

## Technology Used

- **Web Scraping**: Selenium and Undetected Chromedriver for Python.
- **Data Analysis**: Python (Pandas) for cleaning and structuring the scraped data.
- **Data Visualization**: Tableau for creating dashboards.
- **GitHub**: Used to store and version-control the project.

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/ahmedtanvir47/RealEstate_Florida/.git
   ```

This project is done using Python 3.12.5. Please install the latest version of Python before running the project.

2. Intialize and activate virtual environment
```bash
virtualenv  venv
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```


4. Run the scraper scripts
```bash
python scraper.py
```

5. Run all the cells in the data transformation notebook in google colab or download the [notebook](.notebook/notebook.ipynb) and run it in Jupyter.

6. You will get a file named `property_cleaned.csv` as final data.

7. Open the `SJR Journal Ranking Analysis.twb` file in Tableau (or open the public tableau [link][dashboard-url]) and connect the `combined_journal_ranking_data.csv` file to the workbook.

## Conclusion
This project provides valuable insights into the Florida real estate market. By analyzing broker performance, property prices, and geographic trends, stakeholders can make better decisions in the real estate landscape.


