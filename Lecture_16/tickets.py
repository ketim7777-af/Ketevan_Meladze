class MovieTicket:

    cinema_name = "Rustaveli Cinema"  
    total_tickets_sold = 0 

    def __init__(self, movie_title, seat_number, price):
        self.movie_tittle = movie_title
        self.seat_number = seat_number
        self.price = price
           
    def add_ticket_nums(self, ticket_num):
        MovieTicket.total_tickets_sold += ticket_num      
        
    def display(self):
            
        print(f"Cinema name: {self.cinema_name}")
        print(f"Moie title: {self.movie_tittle}")
        print(f"Seat_number: {self.seat_number}")
        print(f"Price: {self.price}")
        print(f"Total tikets sold: {self.total_tickets_sold}")
        
      
ticket_1 = MovieTicket ("Titanic", "5 / 5", "25 L")
ticket_1.add_ticket_nums(1)
ticket_1.display()

print("=" *30)

ticket_2 = MovieTicket ("Londre", "10 / 15", "15 L")
ticket_2.add_ticket_nums(1)
ticket_2.display()

print("=" *30)

ticket_3 = MovieTicket ("Sali", "12 / 25", "35 L")
ticket_3.add_ticket_nums(2)
ticket_3.display() 
       
    