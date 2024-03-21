A few thoughts
First we have about 1200 1st of the months through the 20th century. Roughly 1/7 of those are going to be Sundays of course. So we can expect an answer of about 171.

Next, given 1 Jan 1900 was a Monday, you can expect every 7 days of that 365 day years to be a Monday as well, in perpetuity. So something like, if day of the year % 7 == 0 it's a Monday.

The same thing for the months, the first day of each month will occur on the same day each year except for leap years. Aka the first of feburary is going to be on the 32nd day of the year, every year, so sunday is ~ doty % 6, that's a hit. 

Badda bing.

First, let's have a date -> int function for "days since Jan 1st 1900"
--

So if 
1/1/1900 - Monday
2/1/1900 - Tuesday
3/1/1900 - Wednesday
4/1/1900 - Thursday
5/1/1900 - Friday
6/1/1900 - Saturday
7/1/1900 - Sunday

You can always find adjacent SDOTW by counting fowards or backwards by 7s

