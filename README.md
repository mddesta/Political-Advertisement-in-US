# Political Advertisement in US

## Background

Analysis of Political Ads on Facebook to determine trends. Built a machine learning tool that was able to differentiate between organic ads in the US and  those run by the Internet Research Agency (Russian troll farm).


## Technologies 

###### Languages:

* Python
* Javascript
* JSON

###### Data Cleaning:

* Pandas
* Jupyter Notebook
* Numpy
* glob

###### Machine Learning:

* Natural Language Tool Kit
* SKLearn

###### Visualization:

* Tableau
* Matplotlib
* Wordcloud

###### Web Development:

* HTML
* CSS
* Bootstrap
* JQuery
* Flask
* Heroku

###### Verision Control:

* Git
* Github

## Visualizations 

###### Findings 

![FB word cloud](https://github.com/mddesta/Political-Advertisement-in-US/blob/master/static/FB_Word_Cloud.png)


###### Foreign Influence 

Word cloud of ads run by the IRA
![IRA Word Cloud](https://github.com/mddesta/Political-Advertisement-in-US/blob/master/static/Russian_Ad_Word_Cloud.png)

Tableau map showing where the IRA targeted
![Tableau Mapping](https://github.com/mddesta/Political-Advertisement-in-US/blob/master/static/Tableau%20Maping.PNG)

###### Machine Learning  

![Ad Length](https://github.com/mddesta/Political-Advertisement-in-US/blob/master/NLP_ML/chart_adlength.png)

This chart shows that in general, the real Facebook ads were longer (had more words in each ad). This makes it easier for the machine learning model to identify the real ads from the fake ones presented by the Internet Research Agency (otherwise known as the “Russian troll farm”). 

![Punctuation](https://github.com/mddesta/Political-Advertisement-in-US/blob/master/NLP_ML/chart_punctuation.png)

This chart shows what percentage of each ad was made up of any of the following punctuation marks: !“#$%&\‘()*+,-./:;<=>?@[\\]^_`{|}~

![Confusion Matrix](https://github.com/mddesta/Political-Advertisement-in-US/blob/master/NLP_ML/confusion_matrix.png)

The confusion matrix visually represents the success of our model at distinguishing ‘fake’ (IRA-created) Facebook ads from real Facebook ads that were accessed through their API. The accuracy of our model was 99.8%, which means that it was able to successfully distinguish between real or fake ads in 99.8% of the test data fed into the model.
