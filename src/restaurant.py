class Restaurant:
    def __init__(self, name):
        self.name = name
        self.reviews = []

    def get_name(self):
        return self.name

    def get_reviews(self):
        return self.reviews
    
    def average_rating(self):
        return sum([review.rating for review in self.reviews])/len(self.reviews)