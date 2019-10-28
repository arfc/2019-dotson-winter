import pandas as pd 
from pandas import read_csv
from matplotlib import pyplot as plt 

path = "./inputfiles/solardata.csv"

# Read in the data
df = read_csv(path)

# converts to datetime index 
df['time'] = pd.to_datetime(df['time'])
# sorts by date
df = df.sort_values(by=['time'])

# groups by year
grouped = df.groupby([df['time'].dt.year])

years = (2015, 2016, 2017, 2018, 2019) # range of years

# output by years
# for year in years:
# 	outfile = "solardata_"+str(year)+".csv"
# 	outdata = grouped.get_group(year)
	# plt.plot(outdata['time'], outdata['measured'])
	# plt.show()
# 	outdata.to_csv(outfile, index=False)


# convert timestamp to minutes
func = lambda x: (x.month-1)*43800  + (x.day-1)*1440 + (x.hour)*60 + x.minute

for year in years:
	outfile = "solardata_minutes_"+str(year)+".csv"
	outdata = grouped.get_group(year)
	outdata['time'] = outdata['time'].apply(func)
	outdata.to_csv(outfile, index=False)


