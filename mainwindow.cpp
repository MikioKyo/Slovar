#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QString>
#include <QDir>
#include <iostream>
#include <cstdlib>
#include <QFile>
#include <QTextStream>
#include <QMessageBox>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    QStringList nameFilter("*.txt");
    QDir directory("C:/Users/Mikio/Desktop/slovar/slbase");
    QStringList txtFilesAndDirectories = directory.entryList(nameFilter);
    foreach (QString str, txtFilesAndDirectories) {
        //cout << str.toLocal8Bit().constData() << endl;
        ui->listWidget->addItem(str);
    }

}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_exitButton_clicked()
{
    exit(0);
}

void MainWindow::on_listWidget_itemClicked(QListWidgetItem *item)
{
    QString dir = ("C:/Users/Mikio/Desktop/slovar/slbase");
    //ui->listWidget->item->text();
   // meti.toLocal8Bit().constData() << endl;




    QFile open(meti);
    if(!meti.open(QIODevice::ReadOnly))
        QMessageBox::information(0, "info", meti.errorString());
    QTextStream in(meti);
    ui->textEdit->setText(in.readLine());
}
