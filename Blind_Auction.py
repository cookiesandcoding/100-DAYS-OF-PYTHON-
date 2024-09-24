from art_bliindauction import logo
print(logo)
end_of_auction=False 
dict_values={}
while not end_of_auction :
  bidder=input("Enter your name ")
  bid_price=int(input("Enter your bid amount "))
  dict_values[bidder]=bid_price
  choice_to_continue = (input(" Are there any more bids ?")).lower()
  if choice_to_continue == "yes" :
   end_of_auction =False 
  else :
    bidding_amount=[]
    for key in dict_values:
      bidding_amount.append(dict_values[key])
      
    maximum_amount=max(bidding_amount)
    for key in dict_values:
     if dict_values[key]==maximum_amount :
       maximum_bidder=key
       print(f" The highest bid amount is {maximum_amount} by {maximum_bidder}")
       end_of_auction =True 
