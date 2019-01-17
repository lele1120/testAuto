# -*- coding: utf-8 -*-
import os


class Config:
    # path
    path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))

    def __init__(self):
        self.xml_report_path = Config.path_dir+'/Report/xml'
        self.html_report_path = Config.path_dir+'/Report/html'


if __name__ == '__main__':
    print(path_dir)
