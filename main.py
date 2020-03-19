import pandas as pd

allData = pd.read_csv('D:\\DeeplyLearning\\Github\\COVID-19\\csse_covid_19_data\\csse_covid_19_time_series\\time_series_19-covid-Confirmed.csv')
allData = allData.groupby(['Country/Region']).sum()
allData = allData.drop(columns=['Lat', 'Long'])
pd.options.display.max_rows
pd.set_option('display.max_rows', None)
print(allData)
allData.to_csv('timeseriesGlobalSum.csv')