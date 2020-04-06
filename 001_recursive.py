def func(arr_param, result, index):
    try:
        result = result + arr_param[index]
        index += 1
        return func(arr_param, result, index)
    except IndexError:
        return result
    pass


def main():
    for i in range(9999):
        arr = range(i)

        my_result = func(arr, 0, 0)

        print('result is: %s, i is: %s ' % (my_result, i))


if __name__ == '__main__':
    main()
