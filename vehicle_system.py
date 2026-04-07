import tkinter as tk
from tkinter import ttk

# =============================================================================
# 1. BASE CLASS (PARENT CLASS) - INHERITANCE ARCHITECTURE
# =============================================================================
class Vehiculo:
    """
    Acts as the Superclass. It encapsulates common properties and behaviors 
    that all specialized vehicle types will inherit.
    """
    def __init__(self, brand, model):
        # Data Encapsulation: Initializing core vehicle attributes
        self.brand = brand
        self.model = model
        self.current_speed = 0

    def acelerar(self, turbo=0, terrain="normal"):
        """
        SIMULATED METHOD OVERLOADING:
        Python uses default arguments to handle multiple method signatures:
        1. acelerar() -> No arguments (Base logic)
        2. acelerar(turbo) -> One argument (Power boost)
        3. acelerar(turbo, terrain) -> Two arguments (Environmental physics)
        """
        # Environmental logic: modifier reduces efficiency on rough surfaces
        modifier = 0.7 if terrain == "rough" else 1.0
        base_increase = 10
        # Formula: Speed calculation based on overloaded parameters
        self.current_speed += (base_increase + turbo) * modifier
        return f"{self.brand} is accelerating..."

    def detener(self):
        """Standard method to reset velocity to zero across all subclasses."""
        self.current_speed = 0
        return f"{self.brand} has stopped."

    def obtener_informacion(self):
        """Returns the current state of the object as a formatted string."""
        return f"Vehicle: {self.brand} {self.model} | Speed: {self.current_speed} km/h"