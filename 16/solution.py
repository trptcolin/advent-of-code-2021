import functools
import operator


def base16_to_2(s):
    value = bin(int(s, base=16))[2:]
    return value.rjust(4, "0")


def chunks(s, length):
    return [s[i : i + length] for i in range(0, len(s), length)]


class LiteralPacket:
    def __init__(self, version, type_id, binary_string):
        self.version = version
        self.type_id = type_id
        groups = chunks(binary_string[6:], 5)
        value_string = ""
        for group in groups:
            value_string += group[1:]
            if group[0] != "1":
                break
        self.value = int(value_string, base=2)
        self.length = int(6 + (len(value_string) / 4) * 5)

    def version_sum(self):
        return self.version

    def eval(self):
        return self.value


class OperatorPacket:
    def __init__(self, version, type_id, binary_string):
        self.version = version
        self.type_id = type_id
        self.length_type_id = int(binary_string[6], base=2)
        if self.length_type_id == 0:
            self.subpacket_bit_length = int(binary_string[7:22], base=2)
            remaining_bit_length = self.subpacket_bit_length
            self.subpackets = []
            relevant_string = binary_string[22 : 22 + self.subpacket_bit_length]
            while remaining_bit_length > 0:
                packet = read_packet(relevant_string)
                self.subpackets.append(packet)
                remaining_bit_length -= packet.length
                relevant_string = relevant_string[packet.length :]
            self.length = 22 + sum([packet.length for packet in self.subpackets])

        else:
            # length_type_id == 0 (since binary)
            self.subpacket_count = int(binary_string[7:18], base=2)
            remaining_subpackets = self.subpacket_count
            self.subpackets = []
            relevant_string = binary_string[18:]
            while remaining_subpackets > 0:
                packet = read_packet(relevant_string)
                self.subpackets.append(packet)
                relevant_string = relevant_string[packet.length :]
                remaining_subpackets -= 1
            self.length = 18 + sum([packet.length for packet in self.subpackets])

    def version_sum(self):
        return self.version + sum([packet.version_sum() for packet in self.subpackets])

    def eval(self):
        subpacket_evals = [packet.eval() for packet in self.subpackets]
        if self.type_id == 0:
            return sum(subpacket_evals)
        elif self.type_id == 1:
            return functools.reduce(operator.mul, subpacket_evals, 1)
        elif self.type_id == 2:
            return min(subpacket_evals)
        elif self.type_id == 3:
            return max(subpacket_evals)
        elif self.type_id == 5:
            return subpacket_evals[0] > subpacket_evals[1]
        elif self.type_id == 6:
            return subpacket_evals[0] < subpacket_evals[1]
        elif self.type_id == 7:
            return subpacket_evals[0] == subpacket_evals[1]

        return None


def read_packet_from_hex(s):
    hex_string = s
    binary_string = "".join([base16_to_2(c) for c in hex_string])
    return read_packet(binary_string)


def read_packet(binary_string):
    version = int(binary_string[:3], base=2)
    type_id = int(binary_string[3:6], base=2)
    if type_id == 4:
        return LiteralPacket(version, type_id, binary_string)
    else:
        return OperatorPacket(version, type_id, binary_string)


def read_input(path):
    with open(path) as f:
        return next(f).strip()  # just 1 long line


def part_one(path):
    hexinput = read_input(path)
    packet = read_packet_from_hex(hexinput)
    return packet.version_sum()


def part_two(path):
    hexinput = read_input(path)
    packet = read_packet_from_hex(hexinput)
    return packet.eval()


if __name__ == "__main__":
    print(part_one("input.txt"))
    print(part_two("input.txt"))
