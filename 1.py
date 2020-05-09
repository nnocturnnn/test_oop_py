

class Computer:
    def __init__(self, cpu, frequency, ram):
        self.cpu = cpu
        self.frequency = int(frequency)
        self.ram = int(ram)

    def quality(self):
        q = self.frequency * 0.1 + self.ram
        return q

    def info(self):
        print("Процессор - " + str(self.cpu))
        print("Частота процессора - " + str(self.frequency))
        print("Обьем оперативної памяті - " + str(self.ram))


class full(Computer):
    def __init__(self, du):
        self.du = du

    def quality(self):
        q = computer.frequency * 0.1 + computer.ram + 0.5 * self.du
        return q


computer = Computer("gdfgdf 4342523",5,1200)
computer2 = full(50)

computer.info()
print(computer.quality())
print(computer2.quality())
