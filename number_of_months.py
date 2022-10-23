def is_leap(year):
  if year % 4 == 0: 
    if year % 100 == 0:
      if year % 400 == 0:
        return 1
      else:
        return 0
    else:
      return 1
  else:
    return 0

def days_in_month(year , month):
   """Takes the year and month as input and displays number of days."""
   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
   value = is_leap(year)
   if value == 0 and month == 2:
     no_of_days = 28
   elif value == 1 and month == 2:
     no_of_days = 29
   else:
     no_of_days = month_days[month - 1]
   return no_of_days

year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)