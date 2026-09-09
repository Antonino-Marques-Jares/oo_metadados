
import pandas as pd
from prettyprinter import pprint


class Tabela():
  def __init__(self) -> None:
    self.tb_nome: str = None
    self.tb_base_de_dados: str = None
    self.tb_camada: str = None
    self.tb_descricao: str = None
    self.tb_colunas: list =[]

  def __repr__(self) -> str:  # Corrigido: dois underscores no final
    return(
        f"{self.__class__.__name__}("
        f"tb_nome: {self.tb_nome!r}, "
        f"tb_base_de_dados: {self.tb_base_de_dados!r}, "
        f"tb_camada: {self.tb_camada!r}, "
        f"tb_descricao: {self.tb_descricao!r}, "
        f"tb_colunas:{self.tb_colunas!r})"
    )

  def load_from_artefato(self, info: dict):
    self.tb_nome = info.get('tb_nome')
    self.tb_base_de_dados = info.get('tb_base_de_dados')
    self.tb_descricao = info.get("tb_descricao")
    self.tb_colunas = info.get("tb_esquema")

  def converte_colunas_em_objetos(self):
    lista_colunas_objetos = []
    for coluna in self.tb_colunas:
      meta_col = Coluna()
      meta_col.load_from_item_em_tabela(coluna)
      lista_colunas_objetos.append(meta_col)
    self.colunas = lista_colunas_objetos

  def calcula_camada(self):
    if self.tb_base_de_dados[:2] == 'bz':
      self.tb_camada = 'bronze'
    elif self.tb_base_de_dados[:2] == 'sl':
      self.tb_camada = 'prata'
    elif self.tb_base_de_dados[:2] == 'gd':
          self.tb_camada = 'ouro'
    else:
      self.tb_camada = None

  def converte_para_dataframe(self) -> pd.DataFrame:
    linhas = []
    serie = {}
    serie["tb_camada"] = self.tb_camada
    serie["tb_base_de_dados"] = self.tb_base_de_dados
    serie["tb_nome"] = self.tb_nome
    serie["tb_descricao"] = self.tb_descricao
    for coluna in self.colunas:
      serie_coluna = serie.copy()
      serie_coluna["cl_nome"] = coluna.cl_nome
      serie_coluna["cl_tipo_de_dado"] = coluna.cl_tipo_de_dado
      serie_coluna["cl_descricao"] = coluna.cl_descricao
      serie_coluna["cl_privacidade"] = coluna.cl_privacidade
      serie_coluna["cl_confidencialidade"] = coluna.cl_confidencialidade
      linhas.append(serie_coluna)
    return pd.DataFrame(linhas)

  
  

  


class Coluna():
  def __init__(self) -> None:
    self.cl_nome: str = None
    self.cl_tipo_de_dado: str = None
    self.cl_descricao: str = None
    self.cl_privacidade: bool = None
    self.cl_confidencialidade: str = None

  def __repr__(self) -> str:  
    return(
        f"{self.__class__.__name__}("
        f"cl_nome: {self.cl_nome!r}, "  
        f"cl_tipo_de_dado: {self.cl_tipo_de_dado!r}, "
        f"cl_descricao: {self.cl_descricao!r}, "
        f"cl_privacidade: {self.cl_privacidade!r}, "
        f"cl_confidencialidade:{self.cl_confidencialidade!r})"
    )

  def load_from_item_em_tabela(self, item: dict):
    self.cl_nome = item.get("cl_nome")  
    self.cl_tipo_de_dado = item.get("cl_tipo_de_dado")
    self.cl_descricao = item.get("cl_descricao")
    self.cl_privacidade = item.get("cl_privacidade")
    self.cl_confidencialidade = item.get("cl_confidencialidade")

