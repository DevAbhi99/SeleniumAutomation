def getWeather(temp):
    if temp>20:
        return 'HOT'
    else:
        return 'COLD'
    
def add(a,b):
    return a+b


def divide(a,b):
    if b==0:
        raise ValueError('cannot divide by 0')
    else:
        return a/b