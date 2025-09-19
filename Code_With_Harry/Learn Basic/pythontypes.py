def add(firstname: str | None, lastname: str = None):
    return firstname.capitalize() + " " + lastname.capitalize()

fname = "harry"
lname = "potter"

full_name = add(fname, lname)
print(full_name)