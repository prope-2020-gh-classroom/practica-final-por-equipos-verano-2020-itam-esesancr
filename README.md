# Adoption of technological tools to provide health services to patients by doctors in México 

- **Project documentation**
- **Project start date:** July 14th 2020
- **Project delivery date:** Sunday July 19th 2020

---

## Participants

|        Name        |     Role      |   GitHub   | Mail                  |
| :----------------: | :-----------: | :--------: | :-------------------- |
| José Roberto Pérez | Developer/PMO | Roberto919 | robertosysm@gmail.com |
|   Cecilia Avilés   |   Developer   |   cecyar   | cecyar@gmail.com      |
|   Sergio Sánchez   |   Developer   |  esesancr  | esesancr@gmail.com    |
|   Erik Palacios    |   Reviewer    | palmoreck  | -                     |

---

## Project objective

**To analyze Mexican doctors' disposition to use technological tools that could enhance their health services by developing three subprojects in order to approach the goal from different angles.**

---

## Subproject A

- Main contributor: Sergio Sánchez Reyes
  - GitHub: esesancr
  - mail: esesancr@gmail.com



### Subproject objective

Try to identify if there is already a relationship between doctor's age and his/her perception about the attractiveness of telemedicine. The analysis includes the following sub-analysis:

- Linear Regression that correlates doctor's age and their Negative perception about the attractiveness of telemedicine (Negative Perception)
- Linear Regression that correlates doctor's age and their Positive perception about the attractiveness of telemedicine (Positive Perception)



### Methodology

#### Linear Regression Model

Recalling what was seen in class, Linear regression attempts to model the relationship between two variables by fitting a linear equation to observed data. 

In our case **the explanatory variable is the doctor's age**, and the **dependent variable is the Negative or Positive perception about the attractiveness of telemedicine**

Since we don't expect a regression line that must pass through the origin we opted for the **regression model with intercept**

$$f(x|\beta) = \beta_0 + \beta_1 x$$ $$(x_i,y_i)\forall i=0,1,\dots,m$$

where $\phi_0(x) = 1$, $\phi_1(x) =x$. And we need to calculate: $\beta_0, \beta_1$.

##### Negative Perception

For the linear regression of the negative perception we performed the following calculations:

$$f(x|\beta) = \beta_0 + \beta_1 x$$

$$p_{np}(x) = 0.00432852x + 0.28488185$$

With our beta's adjusted as $\hat{\beta_0} = 0.28488185$, $\hat{\beta_1} = 0.00432852$.

<p align="centered">
<img src="http://drive.google.com/uc?export=view&id=1I3GCglV21L3zzmmWKfi03IDiX7fzm6N0" alt="a" heigth="700" width="800">
</p>

##### Positive Perception

For the linear regression of the positive perception we performed the following calculations:

$$f(x|\beta) = \beta_0 + \beta_1 x$$

$$p_{np}(x) = -0.0031727x + 0.68710041$$

With our beta's adjusted as $\hat{\beta_0} = 0.68710041$, $\hat{\beta_1} = -0.0031727$.

<p align="centered">
<img src="http://drive.google.com/uc?export=view&id=1GVMRR8B_iSd-t826r9YRwqKYD-N_H1QZ" alt="a" heigth="700" width="800">
</p>



### Results

As we could see in both analyses, we corroborated that a relationship already exists between doctor's age and their willingness to offer telemedicine services and we concluded that **as doctors get older, they are less willing to offer telemedicine medical assistance services.**


### Sources

