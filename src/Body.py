import numpy as np


class Body:

    # G: Unit = m^3 kg^-1 s^-2
    gravatational_constant = 6.67430e-11

    def __init__(self, name, mass, position, velocity):
        self.name = name
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def update_position(self, dt):
        return None

    def get_new_acceleration(self, other_bodies):
        return None

    def update_velocity(self, dt):
        return None

    def compute_force(self, other_body):

        # Distance between the bodies and unit vector
        displacement = other_body.position - self.position
        distance = np.linalg.norm(displacement)

        # Avoid division by zero: no force if positions are identical
        if distance == 0:
            return np.zeros(3)

        # Unit vector (r_hat_ij)
        unit_vector = displacement / distance

        # Gravitational force
        force_magnitude = (self.G * self.mass * other_body.mass) / (distance ** 2)
        force_vector = force_magnitude * unit_vector
        return force_vector

