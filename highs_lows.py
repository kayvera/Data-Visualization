import csv
from  datetime import datetime

from matplotlib import pyplot as plt

# Get dates and high temperatures from file
filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	
	dates, highs = [], []
	for row in reader:
		current_date = datetime.strptime(row[0], "%Y-%m-%d")
		dates.append(current_date)
		
		high = int(row[1])
		highs.append(high)
		
	print(highs)

# Plot data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red')

# Format plot
plt.title("Daily high temperatures, July 2014", fontsize =24)
fig.autofmt_xdate()
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()	
	
#	for index, column_header in enumerate(header_row):
#		print(index, column_header)
