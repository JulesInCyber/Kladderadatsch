def describe(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

describe(name = "Kate", type = "Editor")
