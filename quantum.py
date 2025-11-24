import numpy as np

class QuantumGates:

    # === single-qubit gates ===
    X = np.array([[0, 1],
              [1, 0]], dtype=complex)

    Y = np.array([[0, -1j],
              [1j, 0]], dtype=complex)

    Z = np.array([[1, 0],
              [0, -1]], dtype=complex)

    H = (1/np.sqrt(2)) * np.array([[1, 1],
                               [1, -1]], dtype=complex)

    S = np.array([[1, 0],
              [0, 1j]], dtype=complex)  # phase π/2

    T = np.array([[1, 0],
              [0, np.exp(1j*np.pi/4)]], dtype=complex)  # phase π/4

    # rotation gates
    @staticmethod
    def Rx(theta):
        return np.array([[np.cos(theta/2), -1j*np.sin(theta/2)],
                     [-1j*np.sin(theta/2), np.cos(theta/2)]], dtype=complex)

    @staticmethod
    def Ry(theta):
        return np.array([[np.cos(theta/2), -np.sin(theta/2)],
                     [np.sin(theta/2), np.cos(theta/2)]], dtype=complex)

    @staticmethod
    def Rz(theta):
        return np.array([[np.exp(-1j*theta/2), 0],
                     [0, np.exp(1j*theta/2)]], dtype=complex)

    # === two-qubit gates ===
    CNOT = np.array([[1, 0, 0, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1],
                 [0, 0, 1, 0]], dtype=complex)

    CZ = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, -1]], dtype=complex)

    CY = np.array([[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 0, -1j],
               [0, 0, 1j, 0]], dtype=complex)

    SWAP = np.array([[1, 0, 0, 0],
                 [0, 0, 1, 0],
                 [0, 1, 0, 0],
                 [0, 0, 0, 1]], dtype=complex)

    # === three-qubit gate ===
    CCNOT = np.array([
        [1,0,0,0,0,0,0,0],
        [0,1,0,0,0,0,0,0],
        [0,0,1,0,0,0,0,0],
        [0,0,0,1,0,0,0,0],
        [0,0,0,0,1,0,0,0],
        [0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1],
        [0,0,0,0,0,0,1,0]
    ], dtype=complex)

    # optional: identity
    I2 = np.eye(2, dtype=complex)
    I4 = np.eye(4, dtype=complex)
    I8 = np.eye(8, dtype=complex)

    @staticmethod
    def get_value(idx, q1_idx):
        return (idx >> q1_idx) & 1

    @staticmethod
    def flip(idx, target_idx):
        return idx ^ (1 << target_idx)

    @staticmethod
    def ensure_qubits(state, *qubit_indices):
        max_q = max(qubit_indices)
        required = 2 ** (max_q + 1)

        if state.size < required:
            new_state = np.zeros(required, dtype=state.dtype)
            new_state[:state.size] = state
            return new_state
        return state
