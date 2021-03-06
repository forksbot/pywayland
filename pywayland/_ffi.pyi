from typing import overload, Any, Callable, TypeVar, Union


class Cdata: ...
class CdataArray:
    def __setitem__(self, idx: int, elem: Cdata) -> None: ...
# built-in cdata types
class NullCdata(Cdata): ...
class CharCdata(Cdata): ...
# custom cdata types
class ClientCdata(Cdata): ...
class DisplayCdata(Cdata): ...
class EventLoopCdata(Cdata): ...
class ListenerCdata(Cdata): ...
class QueueCdata(Cdata): ...
class ResourceCdata(Cdata): ...

_FuncType = Callable[..., Any]
_F = TypeVar("_F", bound=_FuncType)
_CdataT = TypeVar("_CdataT", bound=Cdata)


class ffi:
    NULL: NullCdata

    @overload
    @staticmethod
    def new(cdecl: str) -> Cdata: ...
    @overload
    @staticmethod
    def new(cdecl: str, init: Any) -> CdataArray: ...
    @staticmethod
    def gc(cdata: _CdataT, destructor: Callable[[_CdataT], None], size: int = 0) -> _CdataT: ...
    @staticmethod
    def string(cdata: CharCdata) -> str: ...
    @staticmethod
    def release(cdata: Cdata) -> None: ...
    @staticmethod
    def def_extern() -> Callable[[_F], _F]: ...
    @staticmethod
    def from_handle(cdata: Cdata) -> Any: ...


class lib:
    WAYLAND_VERSION_MAJOR: int
    WAYLAND_VERSION_MINOR: int
    WAYLAND_VERSION_MICRO: int

    @staticmethod
    def wl_display_create() -> DisplayCdata: ...
    @staticmethod
    def wl_display_destroy(display: DisplayCdata) -> None: ...
    @staticmethod
    def wl_display_destroy_clients(display: DisplayCdata) -> None: ...
    @staticmethod
    def wl_display_get_event_loop(display: DisplayCdata) -> EventLoopCdata: ...
    @staticmethod
    def wl_display_add_socket(display: DisplayCdata, name: bytes) -> int: ...
    @staticmethod
    def wl_display_add_socket_auto(display: DisplayCdata) -> CharCdata: ...
    @staticmethod
    def wl_display_terminate(display: DisplayCdata) -> None: ...
    @staticmethod
    def wl_display_run(display: DisplayCdata) -> None: ...

    @staticmethod
    def wl_display_get_serial(display: DisplayCdata) -> int: ...
    @staticmethod
    def wl_display_next_serial(display: DisplayCdata) -> int: ...

    @staticmethod
    def wl_display_init_shm(display: DisplayCdata) -> int: ...
    @staticmethod
    def wl_display_add_shm_format(display: DisplayCdata, format: int) -> int: ...

    @staticmethod
    def wl_event_queue_destroy(queue: QueueCdata) -> None: ...

    @staticmethod
    def wl_display_connect(name: Union[bytes, NullCdata]) -> DisplayCdata: ...
    @staticmethod
    def wl_display_connect_to_fd(fd: int) -> DisplayCdata: ...
    @staticmethod
    def wl_display_disconnect(display: DisplayCdata) -> None: ...
    @staticmethod
    def wl_display_get_fd(display: DisplayCdata) -> int: ...
    @staticmethod
    def wl_display_dispatch(display: DisplayCdata) -> int: ...
    @staticmethod
    def wl_display_dispatch_pending(display: DisplayCdata) -> int: ...
    @staticmethod
    def wl_display_dispatch_queue(display: DisplayCdata, queue: QueueCdata) -> int: ...
    @staticmethod
    def wl_display_dispatch_queue_pending(display: DisplayCdata, queue: QueueCdata) -> int: ...
    @staticmethod
    def wl_display_roundtrip(display: DisplayCdata) -> int: ...
    @staticmethod
    def wl_display_roundtrip_queue(display: DisplayCdata, queue: QueueCdata) -> int: ...
    @staticmethod
    def wl_display_get_error(display: DisplayCdata) -> int: ...
    @staticmethod
    def wl_display_read_events(display: DisplayCdata) -> int: ...
    @staticmethod
    def wl_display_prepare_read(display: DisplayCdata) -> int: ...
    @staticmethod
    def wl_display_prepare_read_queue(display: DisplayCdata, queue: QueueCdata) -> int: ...
    @staticmethod
    def wl_display_flush(display: DisplayCdata) -> int: ...
    @staticmethod
    def wl_display_create_queue(display: DisplayCdata) -> QueueCdata: ...

    @staticmethod
    def wl_client_create(display: DisplayCdata, fd: int) -> ClientCdata: ...
    @staticmethod
    def wl_client_destroy(client: ClientCdata) -> None: ...
    @staticmethod
    def wl_client_flush(client: ClientCdata) -> None: ...
    @staticmethod
    def wl_client_add_destroy_listener(client: ClientCdata, listener: ListenerCdata) -> None: ...
    @staticmethod
    def wl_client_get_object(client: ClientCdata, id: int) -> ResourceCdata: ...
    @staticmethod
    def wl_resource_get_user_data(resource: ResourceCdata) -> Cdata: ...

    WL_EVENT_READABLE: int
    WL_EVENT_WRITABLE: int
    WL_EVENT_HANGUP: int
    WL_EVENT_ERROR: int
