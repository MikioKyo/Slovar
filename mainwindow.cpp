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

    QStringList nameFilter("*.txt"); // Фильтр по которому отделяют файлы
    QDir directory("C:/Users/Mikio/Desktop/slovar/slbase"); // Директория с файлами
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

void MainWindow::on_exitButton_clicked() // Кнопка выхода из программы
{
    exit(0);
}

void MainWindow::on_listWidget_itemClicked(QListWidgetItem *item)
{
    QString dir = ("C:/Users/Mikio/Desktop/slovar/slbase/"); // Путь до файла
    QString meti; // Название переменной
    meti=item->text(); // Присваиваем переменной значение нажатого предмета переведённого в текст
    dir.append(meti); // Складываем две переменные.
   // QMessageBox::information(0, "info", dir);



   // ui->listWidget->item->text();
   // meti.toLocal8Bit().constData() << endl;




    QFile listWidgetItem(dir);
    if(!listWidgetItem.open(QIODevice::ReadOnly)) // Если файл не откроется:
        QMessageBox::information(0, "Ошибка!", listWidgetItem.errorString()); // То вывести ошибку
    QTextStream in(&listWidgetItem); // переводим всё в текст стрим
    ui->textEdit->setText(in.readLine()); // скармливаем текст стрим для его открытия
    listWidgetItem.close(); // освобождаем память
}

void MainWindow::on_infoButton_clicked() // Справка
{
    //ui->verticalLayout->;
    //ui->verticalLayout->textBrowser->setText("Чтобы начать работу, выберите тему справа. Для добавления новых файлов... ляляля");
}
