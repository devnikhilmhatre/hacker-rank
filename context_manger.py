class ContextManger:

    __fields = ()

    def __init__(self, fields):
        self.__fields = fields
        print(self.__class__.__fields)

    @property
    def fields(self):
        return self.__fields

    def __enter__(self):
        print('--enter--')
        return self

    def __exit__(self, *args):
        print('--exit--', args)


def some():
    with ContextManger([]) as CM:
        abc = 'z'
        # for i in dir(CM):
        #     pass
    print(abc)


some()