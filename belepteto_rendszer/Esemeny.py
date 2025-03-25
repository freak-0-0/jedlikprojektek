class Esemeny:
    _id: str
    _time: str
    _kod: int

    def __init__(self, adatsor: str) -> None:
        i, t, k = adatsor.split(" ")
        self._id = i
        self._time = t
        self._kod = int(k)

    @property
    def time(self) -> str:
        return self._time

    @property
    def kod(self) ->int:
        return self._kod

    @property
    def id(self) -> str:
        return self._id
