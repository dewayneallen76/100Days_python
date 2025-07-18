import art
print(art.logo)
# TODO-4: Compare bids in dictionary
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bidding = True
while continue_bidding:
    # TODO-1: Ask the user for input
    name = input("What is your name?")
    price = int(input("What is your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    bids[name] = price
    # TODO-3: Whether if new bids need to be added
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if should_continue == 'no':
        continue_bidding = False
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        print("\n" * 20)


