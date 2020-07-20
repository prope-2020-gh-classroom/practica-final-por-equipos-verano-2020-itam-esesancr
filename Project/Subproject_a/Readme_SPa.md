# Subproject a
---
- Main contributor: Sergio Sánchez Reyes
 - GitHub: esesancr
 - mail: esesancr@gmail.com


## Subproject objective

Try to identify if there is already a relationship between doctor's age and his/her perception about the attractiveness of telemedicine. The analysis includes the following sub-analysis:

- Linear Regression that correlates doctor's age and their Negative perception about the attractiveness of telemedicine (Negative Perception)
- Linear Regression that correlates doctor's age and their Positive perception about the attractiveness of telemedicine (Positive Perception)


## Methodology

### Linear Regression Model

Recalling what was seen in class, Linear regression attempts to model the relationship between two variables by fitting a linear equation to observed data. 

In our case **the explanatory variable is the doctor's age**, and the **dependent variable is the Negative or Positive perception about the attractiveness of telemedicine**

Due we don't expect a regression line that must pass through the origin we opted for the **regression model with intercept**

$$f(x|\beta) = \beta_0 + \beta_1 x$$ $$(x_i,y_i)\forall i=0,1,\dots,m$$

where $\phi_0(x) = 1$, $\phi_1(x) =x$. And we need to calculate: $\beta_0, \beta_1$.

#### Negative Perception

For the linear regression of the negative perception we performed the following calculations:

$$f(x|\beta) = \beta_0 + \beta_1 x$$

$$p_{np}(x) = 0.00432852x + 0.28488185$$

With our beta's adjusted as $\hat{\beta_0} = 0.28488185$, $\hat{\beta_1} = 0.00432852$.

<p align="centered">
<img src="http://drive.google.com/uc?export=view&id=1I3GCglV21L3zzmmWKfi03IDiX7fzm6N0" alt="a" heigth="700" width="800">
</p>

#### Positive Perception

For the linear regression of the positive perception we performed the following calculations:

$$f(x|\beta) = \beta_0 + \beta_1 x$$

$$p_{np}(x) = -0.0031727x + 0.68710041$$

With our beta's adjusted as $\hat{\beta_0} = 0.68710041$, $\hat{\beta_1} = -0.0031727$.

<p align="centered">
<img src="http://drive.google.com/uc?export=view&id=1GVMRR8B_iSd-t826r9YRwqKYD-N_H1QZ" alt="a" heigth="700" width="800">
</p>

## Results

As we could see in both analyzes, we corroborated that already exists a relationship between doctor's age and their willingness to offer telemedicine services and we concluded that **as doctors get older, they are less willing to offer telemedicine medical assistance services.**


## Sources
---
1. [Linear_Regression. Yale](http://www.stat.yale.edu/Courses/1997-98/101/linreg.htm)
2. [Mínimos Cuadrados. ITAM](https://github.com/esesancr/Propedeutico/blob/master/Python/clases/3_algebra_lineal/3_minimos_cuadrados.ipynb)
3. J. Kiusalas Numerical Methods in Engineering with Python 3
4. Fabio Nelli - Python Data Analytics with Pandas, NumPy and Matplotlib [2nd ed.]

## Subproject Files
---
- Sp_a_nb.ipynb --> Notebook where the whole project was developed.
- Sp_a_params.py --> File with parameters required for the execution of the Sp_a_nb.ipynb file.
- Sp_a_nb.ipynb --> File with functions utilized in the Sp_a_nb.ipynb file.

