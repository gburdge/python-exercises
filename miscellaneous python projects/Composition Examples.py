class Civic():

    def __init__(self, model, options):

        if model == "2009 LE":
            self.steering_wheel = SteeringWheel(12, 'leather', 'black')
            self.seat = Seat('suede')
        elif model == '2010 SE':
            pass
            # do some stuff.

        for option, boolean in options.items():
            setattr(self, option, boolean)

        setattr(self, 'paint_color', 'rusty_orange')


class SteeringWheel():
    def __init__(self, diameter, material, color):
        self.diameter = diameter
        self.material = material
        self.color = color


class Seat():
    def __init__(self, material):
        self.material = material

my_new_civic = Civic("2009 LE", {'power_steering': True, 'air_conditioning': False, 'mp3_player': True})

print my_new_civic.__dict__
# my_new_civic_steering_wheel = SteeringWheel(12, 'leather', 'black')
# my_new_civic.steering_wheel = my_new_civic_steering_wheel
