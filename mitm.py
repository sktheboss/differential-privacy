from mitmproxy import proxy, options
from mitmproxy.tools.dump import DumpMaster
from mitmproxy.addons import core

# from mitmproxy.options import Options
# from mitmproxy.proxy import ProxyConfig
# from mitmproxy.proxy.server import ProxyServer
# from mitmproxy.tools.dump import DumpMaster

class AddHeader:
    def __init__(self):
        self.num = 0

    def response(self, flow):
        self.num = self.num + 1
        print(self.num)
        flow.response.headers["count"] = str(self.num)


addons = [
    AddHeader()
]

opts = options.Options(listen_host='127.0.0.1', listen_port=8080)
pconf = proxy.(opts)

m = DumpMaster(None)
m.server = proxy.server.ProxyServer(pconf)
# print(m.addons)
m.addons.add(addons)
print(m.addons)
# m.addons.add(core.Core())

try:
    m.run()
except KeyboardInterrupt:
    m.shutdown()