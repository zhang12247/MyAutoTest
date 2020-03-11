import faker


class FakerBean():
    def __init__(self):
        self.ff = faker.Faker(locale='zh-CN')

    def generateIdNumber(self):
        return self.ff.ssn()

    def generateName(self):
        return self.ff.name()


if __name__ == '__main__':
    ff =FakerBean();
    print(ff.generateIdNumber())
    for i in range(100000):
        file = open('/Users/zhangjiabin/Documents/workDocument/name.txt', 'a')
        file.write(ff.generateIdNumber() + ',' + ff.generateName() + '\n')
        file.close()