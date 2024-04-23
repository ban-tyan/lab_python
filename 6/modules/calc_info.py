class Jacket:
    def __init__(self):
        self.name = "Пиджак"
        self.sewing_cost = 50
        self.fabric_consumption = 3
        self.accessories_cost = 10


class Trousers:
    def __init__(self):
        self.name = "Брюки"
        self.sewing_cost = 40
        self.fabric_consumption = 2.5
        self.accessories_cost = 8

class Suit:
    def __init__(self):
        self.name = "Тройка"
        self.sewing_cost = 100
        self.fabric_consumption = 5
        self.accessories_cost = 20
        
class Calculations:
    @staticmethod
    def calculate_fabric_cost(calc_info, size, fabric_price_per_square_meter):
        fabric_cost = size * fabric_price_per_square_meter * calc_info.fabric_consumption
        return fabric_cost

    @staticmethod
    def calculate_total_cost(calc_info, size, fabric_price_per_square_meter):
        fabric_cost = Calculations.calculate_fabric_cost(calc_info, size, fabric_price_per_square_meter)
        total_cost = fabric_cost + calc_info.sewing_cost + calc_info.accessories_cost
        return total_cost