# Function "hotel_cost" captures in the num_nights
# outputs total_cost as num_nights * hotel_price
def hotel_cost(num_nights):
    total_cost = num_nights * hotel_price
    return total_cost

# Function "plane_cost" captures in city_flight
# Returns flight price based on city
def plane_cost(city_flight):
    if city_flight == "Lanseria":
        return 1500
    elif city_flight == "Johannesburg":
        return 1450
    elif city_flight == "Cape Town":
        return 2500
    elif city_flight == "Port Elizabeth":
        return 2300
    elif city_flight == "George":
        return 1600
    elif city_flight == "Durban":
        return 1100
    
    # Should the city not be listed in the provided options, prompt the user to input the cost of their flight manually

    else:
        enter_flight_cost = int(input("The city provided does not match any in our established list. Could you please input the cost of your flight?: "))
        return enter_flight_cost

# Define a function named "car_rental" which accepts the number of days a car is rented
# It calculates the total rental cost as the product of the number of days and the daily rental rate

def car_rental(rental_days):
    car_rental_price = rental_days * rental_price
    return car_rental_price

# Define a universal function "holiday_cost" that receives plane_cost, hotel_cost, and car_rental as arguments
# It calculates the total_holiday_cost by adding up the aforementioned costs

def holiday_cost():
    flight_round_trip_cost = flight_cost * 2
    total_holiday_cost = round(hotel_cost(num_nights) + car_rental(rental_days) + flight_round_trip_cost, 2)
    return total_holiday_cost

# Prompt the user to specify the city of their flight destination
# Assign the flight_cost to a variable to prevent repeated invocations of the plane_cost function

city_flight = input("To which city are you flying to?: ").capitalize()
flight_cost = plane_cost(city_flight)

# Request user to input number of night of travel
num_nights = int(input("How many nights will you be staying?:  "))

# Prompt the user to specify the duration of the car rental in days
# Ensure that the number of rental days does not exceed the number of nights booked
# Employ a while loop and an if-statement for validation

while True:
    rental_days = int(input("How many days do you want to rent a car?: "))
    if rental_days > num_nights:
        print("Your car rental days exceed your holiday days. Please re-enter your car rental days.")
        continue
    else:
        break

# Request user to input the daily car rental rate
rental_price = float(input("What is the car rental rate per day?: "))

# Request user to input the hotel rate
hotel_price = float(input("What is the hotel rate per night?: "))

# output the hotel, flights, car rental and holiday cost prices total
print(f"Your return flights to {city_flight} will cost R{flight_cost*2}.")
print(f"The total hotel cost for {num_nights} days will be R{hotel_cost(num_nights)}.")
print(f"The total car rental cost for {rental_days} days will be R{car_rental(rental_days)}.")
print()
print(f"The total holiday cost will be R{holiday_cost()}.")