def is_person(person):
    """validates that input is not an empty string
    Examples:
        >>> is_person("   ")
        False
        >>> is_person('Henna')
        True
    """
    person = person.strip()
    if person:
        return True
    else:
        return False 
