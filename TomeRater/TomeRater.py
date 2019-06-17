#book
class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        
    def get_title(self):
         return title
    def get_isbn(self):
        return isbn
    def set_isbn(self, isbn):
        self.isbn = isbn
        return "this books's isbn has been updated"
    
    def add_rating(self, rating):
         if rating>=0 and rating <=4:
            self.ratings.append(rating)
         else:
            return "Invalid  Rating"
    def __eq__(other_user):
        
       if self.title == other_user.title and self.isbn == other_user.isbn:
            return "both have teh same title and isbn"
    def get_average_rating(self):
        
      total_rating = 0
      for rating in self.books:
        total_rating += self.books.rating
        average_rating = total_rating/len(self.books)
    def __hash__(self):
        return hash((self.title, self.isbn))
    
       
# fiction
class Fiction(book):
       def __init__(self,author, title, isbn):
           super().__init__(title, isbn)
           self.author= author
       def get_author(self):
            return self.author
        
       def ___repr__(self):
          return self.title +"by" +self.author
 # Non- Fiction      
class Non_Fiction(book):
       def __init__(self, title, subject, level, isbn):
           super().__init__(title, isbn)
           self.subject= subject
           self.level = level
       def get_subject(self):
            return self.subject
       def get_level(self):
            return self.get_level
           
       def ___repr__(self):
          return self.title + "a" + self.level+ "manual on " + self.subject
 
       
    
  #user      
     

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = { }
    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        return "Users Email has need updated"

    def __repr__(self):
        
          return self.name + "email:"  + (self.email) + "-"+ "Books read :" + len(self.books)
    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return "both are same"
    def __read_book(self, book, rating = None):
      self.books[book:rating] = rating

    def get_average_rating(self):
        
      total_rating = 0
      for rating in self.rating:
        total_rating += rating
        average_rating = total_rating/len(self.rating)
      return average_rating      
   
# TomeRater
class TomeRater:
    def __init__(self):
     self.users = {}
     self.books = {}

    def create_book(self, title, isbn):
     return Books(title, isbn)

    def create_novel(self, title, author, isbn):
     return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject,level, isbn):
     return Non_Fiction(title, subject, level, isbn)
    
    def add_book_to_user(self, book, email, rating = None):
      for user in self.user:
         if email not in self.email:
           return "No user with email {email}".format(email = email)
         else:
          user.read_book(book, rating)
          user.add_rating(book, rating)
         if book not in self.books:
           self.books[book] = 1
         else:
          self.books[book] += 1

    def add_user(self, name, email, user_books = None):
      if user_books:
        for book in user_books:
          self.add_book_to_user(name, email)
      return User(name, email)

    def print_catalog(self):
      for book in self.books:
        print(book)

    def print_users(self):
      for user in self.users:
        print(user)

    def most_read_book(self):
      most_read = 0
      for value in self.books.values():
        if value > most_read:
          return most_read

    def highest_rated_book(self):
      highest_rated = 0
      for book in self.books:
        rating = book.get_average_rating()
        if rating > highest_rated:
          highest_rated = rating
          return highest_rated

    def most_positive_user(self):
      high_rated = 0
      for user in self.users:
        rating = user.get_average_rating()
        if rating > high_rated:
          high_rated = rating
          return high_rated    
    





