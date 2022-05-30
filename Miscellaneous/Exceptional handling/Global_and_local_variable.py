x=20
def fun():
    x=10
    print(x)
    def abc():
        y=20
        print(y)
    abc()
    fun()
print(x)
