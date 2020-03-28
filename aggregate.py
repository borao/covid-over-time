import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def get_county_data(state, county):
    df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv", index_col=0, parse_dates=True)
    df = df[(df['state'] == state) & (df['county'] == county)]
    assert df.index.is_monotonic_increasing
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel("Date")
    ax.set_ylabel("Cases")
    fig.suptitle(str(county + " County, " + state + " - Coronavirus Cases"))
    ax.plot(df.index, df.cases)
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    return fig