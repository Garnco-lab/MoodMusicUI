#include "mainwindow.h"

#include "ui_mainwindow.h"

#include <QtCore>

#include <QPixmap>

#include <QtDebug>

#include <QString>

#include <QTimer>

#include <QProcess>

#include <string>

#include <stdlib.h>

#include <stdio.h>

#include <QFuture>

class MyThread : public QThread {
    void run() override {
        system("cd C:\\Users\\Steven\\MoodMusic && python main.py");
    }
};



MainWindow::MainWindow(QWidget * parent): QMainWindow(parent), ui(new Ui::MainWindow) {
  ui -> setupUi(this);
  this->setStyleSheet("background-color: black;");

  int w = ui->label_pic->width();
  int h = ui->label_pic->height();

  QPixmap pix("C:/Users/Steven/Documents/MoodMusicUI/images/brain.png");
  ui -> label_pic -> setPixmap(pix.scaled(w, h, Qt::KeepAspectRatio));

  ui -> progressBar -> setValue(ui -> horizontalSlider -> value());
  connect(ui -> horizontalSlider, SIGNAL(valueChanged(int)), ui -> progressBar, SLOT(setValue(int)));

  MyThread *thread = new MyThread;
  thread->start();
//  QProcess process;
//  process.start("cmd.exe", QStringList() << "C:\\Users\\Steven\\MoodMusic && python main.py");
//  process.waitForFinished(-1);

}

MainWindow::~MainWindow() {
  delete ui;
}
