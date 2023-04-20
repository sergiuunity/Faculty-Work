#include "mainwindow.h"
#include "testing/ActionTest.h"
#include "testing/ExhibitTest.h"
#include "testing/GalleryTest.h"
#include "testing/ControllerTest.h"

#include <QApplication>


int main(int argc, char *argv[])
{
    ActionTest::runAllTests();
        ExhibitTest::runAllTests();
        PaintingTest::runAllTests();
        GalleryTest::runAllTests();
        ControllerTest::runAllTests();

    QApplication a(argc, argv);
    MainWindow w;
    w.show();
    return a.exec();
}
