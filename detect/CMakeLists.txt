cmake_minimum_required(VERSION 3.10)
project(RMArmorDetect)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 找 OpenCV
find_package(OpenCV REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

# 添加可执行文件
add_executable(main src/main.cpp)

# 链接 OpenCV
target_link_libraries(main ${OpenCV_LIBS})