class ContadorReintentos:
    """Ver TAREAS.md, tarea t11."""
    def registrar_fallo(self, tipo: str) -> None:
        raise NotImplementedError
    def puede_reintentar(self) -> bool:
        raise NotImplementedError
    def reiniciar(self) -> None:
        raise NotImplementedError
