import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns

conn = sqlite3.connect('../../data/database/PPP.db')
c = conn.cursor()

# SQL query to extract city-wise total loan amount
sql_query = """
SELECT Addresses.City, SUM(Loans.LoanAmount) as TotalLoan
FROM Loans
JOIN Addresses ON Loans.AddressID = Addresses.ID
GROUP BY Addresses.City
ORDER BY TotalLoan DESC
"""

city_loan_df = pd.read_sql_query(sql_query, conn)

conn.close()

top_cities = city_loan_df.head(10)

plt.figure(figsize=(12, 8))
colors = sns.color_palette('viridis', len(top_cities))
bars = plt.barh(top_cities['City'][::-1], top_cities['TotalLoan'][::-1], color=colors)
plt.xlabel('Total Loan Amount (in millions)', fontsize=14)
plt.ylabel('City', fontsize=14)
plt.title('Top 10 Cities by Total PPP Loan Amount', fontsize=16)

formatter = ticker.FuncFormatter(lambda x, pos: f'{x / 1e6:.0f}M')
plt.gca().xaxis.set_major_formatter(formatter)

plt.xlim(0, top_cities['TotalLoan'].max() * 1.2)

plt.grid(axis='x')

plt.tick_params(axis='both', which='major', labelsize=12)

for bar in bars:
    width = bar.get_width()
    plt.text(width * 1.01, bar.get_y() + bar.get_height() / 2, f'{width / 1e6:.0f}M', ha='left', va='center')

plt.annotate('Honolulu received the highest loan amount',
             xy=(top_cities['TotalLoan'].max(), 9),
             xycoords='data',
             xytext=(-200, -50),
             textcoords='offset points',
             arrowprops=dict(arrowstyle="->",
                             connectionstyle="arc3,rad=.2"))

plt.show()
