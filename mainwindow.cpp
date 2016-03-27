#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QString>
#include <QDir>
#include <iostream>
#include <cstdlib>
#include <QFile>
#include <QTextStream>
#include <QMessageBox>
#include <QHBoxLayout>
#include "QTime"
#

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

    QFile listWidgetItem(dir);
    if(!listWidgetItem.open(QIODevice::ReadOnly)) // Если файл не откроется:
        QMessageBox::information(0, "Ошибка!", listWidgetItem.errorString()); // То вывести ошибку
    QTextStream in(&listWidgetItem); // переводим всё в текст стрим
    QString text_label = in.readLine();
    ui->nameLabel->setText(text_label);
    QString line;

    do {
        line = in.readLine();
        QStringList list1 = line.split(";");
      //  QMessageBox::information(0, "!!!!", line);

        if (list1.count() == 3){
        ui->textEdit->setText(list1[0]);
        ui->answerButton->setText(list1[1]);
        ui->answerButton_2->setText(list1[2]);
        QTime midnight(0,0,0);
        qsrand(midnight.secsTo(QTime::currentTime()));
        int qrand();
        bool buttonOn;
        buttonOn = false;
 //       QObject::connect(&ui->answerButton, SIGNAL(clicked()), &buttonOn, SLOT());
        QCoreApplication::processEvents();

}
        else;



    } while (!line.isNull());

    listWidgetItem.close(); // освобождаем память

}

void MainWindow::on_infoButton_clicked() // Справка
{
    QWidget *layout = new QWidget;
    QTextEdit *infoText = new QTextEdit;
    QHBoxLayout *infoWindow = new QHBoxLayout;
    layout->setLayout(infoWindow);
    infoWindow->addWidget(infoText);
    infoText->setReadOnly(true);
    infoText->setText("Пробная справкагнрн7гр67горпамиигнр67отттттттттттть");
    layout->show();
}

void MainWindow::buttonOn()
{
    QMessageBox::information(this, "Title", "Hello World!");
}
