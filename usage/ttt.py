import inspect

from test_case.get_test_value_by_yaml import get_value


def get_current_function_name():
    return inspect.stack()[1][3]

class MyClass:
    def function_one(self):

        print("%s.%s invoked"%(self.__class__.__name__, get_current_function_name()))
        print(get_current_function_name())

if __name__ == "__main__":
    # myclass = MyClass()
    # myclass.function_one()
    # my_name = "我的名字"
    my_id = str(get_value("xc手机号")) #13911645993
    # print(my_id)
    # print(my_id[3:7])
    print(my_id.replace((my_id[3:7]), "****"))
