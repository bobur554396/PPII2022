# date with format: 20.02.2021
# ex1: [0-9]+\.[0-9]+\.[0-9]+
# ex2: [0-9]{2}\.[0-9]{2}\.[0-9]{4}
# ex3: \d{2}\.\d{2}\.\d{4}


# time with format: 14: 56: 10
# \d{2}:\d{2}:\d{2}



# phone: +7707-123-11-22  ----- +7(707)123-11-22 ---- 8(707)123-11-22
# ex: \+7\d{3}-\d{3}-\d{2}-\d{2}
# ex: (\+7|8)\(?\d{3}\)?-?\d{3}-\d{2}-\d{2}


# email: bobur.mukhsimbaev@kbtu.kz
# ex1: [a-z]+\.[a-z]+@[a-z]+\.[a-z]+
# \w+\.?\w+@\w+\.\w{2,5}
