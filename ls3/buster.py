# a = [i for i in range(1,100) if i%2==0]
# print(a)

from functools import lru_cache
@lru_cache(None)
def f(x):
    if x <= 0:
        return 1
    if x % 2 == 0:
        return f(x-2)+f(x-4)
    if x % 2 == 1:
        return f(x-1)+f(x-3)

print(f(100))