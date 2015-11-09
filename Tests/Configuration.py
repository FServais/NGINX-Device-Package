from NGINXConfiguration.NginxBackend import NginxBackend
from NGINXConfiguration.NginxBackendServer import NginxBackendServer
from NGINXConfiguration.NginxBackendServerParameters import NginxBackendServerParameters
from NGINXConfiguration.NginxConfiguration import NginxConfiguration
from NGINXConfiguration.NginxFrontend import NginxFrontend
from NGINXConfiguration.NginxServerLocation import NginxServerLocation

__author__ = 'Fabrice Servais'

# -- Backend
backend_name = "backend"

# Servers
server1 = NginxBackendServer(address="10.9.218.1", params=NginxBackendServerParameters(weight=2))
server2 = NginxBackendServer(address="10.9.218.2", params=NginxBackendServerParameters(weight=3))

backend = NginxBackend(name=backend_name, server_pool=[server1, server2])

# -- Frontend
# Location
location = NginxServerLocation(backend_name, '/')
frontend = NginxFrontend(locations=location)

# Configuration
config = NginxConfiguration(frontend, backend)

print("-------- Configuration ---------")
print(config)
print("\n------ Configuration File ------")
print(config.export())
print("--------------------------------")