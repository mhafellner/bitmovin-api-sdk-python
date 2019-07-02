# coding: utf-8

from bitmovin.models.input_stream import InputStream
from bitmovin.models.stream_selection_mode import StreamSelectionMode
import pprint
import six
from datetime import datetime
from datetime import date as validation_date
from enum import Enum


class DvbTeletextInputStream(InputStream):
    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    @property
    def openapi_types(self):
        types = super(DvbTeletextInputStream, self).openapi_types
        types.update({
            'input_id': 'str',
            'input_path': 'str',
            'selection_mode': 'StreamSelectionMode',
            'position': 'int',
            'page': 'int'
        })
        return types

    @property
    def attribute_map(self):
        attributes = super(DvbTeletextInputStream, self).attribute_map
        attributes.update({
            'input_id': 'inputId',
            'input_path': 'inputPath',
            'selection_mode': 'selectionMode',
            'position': 'position',
            'page': 'page'
        })
        return attributes

    def __init__(self, input_id=None, input_path=None, selection_mode=None, position=None, page=None, *args, **kwargs):
        super(DvbTeletextInputStream, self).__init__(*args, **kwargs)

        self._input_id = None
        self._input_path = None
        self._selection_mode = None
        self._position = None
        self._page = None
        self.discriminator = None

        if input_id is not None:
            self.input_id = input_id
        if input_path is not None:
            self.input_path = input_path
        if selection_mode is not None:
            self.selection_mode = selection_mode
        if position is not None:
            self.position = position
        if page is not None:
            self.page = page

    @property
    def input_id(self):
        """Gets the input_id of this DvbTeletextInputStream.

        Id of input

        :return: The input_id of this DvbTeletextInputStream.
        :rtype: str
        """
        return self._input_id

    @input_id.setter
    def input_id(self, input_id):
        """Sets the input_id of this DvbTeletextInputStream.

        Id of input

        :param input_id: The input_id of this DvbTeletextInputStream.
        :type: str
        """

        if input_id is not None:
            if not isinstance(input_id, str):
                raise TypeError("Invalid type for `input_id`, type has to be `str`")

        self._input_id = input_id


    @property
    def input_path(self):
        """Gets the input_path of this DvbTeletextInputStream.

        Path to media file

        :return: The input_path of this DvbTeletextInputStream.
        :rtype: str
        """
        return self._input_path

    @input_path.setter
    def input_path(self, input_path):
        """Sets the input_path of this DvbTeletextInputStream.

        Path to media file

        :param input_path: The input_path of this DvbTeletextInputStream.
        :type: str
        """

        if input_path is not None:
            if not isinstance(input_path, str):
                raise TypeError("Invalid type for `input_path`, type has to be `str`")

        self._input_path = input_path


    @property
    def selection_mode(self):
        """Gets the selection_mode of this DvbTeletextInputStream.

        Specifies the algorithm how the stream in the input file will be selected

        :return: The selection_mode of this DvbTeletextInputStream.
        :rtype: StreamSelectionMode
        """
        return self._selection_mode

    @selection_mode.setter
    def selection_mode(self, selection_mode):
        """Sets the selection_mode of this DvbTeletextInputStream.

        Specifies the algorithm how the stream in the input file will be selected

        :param selection_mode: The selection_mode of this DvbTeletextInputStream.
        :type: StreamSelectionMode
        """

        if selection_mode is not None:
            if not isinstance(selection_mode, StreamSelectionMode):
                raise TypeError("Invalid type for `selection_mode`, type has to be `StreamSelectionMode`")

        self._selection_mode = selection_mode


    @property
    def position(self):
        """Gets the position of this DvbTeletextInputStream.

        Position of the stream

        :return: The position of this DvbTeletextInputStream.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this DvbTeletextInputStream.

        Position of the stream

        :param position: The position of this DvbTeletextInputStream.
        :type: int
        """

        if position is not None:
            if not isinstance(position, int):
                raise TypeError("Invalid type for `position`, type has to be `int`")

        self._position = position


    @property
    def page(self):
        """Gets the page of this DvbTeletextInputStream.

        Page number of the subtitles

        :return: The page of this DvbTeletextInputStream.
        :rtype: int
        """
        return self._page

    @page.setter
    def page(self, page):
        """Sets the page of this DvbTeletextInputStream.

        Page number of the subtitles

        :param page: The page of this DvbTeletextInputStream.
        :type: int
        """

        if page is not None:
            if not isinstance(page, int):
                raise TypeError("Invalid type for `page`, type has to be `int`")

        self._page = page

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = super(DvbTeletextInputStream, self).to_dict()

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[self.attribute_map.get(attr)] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[self.attribute_map.get(attr)] = value.to_dict()
            elif isinstance(value, Enum):
                result[self.attribute_map.get(attr)] = value.value
            elif isinstance(value, dict):
                result[self.attribute_map.get(attr)] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[self.attribute_map.get(attr)] = value
            if issubclass(DvbTeletextInputStream, dict):
                for key, value in self.items():
                    result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DvbTeletextInputStream):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other