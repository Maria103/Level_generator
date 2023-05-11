add_library(
    level_generator
    level_generator.h
    level_generator.cpp
)

add_executable(
    level_generator_app
    level_generator_app.cpp
)

target_link_libraries(
    level_generator_app
    level_generator
)

# check if Doxygen is installed
find_package(Doxygen)
if (DOXYGEN_FOUND)
    # set input and output files
    set(DOXYGEN_IN ${CMAKE_CURRENT_SOURCE_DIR}/Doxyfile)
    set(DOXYGEN_OUT ${CMAKE_CURRENT_BINARY_DIR}/Doxyfile.in)

    # request to configure the file
    configure_file(${DOXYGEN_IN} ${DOXYGEN_OUT} @ONLY)
    message("Doxygen build started")

    # note the option ALL which allows to build the docs together with the application
    add_custom_target( doc_doxygen ALL
        COMMAND ${DOXYGEN_EXECUTABLE} ${DOXYGEN_OUT}
        WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
        COMMENT "Generating API documentation with Doxygen"
        VERBATIM )
else (DOXYGEN_FOUND)
  message("Doxygen need to be installed to generate the doxygen documentation")
endif (DOXYGEN_FOUND)

install(TARGETS level_generator_app DESTINATION out DESTINATION images DESTINATION lib DESTINATION bin)
install(FILES PacmanGAME.py DESTINATION bin)
install(FILES level_generator.h DESTINATION lib)
install(FILES level_generator.cpp DESTINATION lib)
install(FILES new_level.txt DESTINATION out)
install(FILES headdown.png DESTINATION images)
install(FILES headup.png DESTINATION images)
install(FILES headleft.png DESTINATION images)
install(FILES headright.png DESTINATION images)
install(FILES snakebody.png DESTINATION images)
install(FILES apple.png DESTINATION images)
install(FILES wall.png DESTINATION images)