import json

class RegisterAccount:
    def __init__(self, fullname: str, age: int,  contact: int, postcode: str, init_amount = 0):
        self.fullname = fullname
        self.age = age
        self.contact = contact
        self.postcode = postcode
        self.init_amount = init_amount

    def to_dict(self):
        db = {
            "fullname":self.fullname,
            "age":self.age,
            "contact":self.contact,
            "postcode":self.postcode,
            "init_amount":self.init_amount
        }
        return db



    
