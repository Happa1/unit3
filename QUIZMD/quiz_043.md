# Quiz 043
![quiz_043.jpg](..%2Fassets%2Fprompt%2Fquiz_043.jpg)
**Fig.1:** prompt of quiz 043

## 1. flow of chart

**Fig.2:** algorithm flow chart of quiz 043

## 2. solution
```.py

CREATE TABLE Movies(
    id INTEGER primary key,
    year int,
    budget REAL,
    category varchar(100),
    director varchar(100),
    producer varchar(100),
    name varchar(100)
 )

INSERT into Movies(year, budget, category, director, producer, name)
values ('2020', '700000','fantasy', 'Makoto Shinkai', 'Toho','tenkino-ko')

INSERT into Movies(year, budget, category, director, producer, name)
values ('2019', '1000000','SF', 'George Lucas', 'George Lucas','Star Wars')

CREATE TABLE actors(
    id INTEGER primary key ,
    name varchar(100),
    age int
)

CREATE TABLE genre(
    id INTEGER primary key,
    name varchar(100)
)
```

## 3. Proof of work
![evidence_043.png](..%2Fassets%2Fevidence%2Fevidence_043.png)
**Fig.3:** Evidence for quiz 043