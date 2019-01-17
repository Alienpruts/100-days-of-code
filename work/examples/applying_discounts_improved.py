customers = [
    dict(id=1, total=200, coupon_code='F20'),
    dict(id=2, total=150, coupon_code='P30'),
    dict(id=3, total=100, coupon_code='P50'),
    dict(id=4, total=110, coupon_code='F15'),
]

discounts = {
    'F20': (0.0, 20.0),  # (percent, fixed)
    'P30': (0.3, 0.0),  # (percent, fixed)
    'P50': (0.5, 0.0),  # (percent, fixed)
    'F15': (0.0, 15.0),  # (percent, fixed)

}

for customer in customers:
    code = customer['coupon_code']
    # This is the dispatcher : we seek our code (and the values in it) in the dict
    # and set defaults for when it is not found.
    percent, fixed = discounts.get(code, (0.0, 0.0))
    customer['discount'] = percent * customer['total'] + fixed

for customer in customers:
    print(customer['id'], customer['total'], customer['discount'])
