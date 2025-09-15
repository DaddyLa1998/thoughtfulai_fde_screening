# thoughtfulai_fde_screening

Scan(Packages):
    Scan a list of packages based on their dimensions and mass.

        Args:
            packages: List of tuples/lists containing (width, height, length, mass)
        
        Returns:
            List of strings: ["REJECTED", "SPECIAL", "STANDARD"] for each package


Sort(width, height, length, mass):
    Classify a single package based on its dimensions and mass.
        
        Args:
            width, height, length: Dimensions
            mass: Mass of the package
        
        Returns:
            str: "REJECTED", "SPECIAL", or "STANDARD"
