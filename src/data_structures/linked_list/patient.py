class Patient:
    def __init__(self, id, name, age, illness, emergency_level):
        self.id = id
        self.name = name
        self.age = age
        self.illness = illness
        self.emergency_level = emergency_level

    def __repr__(self):
        return f"Patient(id={self.id}, name='{self.name}', age={self.age}, illness='{self.illness}', emergency_level={self.emergency_level})"

    def to_tuple(self):
        return [self.id, self.name, self.age, self.illness, self.emergency_level]