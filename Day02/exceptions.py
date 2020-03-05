try:
    f = open('xyz.txt', 'r')
    '''
    except ZeroDivisionError:
        print('Division by zero not allowed')
    except FileNotFoundError:
        print('File not found!')
    '''
except Exception as E:
    print('File not found!')
    print(E)
finally:
    print('Thank you!')
