class Patient:
    def __init__(self, name, condition, urgency):
        self.name = name
        self.condition = condition
        self.urgency = urgency 

    def __repr__(self):
        return f"{self.name} ({self.condition}) - Urgency {self.urgency}"



