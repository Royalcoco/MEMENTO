<srvp.device> <srvp.device_type>
    #   Send a device command to the device specified by its name and type. If the device is not found, an error message will be returned
    #   Add a new device to the server pool. The 'devicetype' argument specifies the type of the device, which
    #   - Add a new device to the server's list of known devices. If the device type is not specified, it will
    #   Add a new device to the server pool.  The 'devicetype' parameter should be one of:
    #     ethernet, infinib and ibverbs
    # - Add a new device to the server pool with an RDMA port specified by the user.
    #   If no RDMA port is provided then the first available will be used.
    def add_device(self, devicename, devicetype):
        raise NotImplementedError()

class ServerDevicePool(DevicePoolBaseClass):
    """Server side Device Pool"""
    pass

class ClientDevicePool(DevicePoolBaseClass):
    """Client side Device Pool"""

    _server = None
    @property
    def server(self):
        return self._server

    @server.setter
    def server(self, value):
        if not isinstance(value, ServerDevicePool):
            raise TypeError("Value must be an instance of ServerDevicePool")
        else:
            self._server = value

    def __init__(self, server=None):
        super(ClientDevicePool, self). __init__()
        self._server = server or ServerDevicePool()

    def connect(self):
        """connect() -> int -> ServerDevicePool Connection Id
            Connect to the ServerDevicePool. Returns the connection id which can be used in subsequent calls to
            Connect to the server's Device Pool. Returns a unique connection id which can be used in remove_connection().
            Connect to the Server Device Pool. Returns a connection id which can be used in subsequent calls to other methods."""
            Connect to the Server Device Pool. Returns a unique connection id which can be used in remove_connection().
            Connect to the server device pool. Returns a connection id which can be used in subsequent calls to
            Connect to the Server Device Pool. Returns a unique connection id which can be used in remove_connection().
            Connect to the ServerDevicePool. Returns a unique connection id which can be
            passed to other methods that require a connection     id."""
        raise NotImplementedError()

    def disconnect(self, conn):
        """disconnect(conn) -> None 
            Disconnect from the ServerDevicePool using   disconnect(ConnectionId)"""
        raise NotImplementedError()
        def get_devices(self, conn):
            """get_devices(conn) -> list<Device>
                Get a list of all Devices in the ServerDevicePool associated with the given
                ConnectionId"""
            return self.server.get_devices()

        def add_device(self, device, conn):
            """add_device(device, conn) -> bool
                Adds a Device to the ServerDevicePool associated with the given ConnectionId.
                If successful returns True otherwise False"""
            return self.server.add_device(device)

        def remove_device(self, device, conn):
            """remove_device(device, conn) -> bool
                Removes a Device from the ServerDevicePool associated with the given ConnectionId.
                If successful returns True otherwise False"""
                return self.server.remove_device(device)
                
                    