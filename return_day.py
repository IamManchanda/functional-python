""" Python Functions """

def return_day(num):
    days = ["Sunday","Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday"]
    if num > 0 and num <= len(days):
        return days[num-1]
    return None

print( return_day(1) )
print( return_day(2) )
print( return_day(3) )
print( return_day(4) )
print( return_day(5) )
print( return_day(6) )
print( return_day(7) )
print( return_day(42) )
