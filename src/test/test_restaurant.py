from restaurant import Restaurant
from customer import Customer
from review import Review


def test_restaurant_init_name():
    """
    Should be able to initialize a restaurant with a name
    """
    restaurant = Restaurant("Monk's Cafe")
    assert restaurant.name == "Monk's Cafe"

def test_restaurant_get_name():
    """
    get_name() should return the restaurant's name
    """
    restaurant = Restaurant("Monk's Cafe")
    restaurant.get_name() == "Monk's Cafe"

def test_restaurant_get_reviews():
    """
    get_reviews() should return the list of reviews
    for the restaurant
    """
    restaurant = Restaurant("Monk's Cafe")
    customer = Customer('Jane', 'Doe')
    review = Review(customer, restaurant, 5)
    restaurant.reviews = [review]
    assert restaurant.get_reviews() == [review]

def test_restaurant_average_rating():
   
    restaurant = Restaurant("Monk's Cafe")
    review_1 = Review('Jane', restaurant, 5)
    review_2 = Review('Bob', restaurant, 7)
    review_3 = Review('Nick', restaurant, 3)
    restaurant.reviews = [review_1, review_2, review_3]
    assert restaurant.average_rating() == 5

