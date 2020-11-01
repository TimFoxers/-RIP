# Класс браузера
class Browser:
    currentId = 0
    # Используем для браузера следующие параметры:
    # Название, компания - разработчик.
    def __init__(self, Name, Developer, computerId):
        Browser.currentId = Browser.currentId + 1
        self.id = Browser.currentId
        self.Name = Name
        self.Developer = Developer
        self.computerId = computerId

    def __repr__(self):
        return "{0}, разработанный {1}".format(self.Name, self.Developer)



# Класс компьютера
class Computer:
    currentId = 0
    def __init__(self, name):
        Computer.currentId = Computer.currentId + 1
        self.id = Computer.currentId
        self.name = name


# Класс М-М связи
class CompProc:
    def __init__(self, browsId, compId):
        self.proc = browsId
        self.comp = compId


# Данные по браузерам
browsList = [
    Browser("Mozilla Firefox", "Mozilla Corporation", 1),
    Browser("Chrome", "Google", 2),
    Browser("Internet Explorer", "Microsoft", 3),
    Browser("Safari", "Apple", 5),
    Browser("Opera", "Opera Software", 4),
    Browser("Edge", "Microsoft", 6),
]
# Данные по компьютерам
compList = [
    Computer("Компьютер декана"),
    Computer("Лабораторный компьютер студента 600"),
    Computer("Персональный компьютер студента"),
    Computer("Ноутбук студента"),
    Computer("Преподавательский компьютер"),
    Computer("Компьютер рабочего"),
]
# Данные по связям (М-М)
prompList = [
    CompProc(3, 1),
    CompProc(4, 1),
    CompProc(3, 2),
    CompProc(5, 1),
    CompProc(1, 5),
    CompProc(2, 3),
    CompProc(6, 4),
    CompProc(4, 5),
    CompProc(1, 1),
    CompProc(2, 2),
    CompProc(4, 6),
    CompProc(3, 2)
]


def main():
    # Получим данные для О-М
    omDataList = list((computer, browser)
                      for computer in compList
                      for browser in browsList
                      if (computer.id == browser.computerId))

    # Задание 1:
    # На консоль выбрасывается информация о компьютерах,
    # в названии которых есть/нет подстрока "студента", а так же о браузерах на них
    print("\nРезультат выполнения задания 1:\n")
    for i in omDataList:
        if "студента" not in i[0].name:
            print("\t" + i[0].name + " имеет браузер ", repr(i[1]), sep='')

    # Задание 2:
    # На консоль выбрасывается информация о среднем количестве символов названия браузера
    # (ну нет у браузеров числительных характеристик) данного компьютера
    print("\nРезультат выполнения задания 2:\n")
    browsAvgList = list()
    # Перебираем компьютеры
    for comp in compList:
        # Ищем соответствующие браузеры
        brList = list(filter(lambda x: comp.id == x[1].computerId, omDataList))
        browsAverage = 0
        for item in brList:
            br = item[1]
            browsAverage = browsAverage + len(br.Name)
        browsAverage = round(browsAverage / len(brList), 2)
        browsAvgList.append((comp.name, browsAverage))
    for item in sorted(browsAvgList, key=lambda x: x[1]):
        print("\tДля компьютера \"{0}\" в среднем {1} символов в браузере".format(item[0], item[1]))


    # Предварительно получим данные для М-М
    mmDataList = list((computer.name, browser.id)
                      for computer in compList
                      for browser in browsList
                      for comp, proc in list((item.comp, item.proc) for item in prompList)
                      if computer.id == comp and browser.id == proc)

    # Задание 3:
    # На консоль выбрасывается информация о браузерах,
    # имя которых длиннее, чем 10 символов
    print("\nРезультат выполнения задания 3:\n")
    for browser in browsList:
        if len(browser.Name) < 10:
            continue
        # Ищем все связанные компьютеры
        computerList = list(filter(lambda x: br.id == x[1], mmDataList))
        print("\tБраузер {}, используется в ".format(repr(browser)))
        if len(computerList) == 0:
            print("\t\t ------------------")
        else:
            for item in computerList:
                print("\t\t", item[0])


if __name__ == '__main__':
    main()