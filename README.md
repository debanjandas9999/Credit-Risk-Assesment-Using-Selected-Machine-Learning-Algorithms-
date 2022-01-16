Final Year Project

Topic - Credit Risk Assessment Using Selected Machine Learning Algorithms. 
Name - Debanjan Das
Student ID - 17202833

Website link - https://debanjandas-loanpredictor-rtbl5.ondigitalocean.app/

![image](https://user-images.githubusercontent.com/47033532/149674938-98266aad-0955-4996-b4b1-27bb63a63651.png)



Report Link - https://github.com/debanjandas9999/Credit-Risk-Assesment-Using-Selected-Machine-Learning-Algorithms-/blob/main/UCD_CS_FYP___CreditRiskAssessmentReport.pdf

Abstract 

It is important for a bank to assess its credit risk and the extent of its exposure in the event of
non-performing customers. Statistical approaches have been used to estimate this type of risk for
decades, and with recent advances in the field of machine learning, there has been an interest
in seeing whether machine learning algorithms can achieve better risk quantification. The aim
of this study is to see which approach from a collection of machine learning techniques performs
the best in default prediction when model evaluation parameters are chosen. Logistic Regression,
Random Forest, XGBoost, and Artificial Neural Network were the techniques studied. To address
the imbalance between classes for the response variable, an oversampling technique known as
SMOTE was used. In order to enhance model accuracy, data was divided into clusters, followed
by the deployment of Machine Learning models on each of these clusters. In terms of the chosen
model evaluation metric, the results showed that XGBoost with hyperparameter tuning achieved
the best result. An attempt has also been made to simulate data in a pandemic environment and
the built-in model has been adjusted accordingly to assess credit risk.

Core Requirements

• In this project, our main objective is to develop a machine learning model to help predict
if a bank would grant a loan to a client. Various machine learning algorithms like Neural
Networks, Logistic Regression, Boosted Decision Trees and Random Forest would be used
to correctly classify the outcome of a loan. The motivation behind using these algorithms
can be understood in the ‘Related Work’ section.

• We also aim to identify the features that play a crucial role in determining the result
of the loan process. Different feature selection methods (like Information Gain) would be
implemented to find the most relevant features. A model with a certain number of features
leads to better accuracy. Further Data Analysis would be performed to explore exciting
hidden patterns that might exist.

• Another goal is to conduct customer segmentation [3] using suitable clustering methods.
Customer segmentation is the process of dividing customers into groups based on common
characteristics so companies can market to each group effectively and appropriately. As a
part of this project, we aim to find out which cluster of people tend to get a loan. A financial
institution might segment customers according to a wide range of factors, which can be used
for filtered marketing purposes.

Advanced Requirements

• The possibility of a global pandemic/market crash would also be taken into consideration.
A new dataset would be simulated for the same people that would look like one affected
by a pandemic/market crash. A credit score would be calculated for each customer. Following that, both the datasets would be compared and the model would be able to identify
the pandemic affected people automatically based on the credit score. The most affected
columns would tend to be Job, Income, etcetera. The built-in model would then be adjusted
to predict for the pandemic affected people – where factors like deflation rate (last year vs
current year) and decrease in salary might be taken into consideration to measure the risk
of lending a loan.

• Finally, a User Interface would be designed where the user can fill in the attributes required
for a loan and check eligibility.

The project can be divided into 3 sections - 

1. Jupyter Notebook and R program (to prepare dataset)
2. Loan Prediction website code. 
3. Final Year Project Report 

Steps to run website - 

1. Install python.
2. Run app.py by using the following command on the terminal: python app.py 
3. Click on the link that is shown in the terminal. 

Library Requirements - 

absl-py==0.11.0
aiohttp==3.7.1
async-timeout==3.0.1
attrs==20.2.0
certifi==2020.6.20
chardet==3.0.4
click==7.1.2
cycler==0.10.0
fastapi==0.63.0
Flask==1.1.2
h11==0.12.0
h5py==2.10.0
idna==2.10
itsdangerous==1.1.0
Jinja2==2.11.3
joblib==0.17.0
kiwisolver==1.2.0
Markdown==3.3.3
MarkupSafe==1.1.1
matplotlib==3.3.2
multidict==5.0.0
numpy==1.19.2
pandas==1.1.3
Pillow==8.0.0
protobuf==3.14.0
pydantic==1.8.1
pyparsing==2.4.7
python-dateutil==2.8.1
pytz==2020.1
scikit-learn==0.23.2
scipy==1.5.2
six==1.15.0
sklearn==0.0
slackclient==2.9.3
starlette==0.13.6
threadpoolctl==2.1.0
typing-extensions==3.7.4.3
uvicorn==0.13.4
Werkzeug==1.0.1
xgboost==1.4.2
yarl==1.6.2
