import classes

password = str(input("Password: "))

print(classes.Checked().check_entropy(password))