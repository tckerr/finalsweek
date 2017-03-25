class RouteRegister:

	def RegisterAll(self, router_source, router_destination):
		for route in router_source.registry:
			router_destination.register(*route)