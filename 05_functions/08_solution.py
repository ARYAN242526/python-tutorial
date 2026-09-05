def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="shaktiman", power="lasers")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lasers", enemy="Dr. Jackaal")