import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

#Scraping MN Department of health website's Testing data table
r = requests.get("https://www.health.state.mn.us/diseases/coronavirus/situation.html#testing1")
soup = BeautifulSoup(r.text, "html.parser")
table = soup.find("table", {"id":"labtable"})
rows = table.find_all("tr")
col_headers = table.find_all("th")

#Write table to csv file
with open('MN_Covid_Testing.csv', 'w') as f:
    writer = csv.writer(f)
    current_row = [header.text for header in col_headers]
    writer.writerow(current_row)
    for row in rows:
        cells = row.find_all("td")
        if len(cells) > 0:
            #replacing commas to keep structure of csv file
            current_row = [cells[i].text.replace(',','') for i in range(0, len(cells))]
            writer.writerow(current_row)

#Store csv into Pandas df and store each column in a separate array
df = pd.read_csv("MN_Covid_Testing.csv", parse_dates=['Date reported to MDH'])
x = df[df.columns[0]]
y1_temp = df[df.columns[3]]
y2_temp = df[df.columns[2]]
y3_temp = df[df.columns[1]]
x = x[:len(x):2]
y1 = y1_temp[:len(y1_temp):2]
y2 = y2_temp[:len(y2_temp):2]
y3 = y3_temp[:len(y3_temp):2]

#Replicate Testing Graph shown above table
fig, (ax1, ax2) = plt.subplots(2,1, figsize=(10,5))

#Add main subplot and hide frame and ticks, so that the y-axis has a central label
fig.add_subplot(111, frameon=False)
plt.tick_params(labelcolor='none', top=False, bottom=False, left=False, right=False)
fig.suptitle("Coronavirus Testing MN")
plt.xlabel('Date reported to MDH')
plt.ylabel('Approximate Number of Completed Tests', labelpad=40)

#Line graph of Total Cases
ax1.plot(x, y1)

#Stacked bar graph of individual cases
ax2.bar(x, y2, width = 1.0, label = 'Completed tests external labs (daily)', color = 'm')
ax2.bar(x, y3, width = 1.0, label = 'Completed tests MDH (daily)', color = 'indigo')
ax2.legend(loc = "upper left", fontsize = 7)
ax1.fill_between(x[len(x)-5:len(x)], y1[len(x)-5:len(x)], alpha = 0.5, color='grey', transform=ax1.get_xaxis_transform())
ax2.fill_between(x[len(x)-5:len(x)], y2[len(x)-5:len(x)], alpha = 0.5, color='grey', transform=ax2.get_xaxis_transform())

#Adjusing tick alignment and format to match graph on website
ax1.set_xticklabels(x,rotation=90, fontsize=5)
ax2.set_xticklabels(x,rotation=90, fontsize=5)
ax1.yaxis.set_major_formatter(mticker.ScalarFormatter())
ax1.yaxis.get_major_formatter().set_scientific(False)
ax2.yaxis.set_major_formatter(mticker.ScalarFormatter())
ax2.yaxis.get_major_formatter().set_scientific(False)
ax1.get_yaxis().set_major_formatter(mticker.FuncFormatter(lambda x, p: format(int(x), ',')))
ax2.get_yaxis().set_major_formatter(mticker.FuncFormatter(lambda x, p: format(int(x), ',')))

#Setting spacing of major ticks
major_ticks_1 = np.arange(0, 2000000, 200000)
major_ticks_2 = np.arange(0, 50000, 10000)
ax1.set_yticks(major_ticks_1)
ax2.set_yticks(major_ticks_2)

#Adding horizontal grid lines to major ticks
ax1.grid(axis = 'y', which='major')
ax2.grid(axis = 'y', which='major')

plt.tight_layout(pad=0.5)
plt.show()
