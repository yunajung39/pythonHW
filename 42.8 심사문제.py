def html_tag(name):
    def real_decorator(x):
        def wrapper():
                return "<{0}>{1}</{0}>".format(name,x())
        return wrapper
    return real_decorator

a, b = input().split()
 
@html_tag(a)
@html_tag(b)
def hello():
    return 'Hello, world!'
 
print(hello())