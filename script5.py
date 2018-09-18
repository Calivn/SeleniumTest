# -*- coding: utf-8 -*-

from selenium import webdriver
import csv


date_file = 'www.csv'
date = csv.reader(open(date_file, 'r'))

for user in date:
    print(user[1])