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
        # =============================================================================
# 2. SUBCLASSES - DEMONSTRATING POLYMORPHISM & OVERRIDING
# =============================================================================

class AutoElectrico(Vehiculo):
    """
    Child class representing Electric Vehicles. 
    It overrides methods to implement specific EV physics.
    """
    def acelerar(self, turbo=0, terrain="normal"):
        # Executes parent logic while adding specific electric torque bonus
        super().acelerar(turbo, terrain)
        self.current_speed += 5 
        return f"[Electric] {self.brand} accelerating silently (Instant Torque)."

    def detener(self):
        # Total method overriding for regenerative braking logic
        self.current_speed = 0
        return f"[Electric] {self.brand} stopped with Regenerative Braking."

class Moto(Vehiculo):
    """Specialized subclass for high-performance Motorcycles."""
    def acelerar(self, turbo=0, terrain="normal"):
        # Polymorphism: Motorcycles ignore base physics for faster acceleration
        self.current_speed += (25 + (turbo * 1.5))
        return f"[Motorcycle] {self.brand} reaches high speed quickly!"

class Camion(Vehiculo):
    """Specialized subclass for heavy-duty Truck simulation."""
    def acelerar(self, turbo=0, terrain="normal"):
        # Polymorphism: High mass results in significantly lower acceleration
        self.current_speed += (5 + (turbo * 0.2))
        return f"[Truck] {self.brand} accelerating slowly due to heavy load."
        # =============================================================================
# 3. GUI LAYER (TKINTER) - PROFESSIONAL INTERFACE (ENGLISH)
# =============================================================================

class SmartMobilityUI:
    """
    Responsible for the Presentation Layer. 
    Decouples the UI logic from the core Object-Oriented models.
    """
    def __init__(self, window):
        self.window = window
        self.window.title("Smart Mobility Simulator v1.0")
        self.window.geometry("550x550")
        
        # POLYMORPHIC LIST: Array containing different object types.
        # This allows us to treat all instances as 'Vehiculo' via Polymorphism.
        self.vehicles = [
            AutoElectrico("Tesla", "Model 3"),
            Moto("Kawasaki", "Ninja 650"),
            Camion("Kenworth", "T680")
        ]
        
        self.setup_ui()

    def setup_ui(self):
        """Builds all graphical widgets using English labels as per requirements."""
        # Main Title Header
        ttk.Label(self.window, text="Vehicle Simulation Control", font=("Arial", 14, "bold")).pack(pady=15)

        # Action Buttons Container (Frame)
        btn_frame = ttk.Frame(self.window)
        btn_frame.pack(pady=10)

        # UI Triggers for Polymorphic tests
        ttk.Button(btn_frame, text="Accelerate All", command=self.run_acceleration).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="Stop All", command=self.run_stop).grid(row=0, column=1, padx=10)

        # Output Display (Simulation Log)
        ttk.Label(self.window, text="Execution Log:").pack(anchor="w", padx=25)
        self.display = tk.Text(self.window, height=18, width=60, bg="#1e1e1e", fg="#00ff00")
        self.display.pack(pady=10, padx=20)
        
        # Utility button to clear terminal
        ttk.Button(self.window, text="Clear Log", command=self.clear_display).pack(pady=5)

    def run_acceleration(self):
        """
        SINGLE LOOP POLYMORPHISM TEST:
        Calls the same method name 'acelerar' for all objects in the list.
        Each object responds according to its specific subclass implementation.
        """
        self.display.insert(tk.END, ">>> INITIATING SPEED TEST...\n")
        
        # Iterating through objects of different classes
        for v in self.vehicles:
            # Runtime Polymorphism: Python resolves the method at execution time
            result = v.acelerar(turbo=10, terrain="normal") 
            info = v.obtener_informacion()
            # Pushing results to the UI Log
            self.display.insert(tk.END, f"{result}\n{info}\n\n")
            
        self.display.see(tk.END)

    def run_stop(self):
        """Executes emergency stopping sequence for all fleet objects."""
        self.display.insert(tk.END, ">>> EMERGENCY BRAKE APPLIED...\n")
        for v in self.vehicles:
            msg = v.detener()
            self.display.insert(tk.END, f"{msg}\n")
        self.display.insert(tk.END, "Status: All vehicles are stationary.\n\n")
        self.display.see(tk.END)

    def clear_display(self):
        """Clears the text area of the UI display."""
        self.display.delete('1.0', tk.END)

# =============================================================================
# 4. MAIN ENTRY POINT
# =============================================================================
if __name__ == "__main__":
    # Initializing the Tkinter event loop
    root = tk.Tk()
    app = SmartMobilityUI(root)
    root.mainloop()