# Quiz 045
![quiz_045.jpg](..%2F..%2Fassets%2Fprompt%2Fquiz_043-050%2Fquiz_045.jpg)
**Fig.1:** prompt of quiz 045

## 1. flow of chart
![quiz_diagram_045.jpg](..%2F..%2Fassets%2Fflowchart%2Fflowchart_043-050%2Fquiz_diagram_045.jpg)
**Fig.2:** UML diagram of quiz 045

## 2. solution
```.py
SELECT t.account_id,
       c.first_name,
       c.last_name,
       a.account_type,
       SUM(CASE WHEN transaction_type = 'deposit' THEN amount ELSE 0 END) -
       SUM(CASE WHEN transaction_type = 'withdraw' THEN amount ELSE 0 END) AS net_deposit,
    a.balance
FROM main.transactions t
join main.accounts a on t.account_id = a.account_id
join main.customers c on a.customer_id = c.customer_id
GROUP BY t.account_id
having net_deposit != a.balance;
```

## 3. Proof of work
![evidence_045.png](..%2F..%2Fassets%2Fevidence%2Fevidence_043-050%2Fevidence_045.png)
**Fig.3:** Evidence for quiz 045