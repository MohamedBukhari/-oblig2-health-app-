class Health:
    def __init__(self, name, weight_kg, height_m):
        if not name:
            raise ValueError("Name is empty...")

        if weight_kg <= 0:
            raise ValueError("weight must be positive...")

        if height_m <= 0:
            raise ValueError("height_m must be positive...")

        self.name = name
        self.weight_kg = weight_kg
        self.height_m = height_m
        self.bmi = round(weight_kg / (height_m ** 2), 2)

    def get_category(self):
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    def get_health_advice(self):
            category=self.get_category()
            if category=="Underweight":
                return "eat more healthy food"
            if category=="Normal":
                return "Maintain lifestyle"
            if category=="Overweight":
                return "make haelthy diet"
            if category=="Obese":
                return " you must go to doctor"
    def get_idael_weight(self):
        return round( 22*(self.height_m**2),1)
    