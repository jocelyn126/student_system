import os
import re
from common.iterable_tools import IterableHelper

file_name = "students_info.txt"
start_id = 1000


def menu():
    print('''
        ╔———————学生信息管理系统————————╗
    │                                              │
    │   =============== 功能菜单 ===============   │
    │                                              │
    │   1 录入学生信息                             │
    │   2 查找学生信息                             │
    │   3 删除学生信息                             │
    │   4 修改学生信息                             │
    │   5 排序                                     │
    │   6 统计学生总人数                           │
    │   7 显示所有学生信息                         │
    │   0 退出系统                                 │
    │  ==========================================  │
    │  说明：通过数字或↑↓方向键选择菜单          │
    ╚———————————————————————╝
    ''')


def main():
    while True:
        menu()
        option = input("请输入数字:")
        option_str = re.sub("\D", "", option)
        option_dict = {
            '1': insert,
            '2': search,
            '3': delete,
            '4': modify,
            '5': sort,
            '6': total,
            '7': show
        }
        if option_str in ['0', '1', '2', '3', '4', '5', '6', '7']:
            if option_str == "0":
                print("程序退出")
                break
            else:
                option_dict[option_str]()
        else:
            print("输入错误, 请重新输入")


def __generate_id():
    global start_id
    start_id += 1
    return start_id


def insert():
    temp_student_list = []
    mark = True
    while mark:
        name = input("请输入姓名: ")
        if not name:
            break
        id = __generate_id()
        english = __get_int("请输入英语成绩:")
        python = __get_int("请输入python成绩:")
        c_language = __get_int("请输入c语言成绩:")
        student_dict = {"id": id, "name": name, "english": english, "python": python, "c": c_language}
        temp_student_list.append(student_dict)
        is_mark = input("是否继续添加？（y/n）:")
        if is_mark == "y":
            mark = True
        else:
            mark = False
    save(temp_student_list)
    print("信息录入完毕.")


def save(temp_student_list):
    with open(file_name, "a") as file:
        for line in temp_student_list:
            file.write(str(line),"\n")
    file.close()


def search():
    mark = True
    temp_student_list = []
    while mark:
        id = ""
        name = ""
        if os.path.exists(file_name):
            choice = input("按ID查输入1；按姓名查输入2：")
            if choice == "1":
                id = input("请输入学生ID：")
            elif choice == "2":
                name = input("请输入学生姓名：")
            else:
                print("您的输入有误，请重新输入！")
                search()
            with open(file_name, "r")as file:
                student_info = file.readlines()
                for line in student_info:
                    student_dict = dict(eval(line))
                    if id:
                        if student_dict["id"] == __get_int(id):
                            temp_student_list.append(student_dict)
                    elif name:
                        if student_dict["name"] == name:
                            temp_student_list.append(student_dict)
                show_student(temp_student_list)
                temp_student_list.clear()
                is_mark = input("是否继续查询？（y/n）:")
                if is_mark == "y":
                    mark = True
                else:
                    mark = False
        else:
            print("数据不存在")
            return


def show_student(studentList):
    if not studentList:
        print("(o@.@o) 无数据信息 (o@.@o) \n")
        return
    format_title = "{:^6}{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^10}"
    print(format_title.format("ID", "名字", "英语成绩", "Python成绩", "C语言成绩", "总成绩"))
    format_data = "{:^6}{:^12}\t{:^12}\t{:^12}\t{:^12}\t{:^12}"
    for info in studentList:
        print(format_data.format(str(info.get("id")), info.get("name"), str(info.get("english")), str(info.get("python")),
                                 str(info.get("c")),
                                 str(info.get("english") + info.get("python") + info.get("c")).center(12)))

