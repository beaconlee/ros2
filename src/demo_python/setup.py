from setuptools import find_packages, setup

package_name = "demo_python"

setup(
    name=package_name,
    version="0.0.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        # 这个文件的作用是帮助 ament 索引工具来识别该功能包,
        #    并用于在 ros2 中注册和查找包资源
        """
          详细作用
          包注册:ROS 2 使用 ament_index 来管理包和资源。该空文件的存在是为了让 ament 知道该包是一个有效的 ROS 2 包，并确保在 ament 索引中可以找到该包。

          资源索引:ament_index 使用该文件来创建包的资源索引路径。这样，其他包或工具可以通过 ament_index API 来查找并使用该包中的资源(例如配置文件、Launch 文件等)，而不需要知道包的实际路径。

          结构约定:ROS 2 在功能包的目录结构中，要求 resource 文件夹下包含一个与包名相同的文件，以满足 ROS 2 工具链的查找机制。
        """
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="root",
    maintainer_email="bquanlicn@gmail.com",
    description="TODO: Package description",
    license="Apache-2.0",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": ["python_node=demo_python.node_python:main"],
    },
)
