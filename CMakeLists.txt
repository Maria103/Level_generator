cmake_minimum_required(VERSION 3.12)

project(coursework_melnikova)

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY${CMAKE_CURRENT_SOURCE_DIR}/bin)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_DEBUG${CMAKE_CURRENT_SOURCE_DIR}/bin.dbg)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELEASE${CMAKE_CURRENT_SOURCE_DIR}/bin.rel)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY_RELWITHDEBINFO${CMAKE_CURRENT_SOURCE_DIR}/bin.relwithdbg)

include_directories(
  prj.lab
)

add_subdirectory(prj.lab)



