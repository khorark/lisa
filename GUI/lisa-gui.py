#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lisa.py
#
#  Copyright 2015 Arkadiy <arkadiy@arkadiy-SVE1511T1RW>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import os
import shutil
import time
import sys
from windows import Ui_MainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import res


class Lisa_win(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setStyleSheet(open('style.qss').read())
        self.open_btn.clicked.connect(self.showDialog)
        self.actionOpen_Dir.triggered.connect(self.showDialog)
        self.actionExit.triggered.connect(exit)
        self.action_2.triggered.connect(self.help)
        self.actionAbout.triggered.connect(self.about)
        self.start_btn.clicked.connect(self.sorted)
        self.month_chb.setVisible(0)
        self.year_chb.setVisible(0)
        # self.date_rb.clicked.connect(self.show_options)
        # self.extens_rb.clicked.connect(self.show_options)

    def showDialog(self):
        try:
            self.progress_pg.setValue(0)
            dir_name = QFileDialog.getExistingDirectory(
                self, 'Open file')
            list_files = os.listdir(dir_name)
            self.dir_name_le.setText(dir_name)
            self.list_files_lw.clear()
            for i in list_files:
                item = QListWidgetItem(i)
                if os.path.isdir(os.path.join(dir_name, i)):
                    item.setIcon(QIcon(':/icons/icons/folder.png'))
                if os.path.isfile(os.path.join(dir_name, i)):
                    item.setIcon(QIcon(':/icons/icons/file.png'))
                self.list_files_lw.addItem(item)
        except:
            pass

    def show_options(self):
        if self.date_rb.isChecked():
            self.month_chb.setVisible(1)
            self.year_chb.setVisible(1)
        else:
            self.month_chb.setVisible(0)
            self.year_chb.setVisible(0)

    def sorted(self):
        if self.extens_rb.isChecked() or self.date_rb.isChecked():
            self.list_files_lw.clear()
            directory = self.dir_name_le.text()
            self.start_btn.setEnabled(0)
            if directory:
                files = os.listdir(directory)
                step_pb = 100 / len(files)
                if self.extens_rb.isChecked():
                    self.sort_by_ext(directory, files, step_pb)
                elif self.date_rb.isChecked():
                    self.sort_by_date(directory, files, step_pb)
                self.progress_pg.setValue(100)
                self.finish()
            else:
                QMessageBox.question(
                    self, 'Message', "Please select directory to sort", QMessageBox.Ok)
        else:
            QMessageBox.question(
                self, 'Message', "Please select type sort", QMessageBox.Ok)

    def finish(self):
        self.start_btn.setEnabled(1)
        QMessageBox.question(self, 'Message',
                             "All files by sorted", QMessageBox.Ok)

    def help(self):
        QMessageBox.question(
            self, 'Help', 'This programm written Python3. Sorted your files in directory by date or extension.\nSorted by date: /home/user/downloads ==> /home/user/downloads/years/month\nExample: /home/user/download/2015/July\nType sorted extension: /home/user/downloads/pdf', QMessageBox.Ok)

    def about(self):
        QMessageBox.question(
            self, 'About author', 'This is GUI interface for Lisa - Programm sorted your files\nAuthor: Khorark\nEmail: khorark@gmail.com\nVerion: 1.01 - 2016.03.10', QMessageBox.Ok)

    def sort_by_ext(self, directory, files, step_pb):
        for i in files:
            ext = os.path.splitext(i)
            if ext[1] != '':
                dst_dir = os.path.join(directory, ext[1][1:])
                if os.path.exists(dst_dir) == False:
                    os.mkdir(dst_dir)

                shutil.move(os.path.join(directory, i),
                            os.path.join(dst_dir, i))
                print('{} ==> {}'.format(os.path.join(
                    directory, i), os.path.join(dst_dir, i)))
                self.list_files_lw.addItem('{} ==> {}'.format(os.path.join(
                    directory, i), os.path.join(dst_dir, i)))
                self.progress_pg.setValue(
                    self.progress_pg.value() + step_pb)

    def sort_by_date(self, directory, files, step_pb):
        for i in files:
            abs_path = os.path.join(directory, i)
            if os.path.isdir(abs_path) == False:
                acc_time = time.gmtime(os.path.getmtime(abs_path))
                file_time_year = time.strftime('%Y', acc_time)
                file_time_month = time.strftime('%B', acc_time)

                dst_dir_year = os.path.join(directory, file_time_year)
                dst_dir_month = os.path.join(dst_dir_year, file_time_month)
                if os.path.exists(dst_dir_year) == False:
                    os.mkdir(dst_dir_year)
                if os.path.exists(dst_dir_month) == False:
                    os.mkdir(dst_dir_month)

                shutil.move(os.path.join(directory, i),
                            os.path.join(dst_dir_month, i))
                print('{} ==> {}'.format(
                    abs_path, os.path.join(dst_dir_month, i)))
                self.list_files_lw.addItem('{} ==> {}'.format(
                    abs_path, os.path.join(dst_dir_month, i)))
                self.progress_pg.setValue(
                    self.progress_pg.value() + step_pb)

    def sort_by_year(self, directory, files, step_pb):
        pass

    def sort_by_month(self, directory, files, step_pb):
        pass


if __name__ == '__main__':
    app = QApplication([])
    w = Lisa_win()
    w.show()
    app.exec_()
