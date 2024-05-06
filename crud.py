def create_client(name, email, phone_number, address):
    return Client.objects.create(name=name, email=email, phone_number=phone_number, address=address)

def get_all_clients():
    return Client.objects.all()

def get_client_by_id(client_id):
    return Client.objects.get(id=client_id)

def update_client(client, **kwargs):
    for key, value in kwargs.items():
        setattr(client, key, value)
    client.save()

def delete_client(client):
    client.delete()


# Для модели "Товар"
def create_product(name, description, price, quantity):
    return Product.objects.create(name=name, description=description, price=price, quantity=quantity)

def get_all_products():
    return Product.objects.all()

def get_product_by_id(product_id):
    return Product.objects.get(id=product_id)

def update_product(product, **kwargs):
    for key, value in kwargs.items():
        setattr(product, key, value)
    product.save()

def delete_product(product):
    product.delete()


# Для модели "Заказ"
def create_order(client, products, total_amount):
    order = Order.objects.create(client=client, total_amount=total_amount)
    order.products.add(*products)
    return order

def get_all_orders():
    return Order.objects.all()

def get_order_by_id(order_id):
    return Order.objects.get(id=order_id)

def update_order(order, **kwargs):
    for key, value in kwargs.items():
        setattr(order, key, value)
    order.save()

def delete_order(order):
    order.delete()