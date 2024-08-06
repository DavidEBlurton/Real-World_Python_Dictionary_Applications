# 2. Python Programming Challenges for Customer Service Data Handling
# Objective: This assignment is designed to test and enhance your Python programming skills, focusing on real-world applications in customer service data management. You will practice correcting code, organizing customer data, and implementing a feedback system using Python dictionaries.

# Task 1: Customer Service Ticket Tracker Demonstrate your ability to use nested collections and loops by creating a system to track customer service tickets.

# Problem Statement: Develop a program that:

# Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
# Implement functions to:
# Open a new service ticket.
# Update the status of an existing ticket  to "closed".
# Display all tickets.
# (Bonus) filter by status
#  Initialize with some sample tickets and include functionality for additional ticket entry.
# Example ticket structure:


service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}}

def next_id():
    last_id = 0
    for id in service_tickets.keys():
        if id > last_id:
            last_id = id
    return last_id + 1
    
def open_new():
    new_id = next_id()
    while True:
        customer = input('Please enter customer name: \n')
        issue = input('Please tell us your issue: \n')
        status = ('open')
        print(f'Customer: {customer}, Issue: {issue}')
        correct = input('Is this correct? (y/n)').lower()
        if correct == 'y':
            service_tickets[new_id] = {'Customer': customer, 'Issue': issue, 'Status': status}
            break
        else:
            continue
        
def change_status():
    servive_ticket_id = int(input('Please give us your service ticket number.'))
    print(service_tickets[servive_ticket_id]['Status'])
    if service_tickets[servive_ticket_id]['Status'] == 'open':
        service_tickets[servive_ticket_id]['Status'] = 'closed'
    print(service_tickets[servive_ticket_id]['Status'])



def main():
    while True:
        action = input('''
     Customer Service Center
     ------------------------
    1 - Open new service ticket
    2 - Update sevice ticket to closed
    3 - Display all tickets
    4 - Quit
    ''')

        if action == '1':
            open_new()
        elif action == '2':
            change_status()
        elif action == '3':
            print(service_tickets)
        elif action == '4':
            print("Thank you for using our customer service.")
        else: 
            print("Please make a valid selection")


main()
