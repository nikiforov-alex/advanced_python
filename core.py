"""Create metaclass for work with property."""


class MyMetaClass(type):
    """Metaclass which make properties of methods with a specific format."""

    def __new__(mcs, name, bases, classdict):
        """Magic method wherein properties are created."""
        property_keys = ('get_', 'set_', 'del_')
        property_args = ('fget', 'fset', 'fdel')
        attrs = set(key[4:] for key, item in classdict.items()
                    if key.startswith(property_keys))
        for attr in attrs:
            property_kwargs = {}
            for key, arg in zip(property_keys, property_args):
                new_key = key + attr
                property_kwargs[arg] = classdict.get(new_key)
            new_attr = property(**property_kwargs)
            classdict[attr] = new_attr
        return type.__new__(mcs, name, bases, classdict)


class Example(metaclass=MyMetaClass):
    """Class-example which demonstrates work with metaclass."""

    def __init__(self):
        """Initialize class-example."""
        self._x = None

    def get_x(self):
        """Get 'x'."""
        return self._x

    def set_x(self, value):
        """Set 'x'."""
        self._x = value

    def get_y(self):
        """Get 'y'."""
        return 'y'

    def del_x(self):
        """Delete 'x'."""
        print('DEL x')


def main():
    """Run main function."""
    ex = Example()
    ex.x = 255
    print(ex.x)
    del ex.x
    print(ex.y)


if __name__ == '__main__':
    main()
