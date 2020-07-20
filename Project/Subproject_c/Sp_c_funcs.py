## SUBPROJECT C - FUNCTIONS FILE
#### Author: Rob (GitHub: Roberto919)
#### Date: 16 July 2020





'--------------------------------------------------------------------------------'
#############
## Imports ##
#############


## Python libraries
import pandas as pd
import matplotlib.pyplot as plt


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



## Creating variables count crossing table
def vars_cross_df(df, ct_col, rc):
    """
    Creating variables count crossing table
        args:
            df (dataframe): dataframe that contains columns that will be crossed
            ct_col (list): list of one element with the name of the column that will serve as a reference to count crossings
            rc (list): list of columns that will be crossed
        returns:
            dfx (dataframe): resulting crossed table
    """

    dfx = df.copy()

    ## Creating crossing table
    dfx = dfx.loc[:, rc + ct_col].groupby(rc).count().unstack()
    dfx.columns = dfx.columns.droplevel()
    dfx.fillna(value=0, inplace=True)

    return dfx



## Creating bar graph of selected variable
def one_bar_graph(df, ct_var, bar_var, color):
    """
    Creating bar graph of selected variable
        args:
            df (dataframe): dataframe that contains column that will be plotted
            ct_var (list): list of one element with the name of the column that will serve as a reference to count entries
            bar_var (list): list of one element with the name of the column that will be graphed
            color (string): colour of graph
        returns:
            -
    """

    ## Create dictionary with counted values for graph
    dicv = df.loc[:, ct_var + bar_var].groupby(bar_var).count().to_dict('index')

    ## Creating and printing plot
    fig, ax = plt.subplots()

    plt.bar(
        dicv.keys(),
        [val[ct_var[0]] for val in dicv.values()],
        color=color
    )

    fig.set_size_inches(12, 5)

    plt.title(bar_var[0])

    plt.show()


    return



## Creating data count summary for a variable
def var_count_summary(df, ct_var, rc):
    """
    Creating data count summary for a variable
        args:
            ct_var (list): list of one element with the name of the column that will serve as a reference to count entries
            rc (list): list of one element with the name of the column that will be summarized
        returns:
            -
    """

    ## Creating count summary table
    dfx1 = df.loc[:, ct_var + rc].groupby(rc).count()
    id_sum = dfx1[ct_var[0]].sum()
    dfx1['Prop'] = dfx1[ct_var[0]].apply(lambda x: x/id_sum)

    ## Printing result
    print(dfx1)


    return
