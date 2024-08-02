

auction_detail={}
stop_bid=False

while not stop_bid:
    
    print("welcome to slient bid auction")
    name=input("Enter your name: ")
    bid=int(input("Enter your biding amount:"))
    auction_detail[name]=bid
    bid_continue=input("Do you want to continue yes or no: ").lower()
    if bid_continue =="yes":
        stop_bid=False
    elif bid_continue=="no":
        stop_bid=True
        maxbid=0
        biddername=''
        for bid in auction_detail:
            if auction_detail[bid]>maxbid:
                maxbid=auction_detail[bid]
                biddername=bid 
    
        print(f'The max bid is ${maxbid} by {biddername}')    