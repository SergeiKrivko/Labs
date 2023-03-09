import custom_random
import random
import struct
import os

import in_out


class DataBase:
    def __init__(self, file_name, columns_names=None, columns_format=None, column_width=None, sep=','):
        self.columns_names = columns_names
        self.columns_format = columns_format
        self.column_width = column_width
        self.file_name = file_name
        try:
            self.file = open(file_name, mode='a+')
        except FileNotFoundError:
            self.file = open(file_name, mode='w')
            self.file.close()
            self.file = open(file_name, mode='a+')
        self.sep = sep

    def print_data_base(self):
        self.file.seek(0)
        for line in self.file:
            a = line.strip().split(',')
            for i in range(len(a)):
                print('| {0:{1}}'.format(a[i], self.column_width[i]), end='')
            print(' |')

    def initialise(self):
        self.file.close()
        self.file = open(self.file_name, mode='w')
        self.file.close()
        self.file = open(self.file_name, mode='a+')

    def add_line(self, row):
        self.file.write(self.sep.join(map(str, row)))
        self.file.write('\n')

    def search(self, value):
        self.file.seek(0)
        res = []
        for line in self.file:
            a = line.split(',')
            for i in range(len(a)):
                a[i] = self.columns_format[i](a[i].strip())
            if a[0] == value:
                res.append(a)
        return res

    def two_column_search(self, value1, value2):
        self.file.seek(0)
        res = []
        for line in self.file:
            a = line.split(',')
            for i in range(len(a)):
                a[i] = self.columns_format[i](a[i].strip())
            if a[0] == value1 and a[1] == value2:
                res.append(a)
        return res


class DataBaseBin:
    def __init__(self, file_name, columns_names=None, columns_format=None, column_size=None):
        self.columns_names = columns_names
        self.columns_format = columns_format
        self.column_size = column_size
        self.file_name = file_name
        try:
            self.file = open(file_name, mode='br+')
        except FileNotFoundError:
            self.file = open(file_name, mode='bw')
            self.file.close()
            self.file = open(file_name, mode='br+')
        self.pack_format = ''
        self.row_size = 0
        for i in range(len(columns_format)):
            if columns_format[i] == str:
                self.pack_format += str(self.column_size[i]) + 's'
                self.row_size += self.column_size[i]
            elif columns_format[i] == int:
                if self.column_size[i] <= 2:
                    self.pack_format += 'h'
                    self.row_size += 2
                elif self.column_size[i] <= 4:
                    self.pack_format += 'i'
                    self.row_size += 4
                elif self.column_size[i] <= 8:
                    self.pack_format += 'q'
                    self.row_size += 8
            elif columns_format[i] == float:
                self.pack_format += 'f'
                self.row_size += 4
        self.size = os.path.getsize(self.file_name) // self.row_size

    def clear(self):
        self.file.close()
        self.file = open(self.file_name, 'bw')
        self.file.close()
        self.file = open(self.file_name, 'br+')

    def read_row(self, index=None):
        if index:
            self.file.seek(index)
        a = struct.unpack(self.pack_format, self.file.read(self.row_size))
        row = []
        for i in range(len(a)):
            if self.columns_format[i] == str:
                row.append(a[i].decode('utf-8'))
            else:
                row.append(a[i])
        return row

    def print(self):
        self.file.seek(0)
        for _ in range(self.size):
            row = self.read_row()
            for i in range(len(row)):
                if self.columns_format[i] == int or self.columns_format[i] == float:
                    print('| {0:10.5g}'.format(row[i]), end='')
                else:
                    print('| {0:{1}}'.format(row[i], self.column_size[i]), end='')
            print(' |')

    def input_row(self):
        row = []
        for i in range(len(self.columns_format)):
            while True:
                a = (in_out.input_value('Введите значение поля "{}"'.format(self.columns_names[i]),
                                        self.columns_format[i]))
                if self.columns_format[i] == str and len(a) > self.column_size[i]:
                    print('Слишком длинное значение')
                elif self.columns_format[i] == int and a > 2 ** (8 * self.column_size[i]):
                    print('Слишком большое число')
                else:
                    row.append(a)
                    break
        return row

    def add_row(self, row, index=None):
        if index is not None:
            if index >= 0:
                self.file.seek(index * self.row_size)
            else:
                self.file.seek((-index - 1) * self.row_size, 2)
        self.file.write(struct.pack(self.pack_format,
                                    '{:{}}'.format(row[0], self.column_size[0]).encode('utf-8'),
                                    '{:{}}'.format(row[1], self.column_size[1]).encode('utf-8'),
                                    row[2],
                                    '{:{}}'.format(row[3], self.column_size[3]).encode('utf-8')))
        self.size += 1

    def search(self, value):
        self.file.seek(0)
        for _ in range(self.size):
            row = self.read_row()
            if row[0].strip() == value:
                for i in range(len(row)):
                    if self.columns_format[i] == int or self.columns_format[i] == float:
                        print('| {0:10.5g}'.format(row[i]), end='')
                    else:
                        print('| {0:{1}}'.format(row[i], self.column_size[i]), end='')
                print(' |')

    def two_columns_search(self, value1, value2):
        self.file.seek(0)
        for _ in range(self.size):
            row = self.read_row()
            if row[0].strip() == value1 and row[2].strip() == value2:
                for i in range(len(row)):
                    if self.columns_format[i] == int or self.columns_format[i] == float:
                        print('| {0:10.5g}'.format(row[i]), end='')
                    else:
                        print('| {0:{1}}'.format(row[i], self.column_size[i]), end='')
                print(' |')
