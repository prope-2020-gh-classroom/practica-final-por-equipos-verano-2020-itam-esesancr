## SUBPROJECT C - FUNCTIONS FILE
#### Author: Rob (GitHub: Roberto919)
#### Date: 16 July 2020





'--------------------------------------------------------------------------------'
#############
## Imports ##
#############


## Ancillary modules
from Sp_c_params import *





'--------------------------------------------------------------------------------'
###############
## Functions ##
###############


## Cleaning newly imported dataframe
def cleaning_df(df):
    """
    Cleaning newly imported dataframe
        args:
            df (dataframe): newly imported dataframe
        returns:
            df (dataframe): cleaned dataframe
    """

    ## Eliminating non relevant columns
    df.drop([nr for nr in df.columns if nr not in rc], axis=1, inplace=True)

    ## Assigning short columns names to relevant columns
    df.rename(rc, axis=1, inplace=True)

    ## Cleaning 'dirty' entries in 'Considera_tele' column
    df['Considera_tele'] = df['Considera_tele'].apply(lambda x: 'NO' if x.strip() == 'No' else x)

    ## Eliminating spaces in 'Pagar_cuanto' column
    df['Pagar_cuanto'] = df['Pagar_cuanto'].apply(lambda x: x.strip())