1. [Linear_Regression. Yale](http://www.stat.yale.edu/Courses/1997-98/101/linreg.htm)
2. [Mínimos Cuadrados. ITAM](https://github.com/esesancr/Propedeutico/blob/master/Python/clases/3_algebra_lineal/3_minimos_cuadrados.ipynb)
3. J. Kiusalas Numerical Methods in Engineering with Python 3
4. Fabio Nelli - Python Data Analytics with Pandas, NumPy and Matplotlib [2nd ed.]

### Subproject Files

- *Sp_a_nb.ipynb*   -->  Notebook where the whole project was developed.
- *Sp_a_params.py*  -->  File with parameters required for the execution of the Sp_a_nb.ipynb file.
- *Sp_a_nb.ipynb*   -->  File with functions used in the Sp_a_nb.ipynb file.


---

## Subproject B

- Main contributor: Cecilia Avilés Robles
  - GitHub: cecyar 
  - mail: cecyar@gmail.com



### Subproject objective

Analyze what are the attributes that doctors value the most in a technological platform that could enhance their services. This should be accomplished by examining the answers given to the question _"Seleccione las funcionalidades que considera importantes para que estén presentes en una plataforma digital que lo apoye con la gestión de sus servicios médicos."_

This analysis must consider the following two conditions:

- **Default answers**: Pre-written answers given to choose from (either 1 to all).
- **Free text**: In case the subject did not want to select a default answer, he/she was given the option to write his/her own.



### Methodology

Text input had to be analyzed for this subproject, which means working with strings mainly. 

For this matter, the libraries [Pandas](https://pandas.pydata.org/) and [NLTK](https://www.nltk.org/) were used in order to handle the information in dataframes and work with human language data.

The condition in which a default answer was selected was mainly analyzed with [Pandas](https://pandas.pydata.org/), and the condition for free text was examined with [NLTK](https://www.nltk.org/).



### Results

Our sample size consisted of _765_ answers given by _765_ doctors. 

An _82%_ selected one of the default answers. The top three default answers chosen were:
- Creación automática de videoconferencias con clientes (536 times).
- Administración de citas (379 times).
- Envío y recepción de documentos con cliente (363 times).

A _13%_ choose not to select a default answer, opting to write their own instead. From this: 
- The most common given answer was negative towards the digital platform, representing roughly the _10%_ of the total sample. 
- Almost the _1.5%_ value attributes of either _quality_ or _information_ on the hypothetical digital platform. 
- The rest of the written answers do not provide any significant information due to very low sample size and no specific trend observed.



### Sources

1. [Text Mining in Python](https://medium.com/towards-artificial-intelligence/text-mining-in-python-steps-and-examples-78b3f8fd913b)
2. [Text Analytics for Beginners using NLTK](https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk)
3. [The Python Graph Gallery](https://python-graph-gallery.com/)



### Subproject Files

1. *Sp_b_nb.ipynb*  -->  JupyterLab notebook where the subproject was developed.

---

## Subproject C

- Main contributor: Roberto Pérez
  - GitHub: Roberto919 
  - mail: robertosysm@gmail.com



### Subproject objective

Analyze whether the results obtained from two distinct survey responses are independent using a statistical hypothesis test. The analysis should encompass the following tests:

- **Test for independence 1**
  - Variable 1: doctors' expected regularity use of the platform
  - Variable 2: doctors' perception about their patients interest to take virtual medical sessions
- **Test for independence 2**
  - Variable 1: doctors' perception about the future of telemedicine
  - Variable 2: doctors' willingness to pay for a telemedicine platform
- **Test for independence 1**
  - Variable 1: doctors' perception about their patients interest to take virtual medical sessions
  - Variable 2: doctors' willingness to pay for a telemedicine platform



### Methodology

The Chi-square test for independence (or Pearson's chi-square test) was used to determine if there is dependence between two selected sets of data.

This project was developed in Python, mainly using the tools [scipy.stats.chi2_contingency](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html) and [scipy.stats.chisquare](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html?highlight=stats%20chisquare#scipy.stats.chisquare) tools included in the [SciPy](https://www.scipy.org/) library.

For all the tests conducted the hypotheses evaluated were defined as follows:

- $$H_0: \text{the two variables are independent}$$
- $$H_1: \text{the two variables are dependent}$$

A comparison between alpha ($\alpha$) and the p-value was used to reject or approve the null hypothesis ($H_0$).



### Results

Before the results were obtained, we expected for all the proposed tests to yield a result in which the null hypothesis ($H_0$) is rejected. This is because essentially all the variables tested come from the same survey, thus it is logical to think that the variables' behavior would be consistent.

As expected, for all three tests the p-value obtained is lower than the alpha ($\alpha$), thus indicating a dependence among the variables compared.



### Sources

1. [Shinichi Okada - Gentle Introduction to Chi-Square Test for Independence](https://towardsdatascience.com/gentle-introduction-to-chi-square-test-for-independence-7182a7414a95)
2. [Minitab 18 - ¿Qué es una prueba de chi-cuadrada?](https://support.minitab.com/es-mx/minitab/18/help-and-how-to/statistics/tables/supporting-topics/chi-square/what-is-a-chi-square-test/)
3. [Lisa Sullivan, PhD - Hypothesis Testing - Chi Squared Test](https://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_HypothesisTesting-ChiSquare/BS704_HypothesisTesting-ChiSquare_print.html)



### Subproject Files

1. *Sp_c_nb.ipynb*   -->  Notebook where the whole project was developed.
2. *Sp_c_params.py*  -->  File with parameters required for the execution of the *Sp_c_nb.ipynb* file.
3. *Sp_c_nb.ipynb*   -->  File with functions used in the *Sp_c_nb.ipynb* file.



---

*End of document*

---
