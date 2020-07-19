## SUBPROJECT A - FUNCTIONS FILE
#### Author: Rob (GitHub: Roberto919)
#### Date: 17 July 2020
#### Modified by: Sergio (GitHub: esesancr)





'--------------------------------------------------------------------------------'
#############
## Imports ##
#############


## Ancillary modules
from Sp_a_params import *





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