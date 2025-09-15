class Solution():
    def __init__(self):
        pass
        
    def sort(self, packages):
        """
        Sort a list of packages based on their dimensions and mass.
        
        Args:
            packages: List of tuples/lists containing (width, height, length, mass)
        
        Returns:
            List of strings: ["REJECTED", "SPECIAL", "STANDARD"] for each package
        """
        results = []
        
        for package in packages:
            width, height, length, mass = package
            result = self.sort(width, height, length, mass)
            results.append(result)
        
        return results
    
    def sort(self, width, height, length, mass):
        """
        Classify a single package based on its dimensions and mass.
        
        Args:
            width, height, length: Dimensions
            mass: Mass of the package
        
        Returns:
            str: "REJECTED", "SPECIAL", or "STANDARD"
        """
        volume = width * height * length

        is_bulky = volume >= 1000000 or width >= 150 or height >= 150 or length >= 150
        is_heavy = mass >= 20

        if is_bulky and is_heavy:
            return "REJECTED"
        elif is_bulky or is_heavy:
            return "SPECIAL"
        else:
            return "STANDARD"
