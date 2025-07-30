def format_name(f_name, l_name):
    """Takes a first and last name and format it to return the title case
    version of the name"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")


def multiply(num_1, num_2):
    """Multiplies num_1 and num_2"""
    return num_1 * num_2


print(multiply(3, 5))
