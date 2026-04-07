def response(hey_bob):
    ask_question = hey_bob.strip().endswith('?')
    yelling = hey_bob.isupper()
    
    if yelling and ask_question:
        return "Calm down, I know what I'm doing!"
    if yelling:
        return "Whoa, chill out!"
    if ask_question:
        return "Sure."
    if not hey_bob.strip():
        return "Fine. Be that way!"
    else:
        return "Whatever."
