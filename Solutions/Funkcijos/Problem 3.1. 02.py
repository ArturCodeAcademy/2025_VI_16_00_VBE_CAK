def month_name(month_number):
    if month_number == 1:
        return "Sausis"
    elif month_number == 2:
        return "Vasaris"
    elif month_number == 3:
        return "Kovas"
    elif month_number == 4:
        return "Balandis"
    elif month_number == 5:
        return "Geguze"
    elif month_number == 6:
        return "Birzelis"
    elif month_number == 7:
        return "Liepa"
    elif month_number == 8:
        return "Rugpjutis"
    elif month_number == 9:
        return "Rugsejis"
    elif month_number == 10:
        return "Spalis"
    elif month_number == 11:
        return "Lapkritis"
    elif month_number == 12:
        return "Gruodis"
    else:
        return "Neteisingas mėnesio numeris"


def month_name2(month_number):
    months = ["Sausis", "Vasaris", "Kovas", "Balandis", "Geguze", "Birzelis",
              "Liepa", "Rugpjutis", "Rugsejis", "Spalis", "Lapkritis", "Gruodis"]
    if 1 <= month_number <= 12:
        return months[month_number - 1]
    else:
        return "Neteisingas mėnesio numeris"

n = int(input())
print(month_name2(n))