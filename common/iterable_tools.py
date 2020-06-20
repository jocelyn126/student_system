"""
    可迭代对象的工具箱
"""

"""
    精通函数式编程  
        在实际项目中，根据需求实现了各种功能。 但是很多功能主体部分相同，只是核心算法不同。
        将多个功能的主体部分,也就是通用代码定义到IterableHelper类中。
        将不同的核心算法使用函数类型的形参隔离，将不同算法通过lambda表达式传递进来。
        这个思想，与面向对象编程是异曲同工。
        ....
"""


class IterableHelper:
    """
        可迭代对象助手类:负责定义对可迭代对象的常用操作
    """

    @staticmethod
    def find_all(list_target, func):
        """

        :param list_target:
        :param func:
        :return:
        """
        for item in list_target:
            # if item.price > 10000:
            if func(item):
                yield item

    @staticmethod
    def find_single(list_target, func):
        for item in list_target:
            if func(item):
                return item

    @staticmethod
    def get_count(list_target, func):
        count = 0
        for item in list_target:
            if func(item):
                count += 1
        return count

    @staticmethod
    def select(list_target, func):
        for item in list_target:
            yield func(item)

    @staticmethod
    def get_max(list_target,*, func):
        max_value = list_target[0]
        for i in range(1, len(list_target)):
            if func(max_value) < func(list_target[i]):
                max_value = list_target[i]
        return max_value

    @staticmethod
    def get_min(list_target, func):
        min_value = list_target[0]
        for i in range(1, len(list_target)):
            if func(min_value) > func(list_target[i]):
                min_value = list_target[i]
        return min_value

    @staticmethod
    def order_by(list_target, func):
        for r in range(len(list_target) - 1):
            for c in range(r + 1, len(list_target)):
                if func(list_target[r]) > func(list_target[c]):
                    list_target[r], list_target[c] = list_target[c], list_target[r]

    @staticmethod
    def order_by_descending(iterable_target, func_condition):
        for r in range(len(iterable_target) - 1):
            for c in range(r + 1, len(iterable_target)):
                if func_condition(iterable_target[r]) < func_condition(iterable_target[c]):
                    iterable_target[r], iterable_target[c] = iterable_target[c], iterable_target[r]

    @staticmethod
    def sum(iterable_target, func_handle):
        """
            在可迭代对象中，根据指定逻辑累加其中的元素.
        :param iterable_target:需要累加的数据(可迭代对象)
        :param func_condition:需要累加的逻辑(方法/函数)
        :return:累加结果
        """
        sum_value = 0
        for item in iterable_target:
            # sum_value += item.price
            # sum_value += item.cid
            sum_value += func_handle(item)
        return sum_value

    @staticmethod
    def is_exists(iterable_target, func_condition):
        """
            在可迭代对象中，根据指定条件判断是否存在元素.
        :param iterable_target:需要搜索的数据(可迭代对象)
        :param func_condition:需要判断的条件(方法/函数)
        :return:是否存在(bool类型)。
        """
        for item in iterable_target:
            if func_condition(item): # 调用lambda
                return True
        return False

    @staticmethod
    def delete_all(iterable_target,func_condition):
        for i in range(len(iterable_target)-1,-1,-1):
            # if iterable_target[i].cid % 2:
            # if iterable_target[i].price < 500:
            if func_condition(iterable_target[i]):
                del iterable_target[i]

    @staticmethod
    def delete_duplicates(list_target, func):
        for r in range(len(list_target) - 1, 0, -1):
            for c in range(r):
                if func(list_target[r]) == func(list_target[c]):
                    del list_target[r]
                    break
