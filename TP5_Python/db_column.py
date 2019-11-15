# -*- coding: utf-8 -*-
# TP5 - Thomas ROSSI & Emeric PAIN


class Types:

    def __init__(self):
        self._available_types = {"String": "VARCHAR(64)", "Integer": "INTEGER", "Float": "FLOAT"}

    @property
    def available_types(self):
        return self._available_types

    @available_types.setter
    def available_type(self):
        pass

    @available_types.getter
    def available_type(self):
        return self.available_types()


class Column:

    def __init__(self, data_type=Types.available_types["String"]):
        self._values = None
        assert data_type in self.available_types.values()
        self._data_type = data_type

    @property
    def data_type(self):
        return self._data_type

    @data_type.setter
    def data_type(self):
        pass

    @data_type.getter
    def data_type(self):
        return self.data_type()

    @property
    def values(self):
        return self._values

    @values.setter
    def values(self, value):
        assert type(value) == list, "Column values must be a list"

    @values.getter
    def values(self):
        return self.values()
