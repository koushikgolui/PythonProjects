class BaseOrder:
    id: int
    price: float

    def __init__(self, order_id: int, order_price: float, order_type: str):
        self.id = order_id
        self.price = order_price
        self.order_type = order_type

class OrderType:
    delivery_cost: float = 0.0
    def __init__(self, order_type: str):
        self.order_type = order_type

        if self.order_type == 'Offline':
            self.delivery_cost = 3
        elif self.order_type == 'Online':
            self.delivery_cost = 5
        else:
            self.delivery_cost = float(input())

class OrderProcessor:
    TAX_VALUE: float = 0.01

    def calculate_service_fee(self, order: BaseOrder, ordertype: OrderType) -> float:
        # delivery_cost depends on the type of order:
        # Offline -> static value: 3 euro
        # Online -> static value: 5 euro
        # Test -> dynamic value: we should be able to set any value

        service_fee = order.price * self.TAX_VALUE + ordertype.delivery_cost

        return service_fee