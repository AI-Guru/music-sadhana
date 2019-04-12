
def append_values_to_csv(values, file):
    values = [str(value) for value in values]
    values = ", ".join(values)
    with open(file, "a") as myfile:
        myfile.write(values + "\n")
