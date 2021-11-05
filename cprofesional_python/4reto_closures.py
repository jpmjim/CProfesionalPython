from typing import Generic, TypeVar

T = TypeVar('T')

def make_divisor_by(n: int) -> Generic[T]:
    def numerator(x: int) -> float:
        assert n !=0, 'You cannot divide by zero'
        return x/n
    return numerator

def main():
    divided_by_2 = make_divisor_by(2)
    print(divided_by_2(10))
    divided_by_2 = make_divisor_by(3)
    print(divided_by_2(18))
    divided_by_2 = make_divisor_by(5)
    print(divided_by_2(100))
    divided_by_2 = make_divisor_by(18)
    print(divided_by_2(54))


if __name__ == '__main__':
    main()