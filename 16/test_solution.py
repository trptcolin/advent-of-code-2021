import inspect
import tempfile
import solution

example_input = inspect.cleandoc(
    """
        """
)


def test_read_literal_packet():
    packet = solution.read_packet_from_hex("D2FE28")
    assert packet.version == 6
    assert packet.type_id == 4
    assert packet.value == 2021
    assert packet.length == 21


def test_read_operator_packet_with_bit_length():
    packet = solution.read_packet_from_hex("38006F45291200")
    assert packet.version == 1
    assert packet.type_id == 6
    assert packet.length_type_id == 0
    assert packet.subpacket_bit_length == 27
    subpackets = packet.subpackets
    assert len(subpackets) == 2
    assert subpackets[0].version == 6
    assert subpackets[0].type_id == 4
    assert subpackets[0].value == 10
    assert subpackets[0].length == 11
    assert subpackets[1].version == 2
    assert subpackets[1].type_id == 4
    assert subpackets[1].value == 20
    assert subpackets[1].length == 16


def test_read_operator_packet_with_subpacket_count():
    packet = solution.read_packet_from_hex("EE00D40C823060")
    assert packet.version == 7
    assert packet.type_id == 3
    assert packet.length_type_id == 1
    assert packet.subpacket_count == 3
    subpackets = packet.subpackets
    assert len(subpackets) == 3
    assert subpackets[0].version == 2
    assert subpackets[0].type_id == 4
    assert subpackets[0].value == 1
    assert subpackets[1].version == 4
    assert subpackets[1].type_id == 4
    assert subpackets[1].value == 2
    assert subpackets[2].version == 1
    assert subpackets[2].type_id == 4
    assert subpackets[2].value == 3


def test_nested_operators():
    packet = solution.read_packet_from_hex("8A004A801A8002F478")
    assert packet.version == 4
    packet_1 = packet.subpackets[0]
    assert packet_1.version == 1
    packet_2 = packet_1.subpackets[0]
    assert packet_2.version == 5
    packet_3 = packet_2.subpackets[0]
    assert packet_3.version == 6
    assert packet.version_sum() == 16


def test_more_version_sums():
    packet = solution.read_packet_from_hex("620080001611562C8802118E34")
    assert packet.version_sum() == 12
    packet = solution.read_packet_from_hex("C0015000016115A2E0802F182340")
    assert packet.version_sum() == 23
    packet = solution.read_packet_from_hex("A0016C880162017C3686B18A3D4780")
    assert packet.version_sum() == 31


def test_eval_sum():
    packet = solution.read_packet_from_hex("C200B40A82")
    assert packet.eval() == 3


def test_eval_product():
    packet = solution.read_packet_from_hex("04005AC33890")
    assert packet.eval() == 54


def test_eval_min():
    packet = solution.read_packet_from_hex("880086C3E88112")
    assert packet.eval() == 7


def test_eval_max():
    packet = solution.read_packet_from_hex("CE00C43D881120")
    assert packet.eval() == 9


def test_eval_lt():
    packet = solution.read_packet_from_hex("D8005AC2A8F0")
    assert packet.eval() == 1


def test_eval_gt():
    packet = solution.read_packet_from_hex("F600BC2D8F")
    assert packet.eval() == 0


def test_eval_eq():
    packet = solution.read_packet_from_hex("9C005AC2F8F0")
    assert packet.eval() == 0


def test_eval_more_complex():
    packet = solution.read_packet_from_hex("9C0141080250320F1802104A08")
    assert packet.eval() == 1
