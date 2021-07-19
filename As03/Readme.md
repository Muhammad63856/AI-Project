# Assignment 03
### PROJECT MEMBERS ###
StdID | Name
------------ | -------------
**63856** | **Muhammad Ahmad Quraishi** <!--this is the group leader in bold-->
59440 | Yasir Sana
<!-- Replace name and student ids with acutally group member names and ids-->

## Short Description ## 
Firstly, we downloaded all the required files from Kaggle. Then we removed the text based columns and imported the features in our python code file. We gathered the algorithms that we wanted to apply from Scikit and applied the algorithm on our data file. Afterwards, we ran our program on Test.csv that we downloaded from Kaggle and submitted the results on Kaggle. 

## Findings ##  

**Finding 1: SVM Classification**  
First model that we applied on our data was SVM classification. We imported the libraries of SVM in our python coding file and then went ahead with the coding. We expected to get high result, but surprisingly we only got around 0.622. This low result motivated us to move on to the two other models to get a much better result. 

**Screenshot of SVM submission prediction:**
![submissionSvmp](https://user-images.githubusercontent.com/68788484/126211072-b094f9b5-7542-45d2-96ae-12abaf20d4e9.PNG)



**Finding 2: kNN Classification**  
After tweaking with SVM, we moved on to working with kNN. We decided to change some things before applying kkN in our dataset. The first thing we changed was that, instead of filling empty age cells with Nan values, we first calculated the average of all the oassenger classes and then filled the empty age cells with that average. We did the same with Fare and Embarked column. Then instead of dropping the text based columns, we dropped the columns: Pclass, PassengerID, Parch and SibSp. And we imported the Age, Fare, Sex and Embarked features to our python code file. Then we set different numbers of K neighbors: five, seventeen and nineteen. After that we applied kNN classification on our test and train data and produced a submission file. Afterwards, we posted the file on Kaggle and we got similar results as SVM classfication, even though we anticipated that we would get higher accuracy.

**Screenshot of kNN submission prediction:**
![subKnnai](https://user-images.githubusercontent.com/68788484/126226441-bb313f84-5592-48e6-982f-11af4188418c.PNG)

**Finding 3: Linear Regression**  
After wokring with the first two models, we moved on to the last one and we picked Linear Regression as linear classifier. We did the same thing as kNN, we filled the empty spaces of the Age, Embarked and Fare columns with their averages. Then after splitting the train and test data, we applied the data on Linear Regression and produced a submission file and then uploaded it on Kaggle. And finally, we got much higher accuracy than the first two models. We got a result value of around 0.7. Therefore, we would conclude by stating that according to our findings, Linear Regression is the best model out of the three and filling empty spaces with the mean values did have a positive effect on the overall result.


**Screenshot of Linear Regression submission prediction:**
![subLRai](https://user-images.githubusercontent.com/68788484/126234473-502f8156-0cdf-473a-8e06-c69597c9fe61.PNG)




