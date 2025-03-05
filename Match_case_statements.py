# Match-case statement (switch): An alternative to using many 'elif' statements
#                                Execute some code if a value matches a 'case' (value == case)
#                                Benefits: cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:                                 # à la place de : if day == 1:
            return "it's Monday"
        case 2:                                 # à la place de : elif day == 2:
            return "It's Tuesday"
        case 3:
            return "It's Wednesday"
        case 4:
            return "It's Thursday"
        case 5:
            return "It's Friday"
        case 6:
            return "It's Saturday"
        case 7:
            return "It's Sunday"
        case _:                                 # Wild card = si aucun cas n'est valide -> else statement
            return "Not a valid day"


def is_weekend(day):
    match day:
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case "Saturday" | "Sunday":             # | or operator
            return True
        case _:                                 # Wild card = si aucun cas n'est valide -> else statement
            return "Not a valid day"

print(is_weekend("Sunday"))
