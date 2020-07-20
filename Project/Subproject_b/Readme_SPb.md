# Subproject B

- Main contributor: Cecilia Avilés Robles
  - GitHub: cecyar 
  - mail: cecyar@gmail.com



## Subproject objective

Analyze what are the attributes that doctors value the most in a technological platform that could enhance their services. This should be accomplished by examining the answers given to the question "Seleccione las funcionalidades que considera importantes para que estén presentes en una plataforma digital que lo apoye con la gestión de sus servicios médicos."

This analysis must consider the following two conditions:

- **Default answers**: Pre-written answers given to choose from (either 1 to all).
- **Free text**: In case the subject did not want to select a default answer, he/she was given the option to write his/her own.



## Methodology

Text input had to be analyzed for this subproject, which means working with strings mainly. 

For this matter, the libraries [Pandas](https://pandas.pydata.org/) and [NLTK](https://www.nltk.org/) were used in order to handle the information in dataframes and work with human language data.

The condition in which a default answer was selected was mainly analyzed with Pandas, and the condition for free text was examined with NLTK.



## Results

Our sample size consisted of $765$ answers given by 765 doctors. 

An $82$% selected one of the default answers. The top three default answers chosen were:
- Creación automática de videoconferencias con clientes (536 times).
- Administración de citas (379 times).
- Envío y recepción de documentos con cliente (363 times).

A $13$% choose not to select a default answer, opting to write their own instead. From this: 
- The most common given answer was negative towards the digital platform, representing roughly the $10$% of the total sample. 
- Almost the $1.5$% value attributes of either _quality_ or _information_ on the hypothetical digital platform. 
- The rest of the written answers do not provide any significant information due to very low sample size and no specific trend observed.



## Sources

1. [Text Mining in Python](https://medium.com/towards-artificial-intelligence/text-mining-in-python-steps-and-examples-78b3f8fd913b)

2. [Text Analytics for Beginners using NLTK](https://www.datacamp.com/community/tutorials/text-analytics-beginners-nltk)

3. [The Python Graph Gallery](https://python-graph-gallery.com/)



## Subproject Files

1. *Sp_b_nb.ipynb* --> JupyterLab notebook where the subproject was developed.





