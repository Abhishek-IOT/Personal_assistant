                                     ALGO For the Day of the Date
                                     =============================
                                     
                                     
In this I did a Logic that was told by my soft skills sir.
We have to calculate the no of odds days in the year,month,and days.



For years we have a two logic that=
First Logic=
        5       3       1       0
        100     200     300     400     
        500     600     700     800     
        900     1000    1100    1200    
        1300    1400    1500    1600
        1700    1800    1900    2000
        ....    ....    ...     ...
        ....    ....    ...     ...     
        ....    ....    ...     ...
        ....    .....   ....    ....
        
In this we will see that in 100,500,900th year the odd day will be 5, and so on for the 200,600,1000th year it will be 3,etc.



Second Logic for years=The year that will be given by the user we will take it and with example i will tell u what we will do=
if we are given=2012
then means 11 years in the century are complete and 12 year is going on.
So we will divide 11 by 4 to check the number of leap year that we will have.
Then we all also subract the number of the leap years from 12 to take out the number of leap year for the further calculation.
11/4=3 
means the 3 leap years have happened and 12-3=9 non leap years.
We will now multiply the leap years with 2 and add it to non leap years and then divide it by 7 to get another set of leap years.


For the months we add all the days till the particular date.
That means=for example the date is 10 feb we will add the days till 10 feb that will be 31+10=41
then we will divide the total number of days with 7 to get the number of odds in month.



The Logic behind odd days is because after every four year we will have a extra day.That plays a very important role for collecting the 
odds.




At last we will add all the odds and then divide it by 7. The Reminder will tell us about the day of the date that was supposed to happen.
If Reminder is 0/7=Sunday
               1=Monday
               2=Tuesday
               3=Wednesday
               4=Thursday
               5=Friday
               6)Saturday

