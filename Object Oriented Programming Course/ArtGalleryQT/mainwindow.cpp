#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "QMessageBox"

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setWindowTitle("Art Gallery Manager");
    controlla = GalleryController();
}

MainWindow::~MainWindow()
{
    delete ui;
}


void MainWindow::on_addButton_clicked()
{
    if(!(ui->lineEdit_1->text().isEmpty()) && !(ui->lineEdit_2->text().isEmpty()) && !(ui->lineEdit_3->text().isEmpty()) && !(ui->lineEdit_4->text().isEmpty()) && !(ui->lineEdit_5->text().isEmpty()) && !(ui->lineEdit_6->text().isEmpty()))
    {try
    {
        QString given_id, given_name, given_author, given_estimated_price, given_width, given_height;
        given_id = ui->lineEdit_1->text();
        given_name = ui->lineEdit_2->text();
        given_author = ui->lineEdit_3->text();
        given_estimated_price = ui->lineEdit_4->text();
        given_width = ui->lineEdit_5->text();
        given_height = ui->lineEdit_6->text();
        controlla.append(given_id.toStdString(), given_name.toStdString(), given_author.toStdString(), given_estimated_price.toInt(), given_width.toInt(), given_height.toInt());
        ui->paintings_table->setRowCount(ui->paintings_table->rowCount()+1);
        ui->paintings_table->setItem(ui->paintings_table->rowCount()-1,0, new QTableWidgetItem(given_id));
        ui->paintings_table->setItem(ui->paintings_table->rowCount()-1,1, new QTableWidgetItem(given_name));
        ui->paintings_table->setItem(ui->paintings_table->rowCount()-1,2, new QTableWidgetItem(given_author));
        ui->paintings_table->setItem(ui->paintings_table->rowCount()-1,3, new QTableWidgetItem(given_estimated_price));
        ui->paintings_table->setItem(ui->paintings_table->rowCount()-1,4, new QTableWidgetItem(given_width));
        ui->paintings_table->setItem(ui->paintings_table->rowCount()-1,5, new QTableWidgetItem(given_height));
    }
    catch (int x)
    {
        if (x == -2)
           QMessageBox::critical(this, "Error has occured", "Such painting already exists in the gallery.");
    }
    }
    else
    {
        QMessageBox::critical(this, "Error has occured", "Please fill all lines.");
    }

}


void MainWindow::on_removeButton_clicked()
{
    int r = ui->paintings_table->currentRow();
    if(ui->paintings_table->rowCount() == 0)
    {
       QMessageBox::critical(this, "Er  ror has occured", "There are no paintings in the gallery to be removed.");
    }
    else
    if(r!=-1)
       {
               try
                   {
                       controlla.remove_at_index(r);
                       ui->paintings_table->removeRow(r);

                   }
                   catch (int x)
                   {
                       if (x == -1)
                           QMessageBox::critical(this, "Error has occured", "An error has occured.");
                   }
           }
           else
           {
               QMessageBox::critical(this, "Error has occured", "Please select an painting to be removed.");
           }

}



void MainWindow::on_actionUndo_triggered()
{
    try
    {
        controlla.undo();
        this->update_table();
    }
                catch (int x)
                {
                    QMessageBox::critical(this, "Error has occured", "No add/remove operations have been done.");
                }

}


void MainWindow::on_actionRedo_triggered()
{
    try
    {
        controlla.redo();
        this->update_table();
    }
                catch (int x)
                {
                    QMessageBox::critical(this, "Error has occured", "No undo operations have been done.");
    }
}

void MainWindow::empty_table()
{
    ui->paintings_table->clear();
    while(ui->paintings_table->rowCount()!=0)
        ui->paintings_table->removeRow(0);
}

void MainWindow::update_table()
{
    this->empty_table();
    for(int i=0;i<controlla.size();i++)
    {
        QString given_id, given_name, given_author, given_estimated_price, given_width, given_height;
        Painting currentPainting = controlla.get(i);
        given_id = QString::fromStdString(currentPainting.getId());
        given_name = QString::fromStdString(currentPainting.getName());
        given_author = QString::fromStdString(currentPainting.getAuthor());
        given_estimated_price = QString::number(currentPainting.getEstimated_price());
        given_width = QString::number(currentPainting.getWidth());
        given_height = QString::number(currentPainting.getHeight());
        ui->paintings_table->setRowCount(ui->paintings_table->rowCount()+1);
        ui->paintings_table->setItem(ui->paintings_table->rowCount()-1,0, new QTableWidgetItem(given_id));
        ui->paintings_table->setItem(ui->paintings_table->rowCount()-1,1, new QTableWidgetItem(given_name));
        ui->paintings_table->setItem(ui->paintings_table->rowCount()-1,2, new QTableWidgetItem(given_author));
        ui->paintings_table->setItem(ui->paintings_table->rowCount()-1,3, new QTableWidgetItem(given_estimated_price));
        ui->paintings_table->setItem(ui->paintings_table->rowCount()-1,4, new QTableWidgetItem(given_width));
        ui->paintings_table->setItem(ui->paintings_table->rowCount()-1,5, new QTableWidgetItem(given_height));
    }
}

