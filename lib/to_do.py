def to_do(texts):
    if type(texts) != str:
        raise Exception("Argument must be a string")
    else:
        if "#TODO" in texts: 
            result = True 
            return "This task contains a #TODO." 
        else: 
            result = False 
            return "This task does not contain a #TODO." 
    
