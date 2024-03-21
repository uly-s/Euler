
const {range, when}= require('./eloquent');

const months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

// function to see if a year is a leap year
const isLeap = year => year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0);

// function to set months var based on if it's a leap year
const setLeap = year => months[1] = isLeap(year) ? 29 : 28;

// days since Jan 1st 1900
const daysGoneBy = (day, month, year) => {
    return range(1900, year-1).reduce((sum, val) => sum + (!isLeap(val) ? 365 : 366), 0) + dayOfYear(day, month, year);
}

// need a func for day of year by date
const dayOfYear = (day, month, year) => {
    setLeap(year);
    return months.slice(0, month-1).reduce((sum, val) => sum + val, 0) + day - 1
}

const sunday = (day, month, year) => {
    return (daysGoneBy(day, month, year) + 1) % 7 == 0;
}

//console.log(dayOfTheWeek(daysGoneBy(7, 1, 1900)));

//console.log(daysGoneBy(21, 3, 2024));

let count = 0;

range(1901, 2000).forEach(year => {
    range(1, 12).forEach(month => {
        if(sunday(1, month, year)) count += 1;
    })
})

console.log(count);