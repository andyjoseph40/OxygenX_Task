Title: Loan Default Prediction for a Digital Lending Fintech
Objective:
Your task is to analyze historical loan data and build a model that predicts whether a borrower will default on their loan. This is a critical problem in digital lending, as it helps optimize credit decisions and minimize risk.
Dataset
The dataset provided contains information on past borrowers, including demographic details, financial behavior, and loan performance.
Dataset Columns:
loan_id: Unique identifier for the loan
customer_id: Unique identifier for the borrower
age: Age of the borrower
gender: Male/Female
income: Monthly income of the borrower (in NGN)
loan_amount: Loan amount taken
tenure_months: Loan duration in months
credit_score: A score between 300-850
employment_status: Full-time, Part-time, Self-employed, Unemployed
bank_balance: Current balance in the borrower's bank account
number_of_loans: Number of loans the borrower currently has
missed_payments: Number of past missed payments
defaulted: Target variable (1 = Default, 0 = No Default)

Tasks
1. EDA on the dataset provided
2. Create  new features
3. Train at least one machine learning models to predict loan default 
4. Evaluate models using performance metrics 
5. Insights and Recommendations 
Deliverables
A Jupyter Notebook or Python Script with EDA, model training, and evaluation.
A short presentation (3-5 slides) summarizing key findings and recommendations.

Part 2: SQL Challenges
Assume the cleaned dataset  is stored in an SQL database called loans_db with a table named loan_data)
1. Write and attach the SQL scripts to 
a.Find the top 5 customers with the highest total loan amount.
b.Calculate the average credit score of customers who defaulted.
c.Get the count of loans grouped by tenure category.
d.Identify the percentage of loans that defaulted in each employment category.
e.Retrieve all customers with more than 2 missed payments and a credit score below 500.
f.Find the top 3 loan tenures with the highest default rate.

