def with_custom_message(message):
    def with_message(function):
        print(f"{message}:")
        def wrapper(*args, **kwargs):
            function(*args, **kwargs)
        return wrapper
    return with_message


@with_custom_message("Hola")
def multiply(a, b):
    c = a * b
    print(f"The result of {a} * {b} is {c}")


multiply(10, 2)