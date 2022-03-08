cmake_minimum_required(VERSION 3.21)
project(MoodMusicUI)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(MoodMusicUI
        main.cpp
        mainwindow.cpp
        mainwindow.h)
