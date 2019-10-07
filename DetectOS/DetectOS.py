import distro

class DetectOS:

	def _init_(self):
		self.nom = distro.linux_distribution(full_distribution_name=False)