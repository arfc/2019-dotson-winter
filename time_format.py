import pandas as pd 
from pandas import read_csv
from matplotlib import pyplot as plt 

path = "./data/"

# Read in the data
df = read_csv(path+'solardata.csv')

# converts to datetime index 
df['time'] = pd.to_datetime(df['time'])
# sorts by date
df = df.sort_values(by=['time'])

# groups by year
grouped = df.groupby([df['time'].dt.year])

years = grouped.groups.keys()
print(years)

# output by years
# for year in years:
# 	outfile = "solardata_"+str(year)+".csv"
# 	outdata = grouped.get_group(year)
	# plt.plot(outdata['time'], outdata['measured'])
	# plt.show()
# 	outdata.to_csv(outfile, index=False)


# convert timestamp to minutes
year_minutes = lambda x: (x.month-1)*43800  + (x.day-1)*1440 + (x.hour)*60 + x.minute
month_minutes = lambda x: (x.day-1)*1440 + (x.hour)*60 + x.minute
# for year in years:
# 	outfile = path+"solardata_minutes_"+str(year)+".csv"
# 	outdata = grouped.get_group(year)
	# outdata['time'] = outdata['time'].apply(year_minutes)
# 	outdata.to_csv(outfile, index=False)


# Step 1: group by year
# Step 2: group by month
# loop over years
# for year in years:
# 	# gets the yearly data
# 	yearly = grouped.get_group(year)
# 	# regroups by month
# 	monthly = yearly.groupby(yearly['time'].dt.month)
# 	# get the list of months
# 	months = monthly.groups.keys()
# 	# loops over months
# 	for month in months:
# 		outfile = path+"solardata_minutes_" + str(month) + "_" + str(year)+".csv"
# 		outdata = monthly.get_group(month)
# 		outdata['time'] = outdata['time'].apply(month_minutes)
# 		outdata.to_csv(outfile, index=False)

# # months to minutes
# for year in years:
# 	# gets the yearly data
# 	yearly = grouped.get_group(year)
# 	# regroups by month
# 	monthly = yearly.groupby(yearly['time'].dt.month)
# 	# get the list of months
# 	months = monthly.groups.keys()
# 	# print(months)
# 	# loops over months
# 	for month in months:
# 		# print(month)
# 		outfile = path+"solardata_minutes_" + str(month) + "_" + str(year)+".csv"
# 		outdata = monthly.get_group(month)
# 		outdata['time'] = outdata['time'].apply(month_minutes)
# 		# outdata.to_csv(outfile, index=False)


# make headfiles for each group of months
head_file = {'year':[], 'month':[], 'filename':[]}
metadata = pd.DataFrame(head_file)



