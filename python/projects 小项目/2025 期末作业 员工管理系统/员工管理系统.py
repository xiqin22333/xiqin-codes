class Employee:
    """员工类，用于表示员工的基本信息"""

    def __init__(self, emp_id, name, department, phone):
        """
        初始化员工对象
        emp_id: 工号
        name: 姓名
        department: 部门
        phone: 联系方式
        """
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.phone = phone

    def display_info(self):
        """显示员工信息"""
        print(f"工号: {self.emp_id}")
        print(f"姓名: {self.name}")
        print(f"部门: {self.department}")
        print(f"联系方式: {self.phone}")
        print("-" * 40)


class EmployeeManagementSystem:
    """员工信息管理系统类"""

    def __init__(self):
        """初始化系统，创建员工列表"""
        self.employees = []

    def show_menu(self):
        """显示主菜单"""
        print("\n" + "=" * 40)
        print("员工信息管理系统")
        print("=" * 40)
        print("1. 添加员工")
        print("2. 删除员工")
        print("3. 修改员工信息")
        print("4. 查询员工信息")
        print("5. 显示所有员工")
        print("0. 退出系统")
        print("=" * 40)

    def add_employee(self):
        """添加员工功能"""
        print("\n" + "=" * 40)
        print("添加员工信息")
        print("=" * 40)

        # 获取员工信息
        emp_id = input("请输入工号: ")

        # 检查工号是否已存在
        for employee in self.employees:
            if employee.emp_id == emp_id:
                print("错误：该工号已存在！")
                return False

        name = input("请输入姓名: ")
        department = input("请输入部门: ")
        phone = input("请输入联系方式: ")

        # 创建员工对象
        new_employee = Employee(emp_id, name, department, phone)

        # 添加到员工列表
        self.employees.append(new_employee)
        print(f"员工 {name} 添加成功！")
        return True

    def delete_employee(self):
        """删除员工功能"""
        print("\n" + "=" * 40)
        print("删除员工信息")
        print("=" * 40)

        if len(self.employees) == 0:
            print("系统中暂无员工信息！")
            return False

        emp_id = input("请输入要删除的员工工号: ")

        # 查找并删除员工
        found = False
        for i in range(len(self.employees)):
            if self.employees[i].emp_id == emp_id:
                found = True
                print(f"找到员工: {self.employees[i].name}")
                confirm = input("确定要删除吗？(y/n): ")

                if confirm.lower() == 'y':
                    deleted_name = self.employees[i].name
                    del self.employees[i]
                    print(f"员工 {deleted_name} 已删除！")
                    return True
                else:
                    print("删除操作已取消")
                    return False

        if not found:
            print(f"未找到工号为 {emp_id} 的员工")
            return False

    def update_employee(self):
        """修改员工信息功能"""
        print("\n" + "=" * 40)
        print("修改员工信息")
        print("=" * 40)

        if len(self.employees) == 0:
            print("系统中暂无员工信息！")
            return False

        emp_id = input("请输入要修改的员工工号: ")

        # 查找员工
        found = False
        for employee in self.employees:
            if employee.emp_id == emp_id:
                found = True
                print("当前员工信息:")
                employee.display_info()

                print("\n请输入新的员工信息（直接回车保持原值）:")
                new_name = input(f"姓名 [{employee.name}]: ")
                new_department = input(f"部门 [{employee.department}]: ")
                new_phone = input(f"联系方式 [{employee.phone}]: ")

                # 更新信息
                if new_name:
                    employee.name = new_name
                if new_department:
                    employee.department = new_department
                if new_phone:
                    employee.phone = new_phone

                print("员工信息更新成功！")
                return True

        if not found:
            print(f"未找到工号为 {emp_id} 的员工")
            return False

    def search_employee(self):
        """查询员工信息功能"""
        print("\n" + "=" * 40)
        print("查询员工信息")
        print("=" * 40)

        if len(self.employees) == 0:
            print("系统中暂无员工信息！")
            return False

        print("1. 按工号查询")
        print("2. 按部门查询")
        print("3. 返回主菜单")

        choice = input("请选择查询方式 (1-3): ")

        if choice == "1":
            # 按工号查询
            emp_id = input("请输入工号: ")
            found = False
            for employee in self.employees:
                if employee.emp_id == emp_id:
                    found = True
                    print("\n查询结果:")
                    employee.display_info()
                    break

            if not found:
                print(f"未找到工号为 {emp_id} 的员工")

        elif choice == "2":
            # 按部门查询
            department = input("请输入部门名称: ")
            found_employees = []

            for employee in self.employees:
                if employee.department == department:
                    found_employees.append(employee)

            if len(found_employees) > 0:
                print(f"\n{department} 部门的员工 ({len(found_employees)}人):")
                print("-" * 40)
                for employee in found_employees:
                    print(f"工号: {employee.emp_id}, 姓名: {employee.name}, 联系方式: {employee.phone}")
                print("-" * 40)
            else:
                print(f"未找到 {department} 部门的员工")

        elif choice == "3":
            return True

        else:
            print("无效选择！")

        return True

    def show_all_employees(self):
        """显示所有员工信息"""
        print("\n" + "=" * 40)
        print("所有员工信息")
        print("=" * 40)

        if len(self.employees) == 0:
            print("系统中暂无员工信息！")
        else:
            # 按部门分组显示
            departments = {}
            for employee in self.employees:
                if employee.department not in departments:
                    departments[employee.department] = []
                departments[employee.department].append(employee)

            # 显示每个部门的员工
            for department, emp_list in departments.items():
                print(f"\n【{department}】部门 ({len(emp_list)}人):")
                print("-" * 40)
                for employee in emp_list:
                    print(f"  工号: {employee.emp_id}, 姓名: {employee.name}, 联系方式: {employee.phone}")

            print(f"\n总计: {len(self.employees)} 名员工")

    def run(self):
        """运行员工信息管理系统"""
        # 添加一些示例数据
        self.employees.append(Employee("001", "张三", "技术部", "13800138000"))
        self.employees.append(Employee("002", "李四", "市场部", "13900139000"))
        self.employees.append(Employee("003", "王五", "技术部", "13700137000"))
        self.employees.append(Employee("004", "赵六", "人事部", "13600136000"))

        while True:
            self.show_menu()

            choice = input("请选择操作 (0-5): ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.delete_employee()
            elif choice == "3":
                self.update_employee()
            elif choice == "4":
                self.search_employee()
            elif choice == "5":
                self.show_all_employees()
            elif choice == "0":
                print("感谢使用员工信息管理系统，再见！")
                break
            else:
                print("无效选择，请重新输入！")


# 主程序入口
if __name__ == "__main__":
    # 创建员工管理系统对象
    system = EmployeeManagementSystem()
    # 运行系统
    system.run()
# 1