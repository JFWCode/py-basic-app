# coding=utf-8
# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print("Hi, {0}".format(name))  # 按 ⌘F8 切换断点。

class Test:
    def foo(self):
        print('foo')

    @classmethod
    def cls_foo(cls):
        print('cls_foo')

    @staticmethod
    def static_foo(cls):
        print('static_foo')

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    #print_hi('PyCharm')
    t = Test()
    t.foo()

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
