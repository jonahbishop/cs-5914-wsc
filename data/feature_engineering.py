import pandas as pd

def print_columns(df: pd.DataFrame):
    for column in df.columns:
        print(column)

def remove_columns(df: pd.DataFrame):
    df_div = df.filter(like="Div")
    removable = list(df_div.columns)
    df = df.drop(removable, axis=1)
    df = df.dropna(axis=1, how='all')
    removables = [
        'Year','Tail_Number', 'OriginAirportID',
        'OriginAirportSeqID','OriginCityMarketID','OriginCityName',
        'OriginState','OriginStateFips','OriginStateName','OriginWac', 
        'DestAirportID','DestAirportSeqID','DestCityMarketID',
        'DestCityName','DestState','DestStateFips','DestStateName',
        'DestWac','DepTime', 'DepDelayMinutes', 'DepDel15',
        'DepartureDelayGroups','DepTimeBlk','WheelsOff','WheelsOn',
        'CRSArrTime','ArrTime','ArrDelay','ArrDelayMinutes','ArrDel15',
        'ArrivalDelayGroups','ArrTimeBlk','Cancelled','CancellationCode',
        'Flights','CarrierDelay','WeatherDelay','NASDelay',
        'SecurityDelay','LateAircraftDelay','FirstDepTime',
        'TotalAddGTime','LongestAddGTime'
    ]
    for remove in removables:
        try:
            df = df.drop(remove, axis=1)
        except Exception as e:
            print(f'Already Removed {remove} or {e}')

    return df

def get_data_by_airport(df: pd.DataFrame, city: str) -> pd.DataFrame:
    return df[(df['Origin'].str.contains(city) == True)]

def one_hot_encode(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    try:
        dummy1 = pd.get_dummies(df[column_name])
        dummy1 = dummy1.add_prefix(f"{column_name} - ")
        df = pd.concat([df, dummy1], axis=1).drop(column_name, axis=1)
        df.head()
    except Exception as e:
        print(f"Error in one_hot_encode: {e}")
    return df

def join_by_date(df: pd.DataFrame, weather_df: pd.DataFrame, airport_name: str):
    tmp = df.loc[df['NAME'] == airport_name]
    tmp = tmp.drop(['NAME'], axis=1)
    weather_tmp = weather_df.loc[weather_df['NAME'] == airport_name]
    return pd.merge(tmp, weather_tmp, how='outer', on='DATE')

def create_weather_df() -> pd.DataFrame:
    weather_df = pd.read_csv('weather_data.csv')

    # replace names with airports
    names = {
        'LOS ANGELES INTERNATIONAL AIRPORT, CA US': 'LAX',
        'SEATTLE TACOMA AIRPORT, WA US': 'SEA',
        'ORLANDO INTERNATIONAL AIRPORT, FL US': 'MCO',
        'BUENA VENTURA LAKES 6.0 ENE, FL US': 'MCO',
        'DAL FTW WSCMO AIRPORT, TX US': 'DFW',
        'JFK INTERNATIONAL AIRPORT, NY US': 'JFK',
    }
    weather_df['NAME'] = [names[var] for var in weather_df['NAME']]

    # remove extraneous columns
    weather_removables = [
        'STATION','AWND_ATTRIBUTES','DAPR','DAPR_ATTRIBUTES','MDPR',
        'MDPR_ATTRIBUTES','PGTM', 'PGTM_ATTRIBUTES','TAVG_ATTRIBUTES',
        'TMAX_ATTRIBUTES','TMIN_ATTRIBUTES','WDF2_ATTRIBUTES','WDF5_ATTRIBUTES',
        'WSF2_ATTRIBUTES','WSF5_ATTRIBUTES','WT01','WT02','WT03','WT04','WT05',
        'WT05_ATTRIBUTES','WT06','WT06_ATTRIBUTES','WT07','WT07_ATTRIBUTES',
        'WT08','WT09','WT09_ATTRIBUTES' 
    ]
    for remove in weather_removables:
        try:
            weather_df = weather_df.drop(remove, axis=1)
        except Exception as e:
            print(f'Already Removed {remove} or {e}')

    # one hot encode weather columns
    weather_one_hot_columns = [
        'PRCP_ATTRIBUTES','SNOW_ATTRIBUTES','SNWD_ATTRIBUTES','WT01_ATTRIBUTES',
        'WT02_ATTRIBUTES','WT03_ATTRIBUTES','WT04_ATTRIBUTES','WT08_ATTRIBUTES'
    ]
    for col in weather_one_hot_columns:
        weather_df = one_hot_encode(weather_df, col)
    
    weather_df['DATE'] = pd.to_datetime(weather_df['DATE'])

    # drop any columns with missing values
    weather_df.fillna(0)

    return weather_df

def create_airline_df(file_name: str) -> pd.DataFrame:
    # read in the file
    df = pd.read_csv(f'airline data/all_2019/{file_name}.csv')
    df = remove_columns(df)

    # remove airports not in cites
    tmp_df = pd.DataFrame()
    for city in cities:
        tmp_df = tmp_df.append(get_data_by_airport(df, city))
    df = tmp_df

    # one hot encode several columns
    one_hot_columns = [
        'Reporting_Airline', 'IATA_CODE_Reporting_Airline', 'DOT_ID_Reporting_Airline', 'Dest'
    ]
    for col in one_hot_columns:
        df = one_hot_encode(df, col)

    # assign the label based on DepDelay column
    df['DepDelay'] = [0 if temp <= 0 else 1 for temp in df['DepDelay']]
    df['label'] = df['DepDelay']
    df = df.drop('DepDelay', axis=1)

    # rename the columns for matching with weather data
    df = df.rename(columns={'Origin':'NAME', 'FlightDate':'DATE'})
    
    # change date into datetime type
    df['DATE'] = pd.to_datetime(df['DATE'])

    # reset indices
    df = df.reset_index(drop=True)

    # drop any columns with missing values
    df = df.dropna(how='any')

    return df

if __name__ == '__main__':
    # get the weather data
    cities = ['JFK', 'DFW', 'MCO', 'LAX', 'SEA']
    weather_df = create_weather_df()

    # get the airline data
    file_names = [
        'jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec'
    ]
    for file_name in file_names:
        airport_df = create_airline_df(file_name)


        # join weather data with airline data
        cleaned_df = pd.DataFrame()
        for city in cities:
            cleaned_df = cleaned_df.append(join_by_date(airport_df, weather_df, city))
        cleaned_df = airport_df
        cleaned_df = cleaned_df.drop(['DATE'], axis=1)
        cleaned_df = one_hot_encode(cleaned_df, 'NAME')
        cleaned_df = cleaned_df.reset_index(drop=True)
        cleaned_df = cleaned_df.dropna(how='any')
        cleaned_df.to_csv('cleaned_airline_data/clean_merge_full.csv')
