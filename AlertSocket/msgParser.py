# from pandas import date_range
from messages import *
from utils import *
from datetime import datetime

class Parser:
    def decipher_message(self,node_message):
        
        message_id = str(node_message[6])
        node_id = get_MAC_id_string_from_bytes([node_message[0],node_message[1],node_message[2],node_message[3],node_message[4],node_message[5]])

        if(SSN_MessageID_to_TYPE[message_id] =="STATUS_UPDATE"):
            x = 3
            temperature = get_word_from_bytes(node_message[7],node_message[8]) / 10.0
            humidity = get_word_from_bytes(node_message[9],node_message[10]) / 10.0
            state_flags = node_message[11]
            ssn_uptime = get_int_from_bytes(node_message[60],node_message[61],node_message[62],node_message[63])
            abnormal_activity = Activity_ID_to_TYPE[str(node_message[64])]

            thermistor_1 = 0
            thermistor_2 = 0

            if(len(node_message)>65):
                thermistor_1 = get_word_from_bytes(node_message[65],node_message[66]) / 10.0
                thermistor_2 = get_word_from_bytes(node_message[67],node_message[68]) / 10.0


            machine_load_currents = []
            machine_load_percentages = [] 
            machine_status = []
            machine_state_timestamp = []
            machine_state_duration = []

            offset = 12

            for i in range(0,4):
                machine_load_currents.append(get_word_from_bytes(node_message[12+i * offset],node_message[13 + i * offset]) / 100.0)
                machine_load_percentages.append(node_message[14 + i * offset])
                machine_status.append(State_ID_to_TYPE[str(node_message[15 + i * offset])])
                machine_state_timestamp.append(get_int_from_bytes(node_message[16 + i * offset], node_message[17 + i * offset],node_message[18 + i * offset], node_message[19 + i * offset]))
                machine_state_duration.append(get_int_from_bytes(node_message[20 + i * offset], node_message[21 + i * offset],node_message[22 + i * offset], node_message[23 + i * offset]))
            #70:b3:d5:fe:4d:11
            # SSN_UPTIME: 2022-03-27T13:43:32.000Z,
            #   STATUS: 'OFF',
            #   MACHINE_STATE_TIMESTAMP: 1970-01-01T00:00:00.000Z,
            #   MACHINE_STATE_DURATION: 0,
            #   TIMESTAMP: 2022-03-27T15:08:45.210Z,
            msg = {
                "MAC_ADDRESS":node_id.lower(),
                "CT1":machine_load_currents[0],
                "CT2":machine_load_currents[1],
                "CT3":machine_load_currents[2],
                "MESSAGE_ID":message_id,
                "AMBIENT_TEMPERATURE":temperature,
                "AMBIENT_HUMIDITY":humidity,
                "SSN_UPTIME":datetime.utcfromtimestamp(ssn_uptime).strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                "STATUS":machine_status[0],
                "MACHINE_STATE_TIMESTAMP":datetime.utcfromtimestamp(machine_state_timestamp[0]).strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                "MACHINE_STATE_DURATION":machine_state_duration[0],
                "TIMESTAMP":datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'), #can use [:-3]   
                "THERMISTOR_1": thermistor_1,
                "THERMISTOR_2": thermistor_2,
                "STATUS_FLAG": state_flags,
            }

            return msg
        else:
            return None