# Versions 
- python v3.8.13  
- airflow v2.3.2

# Part 1 Airflow CSV processor  
1. install airflow 
```pip install apache-airflow``` 

- check version with: ```airflow version```  

2. To start scheduler
```
   airflow db init
   airflow scheduler
```
- with a new terminal 
``` 
airflow webserver -p 8080
```
3. run workflow 
```
cp airflow_process_csv.py ~/airflow/dags/
```

4. open https://localhost:8080 to access Airflow


# Part 2 Database design 
> unable to install docker due to device issue.  

The database is designed as following:   
![alt text](https://github.com/dstc0116/de_challenge_2022_06/blob/32f838a45c8f2ec13197bca431e1500c38c05f60/database_er.jpg)  (created with drawio)

SQL  
1. The list of our customers and their spending.
```sql
SELECT customer_name,
customer_phone,
sum(price_paid) as total_spending
FROM Transaction
GROUP BY customer_name
```
2. The top 3 car manufacturers that customers bought by sales (quantity) and the sales number for it in the current month.
```sql
SELECT 
SUM(t.price_paid) as sales,
count(1) as quantity_sold,
c.model_name,
c.manufacturer
FROM Transaction t
JOIN Car c
ON t.car_serial_num = c.serial_num  
WHERE DATE_TRUNC('month', date) = DATE_TRUNC('month', CURRENT_DATE)
GROUP BY c.manufacturer
ORDER BY quantity_sold DESC
LIMIT 3
```
# Part 3: System Design 
   Not familar with system design, shall skip this part. 
# Part 4: Charts and API 
Data is retrieved using ```requests``` and processed with ```pandas ```, ploted with ```plotly```.   
![alt text](https://github.com/dstc0116/de_challenge_2022_06/blob/4436311b0ff23fab21a144c1849570f8fc2571a0/chart.png)

Relevant codes are in : [notebook](https://github.com/dstc0116/de_challenge_2022_06/blob/22fd659b82a30cebd035105da6923e06dc5591d7/Covid-19_chart.ipynb)

# Part 5: Machine Learning 
The goal is to perform a classification.   
Steps:   
1. Read data 
2. transform any categorical values to numerical as following. Though ordinal encoding or label encoding can also be done, but since the labels implies there is some meaning in the label (ie. vhigh is  better than high), assigning values would be more appropriate.
   vhigh = 4  high=3  med=2  low=1
   5more = 6    more =5
   small =1   med=2   big=3
   unacc=1   acc=2  good=3   vgood=4

3. train test split 
4. Model training and prediction 
   - random forest and decision tree are used 
5. Prediction based on given parameter:
   Maintenance = High  
   Number of doors = 4  
   Lug Boot Size = Big  
   Safety = High  
   Class Value = Good  
   Since number of person is not stated, predictions are made for all 3 scenarios (person = [2,4,5])
   The result is "3" for all scenarios. Suggesting given such parameter, regardless of number of person,buying price will be **high**

Relevant codes are in : [notebook](https://github.com/dstc0116/de_challenge_2022_06/blob/fe120226c63fd75a1387d6c3c652c9f7819ba459/machine_learning.ipynb)