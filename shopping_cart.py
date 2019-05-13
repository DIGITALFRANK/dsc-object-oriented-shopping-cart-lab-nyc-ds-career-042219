class ShoppingCart:
    # write your code here
    def __init__(self, total=0, employee_discount=None, items=[]):
        self.total = total
        self.employee_discount = employee_discount
        self.items = items

    def add_item(self, name, price, quantity=1):
        self.items.append({'item': name, 'price': price, 'quantity': quantity})
        self.total += price * quantity

    def mean_item_price(self):
        n_items = 0
        for item in self.items:
            n_items += item['quantity']
        return self.total/n_items

    def median_item_price(self):
        price_list = []
        for item in self.items:
            for i in range(0, item['quantity']):
                price_list.append(item)
        if len(price_list) % 2 == 0:
            return (price_list[len(price_list)/2]['price'] + price_list[len(price_list)//2 - 1]['price'])/2
        else:
            return price_list[len(price_list)//2]['price']

    def apply_discount(self):
        if self.employee_discount is not None:
            return self.total * (1 - (self.employee_discount/100))
        else:
            return 'Sorry, there is no discount to apply to your cart :('

    def void_last_item(self):
        if self.items != []:
            self.total -= self.items[-1]['price']
            self.items.pop()
            return self.total
        else:
            return 'There are no items in your cart!'
