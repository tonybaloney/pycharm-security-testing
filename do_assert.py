
assert 1 == 1

try:
    x = 1
except Exception as ex:
    pass


try:
    x = 1
except:
    # do nothing
    pass

