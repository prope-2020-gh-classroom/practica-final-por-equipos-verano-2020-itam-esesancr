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

## Libraries needed
import datetime

import matplotlib.pyplot as plt

from matplotlib.pyplot import figure

import numpy as np


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


## Function that corrects the parsing of wrong years.
def fix_date(x):
    """
    Function that corrects the parsing of wrong years.
        args:
            x (dataframe): newly imported dataframe
        returns:
            x (dataframe): corrected dataframe
    """
     
    #If converted birthday year is later than 2002 we substract 100 years.
    if x.year > 2002:
        year = x.year - 100
    else:
        year = x.year

    return datetime.date(year,x.month,x.day)


## Function that calculates doctor's age.
def compute_age(x):
    """
    Function that calculates doctor's age based on date of birth 
        args:
            x (dataframe): newly imported dataframe
        returns:
            age (dataframe): dataframe containing doctor's age
    """
        
    age=2020-x.year

    return age


## Function that plots the histogram of a dataframe
def plot_hist(df,df_col,bins):
    """
    Function that plots the histogram of a dataframe based on a speciffic col name. 
        args:
            df (dataframe): source dataframe
            df_col (string): column name that will be plotted in the hist.
            bins (int): number of bins that will contain the histogram
        returns:
            histogram 
    """
    
    fig, ax = plt.subplots()
    fig.set_size_inches(12, 5)

    plt.hist(
        df[df_col],
        color='lightslategray',
        bins=bins
    )

    plt.title('Doctor\'s Age',fontsize=17,color='Navy')
    plt.xlabel('Age',color='Navy')
    plt.ylabel('Count',color='Navy')

    plt.grid(True)
    plt.legend(['Count of Doctor\'s per age'],loc=0)
    plt.show()
    
    
## Function that plots a line chart for a variable (var) grouped by a (group_var)
def plot_line_groupedby(df,var,group_var):
    """
    Function that plots the line char for a variable (var) grouped by a (group_var)
        args:
            df (dataframe): source dataframe
            var (string): name of the variable that will be grouped and plotted in the line chart.
            group_var (string): name of the variable that will group 'var'
        returns:
            line chart
    """
    
    fig, ax = plt.subplots()

    df.groupby([var,group_var]).count().unstack().plot(ax=ax)

    fig.set_size_inches(12, 5)

    plt.title('Doctor\'s Age',fontsize=17,color='Navy')
    plt.xlabel('Age',color='Navy')
    plt.ylabel('Count',color='Navy')

    plt.grid(True)
    plt.legend(['Negative Perception','Positive Perception'],loc=0)
    plt.show()
    

## Function that calculates and plots the Linear Regression with interception for vars x & y    
def linear_regression(x,y,ndegree,label): 
    """
    Function that calculates and plots the Linear Regression with interception for vars x & y
        args:
            x (NumPy array): Independent variable
            y (NumPy array): Dependant variable to be adjusted with the Linear Regression model.
            ndegree (int): Degree of the fitting polynomial
            label(string): Label to be shown in the legend plot
        returns:
            Plot of Linear Regression model with interception
    """

    coefficients = np.polyfit(x,y,ndegree)
    y_hat_numpy = coefficients[1] + coefficients[0] * x

    fig, ax = plt.subplots()

    plt.plot(x, y_hat_numpy, 'k-',
             x, y, 'ro')

    fig.set_size_inches(12, 5)

    plt.title('Linear Regression Model. Age vs Perception of telemedicine',fontsize=15,color='Navy')
    plt.xlabel('Age',color='Navy')
    plt.ylabel('Perception Rate',color='Navy')

    plt.grid(True)
    plt.legend([label,'Data'],loc=0)
    plt.show()