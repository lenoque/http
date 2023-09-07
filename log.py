from datetime import datetime


def logger(path):
    def __logger(old_function):
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)
            with open(path, 'a') as fp:
                dt = datetime.now()
                fp.write(f'{dt} {old_function.__name__}(*{args}, **{kwargs}) -> {result}\n')
            return result

        return new_function

    return __logger
