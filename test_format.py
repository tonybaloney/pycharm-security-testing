# should not
"x ".format(y, z)

z = "testing..."

# should
z.format(y, q)

# should
str(x).format(y)

# should not
f"{x}"

class Foo:
    def format(self, *args):
        pass


i = Foo()

# should not
i.format(n, o)