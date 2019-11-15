# -*- coding: utf-8 -*-
# TP5 - Thomas ROSSI & Emeric PAIN
from TP5_Python.db_column import Column


class Table:

    def __init__(self, table_name, table_columns=None):
        self.name = table_name
        self._columns = table_columns

    @property
    def columns(self):
        return self._columns

    @columns.setter
    def columns(self, value):
        for column in self._columns:
            assert type(self._columns) == Column, "columns must be of type 'Column'"
        self.columns = value

