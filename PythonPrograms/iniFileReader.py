import configparser

config = configparser.ConfigParser()
config.read("Data/config.ini")

val = config.get("facebook","url")
print(val)

config.add_section("Amazon")
config.set("Amazon","url","https://amazon.com")

with open("Data/config.ini","w") as f:
    config.write(f)