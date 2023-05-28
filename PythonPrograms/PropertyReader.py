import configparser
config = configparser.ConfigParser()
config.read("Data/config.properties")
print(config['google']['url'])

config['selenium'] = {"browser":"chrome","timeouts":"30"}
with open("Data/config.properties","w") as file:
    config.write(file)