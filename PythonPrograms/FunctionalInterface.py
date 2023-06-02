def handle_monday():
    print("handle_monday")
def handle_tuesday():
    print("handle_tuesday")
def handle_wednesday():
    print("handle_wednesday")
def handle_thursday():
    print("handle_thursday")
def handle_friday():
    print("handle_friday")
def handle_saturday():
    print("handle_saturday")
def handle_default():
    print("Invalid")

weekday = {
    1:handle_monday,
    2:handle_tuesday,
    3:handle_wednesday,
    4:handle_thursday,
    5:handle_friday,
    6:handle_saturday,
}

day = 5
handler = weekday.get(day,handle_default)
handler()
