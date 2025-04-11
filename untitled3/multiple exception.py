try:
    arr = [1, 2, 3, 4]
    print('value = ', arr[5])
except ArithmeticError as e:
    print('ArithmeticError exception caught - ', e)

except IndexError as e:
    print('IndexError exception caught -', e)
except Exception as e:
    print('Exception exception caught - ', e)