
--- CREATE DATABASE

CREATE DATABASE "loan_data_";
USE "loan_data_";

SELECT * 
FROM loan_data_


-- Find the top 5 customers with the highest total loan amount
SELECT TOP 10 customer_id, SUM(loan_amount) AS total_loan_amount
FROM loan_data_
GROUP BY customer_id
ORDER BY total_loan_amount DESC;


-- Calculate the average credit score of customers who defaulted.
SELECT AVG(credit_score) AS avg_credit_score_defaulted
FROM loan_data_
WHERE defaulted = 1


-- Get the count of loans grouped by tenure category
--(Since no tenure categories are predefined, we assume ranges for categorization.)
SELECT 
    CASE 
        WHEN tenure_months <= 12 THEN 'Short-term'
        WHEN tenure_months BETWEEN 13 AND 36 THEN 'Medium-term'
        ELSE 'Long-term'
    END AS tenure_category,
    COUNT(*) AS loan_count
FROM loan_data_
GROUP BY 
    CASE 
        WHEN tenure_months <= 12 THEN 'Short-term'
        WHEN tenure_months BETWEEN 13 AND 36 THEN 'Medium-term'
        ELSE 'Long-term'
    END;


-- Identify the percentage of loans that defaulted in each employment category.
SELECT employment_status,
       COUNT(CASE WHEN defaulted = 1 THEN 1 END) * 100.0 / COUNT(*) AS default_percentage
FROM loan_data_
GROUP BY employment_status;


-- Retrieve all customers with more than 2 missed payments and a credit score below.
SELECT *
FROM loan_data_
WHERE missed_payments > 2 AND credit_score < 500;


-- Find the top 3 loan tenures with the highest default rate.
SELECT TOP 3 tenure_months, 
       COUNT(CASE WHEN defaulted = 1 THEN 1 END) * 100.0 / COUNT(*) AS default_rate
FROM loan_data_
GROUP BY tenure_months
ORDER BY default_rate DESC