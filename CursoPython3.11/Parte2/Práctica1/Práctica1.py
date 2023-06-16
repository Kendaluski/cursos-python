def http_error(status):
    match status:
        case 400:
            return "Incorrect Request"
        case 404:
            return "Not Found"
        case 418:
            return "Nanomachines Son"
        case _:
            return "Something Else"
print("Introduce un numero: ")
check = int(input())
print(http_error(check))