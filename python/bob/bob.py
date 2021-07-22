def response(hey_bob):
    hey_bob = hey_bob.replace(" ","")
    if hey_bob.isupper() and hey_bob[-1]=='?':
        return "Calm down, I know what I'm doing!"
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    elif len(hey_bob)==0 or all(True if i=='\t' or i=='\r' or i=='\n' else False for i in hey_bob):
        return "Fine. Be that way!"
    elif hey_bob[-1] == "?":
        return "Sure."
    else:
        return "Whatever."
