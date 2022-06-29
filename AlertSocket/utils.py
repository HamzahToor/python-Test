# import numpy as np

def get_MAC_id_from_bytes(bytes):
    return bytes[0:6]


def get_MAC_id_string_from_bytes(bytes):
    return f"{bytes[0]:02X}:{bytes[1]:02X}:{bytes[2]:02X}:{bytes[3]:02X}:{bytes[4]:02X}:{bytes[5]:02X}"



def get_MAC_id_from_bytes(bytes):
    return bytes[0:6]


def get_MAC_id_string_from_bytes(bytes):
    return f"{bytes[0]:02X}:{bytes[1]:02X}:{bytes[2]:02X}:{bytes[3]:02X}:{bytes[4]:02X}:{bytes[5]:02X}"


def get_word_from_bytes(high_byte, low_byte):
    return (high_byte << 8) | low_byte


def get_int_from_bytes(highest_byte, higher_byte, high_byte, low_byte):
    return (highest_byte << 24) | (higher_byte << 16) | (high_byte << 8) | low_byte


def get_bytes_from_int(this_int):
    B1 = (this_int & 0xFF000000) >> 24
    B2 = (this_int & 0x00FF0000) >> 16
    B3 = (this_int & 0x0000FF00) >> 8
    B4 = (this_int & 0x000000FF)
    return B1, B2, B3, B4

