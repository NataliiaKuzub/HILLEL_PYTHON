def dict_constructor(arg_1, arg_2, arg_3, arg_4):
    return {
        "model": arg_1,
        "max_speed": arg_2,
        "engine": dict(capacity=arg_3, power=arg_4)
    }


def data_list():
    return input("Please, enter car data (model/speed/capacity/power): ").split("/")


cars_data = []
k = data_list()
while k != ['']:
    cars_data.append(dict_constructor(k[0], k[1], k[2], k[3]))
    k = data_list()

for car in sorted(cars_data, key=lambda i: int(i["engine"]["power"]), reverse=True):
    print(car)

