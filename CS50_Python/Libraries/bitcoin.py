import sys
import requests
#get value form command line
if len (sys.argv)==2:
    try:
        value=float(sys.argv[1])
    except:
        print("Missing command-line argument is not a number")
        sys.exit(1)
else:
    print("Missing command-line argument")
    sys.exit(1)

try:
    r= requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    response= r.json()
    bitcoin = response['bpi']['USD']['rate_float']
    amount= bitcoin * value
    print(f"${amount:,.4f}")

except requests.RequestException:
    print("RequestException")
    sys.exit(1)
