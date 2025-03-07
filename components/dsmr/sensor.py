import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_ID,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_EMPTY,
    DEVICE_CLASS_GAS,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_VOLTAGE,
    ICON_CURRENT_AC,
    ICON_EMPTY,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_NONE,
    STATE_CLASS_TOTAL_INCREASING,
    UNIT_AMPERE,
    UNIT_CUBIC_METER,
    UNIT_EMPTY,
    UNIT_KILOWATT,
    UNIT_KILOWATT_HOURS,
    UNIT_KILOVOLT_AMPS_REACTIVE_HOURS,
    UNIT_KILOVOLT_AMPS_REACTIVE,
    UNIT_VOLT_AMPS_REACTIVE_HOURS,
    UNIT_VOLT_AMPS_REACTIVE,    
    UNIT_VOLT,
    UNIT_HERTZ,
)
from . import Dsmr, CONF_DSMR_ID

AUTO_LOAD = ["dsmr"]


CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_DSMR_ID): cv.use_id(Dsmr),
        cv.Optional("energy_delivered"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT_HOURS,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
        ),
        cv.Optional("energy_delivered_tariff1"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT_HOURS,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
        ),
        cv.Optional("energy_delivered_tariff2"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT_HOURS,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
        ),
        cv.Optional("energy_delivered_tariff3"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT_HOURS,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
        ),
        cv.Optional("energy_delivered_tariff4"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT_HOURS,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
        ),
        cv.Optional("energy_returned"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT_HOURS,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
        ),
        cv.Optional("energy_returned_tariff1"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT_HOURS,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
        ),
        cv.Optional("energy_returned_tariff2"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT_HOURS,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
        ),
        cv.Optional("energy_returned_tariff3"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT_HOURS,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
        ),
        cv.Optional("energy_returned_tariff4"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT_HOURS,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
        ),        
        cv.Optional("energy_absolute"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT_HOURS,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_ENERGY,
            state_class=STATE_CLASS_TOTAL_INCREASING,
        ),
        cv.Optional("total_imported_energy"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE_HOURS,
            accuracy_decimals=1,
        ),
        cv.Optional("total_exported_energy"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE_HOURS,
            accuracy_decimals=1,
        ),
        cv.Optional("electricity_tariff"): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional("power_delivered"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("power_returned"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_MEASUREMENT,
        ),        
         cv.Optional("reactive_power_qi"): sensor.sensor_schema(
             unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE,
             icon=ICON_EMPTY,
             accuracy_decimals=3,
             device_class=DEVICE_CLASS_POWER,
             state_class=STATE_CLASS_MEASUREMENT,
         ),
         cv.Optional("reactive_power_qii"): sensor.sensor_schema(
             unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE,
             icon=ICON_EMPTY,
             accuracy_decimals=3,
             device_class=DEVICE_CLASS_POWER,
             state_class=STATE_CLASS_MEASUREMENT,
         ),
         cv.Optional("reactive_power_qiii"): sensor.sensor_schema(
             unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE,
             icon=ICON_EMPTY,
             accuracy_decimals=3,
             device_class=DEVICE_CLASS_POWER,
             state_class=STATE_CLASS_MEASUREMENT,
         ),
         cv.Optional("reactive_power_qiv"): sensor.sensor_schema(
             unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE,
             icon=ICON_EMPTY,
             accuracy_decimals=3,
             device_class=DEVICE_CLASS_POWER,
             state_class=STATE_CLASS_MEASUREMENT,
         ),
         cv.Optional("energy_positive_reactive"): sensor.sensor_schema(
             unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE_HOURS,
             icon=ICON_EMPTY,
             accuracy_decimals=3,
             device_class=DEVICE_CLASS_ENERGY,
             state_class=STATE_CLASS_TOTAL_INCREASING,
         ),
         cv.Optional("energy_negative_reactive"): sensor.sensor_schema(
             unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE_HOURS,
             icon=ICON_EMPTY,
             accuracy_decimals=3,
             device_class=DEVICE_CLASS_ENERGY,
             state_class=STATE_CLASS_TOTAL_INCREASING,
         ),
         cv.Optional("reactive_energy_qi"): sensor.sensor_schema(
             unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE_HOURS,
             icon=ICON_EMPTY,
             accuracy_decimals=3,
             device_class=DEVICE_CLASS_ENERGY,
             state_class=STATE_CLASS_TOTAL_INCREASING,
         ),
         cv.Optional("reactive_energy_qii"): sensor.sensor_schema(
             unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE_HOURS,
             icon=ICON_EMPTY,
             accuracy_decimals=3,
             device_class=DEVICE_CLASS_ENERGY,
             state_class=STATE_CLASS_TOTAL_INCREASING,
         ),
         cv.Optional("reactive_energy_qiii"): sensor.sensor_schema(
             unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE_HOURS,
             icon=ICON_EMPTY,
             accuracy_decimals=3,
             device_class=DEVICE_CLASS_ENERGY,
             state_class=STATE_CLASS_TOTAL_INCREASING,
         ),
         cv.Optional("reactive_energy_qiv"): sensor.sensor_schema(
             unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE_HOURS,
             icon=ICON_EMPTY,
             accuracy_decimals=3,
             device_class=DEVICE_CLASS_ENERGY,
             state_class=STATE_CLASS_TOTAL_INCREASING,
         ),

         cv.Optional("instantaneous_power_factor"): sensor.sensor_schema(
             unit_of_measurement=UNIT_EMPTY,
             icon=ICON_EMPTY,
             accuracy_decimals=3,
             device_class=DEVICE_CLASS_EMPTY,
             state_class=STATE_CLASS_NONE,
         ),
         cv.Optional("instantaneous_power_factor_l1"): sensor.sensor_schema(
             unit_of_measurement=UNIT_EMPTY,
             icon=ICON_EMPTY,
             accuracy_decimals=3,
             device_class=DEVICE_CLASS_EMPTY,
             state_class=STATE_CLASS_NONE,
         ),
         cv.Optional("instantaneous_power_factor_l2"): sensor.sensor_schema(
             unit_of_measurement=UNIT_EMPTY,
             icon=ICON_EMPTY,
             accuracy_decimals=3,
             device_class=DEVICE_CLASS_EMPTY,
             state_class=STATE_CLASS_NONE,
         ),
         cv.Optional("instantaneous_power_factor_l3"): sensor.sensor_schema(
             unit_of_measurement=UNIT_EMPTY,
             icon=ICON_EMPTY,
             accuracy_decimals=3,
             device_class=DEVICE_CLASS_EMPTY,
             state_class=STATE_CLASS_NONE,
         ),

        cv.Optional("frequency"): sensor.sensor_schema(
            unit_of_measurement=UNIT_HERTZ,
            icon=ICON_CURRENT_AC,
            accuracy_decimals=1,
        ),

         cv.Optional("absolute_active_energy"): sensor.sensor_schema(
             unit_of_measurement=UNIT_KILOWATT_HOURS,
             icon=ICON_EMPTY,
             accuracy_decimals=3,
             device_class=DEVICE_CLASS_ENERGY,
             state_class=STATE_CLASS_TOTAL_INCREASING,
         ),

        cv.Optional("reactive_power_delivered"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_TOTAL_INCREASING,
        ),
        cv.Optional("reactive_power_returned"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
            state_class=STATE_CLASS_TOTAL_INCREASING,
        ),
        cv.Optional("electricity_threshold_l1"): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_CURRENT,
        ),
        cv.Optional("electricity_threshold_l2"): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_CURRENT,
        ),
        cv.Optional("electricity_threshold_l3"): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            accuracy_decimals=0,
            device_class=DEVICE_CLASS_CURRENT,
        ),
        cv.Optional("electricity_threshold"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_POWER,
        ),
        cv.Optional("electricity_switch_position"): sensor.sensor_schema(
            accuracy_decimals=3,
        ),
        cv.Optional("electricity_failures"): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional("electricity_long_failures"): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional("electricity_sags_l1"): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional("electricity_sags_l2"): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional("electricity_sags_l3"): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional("electricity_swells_l1"): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional("electricity_swells_l2"): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional("electricity_swells_l3"): sensor.sensor_schema(
            accuracy_decimals=0,
        ),
        cv.Optional("current_l1"): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_CURRENT,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("current_l2"): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_CURRENT,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("current_l3"): sensor.sensor_schema(
            unit_of_measurement=UNIT_AMPERE,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_CURRENT,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("power_delivered_l1"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_CURRENT,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("power_delivered_l2"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_CURRENT,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("power_delivered_l3"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_CURRENT,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("power_returned_l1"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_CURRENT,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("power_returned_l2"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_CURRENT,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("power_returned_l3"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOWATT,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_CURRENT,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("reactive_power_delivered_l1"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE,
            accuracy_decimals=3,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("reactive_power_delivered_l2"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE,
            accuracy_decimals=3,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("reactive_power_delivered_l3"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE,
            accuracy_decimals=3,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("reactive_power_returned_l1"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE,
            accuracy_decimals=3,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("reactive_power_returned_l2"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE,
            accuracy_decimals=3,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("reactive_power_returned_l3"): sensor.sensor_schema(
            unit_of_measurement=UNIT_KILOVOLT_AMPS_REACTIVE,
            accuracy_decimals=3,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("voltage_l1"): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_VOLTAGE,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("voltage_l2"): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_VOLTAGE,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("voltage_l3"): sensor.sensor_schema(
            unit_of_measurement=UNIT_VOLT,
            accuracy_decimals=1,
            device_class=DEVICE_CLASS_VOLTAGE,
            state_class=STATE_CLASS_MEASUREMENT,
        ),
        cv.Optional("gas_delivered"): sensor.sensor_schema(
            unit_of_measurement=UNIT_CUBIC_METER,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_GAS,
            state_class=STATE_CLASS_TOTAL_INCREASING,
        ),
        cv.Optional("gas_delivered_be"): sensor.sensor_schema(
            unit_of_measurement=UNIT_CUBIC_METER,
            accuracy_decimals=3,
            device_class=DEVICE_CLASS_GAS,
            state_class=STATE_CLASS_TOTAL_INCREASING,
        ),
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    hub = await cg.get_variable(config[CONF_DSMR_ID])

    sensors = []
    for key, conf in config.items():
        if not isinstance(conf, dict):
            continue
        id = conf.get("id")
        if id and id.type == sensor.Sensor:
            s = await sensor.new_sensor(conf)
            cg.add(getattr(hub, f"set_{key}")(s))
            sensors.append(f"F({key})")

    if sensors:
        cg.add_define(
            "DSMR_SENSOR_LIST(F, sep)", cg.RawExpression(" sep ".join(sensors))
        )
