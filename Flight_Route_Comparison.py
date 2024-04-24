# Imagine you work for an airline and need to compare the flight routes of your airline with a competitor.
# You have two sets of flight destinations, one for each airline. Write a Python program to find out:

# 1.) Destinations that both airlines fly to.
# 2.) Destinations unique to your airline.
# 3.) Whether there are any destinations that neither airline shares.

our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

#1.)
#-- set1.intersection(set2)
def itersect_flights(our_routes, competitor_routes):
    shared_destination = our_routes.intersection(competitor_routes)
    return shared_destination
print(itersect_flights(our_routes, competitor_routes))
#2.)
#-- set1.difference(set2)
def diff_flights(our_routes,competior_routes):
    different_flights = our_routes.difference(competitor_routes)
    return different_flights
print(diff_flights(our_routes,competitor_routes))

#3.)
#-- set.symmetric_difference(set2)
def our_flights(our_routes, competitor_routes):
    just_our_flights = our_routes.symmetric_difference(competitor_routes)
    return just_our_flights
print(our_flights(our_routes, competitor_routes))