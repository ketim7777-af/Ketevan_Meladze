
class SmarDevice:
    def __init__(self, brand):
        self.brand = brand
        self.__is_on = False

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_on = False

    def show_status(self):
        if self.__is_on:
            print("Light is on.")
        else:
            print("Light is off.")

class SmartLight(SmarDevice):
    def __init__(self, brand, brightness):
        super().__init__(brand)

        if 0 <= brightness <= 100:
            self.brightness = brightness
        else:
            raise ValueError("Brightness is between 0 and 100.")

    def turn_on(self):
        super().turn_on()
        print(f"{self.brand}")
        print(f"Brightness: {self.brightness}")


light = SmartLight("Philips", 100)

light.turn_on()
light.show_status()
             



