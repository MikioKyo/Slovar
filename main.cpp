#include "mainwindow.h"
#include <QApplication>
#include <QStringList>
#include <QString>
#include <QDir>
#include <iostream>
#include <cstdlib>
using namespace std;

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    MainWindow w;
    w.show();

    QStringList nameFilter("*.txt");
    QDir directory("C:/Users/Mikio/Desktop/slovar/slbase");
    QStringList txtFilesAndDirectories = directory.entryList(nameFilter);
    foreach (QString str, txtFilesAndDirectories) {
        // cout << str.toLocal8Bit().constData() << endl;
    }
    return a.exec();
}
