days_duration = int(input())
daily_food_cost = int(input())
one_way_flight_cost = int(input())
daily_hotel_cost = int(input())

food_cost = days_duration * daily_food_cost
hotel_cost = (days_duration - 1) * daily_hotel_cost
flight_cost = 2 * one_way_flight_cost

print(food_cost + hotel_cost + flight_cost)
