#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>

#include "controller/Repo_Controller.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:



    void on_addButton_clicked();

    void on_removeButton_clicked();

    void on_actionUndo_triggered();

    void on_actionRedo_triggered();

    void empty_table();

    void update_table();

private:
    GalleryController controlla;
    Ui::MainWindow *ui;
};
#endif // MAINWINDOW_H
