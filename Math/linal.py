from Math.matrix import Matrix


class Basis:
    def __init__(self, *args):
        if len(args) == 1 and args[0].__class__.__name__ == 'Matrix':
            self.matrix = args[0]
            if self.matrix.size_n != self.matrix.size_m:
                raise ValueError('Not square matrix')
            self.n = self.matrix.size_n
            # self.convert_matrix = self.matrix ** -1
            self.vectors = []
            for i in range(self.n):
                self.vectors.append(Vector(*(self.matrix.mtrx[j][i] for j in range(self.n))))
        else:
            self.vectors = args
            self.n = len(args)
            self.matrix = Matrix(
                [list(vector.to_primal_basis().coordinates) for vector in self.vectors]).transpose()
            # self.convert_matrix = self.matrix ** -1
        self.s_mul = lambda v1, v2: sum(v1.coordinates[k] * v2.coordinates[k] for k in range(self.n))

    def __str__(self):
        return str(self.matrix)

    def set_s_mul(self, func):
        self.s_mul = func

    def orto(self):
        vectors = [self.vectors[0]]
        for i in range(1, self.n):
            a = self.vectors[i]
            for v in vectors:
                a -= self.vectors[i].proj(v)
            vectors.append(a)
        return Basis(*vectors)


class Vector:
    def __init__(self, *args, basis=None):
        if len(args) == 1 and args[0].__class__.__name__ == 'Matrix':
            matrix = args[0]
            if matrix.size_n == 1:
                args = matrix.mtrx[0]
            elif matrix.size_m == 1:
                args = tuple(matrix.mtrx[i][0] for i in range(matrix.size_n))
            else:
                raise ValueError('Invalid matrix')
        self.n = len(args)
        if self.n == 0:
            raise ValueError()
        if self.n == 1 and isinstance(args[0], Matrix):
            self.n = args[0].size_n
            self.coordinates = tuple(args[0].mtrx[i][0] for i in range(self.n))
        else:
            self.coordinates = args
        self.basis = basis

    def __add__(self, other):
        if self.n != other.n:
            raise ValueError('Vectors has different n')
        return Vector(*(self.coordinates[i] + other.coordinates[i] for i in range(self.n)))

    def __sub__(self, other):
        if self.n != other.n:
            raise ValueError('Vectors has different n')
        return Vector(*(self.coordinates[i] - other.coordinates[i] for i in range(self.n)))

    def __neg__(self):
        return Vector(*(c * -1 for c in self.coordinates))

    def __bool__(self):
        for c in self.coordinates:
            if c:
                return True
        return False
    
    def __truediv__(self, other):
        return self * (1 / other)

    def __mul__(self, other):
        if isinstance(other, Vector):
            if self.basis != other.basis:
                raise ValueError('vectors in different basises')
            if self.basis is None:
                return sum(self.coordinates[i] * other.coordinates[i] for i in range(self.n))
            return self.basis.s_mul(self, other)
        return Vector(*(self.coordinates[i] * other for i in range(self.n)))

    def __rmul__(self, other):
        return self * other

    def __str__(self):
        res = '{' + str(self.coordinates[0])
        for i in range(1, self.n):
            res += ', ' + str(self.coordinates[i])
        return res + '}'

    def matrix(self):
        return Matrix([list(self.coordinates)]).transpose()

    def to_basis(self, basis):
        if self.basis is None:
            return Vector(basis.matrix ** -1 * self.matrix(), basis=basis)
        return self.to_primal_basis().to_basis(basis)

    def to_primal_basis(self):
        if self.basis is None:
            return self
        return Vector(self.basis.matrix * self.matrix())

    def proj(self, vector):
        return vector * (self * vector / (vector * vector))
