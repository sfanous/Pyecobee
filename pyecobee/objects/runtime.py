"""
This module is home to the Runtime class
"""
from pyecobee.ecobee_object import EcobeeObject


class Runtime(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/Runtime.shtml

    Attribute names have been generated by converting ecobee property names from camelCase to snake_case.

    A getter property has been generated for each attribute.
    A setter property has been generated for each attribute whose value of READONLY is "no".

    An __init__ argument without a default value has been generated if the value of REQUIRED is "yes".
    An __init__ argument with a default value of None has been generated if the value of REQUIRED is "no".
   """
    __slots__ = ['_runtime_rev', '_connected', '_first_connected', '_connect_date_time', '_disconnect_date_time',
                 '_last_modified', '_last_status_modified', '_runtime_date', '_runtime_interval', '_actual_temperature',
                 '_actual_humidity', '_raw_temperature', '_show_icon_mode',
                 '_desired_heat', '_desired_cool', '_desired_humidity', '_desired_dehumidity',
                 '_desired_fan_mode', '_desired_heat_range', '_desired_cool_range']

    attribute_name_map = {'runtime_rev': 'runtimeRev', 'runtimeRev': 'runtime_rev', 'connected': 'connected',
                          'first_connected': 'firstConnected', 'firstConnected': 'first_connected',
                          'connect_date_time': 'connectDateTime', 'connectDateTime': 'connect_date_time',
                          'disconnect_date_time': 'disconnectDateTime', 'disconnectDateTime': 'disconnect_date_time',
                          'last_modified': 'lastModified', 'lastModified': 'last_modified',
                          'last_status_modified': 'lastStatusModified', 'lastStatusModified': 'last_status_modified',
                          'runtime_date': 'runtimeDate', 'runtimeDate': 'runtime_date',
                          'runtime_interval': 'runtimeInterval', 'runtimeInterval': 'runtime_interval',
                          'actual_temperature': 'actualTemperature', 'actualTemperature': 'actual_temperature',
                          'actual_humidity': 'actualHumidity', 'actualHumidity': 'actual_humidity',
                          'raw_temperature': 'rawTemperature', 'rawTemperature': 'raw_temperature',
                          'show_icon_mode': 'showIconMode', 'showIconMode': 'show_icon_mode',
                          'desired_heat': 'desiredHeat', 'desiredHeat': 'desired_heat', 'desired_cool': 'desiredCool',
                          'desiredCool': 'desired_cool', 'desired_humidity': 'desiredHumidity',
                          'desiredHumidity': 'desired_humidity', 'desired_dehumidity': 'desiredDehumidity',
                          'desiredDehumidity': 'desired_dehumidity', 'desired_fan_mode': 'desiredFanMode',
                          'desiredFanMode': 'desired_fan_mode', 'desired_heat_range': 'desiredHeatRange',
                          'desiredHeatRange': 'desired_heat_range', 'desired_cool_range': 'desiredCoolRange',
                          'desiredCoolRange': 'desired_cool_range'}

    attribute_type_map = {'runtime_rev': 'six.text_type', 'connected': 'bool', 'first_connected': 'six.text_type',
                          'connect_date_time': 'six.text_type', 'disconnect_date_time': 'six.text_type',
                          'last_modified': 'six.text_type', 'last_status_modified': 'six.text_type',
                          'runtime_date': 'six.text_type', 'runtime_interval': 'int', 'actual_temperature': 'int',
                          'actual_humidity': 'int', 'raw_temperature': 'int', 'show_icon_mode': 'int',
                          'desired_heat': 'int', 'desired_cool': 'int',
                          'desired_humidity': 'int', 'desired_dehumidity': 'int', 'desired_fan_mode': 'six.text_type',
                          'desired_heat_range': 'List[int]', 'desired_cool_range': 'List[int]'}

    def __init__(self, runtime_rev=None, connected=None, first_connected=None, connect_date_time=None,
                 disconnect_date_time=None, last_modified=None, last_status_modified=None, runtime_date=None,
                 runtime_interval=None, actual_temperature=None, actual_humidity=None, raw_temperature=None,
                 show_icon_mode=None, desired_heat=None,
                 desired_cool=None, desired_humidity=None, desired_dehumidity=None, desired_fan_mode=None,
                 desired_heat_range=None, desired_cool_range=None):
        """
        Construct a Runtime instance
        """
        self._runtime_rev = runtime_rev
        self._connected = connected
        self._first_connected = first_connected
        self._connect_date_time = connect_date_time
        self._disconnect_date_time = disconnect_date_time
        self._last_modified = last_modified
        self._last_status_modified = last_status_modified
        self._runtime_date = runtime_date
        self._runtime_interval = runtime_interval
        self._actual_temperature = actual_temperature
        self._actual_humidity = actual_humidity
        self._raw_temperature = raw_temperature
        self._show_icon_mode = show_icon_mode
        self._desired_heat = desired_heat
        self._desired_cool = desired_cool
        self._desired_humidity = desired_humidity
        self._desired_dehumidity = desired_dehumidity
        self._desired_fan_mode = desired_fan_mode
        self._desired_heat_range = desired_heat_range
        self._desired_cool_range = desired_cool_range

    @property
    def runtime_rev(self):
        """
        Gets the runtime_rev attribute of this Runtime instance.

        :return: The value of the runtime_rev attribute of this Runtime instance.
        :rtype: six.text_type
        """

        return self._runtime_rev

    @property
    def connected(self):
        """
        Gets the connected attribute of this Runtime instance.

        :return: The value of the connected attribute of this Runtime instance.
        :rtype: bool
        """

        return self._connected

    @property
    def first_connected(self):
        """
        Gets the first_connected attribute of this Runtime instance.

        :return: The value of the first_connected attribute of this Runtime instance.
        :rtype: six.text_type
        """

        return self._first_connected

    @property
    def connect_date_time(self):
        """
        Gets the connect_date_time attribute of this Runtime instance.

        :return: The value of the connect_date_time attribute of this Runtime instance.
        :rtype: six.text_type

        Sets the connect_date_time attribute of this Runtime instance.

        :param connect_date_time: The connect_date_time value to set for the connect_date_time attribute of this Runtime instance.
        :type: six.text_type
        """

        return self._connect_date_time

    @connect_date_time.setter
    def connect_date_time(self, connect_date_time):
        self._connect_date_time = connect_date_time

    @property
    def disconnect_date_time(self):
        """
        Gets the disconnect_date_time attribute of this Runtime instance.

        :return: The value of the disconnect_date_time attribute of this Runtime instance.
        :rtype: six.text_type

        Sets the disconnect_date_time attribute of this Runtime instance.

        :param disconnect_date_time: The disconnect_date_time value to set for the disconnect_date_time attribute of this Runtime instance.
        :type: six.text_type
        """

        return self._disconnect_date_time

    @disconnect_date_time.setter
    def disconnect_date_time(self, disconnect_date_time):
        self._disconnect_date_time = disconnect_date_time

    @property
    def last_modified(self):
        """
        Gets the last_modified attribute of this Runtime instance.

        :return: The value of the last_modified attribute of this Runtime instance.
        :rtype: six.text_type
        """

        return self._last_modified

    @property
    def last_status_modified(self):
        """
        Gets the last_status_modified attribute of this Runtime instance.

        :return: The value of the last_status_modified attribute of this Runtime instance.
        :rtype: six.text_type
        """

        return self._last_status_modified

    @property
    def runtime_date(self):
        """
        Gets the runtime_date attribute of this Runtime instance.

        :return: The value of the runtime_date attribute of this Runtime instance.
        :rtype: six.text_type
        """

        return self._runtime_date

    @property
    def runtime_interval(self):
        """
        Gets the runtime_interval attribute of this Runtime instance.

        :return: The value of the runtime_interval attribute of this Runtime instance.
        :rtype: int
        """

        return self._runtime_interval

    @property
    def actual_temperature(self):
        """
        Gets the actual_temperature attribute of this Runtime instance.

        :return: The value of the actual_temperature attribute of this Runtime instance.
        :rtype: int
        """

        return self._actual_temperature

    @property
    def raw_temperature(self):
        """
        Gets the raw_temperature attribute of this Runtime instance.

        :return: The value of the raw_temperature attribute of this Runtime instance.
        :rtype: int
        """

        return self._raw_temperature

    @property
    def show_icon_mode(self):
        """
        Gets the show_icon_mode attribute of this Runtime instance.

        :return: The value of the show_icon_mode attribute of this Runtime instance.
        :rtype: int
        """

        return self._show_icon_mode

    @property
    def actual_humidity(self):
        """
        Gets the actual_humidity attribute of this Runtime instance.

        :return: The value of the actual_humidity attribute of this Runtime instance.
        :rtype: int
        """

        return self._actual_humidity

    @property
    def desired_heat(self):
        """
        Gets the desired_heat attribute of this Runtime instance.

        :return: The value of the desired_heat attribute of this Runtime instance.
        :rtype: int
        """

        return self._desired_heat

    @property
    def desired_cool(self):
        """
        Gets the desired_cool attribute of this Runtime instance.

        :return: The value of the desired_cool attribute of this Runtime instance.
        :rtype: int
        """

        return self._desired_cool

    @property
    def desired_humidity(self):
        """
        Gets the desired_humidity attribute of this Runtime instance.

        :return: The value of the desired_humidity attribute of this Runtime instance.
        :rtype: int
        """

        return self._desired_humidity

    @property
    def desired_dehumidity(self):
        """
        Gets the desired_dehumidity attribute of this Runtime instance.

        :return: The value of the desired_dehumidity attribute of this Runtime instance.
        :rtype: int
        """

        return self._desired_dehumidity

    @property
    def desired_fan_mode(self):
        """
        Gets the desired_fan_mode attribute of this Runtime instance.

        :return: The value of the desired_fan_mode attribute of this Runtime instance.
        :rtype: six.text_type
        """

        return self._desired_fan_mode

    @property
    def desired_heat_range(self):
        """
        Gets the desired_heat_range attribute of this Runtime instance.

        :return: The value of the desired_heat_range attribute of this Runtime instance.
        :rtype: List[int]
        """

        return self._desired_heat_range

    @property
    def desired_cool_range(self):
        """
        Gets the desired_cool_range attribute of this Runtime instance.

        :return: The value of the desired_cool_range attribute of this Runtime instance.
        :rtype: List[int]
        """

        return self._desired_cool_range
