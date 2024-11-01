cmake_minimum_required(VERSION 3.8)
project(node_demo)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

# 1. 
# find dependencies
# 查找头文件和库
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

set(dependences
    rclcpp
)
# 2. 添加可执行文件
add_executable(beacon src/node_demo.cc)
# 设置编译器特性
target_compile_features(beacon PUBLIC cxx_std_20)
# 3. 为 node 添加依赖
ament_target_dependencies(beacon ${dependences})

# 4. 将 cpp_node 拷贝到 install 目录下
# install/node_demo/lib/node_demo 这个目录下
install(TARGETS
  beacon
  DESTINATION lib/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
