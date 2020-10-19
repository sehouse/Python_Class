def computepay(h, r):
    if h > 40 :
        h2 = h - 40
    pay = (40 * r) + (h2 * (r * 1.5))
    return pay

hrs = input("Enter Hours:")
h = float(hrs)
rat = input("Enter Rate:")
r = float(rat)
p = computepay(h, r)
print("Pay",p)
