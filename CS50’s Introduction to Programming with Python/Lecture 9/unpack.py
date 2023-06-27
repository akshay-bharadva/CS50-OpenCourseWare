# * to unpack as list like *[10,20,30]
# ** to unpack as dict like **{price:10,quantity:2,expense:30}
# it's similar to ... operation in JS

def f(*args, **kwargs):
    print(args, kwargs)


f(1, 2, True, "Name", theme="dark", type="landscape")
