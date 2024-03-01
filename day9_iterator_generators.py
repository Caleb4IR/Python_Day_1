# Iterable? __iter__ | Which can be looped as many times, List, dict, setss
# Iterator? __next__ | Can only loop them once | Memory management
# range(0, 100_00_00, 1) | list with 100 mil lots of memory
# iterator remember one thing at time | save memory
# __next__ & __iter__

# nums = [5, 10, 20]
# print(dir(nums))

# nums_iter = nums.__iter__()  # Converts to Iterator | Iterable -> Itertaor
# nums_iter1 = iter(nums)  # <list_iterator object at 0x0000026DDAA5AF50>
# print(nums_iter)  # <list_iterator object at 0x0000026DDAA5AF50>
# print(dir(nums_iter))  # Iterator -> __next__ & __iter__
# # Conclusion: All Iterators are Iterables | but not the other way around

# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))
# print(next(nums_iter))

# Create an iterator and loop it using while loop
# Clue: next()
# clue: Brakes at error


def main():
    nums = [5, 10, 20]

    iterator = iter(nums)

    while True:
        try:
            num = next(iterator)
            print(num)
        except StopIteration:
            break

    nums_iter2 = iter([80, 90, 100])
    for num in nums_iter2:
        print(num)

    class MyRange:
        def __init__(self, start, end):
            self.current = start
            self.end = end

        def __iter__(self):
            return self

        def __next__(self):
            if self.current > self.end:
                raise StopIteration
            self.current += 1
            return self.current - 1

    # x = MyRange(1,5)
    # print(next(x))
    # print(next(x))


def infinite_integers():
    n = 0
    while True:
        yield n  # return then pause
        n += 1


def fibonacci(limit):
    a = 0
    b = 1
    while a < limit:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    # main()
    # for n in MyRange(1, 5):
    #     print(n)
    integers = infinite_integers()
    print(next(integers))
    print(next(integers))
    print(next(integers))

    # fibonacci - generator function
    for num in fibonacci(10):
        print(num)

# Output
# 0 1 1 2 3 5 8
