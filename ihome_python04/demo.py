# coding:utf-8
import functools

def login_required(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """wrapperss"""
        pass
    return wrapper

@login_required
def itcast():
    """itcast python"""
    pass


print(itcast.__name__)
print(itcast.__doc__)