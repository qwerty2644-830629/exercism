PLANET = {'Mercury': 0.2408467, 'Venus':0.61519726, 'Earth': 1.0, 'Mars': 1.8808158, 
         'Jupiter': 11.862615, 'Saturn': 29.447498, 'Uranus': 84.016846, 'Neptune': 164.79132}
earth_time = 60 * 60 * 24 * 365.25

class SpaceAge:
    def __init__(self, seconds):
        self.seconds = seconds

    def on_mercury(self):
        return round(self.seconds / (earth_time * PLANET['Mercury']), 2)

    def on_venus(self):
        return round(self.seconds / (earth_time * PLANET['Venus']), 2)

    def on_earth(self):
        return round(self.seconds / (earth_time * PLANET['Earth']), 2)

    def on_mars(self):
        return round(self.seconds / (earth_time * PLANET['Mars']), 2)

    def on_jupiter(self):
        return round(self.seconds / (earth_time * PLANET['Jupiter']), 2)

    def on_saturn(self):
        return round(self.seconds / (earth_time * PLANET['Saturn']), 2)

    def on_uranus(self):
        return round(self.seconds / (earth_time * PLANET['Uranus']), 2)

    def on_neptune(self):
        return round(self.seconds / (earth_time * PLANET['Neptune']), 2)
