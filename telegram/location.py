class Location:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    
    def __str__(self):
        return f"{self.longitude}X{self.latitude}"
