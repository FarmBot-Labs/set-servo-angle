#!/usr/bin/env python

"""Set servo angle."""

from farmware_tools import get_config_value, device

farmware_name = 'Set Servo Angle'

pin_number = get_config_value(farmware_name, config_name='pin_number')
servo_angle = get_config_value(farmware_name, config_name='servo_angle')

device.set_servo_angle(pin_number, servo_angle)
