#-- You are given a list of customer IDs, some of which are duplicated. Write a Python function that takes in a list of customer ID's, 
#-- removes duplicates, prints each unique id, and returns a set of the unique IDs

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def refined_list (customer_ids):
    customer_set = set(customer_ids)
    return customer_set

print(refined_list(customer_ids))