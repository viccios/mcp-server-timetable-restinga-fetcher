# MCP Server Timetable Restinga Fetcher
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

## Sumário
- [Sobre](#sobre)
- [Como funciona](#como-funciona)
- [Instalação](#instalacao)
- [Documentação](#documentacao)
  - [Ferramentas](#ferramentas)
  - [Usando em um cliente](#usando-em-um-cliente)

<a name="sobre"></a>
## 🧠 Sobre
Este projeto é uma implementação de um servidor MCP escrito em Python com a biblioteca FastMCP.

<a name="como-funciona"></a>
## 💭 Como funciona
Este servidor expõe 8 ferramentas (*tools*) para clientes MCP, permitindo a integração dos dados fornecidos pelo Timetable Restinga Fetcher a uma LLM.

<a name="instalacao"></a>
## 💪 Instalação
Esse projeto é gerenciado com `uv`, um gerenciador de pacotes e projetos para Python. Leia a [página de instalação do uv](https://docs.astral.sh/uv/getting-started/installation/) para informações sobre como instalá-lo e certifique-se de que o Python está disponível também. Após isso, clone o repositório, instale as dependências com o comando `uv sync`, ative o ambiente virtual (*venv*) e então inicie o servidor com o comando `fastmcp run main.py:mcp` ou `fastmcp dev main.py:mcp` para o modo de desenvolvimento (irá instalar o [Inspector](https://modelcontextprotocol.io/docs/tools/inspector#installation-and-basic-usage)).

<a name="documentacao"></a>
## 📜 Documentação
### Ferramentas
Atualmente, 8 ferramentas são expostas pelo servidor MCP.

| Ferramenta | Descrição |
| ---------- | --------- |
| `get_teachers` | Retorna o nome de todos os professores |
| `get_subjects` | Retorna o nome de todas as disciplinas |
| `get_classrooms` | Retorna o número de todas as salas de aula |
| `get_classes` | Retorna o nome de todos os cursos |
| `get_periods` | Retorna o horário de cada período |
| `get_dayparts` | Retorna todas as partes do dia |
| `get_dates` | Retorna todas as datas |
| `get_event_types` | Retorna todos os tipos de evento |

### Usando em um cliente
Para usar o servidor MCP, é necessário configurá-lo em um cliente MCP que suporte *tools*. Abaixo está um exemplo de arquivo `JSON` de conexão para o Cursor:

```json
{
  "mcpServers": {
    "mcp-server-timetable-restinga-fetcher": {
      "command": "<seu-usuario>/.venv/bin/python",
      "args": ["<seu-usuario>/mcp-server-timetable-restinga-fetcher/main.py"]
    }
  }
}
```