def delete():
    mark = True
    while mark:
        id = input("请输入要删除的学生ID：")
        if id:
            if os.path.exists(file_name):
                with open(file_name, 'r') as rfile:
                    read_student_info = rfile.readlines()
        else:
            read_student_info = []
        is_del = False
        if read_student_info:
            with open(file_name, "w") as wfile:
                temp_dict = {}
                for line in read_student_info:
                    temp_dict = dict(eval(line))
                    if temp_dict["id"] != __get_int(id):
                        wfile.write(str(temp_dict) + "\n")
                    else:
                        is_del = True
                if is_del:
                    print("ID为 %s 的学生信息已经被删除..." % id)
                else:
                    print("没有找到ID为 %s 的学生信息..." % id)
        else:
            print("无学生信息...")
            break
        show()
        is_mark = input("是否继续删除？（y/n）:")
        if is_mark == "y":
            mark = True
        else:
            mark = False

def show():
    student_all=[]
    if os.path.exists(file_name):
        with open(file_name,"r") as rfile:
            read_student_info = rfile.readlines()
        for line in read_student_info:
            student_all.append(eval(line))
        if student_all:
            show_student(student_all)
    else:
        print("暂未保存数据信息...")

def modify():
    show()
    if os.path.exists(file_name):
        with open(file_name, "r") as rfile:
            read_student_info = rfile.readlines()
    else:
        return
    id=input("请输入要修改的学生ID：")
    with open(file_name,"w") as wfile:
        for student in read_student_info:
            temp_dict=dict(eval(student))
            if temp_dict["id"]==int(id):
                print("找到了这名学生，可以修改他的信息！")
                temp_dict["name"]=__get_int("请输入姓名：")
                temp_dict["english"]=__get_int("请输入英语成绩：")
                temp_dict["python"]=__get_int("请输入python成绩：")
                temp_dict["c"]=__get_int("请输入c语言成绩：")
                student=str(temp_dict)
                wfile.write(student+"\n")
                print("修改成功！")
            else:
                wfile.write(student+"\n")
    mark = input("是否继续修改其他学生信息？（y/n）：")
    if mark == "y":
        modify()  # 重新执行修改操作
    elif mark == 'n':
        print('结束修改')

def __get_int(message):
    while True:
        try:
            data = int(input(message))
            return data
        except:
            print("输入有误, 请重新输入.")


def sort():
    show()
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:  # 打开文件
            student_old = file.readlines()  # 读取全部内容
            student_new = []
        for list in student_old:
            d = dict(eval(list))  # 字符串转字典
            student_new.append(d)  # 将转换后的字典添加到列表中
    else:
        return
    ascORdesc = input("请选择（0升序；1降序）：")
    if ascORdesc == "0":  # 按升序排序
        ascORdescBool = False  # 标记变量，为False表示升序排序
    elif ascORdesc == "1":  # 按降序排序
        ascORdescBool = True  # 标记变量，为True表示降序排序
    else:
        print("您的输入有误，请重新输入！")
        sort()
    mode = input("请选择排序方式（1按英语成绩排序；2按Python成绩排序；3按C语言成绩排序；0按总成绩排序）：")
    if mode == "1":  # 按英语成绩排序
        IterableHelper.order_by_descending(student_new,lambda x: x["python"])
    elif mode == "2":  # 按Python成绩排序
        student_new.sort(key=lambda x: x["python"], reverse=ascORdescBool)
    elif mode == "3":  # 按C语言成绩排序
        student_new.sort(key=lambda x: x["c"], reverse=ascORdescBool)
    elif mode == "0":  # 按总成绩排序
        student_new.sort(key=lambda x: x["english"] + x["python"] + x["c"], reverse=ascORdescBool)
    else:
        print("您的输入有误，请重新输入！")
        sort()
    show_student(student_new)  # 显示排序结果


def total():
    if os.path.exists(file_name):  # 判断文件是否存在
        with open(file_name, 'r') as rfile:  # 打开文件
            student_old = rfile.readlines()  # 读取全部内容
            amount=IterableHelper.get_count(student_old,lambda student:student)
            print("一共有 %d 名学生！" % amount)

if __name__ == '__main__':
    main()
