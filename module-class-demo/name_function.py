def get_formatted_name(first,last,middle=''):
    if middle:
        full_name=f"{first} {middle} {last}"
    else:
        """返回整洁的姓名"""
        full_name=f"{first} {last}"
    return full_name.title()