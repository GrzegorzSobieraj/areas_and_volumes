class Polygon:
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
        self.sides = [0 for i in range(number_of_sides)]

    def enter_sides(self):
        self.sides = [float(input(f"Enter side {str(i + 1)}: ")) for i in range(self.number_of_sides)]


class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 3)

    def calculate_area(self):
        a, b, c = self.sides
        # Calculate the semi-perimeter
        s = (a + b + c) / 2
        # Calculate area of the triangle
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print(f'Area of the triangle is {area}')
        return area


class Square(Polygon):
    def __init__(self):
        Polygon.__init__(self, 1)

    def calculate_area(self):
        a = self.sides[0]
        # Calculate area of the square
        area = a**2
        print(f'Area of the square is {area}')


class Rectangle(Polygon):
    def __init__(self):
        Polygon.__init__(self, 2)

    def calculate_area(self):
        a, b = self.sides
        # Calculate area of the rectangle
        area = a*b
        print(f'Area of the rectangle is {area}')


class Polyhedron(Polygon):
    pass


class Cube(Polyhedron):
    def __init__(self):
        Polyhedron.__init__(self, 1)

    def calculate_volume(self):
        a = self.sides[0]
        # Calculate volume of the cube
        volume = a**3
        print(f'Volume of the cube is {volume}')


class RegularPyramid(Polyhedron):
    def __init__(self):
        Polyhedron.__init__(self, 3)

    def calculate_volume(self):
        # Calculate area of the base
        base = Triangle()
        base.sides = self.sides
        area_of_base = base.calculate_area()
        height = float(input(f"Enter height of the regular pyramid: "))
        # Calculate volume of the regular pyramid
        volume = (1/3)*area_of_base*height
        print(f'Volume of the regular pyramid is {volume}')


class Oval:
    def __init__(self):
        self.major_radius = 0
        self.minor_radius = 0

    def enter_radiuses(self):
        self.major_radius = float(input(f"Enter major radius: "))
        self.minor_radius = float(input(f"Enter minor radius: "))

    def calculate_area(self):
        from math import pi
        area = self.major_radius * self.minor_radius * pi
        print(f'Area of the oval is {area}')


while True:
    try:
        choice = int(input('\nChoose one of the geometric shapes or 0 to exit:\n'
                           '1. triangle\n'
                           '2. square\n'
                           '3. rectangle\n'
                           '4. cube\n'
                           '5. regular pyramid\n'
                           '6. oval\n'))
    except ValueError:
        continue

    if choice == 1:
        t = Triangle()
        t.enter_sides()
        t.calculate_area()

    elif choice == 2:
        s = Square()
        s.enter_sides()
        s.calculate_area()

    elif choice == 3:
        r = Rectangle()
        r.enter_sides()
        r.calculate_area()

    elif choice == 4:
        c = Cube()
        c.enter_sides()
        c.calculate_volume()

    elif choice == 5:
        rp = RegularPyramid()
        rp.enter_sides()
        rp.calculate_volume()

    elif choice == 6:
        o = Oval()
        o.enter_radiuses()
        o.calculate_area()

    elif choice == 0:
        break

    else:
        continue
