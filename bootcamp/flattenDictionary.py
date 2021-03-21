def flatten_dictionary(dictionary):
    flat = {}
    for key in dictionary:
        if type(dictionary[key]) == dict:
            flatObj = flatten_dictionary(dictionary[key])
        for i in flatObj:
            if i != "" and key != "":
                flat[key + '.' + i] = flatObj[i]
            if i == "" and key != "":
                flat[key] = flatObj[i]
            if key == "" and i != "":
                flat[i] = flatObj[i]
        else:
            flat[key] = dictionary[key]
    return flat
 
