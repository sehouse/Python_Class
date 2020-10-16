hrs = input("Enter Hours:")
rate = input("Enter Rate of Pay:")
h = float(hrs)
if h > 40 :
    ot = h - 40
r = float(rate)
pay = (40 * r) + ((r * 1.5) * ot)
print (pay)
