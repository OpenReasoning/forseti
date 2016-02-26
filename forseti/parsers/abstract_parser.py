import abc


class AbstractParser(object):
    __metaclass__ = abc.ABCMeta

    @staticmethod
    @abc.abstractmethod
    def parse(statement, formula_types):
        """

        :param statement:
        :param formula_types:
        :return:
        """

