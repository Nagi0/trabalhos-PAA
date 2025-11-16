class Line:

    def __init__(self, length: int, m_bus_colors: int, bus_colors: int, m_bus_length: int, bus_length: int):
        self.length = length
        self.m_bus_colors = m_bus_colors
        self.bus_colors = bus_colors

        self.m_bus_length = m_bus_length
        self.bus_length = bus_length
        self.mod = 10**6

    def compute_combinations(self):
        n = self.length // 5
        m_matrix = [[self.m_bus_colors % self.mod, self.bus_colors % self.mod], [1, 0]]

        m_powered_matrix = self._mat_pow(m_matrix, n - 1)

        fn = (m_powered_matrix[0][0] * self.m_bus_colors % self.mod + m_powered_matrix[0][1] * 1) % self.mod

        return f"{fn:06d}"

    def _mat_pow(self, base, e):
        res = [[1, 0], [0, 1]]
        while e > 0:
            if e & 1:
                res = self._mat_mul(res, base)
            base = self._mat_mul(base, base)
            e >>= 1
        return res

    def _mat_mul(self, a_matrix, b_matrix):
        return [
            [
                (a_matrix[0][0] * b_matrix[0][0] + a_matrix[0][1] * b_matrix[1][0]) % self.mod,
                (a_matrix[0][0] * b_matrix[0][1] + a_matrix[0][1] * b_matrix[1][1]) % self.mod,
            ],
            [
                (a_matrix[1][0] * b_matrix[0][0] + a_matrix[1][1] * b_matrix[1][0]) % self.mod,
                (a_matrix[1][0] * b_matrix[0][1] + a_matrix[1][1] * b_matrix[1][1]) % self.mod,
            ],
        ]
