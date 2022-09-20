class Cat:
    name=None
    age=None
    isHappy=None

    def __init__(self, name=None, age=None, isHappy=None):
        self.name=name
        self.age=age
        self.isHappy=isHappy

        self.get_data()

    def set_data(self, name=None, age=None, isHappy=None):
        self.name=name
        self.age=age
        self.isHappy=isHappy

    def get_data(self):
        print(self.name, 'age:', self.age, 'Happy:', self.isHappy)



cat1=Cat('Toms')

'''cat1=Cat('Toms', 3, True)
cat2=Cat('Džeri', 7)

cat1.set_data('Toms', 3, True)
cat2=Cat()
cat2.set_data('Džeri', 7, False)
cat1.get_data()
cat2.get_data()'''



'''cat1.name="Milka"
cat1.age=3
cat1.isHappy=True
print(cat1.name, cat1.age,cat1.isHappy )

cat2=Cat()
cat2.name="Toms"
cat2.age=5
cat2.isHappy=False 
print(cat2.name, cat2.age,cat2.isHappy )'''
