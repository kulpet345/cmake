cmake_minimum_required(VERSION 2.8)

project(main_project)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11 -Wall")

set(SOURCE_EXE C/main.cpp C/main.h A/index.h)

include_directories(.)

find_package(PythonInterp 3 REQUIRED)
include_directories(${PythonInterp_INCLUDE_DIRS})

add_custom_command(
	WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}/A
	COMMAND ${PYTHON_EXECUTABLE} preparing.py
	DEPENDS A/preparing.py
	OUTPUT ${CMAKE_SOURCE_DIR}/A/index.h
)

add_subdirectory(B)

add_executable(main_project ${SOURCE_EXE})

target_link_libraries(main_project B_project)
