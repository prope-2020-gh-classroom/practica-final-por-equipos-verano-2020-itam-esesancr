# Adoption of technological tools by doctors in Mexico to provide health services to patients

- **Project documentation**
- **Project start date:** July 14th 2020
- **Project delivery date:** Sunday July 19th 2020



---

---

## Participants

|        Name        |     Role      |   GitHub   | Mail                  |
| :----------------: | :-----------: | :--------: | :-------------------- |
|    Cecy Aviles     |   Developer   |   cecyar   | cecyar@gmail.com      |
| José Roberto Pérez | Developer/PMO | Roberto919 | robertosysm@gmail.com |
|   Sergio Sánchez   |   Developer   |  esesancr  | esesancr@gmail.com    |
|   Erik Palacios    |   Reviewer    | palmoreck  | -                     |



---

---

## Project objective

**Analyze Mexican's doctors propensity to utilize technological tools to enhance their heath services by developing three subprojects to approach this objective from different angles**

---

## Subproject a

`<Pegar aquí docuementación!!!>`

---

##Subproject b

`<Pegar aquí docuementación!!!>`

---

##Subproject c

- Main contributor: Roberto Pérez
  - GitHub: Roberto919 
  - mail: robertosysm@gmail.com



### Subproject objective

Analyze the whether the results obtained from two distinct survey responses are independent using a statistical hypothesis test. The analysis should encompass the following tests:

- **Test for independence 1**
  - Variable 1: doctors' expected use regularity of the platform
  - Variable 2: doctors' perception about their patients interest to take virtual medical sessions
- **Test for independence 2**
  - Variable 1: doctors' perception about the future of telemedicine
  - Variable 2: doctors' willingness to pay for a telemedicine platform
- **Test for independence 1**
  - Variable 1: doctors' perception about their patients interest to take virtual medical sessions
  - Variable 2: doctors' willingness to pay for a telemedicine platform



###Methodology

The Chi-square test for independence (or Pearson's chi-square test) was used to determine if there is dependence between two selected sets of data.

This project was developed in Python, mainly using the tools *[scipy.stats.chi2_contingency](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chi2_contingency.html)* and [scipy.stats.chisquare](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.chisquare.html?highlight=stats chisquare#scipy.stats.chisquare) tools included in the *[SciPy](https://www.scipy.org/)* library.

For all the tests conducted the hypothesis evaluated were defined as follows:

- $$H_0: \text{the two variables are independent}$$
- $$H_1: \text{the two variables are dependent}$$

A comparison between alpha ($\alpha$) and the p-value was used to reject or approve the null hypothesis ($H_0$).



###Results

Before the results were obtained, we expected for all the proposed tests to yield a result in which the the null hypothesis ($H_0$) is rejected. This is because essentially all the variables tested come from the same survey, thus it is logical to think that the variables' behavior would be consistent.

As expected, the for all three tests the p-value obtained is lower than the alpha ($\alpha$), thus indicating a dependence among the variables compared.



###Sources

1. [Shinichi Okada - Gentle Introduction to Chi-Square Test for Independence](https://towardsdatascience.com/gentle-introduction-to-chi-square-test-for-independence-7182a7414a95)

2. [Minitab 18 - ¿Qué es una prueba de chi-cuadrada?](https://support.minitab.com/es-mx/minitab/18/help-and-how-to/statistics/tables/supporting-topics/chi-square/what-is-a-chi-square-test/)

3. [Lisa Sullivan, PhD - Hypothesis Testing - Chi Squared Test](https://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_HypothesisTesting-ChiSquare/BS704_HypothesisTesting-ChiSquare_print.html)



###Subproject Files

1. *Sp_c_nb.ipynb* --> Notebook where the whole project was developed.
2. *Sp_c_params.py* --> File with parameters required for the execution of the *Sp_c_nb.ipynb* file.
3. *Sp_c_nb.ipynb* --> File with functions utilized in the *Sp_c_nb.ipynb* file.



---

*End of document*

---