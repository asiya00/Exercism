def slices(series, length):
    if length > 0 and length <= len(series):
        i = 0
        li = []
        while len(series[i:i+length]) > length-1:
            li.append(series[i:i+length])
            i += 1
        return(li)
    else:
        raise ValueError("exceeded length value, negative and less than 0 values are not allowed")

    
