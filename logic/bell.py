import qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from typing import Dict

def bell_counts(shots: int = 1000) -> Dict[str, int]:
    
    #2 qbit circuit
    circ = QuantumCircuit(2)
    circ.h(0)
    circ.cx(0, 1)
    circ.measure_all()

    simulator = AerSimulator()
    # Transpile for simulator
    circ = transpile(circ, simulator)

    # Run and get counts
    result = simulator.run(circ, shots=shots, memory=True).result()
    counts = result.get_counts(circ)
    for state in ["00", "01", "10", "11"]:
        counts.setdefault(state, 0)

    return counts
