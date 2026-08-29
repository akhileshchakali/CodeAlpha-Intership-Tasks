stock_prices={'AAPL':180,'TSLA':250,'META':500,'MSFT':420,'AMZN':175,'NFLX':700,'ORCL':175,'UBER':80,'SONY':85}
investment=0
total_investment=0
print(f'Available Stocks: {' '.join(stock_prices.keys())}')
portfolio=[]

while True:
    stock_name=input('\nEnter Stock name (or "DONE" to finish):').upper() #DONE

    if stock_name=='DONE':
        break

    if stock_name not in stock_prices:
        print('stock not available! choose from available stocks')
        continue

    quantity=int(input(f'How Many {stock_name} stocks need:')) 

    price=stock_prices[stock_name]  
    investment=(price*quantity)  
    total_investment+=investment  
    portfolio.append((stock_name,quantity,price,investment)) 



print('\n-------Stock Portfolio-------')
for stock_name,quantity,price,investment in portfolio:
    print(f'{stock_name} : {quantity} shares x ${price} = ${investment}')

print('\n----------------------------')
print(f'Total Investment: ${total_investment}') #$1250

with open('portfolio.txt','w')as f:
    f.write('\n\n-------Stock Portfolio-------\n')
    
    for stock_name,quantity,price,investment in portfolio:
        f.write(f'{stock_name} : {quantity} shares x ${price} = ${investment}\n')

    f.write('\n----------------------------\n')
    f.write(f'Total Investment: ${total_investment}')


print("\nPortfolio saved to portfolio.txt")
    

    
    
