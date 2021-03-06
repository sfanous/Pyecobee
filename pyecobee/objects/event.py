"""
This module is home to the Event class
"""
from pyecobee.ecobee_object import EcobeeObject


class Event(EcobeeObject):
    """
    This class has been auto generated by scraping
    https://www.ecobee.com/home/developer/api/documentation/v1/objects/Event.shtml

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

    __slots__ = [
        '_type',
        '_name',
        '_running',
        '_start_date',
        '_start_time',
        '_end_date',
        '_end_time',
        '_is_occupied',
        '_is_cool_off',
        '_is_heat_off',
        '_cool_hold_temp',
        '_heat_hold_temp',
        '_fan',
        '_vent',
        '_ventilator_min_on_time',
        '_is_optional',
        '_is_temperature_relative',
        '_cool_relative_temp',
        '_heat_relative_temp',
        '_is_temperature_absolute',
        '_duty_cycle_percentage',
        '_fan_min_on_time',
        '_occupied_sensor_active',
        '_unoccupied_sensor_active',
        '_dr_ramp_up_temp',
        '_dr_ramp_up_time',
        '_link_ref',
        '_hold_climate_ref',
        '_fan_speed',
    ]

    attribute_name_map = {
        'type': 'type',
        'name': 'name',
        'running': 'running',
        'start_date': 'startDate',
        'startDate': 'start_date',
        'start_time': 'startTime',
        'startTime': 'start_time',
        'end_date': 'endDate',
        'endDate': 'end_date',
        'end_time': 'endTime',
        'endTime': 'end_time',
        'is_occupied': 'isOccupied',
        'isOccupied': 'is_occupied',
        'is_cool_off': 'isCoolOff',
        'isCoolOff': 'is_cool_off',
        'is_heat_off': 'isHeatOff',
        'isHeatOff': 'is_heat_off',
        'cool_hold_temp': 'coolHoldTemp',
        'coolHoldTemp': 'cool_hold_temp',
        'heat_hold_temp': 'heatHoldTemp',
        'heatHoldTemp': 'heat_hold_temp',
        'fan': 'fan',
        'vent': 'vent',
        'ventilator_min_on_time': 'ventilatorMinOnTime',
        'ventilatorMinOnTime': 'ventilator_min_on_time',
        'is_optional': 'isOptional',
        'isOptional': 'is_optional',
        'is_temperature_relative': 'isTemperatureRelative',
        'isTemperatureRelative': 'is_temperature_relative',
        'cool_relative_temp': 'coolRelativeTemp',
        'coolRelativeTemp': 'cool_relative_temp',
        'heat_relative_temp': 'heatRelativeTemp',
        'heatRelativeTemp': 'heat_relative_temp',
        'is_temperature_absolute': 'isTemperatureAbsolute',
        'isTemperatureAbsolute': 'is_temperature_absolute',
        'duty_cycle_percentage': 'dutyCyclePercentage',
        'dutyCyclePercentage': 'duty_cycle_percentage',
        'fan_min_on_time': 'fanMinOnTime',
        'fanMinOnTime': 'fan_min_on_time',
        'occupied_sensor_active': 'occupiedSensorActive',
        'occupiedSensorActive': 'occupied_sensor_active',
        'unoccupied_sensor_active': 'unoccupiedSensorActive',
        'unoccupiedSensorActive': 'unoccupied_sensor_active',
        'dr_ramp_up_temp': 'drRampUpTemp',
        'drRampUpTemp': 'dr_ramp_up_temp',
        'dr_ramp_up_time': 'drRampUpTime',
        'drRampUpTime': 'dr_ramp_up_time',
        'link_ref': 'linkRef',
        'linkRef': 'link_ref',
        'hold_climate_ref': 'holdClimateRef',
        'holdClimateRef': 'hold_climate_ref',
        'fan_speed': 'fanSpeed',
        'fanSpeed': 'fan_speed',
    }

    attribute_type_map = {
        'type': 'six.text_type',
        'name': 'six.text_type',
        'running': 'bool',
        'start_date': 'six.text_type',
        'start_time': 'six.text_type',
        'end_date': 'six.text_type',
        'end_time': 'six.text_type',
        'is_occupied': 'bool',
        'is_cool_off': 'bool',
        'is_heat_off': 'bool',
        'cool_hold_temp': 'int',
        'heat_hold_temp': 'int',
        'fan': 'six.text_type',
        'vent': 'six.text_type',
        'ventilator_min_on_time': 'int',
        'is_optional': 'bool',
        'is_temperature_relative': 'bool',
        'cool_relative_temp': 'int',
        'heat_relative_temp': 'int',
        'is_temperature_absolute': 'bool',
        'duty_cycle_percentage': 'int',
        'fan_min_on_time': 'int',
        'occupied_sensor_active': 'bool',
        'unoccupied_sensor_active': 'bool',
        'dr_ramp_up_temp': 'int',
        'dr_ramp_up_time': 'int',
        'link_ref': 'six.text_type',
        'hold_climate_ref': 'six.text_type',
        'fan_speed': 'six.text_type',
    }

    def __init__(
        self,
        type_=None,
        name=None,
        running=None,
        start_date=None,
        start_time=None,
        end_date=None,
        end_time=None,
        is_occupied=None,
        is_cool_off=None,
        is_heat_off=None,
        cool_hold_temp=None,
        heat_hold_temp=None,
        fan=None,
        vent=None,
        ventilator_min_on_time=None,
        is_optional=None,
        is_temperature_relative=None,
        cool_relative_temp=None,
        heat_relative_temp=None,
        is_temperature_absolute=None,
        duty_cycle_percentage=None,
        fan_min_on_time=None,
        occupied_sensor_active=None,
        unoccupied_sensor_active=None,
        dr_ramp_up_temp=None,
        dr_ramp_up_time=None,
        link_ref=None,
        hold_climate_ref=None,
        fan_speed=None,
    ):
        """
        Construct an Event instance
        """
        self._type = type_
        self._name = name
        self._running = running
        self._start_date = start_date
        self._start_time = start_time
        self._end_date = end_date
        self._end_time = end_time
        self._is_occupied = is_occupied
        self._is_cool_off = is_cool_off
        self._is_heat_off = is_heat_off
        self._cool_hold_temp = cool_hold_temp
        self._heat_hold_temp = heat_hold_temp
        self._fan = fan
        self._vent = vent
        self._ventilator_min_on_time = ventilator_min_on_time
        self._is_optional = is_optional
        self._is_temperature_relative = is_temperature_relative
        self._cool_relative_temp = cool_relative_temp
        self._heat_relative_temp = heat_relative_temp
        self._is_temperature_absolute = is_temperature_absolute
        self._duty_cycle_percentage = duty_cycle_percentage
        self._fan_min_on_time = fan_min_on_time
        self._occupied_sensor_active = occupied_sensor_active
        self._unoccupied_sensor_active = unoccupied_sensor_active
        self._dr_ramp_up_temp = dr_ramp_up_temp
        self._dr_ramp_up_time = dr_ramp_up_time
        self._link_ref = link_ref
        self._hold_climate_ref = hold_climate_ref
        self._fan_speed = fan_speed

    @property
    def type(self):
        """
        Gets the type attribute of this Event instance.

        :return: The value of the type attribute of this Event instance.
        :rtype: six.text_type
        """

        return self._type

    @property
    def name(self):
        """
        Gets the name attribute of this Event instance.

        :return: The value of the name attribute of this Event instance.
        :rtype: six.text_type
        """

        return self._name

    @property
    def running(self):
        """
        Gets the running attribute of this Event instance.

        :return: The value of the running attribute of this Event
        instance.
        :rtype: bool
        """

        return self._running

    @property
    def start_date(self):
        """
        Gets the start_date attribute of this Event instance.

        :return: The value of the start_date attribute of this Event
        instance.
        :rtype: six.text_type
        """

        return self._start_date

    @property
    def start_time(self):
        """
        Gets the start_time attribute of this Event instance.

        :return: The value of the start_time attribute of this Event
        instance.
        :rtype: six.text_type
        """

        return self._start_time

    @property
    def end_date(self):
        """
        Gets the end_date attribute of this Event instance.

        :return: The value of the end_date attribute of this Event
        instance.
        :rtype: six.text_type
        """

        return self._end_date

    @property
    def end_time(self):
        """
        Gets the end_time attribute of this Event instance.

        :return: The value of the end_time attribute of this Event
        instance.
        :rtype: six.text_type
        """

        return self._end_time

    @property
    def is_occupied(self):
        """
        Gets the is_occupied attribute of this Event instance.

        :return: The value of the is_occupied attribute of this Event
        instance.
        :rtype: bool
        """

        return self._is_occupied

    @property
    def is_cool_off(self):
        """
        Gets the is_cool_off attribute of this Event instance.

        :return: The value of the is_cool_off attribute of this Event
        instance.
        :rtype: bool
        """

        return self._is_cool_off

    @property
    def is_heat_off(self):
        """
        Gets the is_heat_off attribute of this Event instance.

        :return: The value of the is_heat_off attribute of this Event
        instance.
        :rtype: bool
        """

        return self._is_heat_off

    @property
    def cool_hold_temp(self):
        """
        Gets the cool_hold_temp attribute of this Event instance.

        :return: The value of the cool_hold_temp attribute of this Event
        instance.
        :rtype: int
        """

        return self._cool_hold_temp

    @property
    def heat_hold_temp(self):
        """
        Gets the heat_hold_temp attribute of this Event instance.

        :return: The value of the heat_hold_temp attribute of this Event
        instance.
        :rtype: int
        """

        return self._heat_hold_temp

    @property
    def fan(self):
        """
        Gets the fan attribute of this Event instance.

        :return: The value of the fan attribute of this Event instance.
        :rtype: six.text_type
        """

        return self._fan

    @property
    def vent(self):
        """
        Gets the vent attribute of this Event instance.

        :return: The value of the vent attribute of this Event instance.
        :rtype: six.text_type
        """

        return self._vent

    @property
    def ventilator_min_on_time(self):
        """
        Gets the ventilator_min_on_time attribute of this Event
        instance.

        :return: The value of the ventilator_min_on_time attribute of
        this Event instance.
        :rtype: int
        """

        return self._ventilator_min_on_time

    @property
    def is_optional(self):
        """
        Gets the is_optional attribute of this Event instance.

        :return: The value of the is_optional attribute of this Event
        instance.
        :rtype: bool
        """

        return self._is_optional

    @property
    def is_temperature_relative(self):
        """
        Gets the is_temperature_relative attribute of this Event
        instance.

        :return: The value of the is_temperature_relative attribute of
        this Event instance.
        :rtype: bool
        """

        return self._is_temperature_relative

    @property
    def cool_relative_temp(self):
        """
        Gets the cool_relative_temp attribute of this Event instance.

        :return: The value of the cool_relative_temp attribute of this
        Event instance.
        :rtype: int
        """

        return self._cool_relative_temp

    @property
    def heat_relative_temp(self):
        """
        Gets the heat_relative_temp attribute of this Event instance.

        :return: The value of the heat_relative_temp attribute of this
        Event instance.
        :rtype: int
        """

        return self._heat_relative_temp

    @property
    def is_temperature_absolute(self):
        """
        Gets the is_temperature_absolute attribute of this Event
        instance.

        :return: The value of the is_temperature_absolute attribute of
        this Event instance.
        :rtype: bool
        """

        return self._is_temperature_absolute

    @property
    def duty_cycle_percentage(self):
        """
        Gets the duty_cycle_percentage attribute of this Event instance.

        :return: The value of the duty_cycle_percentage attribute of
        this Event instance.
        :rtype: int
        """

        return self._duty_cycle_percentage

    @property
    def fan_min_on_time(self):
        """
        Gets the fan_min_on_time attribute of this Event instance.

        :return: The value of the fan_min_on_time attribute of this
        Event instance.
        :rtype: int
        """

        return self._fan_min_on_time

    @property
    def occupied_sensor_active(self):
        """
        Gets the occupied_sensor_active attribute of this Event
        instance.

        :return: The value of the occupied_sensor_active attribute of
        this Event instance.
        :rtype: bool
        """

        return self._occupied_sensor_active

    @property
    def unoccupied_sensor_active(self):
        """
        Gets the unoccupied_sensor_active attribute of this Event
        instance.

        :return: The value of the unoccupied_sensor_active attribute of
        this Event instance.
        :rtype: bool
        """

        return self._unoccupied_sensor_active

    @property
    def dr_ramp_up_temp(self):
        """
        Gets the dr_ramp_up_temp attribute of this Event instance.

        :return: The value of the dr_ramp_up_temp attribute of this
        Event instance.
        :rtype: int
        """

        return self._dr_ramp_up_temp

    @property
    def dr_ramp_up_time(self):
        """
        Gets the dr_ramp_up_time attribute of this Event instance.

        :return: The value of the dr_ramp_up_time attribute of this
        Event instance.
        :rtype: int
        """

        return self._dr_ramp_up_time

    @property
    def link_ref(self):
        """
        Gets the link_ref attribute of this Event instance.

        :return: The value of the link_ref attribute of this Event
        instance.
        :rtype: six.text_type
        """

        return self._link_ref

    @property
    def hold_climate_ref(self):
        """
        Gets the hold_climate_ref attribute of this Event instance.

        :return: The value of the hold_climate_ref attribute of this
        Event instance.
        :rtype: six.text_type
        """

        return self._hold_climate_ref

    @property
    def fan_speed(self):
        """
        Gets the fan_speed attribute of this Event instance.

        :return: The value of the fan_speed attribute of this Event
        instance.
        :rtype: six.text_type
        """

        return self._fan_speed
