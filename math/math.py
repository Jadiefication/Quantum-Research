from normal import Gates
import numpy as np

from quantum import QuantumGates


class MathMethods:

    @staticmethod
    def full_adder(state, a=0, b=1, cin=2, sum_target=3, carry_target=4):
        # no loop over state
        highest = max(a, b, cin, sum_target, carry_target)
        _state = MathMethods.add_qbits(state, a, b, cin, sum_target, carry_target, highest)
        return _state

    @staticmethod
    def add_qbits(state, a=0, b=1, cin=2, sum_target=3, carry_target=4, highest=None):
        if highest is None:
            highest = max(a, b, cin, sum_target, carry_target)
        _state = MathMethods.carry_logic(state, a, b, cin, highest)
        # XOR sum
        __state = Gates.XOR(Gates.XOR(_state, a, b, sum_target), sum_target, cin, sum_target)
        return __state

    @staticmethod
    def carry_logic(state, a=0, b=1, cin=2, xor_q=3):
        and1_q = xor_q + 1
        and2_q = xor_q + 2
        carry_q = xor_q + 3
        state = QuantumGates.ensure_qubits(state, a, b, cin, xor_q, and1_q, and2_q, carry_q)
        # xor_ab = a XOR b
        state1 = Gates.XOR(state, a, b, xor_q)

        # and1 = a AND b
        state2 = Gates.AND(state1, a, b, and1_q)

        # and2 = cin AND xor_ab
        state3 = Gates.AND(state2, cin, xor_q, and2_q)

        # carry = and1 OR and2
        state4 = Gates.OR(state3, and1_q, and2_q, carry_q)

        return state4

