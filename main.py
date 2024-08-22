reaction = ["дуже погано", "погано", "посередньо", "добре", "дуже добре"]

def reaction_calc(res):
    if res == 0:
        return reaction[0]
    elif 0 < res < 5:
        return reaction[1]
    elif res == 5:
        return reaction[2]
    elif 5 < res < 10:
        return reaction[3]
    else:
        return reaction[4]

def main():
    probability_rain = float(input("Введіть ймовірність дощу у %: "))
    rate_forest = int(input("За шкалою від 1 (жахливо) до 10 (неймовірно), як би ви оцінили «поїздку в ліс»?\n"))
    rate_home = int(input("За шкалою від 1 до 10, як би ви оцінили «залишитися вдома»?\n"))
    
    probability_rain /= 100
    probability_sun = 1 - probability_rain
    res1 = rate_forest * probability_sun + rate_forest * probability_rain
    res2 = rate_home * probability_sun + rate_home * probability_rain
    
    rea1 = reaction_calc(res1)
    rea2 = reaction_calc(res2)
    
    print(f"Поїздка в ліс - це {rea1} ідея.")
    print(f"Залишитися вдома - це {rea2} ідея.")
    
    print("Найкраще ", end="")
    if res1 < res2:
        print("залишитися вдома")
    elif res1 > res2:
        print("поїхати в ліс")
    else:
        print("зробити те, що забажаєте")

if __name__ == "__main__":
    main()
