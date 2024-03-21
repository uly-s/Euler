// function to calculate total days
const calculateDays = (year, month, day, months) => {
    const daysInMonths = months.slice(0, month - 1).reduce((acc, curr) => acc + curr, 0);
    return daysInMonths + day - 1;
}

// function to see if a year is a leap year
const isLeap = year => year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0);

// usage
const months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];
const year = 2022;
const month = 12;
const day = 31;

if (isLeap(year)) {
    months[1] = 29;
}

const totalDays = calculateDays(year, month, day, months);
console.log(totalDays);