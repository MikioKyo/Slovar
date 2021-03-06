#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QListWidgetItem>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_exitButton_clicked();

    void on_listWidget_itemClicked(QListWidgetItem *item);

    void on_infoButton_clicked();

private:
    Ui::MainWindow *ui;
private slots:
    void buttonOn();
    void on_answerButton_clicked();
};

#endif // MAINWINDOW_H
