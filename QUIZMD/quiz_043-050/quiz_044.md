# Quiz 044
![quiz_044.jpg](..%2F..%2Fassets%2Fprompt%2Fquiz_043-050%2Fquiz_044.jpg)
**Fig.1:** prompt of quiz 044

## 1. flow of chart
![quiz_diagram_044.jpg](..%2F..%2Fassets%2Fflowchart%2Fflowchart_043-050%2Fquiz_diagram_044.jpg)
**Fig.2:** ER diagram of quiz num

## 2. solution
```.py
select count(*) from main.INHABITANT where INHABITANT.gender='Male'and INHABITANT.state='Friendly'

select avg(gold), count(*), V.name from INHABITANT join VILLAGE V
on V.villageid = INHABITANT.villageid group by V.name;

select count(*) from main.ITEM where ITEM.item like "A%";

select distinct job from INHABITANT;

select * from main.INHABITANT, main.ITEM where ITEM.owner = INHABITANT.personid and INHABITANT.job='herbalist'

select I.item from INHABITANT join main.ITEM I
on I.owner = INHABITANT.personid where INHABITANT.job='Herbalist';
```

## 3. Proof of work
![evidence1_quiz044.png](..%2F..%2Fassets%2Fevidence%2Fevidence_043-050%2Fevidence1_quiz044.png)
**Fig.3:** Evidence for quiz 044 question 2

![evidence2_quiz044.png](..%2F..%2Fassets%2Fevidence%2Fevidence_043-050%2Fevidence2_quiz044.png)
**Fig.4:** Evidence for quiz 044 question 3

![evidence3_quiz044.png](..%2F..%2Fassets%2Fevidence%2Fevidence_043-050%2Fevidence3_quiz044.png)
**Fig.5:** Evidence for quiz 044 question 4

![evidence4_quiz044.png](..%2F..%2Fassets%2Fevidence%2Fevidence_043-050%2Fevidence4_quiz044.png)
**Fig.6:** Evidence for quiz 044 question 5

![evidence5_quiz044.png](..%2F..%2Fassets%2Fevidence%2Fevidence_043-050%2Fevidence5_quiz044.png)
**Fig.7:** Evidence for quiz 044 question 6
