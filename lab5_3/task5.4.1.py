def hide_email(email):
    # Hide part of the email for privacy
    parts = email.split('@')
    if len(parts) != 2:
        return "Invalid email"
    name, domain = parts
    if len(name) <= 2:
        hidden_name = name[0] + "*" * (len(name)-1)
    else:
        hidden_name = name[0] + "*" * (len(name)-2) + name[-1]
    return f"{hidden_name}@{domain}"

# Collect user data
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")

user_data = {
    "name": name,
    "age": age,
    "email": hide_email(email)
}

print("User data (with hidden email):")
print(user_data)
