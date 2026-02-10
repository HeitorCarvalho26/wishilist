from models.database import Database
from sqlite3 import Cursor
from typing import Self, Any, Optional

class Obra:
    """
        Classe para representar obra, com métodos para salvar, obter, excluir e atualizar tarefas em um banco de dados usando a classe `Database`
    """

    def __inti__(self: Self, titulo_obra: Optional [str], indicacao: Optional[str] = None, id_obra: Optional[int] = None) -> None:
        self.titulo_obra: Optional[str] = titulo_obra
        self.indicacao: Optional[str] = indicacao
        self.id_obra: Optional[int] = id_obra

    @classmethod
    def id(cls, id: int) -> Self:
        with Database() as db:
            query: str = ('SELECT titulo_obra, indicacao FROM obras WHERE id = ?;')
            params: tuple = (id,)
            resultado: list[Any] = db.buscar_tudo(query, params)

            [[titulo, indic]] = resultado
        
        return cls(id_obra=id, titulo_obra=titulo, indicacao=indic)
    
    def salvar_obra(self: Self) -> None:
        with Database() as db:
            query: str ="INSERT INTO tarefas (titulo_tarefa, indicacao) VALUES (?, ?);"
            params: tuple = (self.titulo_obra, self.indicacao)
            db.executar(query, params)