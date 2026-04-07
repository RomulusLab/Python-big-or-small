def response(hey_bob):
    ask_question = hey_bob.strip().endswith('?')
    yelling = hey_bob.isupper()
    
    if yelling and ask_question:
        return "Calm down, I know what I'm doing!"
    elif yelling:
        return "Whoa, chill out!"
    elif ask_question:
        return "Sure."
    elif not hey_bob.strip():
        return "Fine. Be that way!"
    else:
        return "Whatever."
