class CustomMeta():
    def __new__(metaclass, name, parents, attr):
        
        new_attr = {}
        for key, val in attr.items():
            if not name.startswith('__'):
                new_attr["custom_" + key] = val
            else:
                new_attr[key] = val

        return type(name, parents, new_attr)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def line(self):
        return 100

inst = CustomClass()
inst.custom_x
inst.custom_line()

#inst.x  # ошибка
#inst.line() # ошибка
