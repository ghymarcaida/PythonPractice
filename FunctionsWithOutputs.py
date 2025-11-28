# Learning to work with Functions with Outputs

def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    
    return f"{formatted_f_name} {formatted_l_name}" #the return key is what differentiates a function with an output from other functions

formatted_string = format_name("garth", "marcaida")
print(formatted_string)