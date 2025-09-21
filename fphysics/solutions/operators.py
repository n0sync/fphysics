class QuantumOperator:
    def __init__(self, name, matrix):
        self.name = name
        self.matrix = matrix
    
    def operate(self, vector):
        result = [sum(x * y for x, y in zip(row, vector)) for row in self.matrix]
        return result

