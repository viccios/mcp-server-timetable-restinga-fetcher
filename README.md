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

Este servidor expõe 8 ferramentas (_tools_) para clientes MCP, permitindo a integração dos dados fornecidos pelo Timetable Restinga Fetcher a uma LLM.

<a name="instalacao"></a>

## 💪 Instalação

Esse projeto é gerenciado com `uv`, um gerenciador de pacotes e projetos para Python. Leia a [página de instalação do uv](https://docs.astral.sh/uv/getting-started/installation/) para informações sobre como instalá-lo e certifique-se de que o Python está disponível também. Após isso, clone o repositório, instale as dependências com o comando `uv sync`, ative o ambiente virtual (_venv_), crie um arquivo `.env` ou copie o existente `cp .env.example .env` e então inicie o servidor com o comando `fastmcp run main.py:mcp` ou `fastmcp dev main.py:mcp` para o modo de desenvolvimento (irá instalar o [Inspector](https://modelcontextprotocol.io/docs/tools/inspector#installation-and-basic-usage)).

<a name="documentacao"></a>

## 📜 Documentação

### Ferramentas

Atualmente, 8 ferramentas são expostas pelo servidor MCP.

| Ferramenta                | Descrição                                                                                     |
| ------------------------- | --------------------------------------------------------------------------------------------- |
| `get_periods`             | Retorna os períodos das aulas                                                                 |
| `get_subjects`            | Retorna as disciplinas                                                                        |
| `get_teachers`            | Retorna os professores                                                                        |
| `get_classes`             | Retorna as turmas                                                                             |
| `get_classrooms`          | Retorna as salas de aula                                                                      |
| `get_class_schedule`      | Retorna as turmas com informações detalhadas sobre os horários                                |
| `get_teachers_schedule`   | Retorna os professores com informações detalhadas sobre suas turmas, salas de aula e horários |
| `get_classrooms_schedule` | Retorna as salas de aula com informações detalhadas sobre as turmas, professores e horários   |

É necessário configurar a URL da API do Timetable Restinga Fetcher através do arquivo `.env`.
Um exemplo de configuração está disponível no arquivo `.env.example`.

### Usando em um cliente

Para usar o servidor MCP, é necessário configurá-lo em um cliente MCP que suporte _tools_. Abaixo está um exemplo de arquivo `JSON` de conexão para o Cursor (sistemas Unix-like). Use caminhos absolutos.

```json
{
  "mcpServers": {
    "mcp-server-timetable-restinga-fetcher": {
      "command": "/home/<seu-usuario>/<pasta-projeto>/.venv/bin/python",
      "args": [
        "/home/<seu-usuario>/<pasta-projeto>/mcp-server-timetable-restinga-fetcher/main.py"
      ]
    }
  }
}
```
