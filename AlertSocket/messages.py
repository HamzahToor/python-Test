SSN_MessageType_to_ID = {
    'GET_MAC':               "1",
    'SET_MAC':               "2",
    'GET_TIMEOFDAY':         "3",
    'SET_TIMEOFDAY':         "4",
    'GET_CONFIG':            "5",
    'SET_CONFIG':            "6",
    'ACK_CONFIG':            "7",
    'STATUS_UPDATE':         "8",
    'RESET_MACHINE_TIME':    "9",
    'DEBUG_EEPROM_CLEAR':   "10",
    'DEBUG_RESET_SSN':      "11"
}

SSN_MessageID_to_TYPE = {
    "1":  'GET_MAC',
    "2":  'SET_MAC',
    "3":  'GET_TIMEOFDAY',
    "4":  'SET_TIMEOFDAY',
    "5":  'GET_CONFIG',
    "6":  'SET_CONFIG',
    "7":  'ACK_CONFIG',
    "8":  'STATUS_UPDATE',
    "9":  'RESET_MACHINE_TIME',
    "10": 'DEBUG_EEPROM_CLEAR',
    "11": 'DEBUG_RESET_SSN'
}

SSN_Message_Sizes = {
    'GET_MAC':               3,
    'SET_MAC':               7,
    'GET_TIMEOFDAY':         3,
    'SET_TIMEOFDAY':         5,
    'GET_CONFIG':            3,
    'SET_CONFIG':            "6",
    'ACK_CONFIG':            "7",
    'STATUS_UPDATE':         60,
    'RESET_MACHINE_TIME':    "9",
    'DEBUG_EEPROM_CLEAR':   "10",
    'DEBUG_RESET_SSN':      "11"
}

Activity_ID_to_TYPE = {
    "0": "NORMAL",
    "1": "ABNORMAL",
    "2": "Temperature Sensor Read Error Condition",
    "3": "Temperature Sensor CRC Error Condition",

}

State_ID_to_TYPE = {
    "0": "OFF",
    "1": "IDLE",
    "2": "ON"
}