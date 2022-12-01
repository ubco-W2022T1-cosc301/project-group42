import pandas as pd
import numpy as np

def load_and_process(url_or_path_to_csv_file):

    # Method Chain 1 (Load data and deal with missing data)

    df1 = (
        pd.read_csv(url_or_path_to_csv_file, skiprows =4)
        .drop(columns = ['Country Code','Indicator Name','Indicator Code', 
        '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968',
        '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', 
        '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
        '1987', '1988', '1989', 
        #remove below lines for 1990-2019 data
        '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998',
        '1999', '2000', '2001', '2002', '2003', '2004',
                         '2020', '2021', 'Unnamed: 66'],axis=1)
        .dropna().reset_index(drop=True)
        .reset_index(drop=True)
        
    )

    # Method Chain 2 (Create new columns, drop others, and do processing)

    N = df1['Country Name'] 
    df2 = (
        df1    
        .drop(columns=['Country Name'], axis=1)
        .set_index(N)
        .rename_axis('year', axis='columns')
        .swapaxes("index", "columns")
    )

    # Make sure to return the latest dataframe
    return df2 

