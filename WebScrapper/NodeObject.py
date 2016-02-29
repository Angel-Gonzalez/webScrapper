#!/bin/python3
class NodeObject(object):
    """
    Hierarchical object representation
    """

    def __init__(self, name, parent=None):

        self._name = name
        self._children = []
        self._parent = parent

        if parent is not None:
            parent.append(self)

    @staticmethod
    def type_info():
        """
        Get the type of node
        :return: string
        """
        return "NODE"

    def append(self, child):
        """
        Append a NodeObject child
        :param child: NodeObject
        :return:
        """
        self._children.append(child)

    def insert(self, position: int, child):
        """
        Insert a NodeObject child into position
        :param position: int
        :param child: NodeObject
        :return: bool
        """
        if position < 0 or position > len(self._children):
            return False

        self._children.insert(position, child)
        child._parent = self
        return True

    def remove(self, position: int):
        """
        Remove a NodeObject child
        :param position: int
        :return: bool
        """
        if position < 0 or position > len(self._children):
            return False

        child = self._children.pop(position)
        child._parent = None

        return True

    @property
    def name(self):
        """
        Get the name of the current NodeObject
        :return: string
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Set the name of the current NodeObject
        :param name:
        :return:
        """
        self._name = name

    def child(self, row: int):
        """
        Get the NodeObject child in the position, zero based index
        :param row:
        :return: NodeObject
        """
        return self._children[row]

    def count(self):
        """
        Get the child count of the current NodeObject
        :return: int
        """
        return len(self._children)

    def parent(self):
        """
        Get the NodeObject of the current Node
        :return: NodeObject
        """
        return self._parent

    def row(self):
        """
        Get the zero based index position of the current NodeObject within its parent
        :return: int
        """
        if self._parent is not None:
            return self._parent._children.index(self)

    def log(self, tabLevel=-1):
        """
        String representation of the current Node Object
        :param tabLevel:
        :return: String
        """
        output = ""
        tabLevel += 1

        for i in range(tabLevel):
            output += "\t"

        output += self._name + "\n"

        for child in self._children:
            output += child.log(tabLevel)

        tabLevel -= 1

        return output

    def __repr__(self):
        return self.log()


class CountryNode(NodeObject):
    @staticmethod
    def type_info():
        return "COUNTRY"


class StateNode(NodeObject):
    @staticmethod
    def type_info():
        return "STATE"


class CityNode(NodeObject):
    @staticmethod
    def type_info():
        return "CITY"


class ZipNode(NodeObject):
    @staticmethod
    def type_info():
        return "ZIPCODE"


class CategoryNode(NodeObject):
    @staticmethod
    def type_info():
        return "CATEGORY"


class BusinessNode(NodeObject):
    def __init__(self, name, parent=None):
        super().__init__(name, parent)
        self.phone = ""
        self.address = ""
        self.fax = ""
        self.email = ""
        self.web = ""

    @staticmethod
    def type_info():
        return "BUSINESS"

    @property
    def phone(self):
        return self.phone

    @phone.setter
    def phone(self, value):
        self.phone = value

    @property
    def address(self):
        return self.address

    @address.setter
    def address(self, value):
        self.address = value

    @property
    def fax(self):
        return self.fax

    @fax.setter
    def fax(self, value):
        self.fax = value

    @property
    def email(self):
        return self.email

    @email.setter
    def email(self, value):
        self.email = value

    @property
    def web(self):
        return self.web

    @web.setter
    def web(self, value):
        self.web = value
