def test_function():
    result = 5+9
    print('Test function: ', result)
    print(bytes(14))
    return(bytes(result))

def testing(test_function):
    result = test_function()
    print(result)

testing(test_function)