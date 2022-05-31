CREATE TABLE pharmaceuticalDB(
    id INT AUTO_INCREMENT,
    Store INT,
    DayOfWeek INT,
    Date DATETIME,
    Sales FLOAT,
    Customers FLOAT,
    Open INT,
    Promo INT,
    SchoolHoliday INT,
    StateHoliday INT,
    Week_Number INT,
    Day INT,
    Month INT,
    Year INT,
    weekday INT,
    day_of_year INT, 
    StoreType INT,   
    Assortment VARCHAR(255),
    CompetitionDistance FLOAT,
    CompetitionOpenSinceMonth FLOAT,
    CompetitionOpenSinceYear FLOAT,
    Promo2 INT,
    Promo2SinceWeek FLOAT,
    Promo2SinceYear FLOAT,
    PromoInterval VARCHAR(255),
    PRIMARY KEY(id)
);