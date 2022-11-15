class classname:
    def createname(self, name):
        self.name = name

    def displayname(self):
        return self.name

    def saying(self):
        print("Hello %s" % self.name)


first = classname
second = classname

first.createname("Bobby", "test")
