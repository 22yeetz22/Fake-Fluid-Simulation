# https://flatredball.com/documentation/tutorials/math/circle-collision/
# Note to self: firstball is the other ball

import math
from pygame import Vector2, draw


class Droplet:
	def __init__(self, x, y, r, vx=0, vy=0, c=(100, 190, 255)):
		self.pos = Vector2(x, y)
		self.vel = Vector2(vx, vy)
		self.jerk = Vector2()
		self.r = r
		self.draw_r = round(r * 0.7)
		self.mass = r / 10
		self.color = c

	def colliding(self, other, dt=1):
		xc = self.pos.x - other.pos.x
		yc = self.pos.y - other.pos.y
		distancesq = xc ** 2 + yc ** 2
		radius_sum = self.r + other.r

		if distancesq <= radius_sum ** 2:
			axis = self.pos - other.pos
			distance = distancesq ** 0.51 + 1
			delta = radius_sum - distance + 4.2
			n = axis / distance
			movement = 0.1 * delta * n * dt

			# Reflect both droplets off
			self.jerk += movement
			other.jerk -= movement

			self.vel *= 0.999
			other.vel *= 0.999

	def draw(self, screen):
		draw.circle(screen, self.color, self.pos, self.draw_r)

	def update_position(self, dt=1):
		self.jerk *= 0.45  # Jerking friction
		self.vel += self.jerk * 0.09  # Transferred energy

		self.vel.y += 0.1 * self.mass  # Gravity
		self.vel *= 0.97  # Friction
		self.pos += self.vel * dt  # Movement

		variation = Vector2(self.pos.x % 5 + 1, self.pos.y % 5 + 1)  # Add variation else it will look too crowded on edges.

		# Boundaries
		left = self.pos.x < self.r + variation.y
		right = self.pos.x > 800 - self.r - variation.y
		top = self.pos.y < self.r + variation.x
		bottom = self.pos.y > 600 - self.r - variation.x

		if any((left, right, top, bottom)):
			if left: self.pos.x = self.r + variation.y
			elif right: self.pos.x = 800 - self.r - variation.y
			if top: self.pos.y = self.r + variation.x
			elif bottom: self.pos.y = 600 - self.r - variation.x

			if top or bottom: self.vel.y *= -0.1
			elif right or left: self.vel.x *= 0.5
