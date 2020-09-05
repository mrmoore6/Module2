
def convert_to_months(year):
    months = year * 12
    return(months)


if __name__ == '__main__':
    age_in_months = int(input("Enter years"))
    age_in_years = convert_to_months(age_in_months)
    print(age_in_years, "months")



#FFF
