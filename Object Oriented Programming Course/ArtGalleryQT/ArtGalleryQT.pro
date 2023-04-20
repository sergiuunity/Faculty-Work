QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

CONFIG += c++17

# You can make your code fail to compile if it uses deprecated APIs.
# In order to do so, uncomment the following line.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0

SOURCES += \
    controller/Repo_Controller.cpp \
    domain/Action.cpp \
    domain/Exhibit.cpp \
    main.cpp \
    mainwindow.cpp \
    repository/Gallery.cpp \
    testing/ActionTest.cpp \
    testing/ControllerTest.cpp \
    testing/ExhibitTest.cpp \
    testing/GalleryTest.cpp

HEADERS += \
    controller/Repo_Controller.h \
    domain/Action.h \
    domain/Exhibit.h \
    mainwindow.h \
    repository/Gallery.h \
    testing/ActionTest.h \
    testing/ControllerTest.h \
    testing/ExhibitTest.h \
    testing/GalleryTest.h

FORMS += \
    mainwindow.ui

# Default rules for deployment.
qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target

DISTFILES += \
    generated_files/data.csv \
    generated_files/generated_testing_fileOperations.csv
