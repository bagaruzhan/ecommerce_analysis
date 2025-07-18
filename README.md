# E-Commerce Sales Analysis 🇧🇷

This project analyzes Brazilian eCommerce data using Python, SQLite, and data visualization libraries (Matplotlib & Seaborn).  
The analysis includes sales trends, revenue, top categories, payment methods, shipping, customer geography, delivery time, and profit margin.

## Dataset

- **Source**: [Kaggle – Target Dataset by Devaraj V88](https://www.kaggle.com/datasets/devarajv88/target-dataset)
- **Files include**: `customers.csv`, `orders.csv`, `order_items.csv`, `products.csv`, `sellers.csv`, `payments.csv`, `geolocation.csv`

## Note about data files

The dataset is **not included in this repository** due to its large size.

To run the notebook successfully, please download the original data files and place them in the `data/` directory.

You can request the dataset by contacting me directly or download it from the link above.

## Key Insights

- Over 96% of orders were successfully delivered.
- Peak sales occurred between **Nov 2017 – Apr 2018**.
- Highest-grossing product category: *Bed, Table, and Bath*.
- **Credit card** is the most used payment method.
- **São Paulo** has the highest number of customers.
- Average freight cost: **$19.99**
- Delivery time varies widely, from **18 to 29 days**.
- Some products have extreme profit margins (up to **6500%**).

## Project Files

- `ecommerce_analysis.ipynb` – full analysis notebook.
- `requirements.txt` – Python libraries used.
- `.gitignore` – to exclude unnecessary files (like large CSVs).
- *(CSV data files are not included – see above note.)*

## Tools & Technologies

- **Python**
- **Pandas**, **NumPy**
- **Matplotlib**, **Seaborn**
- **SQLite** (via `sqlite3` module)
- **Jupyter Notebook**

