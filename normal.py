import numpy as np

from quantum import QuantumGates


class Gates:

    @staticmethod
    def NOT(state, target_idx=0):
        new_state = np.zeros_like(state)
        for i in range(len(state)):
            flipped_index = QuantumGates.flip(i, target_idx)
            new_state[flipped_index] = state[i]
        return new_state

    @staticmethod
    def AND(state, q1_idx=0, q2_idx=1, target_idx=2):
        new_state = np.zeros_like(state)
        for i in range(len(state)):
            # Get the values of the qubits at q1_idx and q2_idx by reading bits in i
            if QuantumGates.get_value(i, q1_idx) and QuantumGates.get_value(i, q2_idx):
                # Both control qubits are 1 → flip the target qubit using XOR
                flipped_index = QuantumGates.flip(i, target_idx)
                # Move the amplitude from the old state to the new index
                new_state[flipped_index] = state[i]
            else:
                # Otherwise, leave the amplitude as-is
                new_state[i] = state[i]
        return new_state

    @staticmethod
    def OR(state, q1_idx=0, q2_idx=1, target_idx=2):
        new_state = np.zeros_like(state)
        for i in range(len(state)):
            # Get the values of the qubits at q1_idx and q2_idx by reading bits in i
            if QuantumGates.get_value(i, q1_idx) or QuantumGates.get_value(i, q2_idx):
                # Both control qubits are 1 → flip the target qubit using XOR
                flipped_index = QuantumGates.flip(i, target_idx)
                # Move the amplitude from the old state to the new index
                new_state[flipped_index] = state[i]
            else:
                # Otherwise, leave the amplitude as-is
                new_state[i] = state[i]
        return new_state

    @staticmethod
    def IMPLY(state, q1_idx=0, q2_idx=1, target_idx=2):
        new_state = np.zeros_like(state)

        for i in range(len(state)):
            q1 = QuantumGates.get_value(i, q1_idx)
            q2 = QuantumGates.get_value(i, q2_idx)

            # implication is false only when q1=1 and q2=0
            imply = not (q1 == 1 and q2 == 0)

            if imply:
                flipped_index = QuantumGates.flip(i, target_idx)
                new_state[flipped_index] = state[i]
            else:
                new_state[i] = state[i]

        return new_state

    @staticmethod
    def XOR(state, q1_idx=0, q2_idx=1, target_idx=2):
        new_state = np.zeros_like(state)
        for i in range(len(state)):
            q1 = QuantumGates.get_value(i, q1_idx)
            q2 = QuantumGates.get_value(i, q2_idx)

            # XOR condition: flip if exactly one of them is 1
            if q1 ^ q2:
                flipped_index = QuantumGates.flip(i, target_idx)
                new_state[flipped_index] = state[i]
            else:
                new_state[i] = state[i]
        return new_state

    @staticmethod
    def NOR(state, q1_idx=0, q2_idx=1, target_idx=2):
        return Gates.NOT(Gates.OR(state, q1_idx, q2_idx, target_idx))

    @staticmethod
    def NAND(state, q1_idx=0, q2_idx=1, target_idx=2):
        return Gates.NOT(Gates.AND(state, q1_idx, q2_idx, target_idx))

    @staticmethod
    def NIMPLY(state, q1_idx=0, q2_idx=1, target_idx=2):
        return Gates.NOT(Gates.IMPLY(state, q1_idx, q2_idx, target_idx))

    @staticmethod
    def XNOR(state, q1_idx=0, q2_idx=1, target_idx=2):
        return Gates.NOT(Gates.XOR(state, q1_idx, q2_idx, target_idx))
