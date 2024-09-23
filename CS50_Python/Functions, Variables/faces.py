def main ():
    #get user input
    msg = input()
    #call convert function
    result =convert(msg)
    #Print the result
    print(result)
def convert (msg):
    #Replace :) for happy emoji
    msg1=msg.replace(":)", '🙂')
    #Replace :) for sad emoji
    msg2=msg1.replace(":(", '🙁')
    #Print string
    return msg2
main()