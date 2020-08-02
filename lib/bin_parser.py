import struct
import numpy as np


def main():
    """Read catman 5.0 format. Format documented at :
    https://docs.google.com/spreadsheets/d/1dZOw9L6_ukHNYlcR-n64DuRZ702nBq6jjA169q-aCz0/edit#gid=0"""
    with open(r"C:\Users\KNAPP\PycharmProjects\csv_parsing\test_samples\2020_07_22_U_4.8_0deg_2.BIN", "rb") as f:

        # read global section
        file_id = int.from_bytes(f.read(2), byteorder='little')
        data_offset = int.from_bytes(f.read(4), byteorder='little')
        comment_length = int.from_bytes(f.read(2), byteorder='little')
        comment = f.read(comment_length).decode(encoding='latin_1')

        # read reserved strings
        reserved_strings = []
        for i in range(32):
            header_length = int.from_bytes(f.read(2), byteorder='little')
            header = f.read(header_length).decode(encoding='latin_1')
            reserved_strings.append(header)

        number_of_channels = int.from_bytes(f.read(2), byteorder='little')
        print(number_of_channels, "channels")
        maximum_channel_length = int.from_bytes(f.read(4), byteorder='little')

        for i in range(number_of_channels):
            offset_channel = int.from_bytes(f.read(4), byteorder='little')

        reduction_factor = int.from_bytes(f.read(4), byteorder='little')

        # Channel header section
        channels =[]
        for i in range(number_of_channels):
            channel = {}
            channel_number = int.from_bytes(f.read(2), byteorder='little')
            channel["length"] = int.from_bytes(f.read(4), byteorder='little')
            channel_name_length = int.from_bytes(f.read(2), byteorder='little')
            channel_name = f.read(channel_name_length).decode(encoding='latin_1')
            channel_unit_name_length = int.from_bytes(f.read(2), byteorder='little')
            channel_unit_name = f.read(channel_unit_name_length).decode(encoding='latin_1')
            channel_comment_length = int.from_bytes(f.read(2), byteorder='little')
            channel_comment = f.read(channel_comment_length).decode(encoding='latin_1')
            print(f"{channel_name}, ({channel_unit_name}) : {channel_comment}")
            channel_format = int.from_bytes(f.read(2), byteorder='little')
            channel_data_width = int.from_bytes(f.read(2), byteorder='little')
            channel_datetime = struct.unpack('d',f.read(8))
            channel_extended_name_length = int.from_bytes(f.read(4), byteorder='little')
            channel_extended_name_bytes = f.read(channel_extended_name_length)
            channel_extended_name = channel_extended_name_bytes.decode(encoding='latin_1')
            channel_linearisation_mode = int.from_bytes(f.read(1), byteorder='little')
            channel_user_scale = int.from_bytes(f.read(1), byteorder='little')
            channel_linearisation_points = int.from_bytes(f.read(1), byteorder='little')
            thermo_type = int.from_bytes(f.read(2), byteorder='little')
            formula_length = int.from_bytes(f.read(2), byteorder='little')
            formula = f.read(formula_length).decode(encoding='latin_1')
            DB_sensor_info_length = int.from_bytes(f.read(4), byteorder='little')
            DB_sensor_info = f.read(DB_sensor_info_length).decode(encoding='latin_1')
            channels.append(channel)
        f.read((3*8192)-f.tell())  # fudge to find start of data - I dont understand why this works
        # Read Data
        for i in range(number_of_channels):
            channels[i]["data"] = np.frombuffer(f.read(8*channels[i]["length"]), dtype='<f8')


if __name__ == '__main__':
    main()
    