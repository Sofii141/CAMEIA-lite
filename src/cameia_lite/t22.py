class RegistroIdempotente:
    """Ver TAREAS.md, tarea t22."""
    def registrar(self, clave: str, cuerpo: dict) -> tuple[int, dict | None]:
        raise NotImplementedError
    def total(self) -> int:
        raise NotImplementedError
