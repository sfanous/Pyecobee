"""
This module is home to the VoiceEngine class
"""
from pyecobee.ecobee_object import EcobeeObject


class VoiceEngine(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/VoiceEngine.shtml

    Attribute names have been generated by converting ecobee property
    names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value
    of READONLY is "no".

    An __init__ argument without a default value has been generated if
    the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated
    if the value of REQUIRED is "no".
    """

    __slots__ = ['_name', '_enabled']

    attribute_name_map = {'name': 'name', 'enabled': 'enabled'}

    attribute_type_map = {'name': 'six.text_type', 'enabled': 'bool'}

    def __init__(self, name=None, enabled=None):
        """
        Construct a VoiceEngine instance
        """
        self._name = name
        self._enabled = enabled

    @property
    def name(self):
        """
        Gets the name attribute of this VoiceEngine instance.

        :return: The value of the name attribute of this VoiceEngine
        instance.
        :rtype: six.text_type
        """

        return self._name

    @property
    def enabled(self):
        """
        Gets the enabled attribute of this VoiceEngine instance.

        :return: The value of the enabled attribute of this VoiceEngine
        instance.
        :rtype: bool
        """

        return self._enabled
