class Solution():
    def __init__(self):
        pass
        
    def sort(self, packages):

        results = []
        
        for package in packages:
            width, height, length, mass = package
            result = self.sort(width, height, length, mass)
            results.append(result)
        
        return results
    
    def sort(self, width, height, length, mass):

        volume = width * height * length

        is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
        is_heavy = mass >= 20

        if is_bulky and is_heavy:
            return "REJECTED"
        elif is_bulky or is_heavy:
            return "SPECIAL"
        else:
            return "STANDARD"

