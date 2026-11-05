"""Gera os arquivos LaTeX e PDFs dos vinte cards da Sprint 4."""

from pathlib import Path
from subprocess import run


RAIZ = Path(__file__).parent
AUTOR = "Matheus Moreli Durão Silva\\\\ Matrícula 12621CBS217\\\\ Cibersegurança - Bacharelado - Noturno"

CARDS = [
    ("S4_01", "Arquitetura de Software e Separação de Camadas", "camadas", "diagrama_camadas.md", "A aplicação separa interface, regras de negócio, modelos, persistência e cálculo de risco. A interface só conversa com o usuário; inventario.py aplica as regras; modelos.py descreve os objetos; persistencia.py lê e grava JSON; risco.py calcula as matrizes.", "O diagrama mostra a direção das dependências. A regra importante é que a camada de domínio não depende do terminal. Assim, as mesmas regras podem ser testadas sem input ou print."),
    ("S4_02", "Princípios SOLID", "solid", "solid.md", "O projeto aplica responsabilidades pequenas: InterfaceTerminal cuida da navegação, Inventario coordena as regras e AnalisadorRisco cuida da matemática. Os tipos de ativo herdam de Equipamento sem exigir condicionais espalhadas.", "O exemplo é didático: não cria abstrações desnecessárias. O ganho está em cada arquivo ter uma responsabilidade clara e testável."),
    ("S4_03", "Padrões de Projeto", "padrões", "padroes.md", "O padrão escolhido é uma fachada simples: Inventario concentra as operações usadas pela interface. A fábrica criar_ativo escolhe a classe de ativo a partir do tipo cadastrado.", "São padrões usados onde ajudam o código existente. Não foram adicionadas camadas artificiais apenas para citar nomes de padrões."),
    ("S4_04", "Persistência JSON e Modelagem Orientada a Objetos", "JSON e POO", "modelo_json.md", "Cada ativo é um objeto com dados, vulnerabilidades, dependências e histórico. persistencia.py transforma os objetos em uma lista JSON ao salvar e recria os objetos ao carregar.", "O JSON continua simples, legível e suficiente para o porte do trabalho. As validações acontecem antes da gravação, para não salvar registros incoerentes."),
    ("S4_05", "Arquitetura Cliente-Servidor e Multicamadas", "cliente-servidor", "cliente_servidor.md", "O terminal é o cliente da aplicação local. O serviço HTTP somente leitura já existente reutiliza Inventario e risco.py, sem duplicar regras. Isso demonstra a separação entre apresentação, serviço e domínio.", "O servidor não foi iniciado nesta etapa. O entregável descreve a divisão e aponta os arquivos que permitem a execução posterior sem mudar o CRUD."),
    ("S4_06", "Consultas SQL com JOIN", "SQL JOIN", "consultas_join.sql", "O arquivo SQL usa tabelas Ativo e Vulnerabilidade ligadas por ativo_id. INNER JOIN mostra somente ativos com vulnerabilidades; LEFT JOIN também mantém ativos sem vulnerabilidade.", "Embora o projeto final use JSON por ser introdutório, as consultas deixam claro como a mesma relação seria buscada em um banco relacional."),
    ("S4_07", "Relatórios SQL com GROUP BY", "SQL GROUP BY", "relatorios_group_by.sql", "Os relatórios agrupam vulnerabilidades por ativo e por prioridade. COUNT, AVG e HAVING tornam visível a quantidade de falhas e a média de CVSS sem consultar registro por registro.", "O objetivo é estudar relatórios relacionais. Não há banco SQL instalado no projeto, pois isso não é necessário para o requisito atual de persistência JSON."),
    ("S4_08", "Tabelas Hash e Otimização de Consultas", "hash", "tabela_hash.py", "O dicionário Python usa uma tabela hash. No inventário, os ativos são guardados por ID, então consultar_por_id acessa diretamente a chave em vez de percorrer todos os itens.", "O exemplo compara a ideia de busca por chave com busca linear. No código principal, o dicionário é a solução mais simples e já atende ao problema."),
    ("S4_09", "Árvore Binária de Busca", "árvore binária", "arvore_busca.py", "A árvore coloca valores menores à esquerda e maiores à direita. A travessia em ordem produz uma lista ordenada, relacionando estrutura de dados e busca.", "É um exemplo independente para o estudo do card. O inventário mantém dicionários e sorted, porque são mais adequados e legíveis para a quantidade pequena de ativos."),
    ("S4_10", "Grafos, BFS e DFS", "grafos", "grafo_busca.py", "As dependências de ativos formam um grafo dirigido. BFS explora vizinhos por nível; DFS segue um caminho antes de retroceder. O exemplo usa os IDs dos ativos como vértices.", "O cálculo de risco usa a matriz de dependências. BFS e DFS servem para entender e inspecionar caminhos, sem substituir o cálculo linear já exigido."),
    ("S4_11", "Merge Sort", "Merge Sort", "merge_sort.py", "Merge Sort divide a lista ao meio, ordena as partes e faz a intercalação. A saída preserva todos os elementos e deixa explícita a etapa de combinação.", "O algoritmo foi implementado para estudo. Na aplicação, sorted é a opção correta e simples, pois a linguagem já fornece uma ordenação confiável."),
    ("S4_12", "Quick Sort", "Quick Sort", "quick_sort.py", "Quick Sort escolhe um pivô, separa menores, iguais e maiores e ordena as partes. O exemplo evita alterar a lista original para facilitar a conferência.", "O card compara estratégias de ordenação. Não há motivo para substituir sorted por uma implementação própria no programa final."),
    ("S4_13", "Complexidade de Algoritmos", "complexidade", "complexidade.md", "A busca por ID em dicionário é tratada como O(1) em média. Filtrar ativos percorre a coleção, O(n). A eliminação de Gauss para uma matriz n por n é O(n³).", "A análise explica por que o projeto usa dicionário para identificação e mantém o cálculo de risco claro, adequado ao tamanho acadêmico da base."),
    ("S4_14", "Testes Automatizados com Pytest", "Pytest", "testes_pytest.py", "A suíte principal possui testes de regras, persistência, interface e álgebra linear. O arquivo do card inclui testes Pytest pequenos para as funções puras e o comando python -m pytest executa também testes unittest existentes.", "A simulação é testada para provar duas propriedades: ela propaga o risco conforme o peso e não adiciona vulnerabilidade ao JSON nem ao objeto."),
    ("S4_15", "Conceitos de Docker", "Docker", "docker_conceitos.md", "O documento diferencia imagem, container, volume e porta. A imagem é a receita; o container é a execução isolada; o volume preserva dados fora da camada descartável.", "Não houve execução de Docker por orientação expressa do aluno. O conteúdo é preparação teórica, sem alegar imagem criada ou servidor entregue."),
    ("S4_16", "Dockerfile, Imagem e Python", "Dockerfile", "Dockerfile.exemplo", "O Dockerfile de referência parte de Python, copia o código, define o diretório de trabalho e inicia app.py. Ele não instala banco nem dependência desnecessária.", "O arquivo é uma evidência de configuração. A construção da imagem não foi executada nesta etapa."),
    ("S4_17", "Docker Compose", "Docker Compose", "compose.yml", "O compose de referência define um único serviço para o inventário e um volume para dados. Ele é suficiente para demonstrar composição sem inventar serviços que o projeto não usa.", "O compose não foi iniciado. Isso respeita a decisão de não subir Docker ou servidor agora."),
    ("S4_18", "Monitoramento e Logs", "monitoramento", "monitoramento.md", "O plano define sinais objetivos: processo ativo, leitura válida do JSON, testes verdes e falha de salvamento informada. Logs devem registrar evento e resultado, sem guardar dados sensíveis.", "Nenhum monitor foi ligado nesta etapa. O documento separa claramente evidência possível agora de monitoramento que depende do container ou servidor."),
    ("S4_19", "Linux e Preparação de Deploy", "Linux", "deploy_linux.md", "O roteiro explica usuário sem privilégios, cópia do projeto, permissão mínima para dados e verificação de versão do Python. Também lista comandos de checagem antes de publicar.", "Nenhum servidor Linux foi acessado. O conteúdo é plano de execução e checklist, não uma declaração de deploy concluído."),
    ("S4_20", "Integração Final em Container", "integração", "integracao.md", "A integração prevista é simples: imagem do mesmo código, volume para dados, execução de app.py e validação do CRUD, riscos e simulação. A documentação inclui os critérios para aceitar a execução futura.", "Este card depende de Docker e de servidor. Por orientação atual, o procedimento está pronto, mas a execução não foi feita e não foi marcada como comprovada."),
]


def escapar(texto):
    caracteres = {"&": r"\&", "%": r"\%", "_": r"\_", "#": r"\#"}
    return "".join(caracteres.get(letra, letra) for letra in texto)


def texto_latex(codigo, titulo, estudo, arquivo, aplicacao, explicacao):
    return f'''\\documentclass[12pt]{{article}}
\\usepackage[utf8]{{inputenc}}
\\usepackage[T1]{{fontenc}}
\\usepackage[brazil]{{babel}}
\\usepackage[a4paper,margin=2.5cm]{{geometry}}
\\usepackage{{enumitem}}
\\setlist[itemize]{{noitemsep,topsep=4pt}}
\\title{{Sprint 4 - {escapar(codigo)}\\\\{escapar(titulo)}}}
\\author{{{AUTOR}}}
\\date{{2026}}
\\begin{{document}}
\\maketitle

\\section*{{Entregável e checklist}}
Este documento registra o card {escapar(codigo)}, o conteúdo estudado, a aplicação no Inventário de Ativos e a forma de conferência. O arquivo complementar é \\texttt{{{escapar(arquivo)}}}. A entrega mantém o escopo introdutório: código claro, funções pequenas e nenhuma dependência que não seja necessária.

\\begin{{itemize}}
\\item Conceito: {escapar(estudo)}.
\\item Evidência: documento e, quando aplicável, exemplo executável na mesma pasta.
\\item Ligação com o trabalho: referência direta aos arquivos do repositório principal.
\\item Conferência: leitura do exemplo, execução dos testes e comparação com a explicação abaixo.
\\end{{itemize}}

\\section*{{O que foi estudado e aplicado}}
{escapar(aplicacao)}

\\section*{{Lógica da decisão}}
{escapar(explicacao)}

\\section*{{Como conferir}}
Abra o arquivo complementar desta pasta. Para verificar o projeto principal, execute \\texttt{{python -m unittest -v}} e \\texttt{{python -m flake8 .}} na raiz. Os testes não modificam a base real. Quando o card trata Docker, Linux ou servidor, a documentação deve ser lida como preparação: a execução ficou deliberadamente pendente nesta etapa.

\\section*{{Conclusão}}
O card foi documentado de forma verificável e conectado ao Inventário de Ativos, sem trocar uma solução simples por uma estrutura desnecessária.
\\end{{document}}
'''


EXEMPLOS = {
    "diagrama_camadas.md": "# Diagrama de camadas\n\n```text\nUsuário\n  |\ninterface.py (menus, teclas e mensagens)\n  |\ninventario.py (regras e operações)\n  |-----------------------------|\nmodelos.py (Ativo e Vulnerabilidade)  risco.py (matrizes e Gauss)\n  |\npersistencia.py (JSON)\n  |\ndados/inventario.json\n```\n\nA interface não valida regra de negócio por conta própria. A persistência não imprime menus. Essa separação permite testar cada parte isoladamente.\n",
    "solid.md": "# SOLID aplicado sem exagero\n\n- **Responsabilidade única:** cada arquivo tem uma função principal.\n- **Aberto/fechado:** novos tipos de ativo podem herdar de Equipamento sem reescrever o CRUD.\n- **Substituição:** Notebook e Servidor podem ser tratados como Equipamento.\n- **Interface pequena:** o terminal pede apenas operações necessárias ao Inventario.\n- **Dependência:** regras não dependem de input/print, portanto podem ser testadas.\n\nO objetivo é organização, não criar classes vazias.\n",
    "padroes.md": "# Padrões identificados\n\n`criar_ativo` atua como uma fábrica simples: recebe o tipo e devolve a classe correta. `Inventario` é uma fachada para o CRUD: a interface pede cadastrar, buscar ou atualizar sem conhecer todos os detalhes internos.\n\nEsses padrões aparecem no código porque reduzem condicionais e duplicação; não foram adicionados frameworks ou estruturas extras.\n",
    "modelo_json.md": "# Modelo JSON\n\n```json\n{\n  \"id\": 2,\n  \"nome\": \"SRV-WEB-01\",\n  \"tipo\": 2,\n  \"vulnerabilidades\": [{\"cve\": \"CVE-2026-0001\", \"cvss\": 8.0}],\n  \"dependencias\": [{\"ativo_id\": 1, \"peso\": 0.25}]\n}\n```\n\nO repositório grava uma lista desses objetos. Ao carregar, valida ID, dados obrigatórios, CVSS e dependências antes de aceitar a base.\n",
    "cliente_servidor.md": "# Cliente, serviço e domínio\n\n```text\nTerminal -> InterfaceTerminal -> Inventario -> Modelos/JSON\n                                  |\n                                  -> risco.py\nServiço HTTP somente leitura ------^\n```\n\nO terminal e o serviço podem consultar a mesma regra. A regra não precisa saber se o pedido veio de uma tela ou de uma rota HTTP.\n",
    "complexidade.md": "# Complexidade usada no trabalho\n\n| Operação | Ordem | Motivo |\n|---|---:|---|\n| Buscar ID no dicionário | O(1) médio | acesso por chave hash |\n| Listar ou filtrar ativos | O(n) | examina os registros |\n| Ordenar lista | O(n log n) | algoritmo interno de `sorted` |\n| Eliminação de Gauss | O(n³) | pivôs, linhas e colunas |\n\nA base acadêmica é pequena. A prioridade é manter o código verificável e escolher o dicionário onde ele melhora a busca.\n",
    "docker_conceitos.md": "# Conceitos Docker\n\n- **Imagem:** receita imutável com Python e o código.\n- **Container:** processo criado a partir da imagem.\n- **Volume:** local persistente para `dados/inventario.json`.\n- **Porta:** ligação para um serviço de rede, se ele for necessário.\n\nNenhum destes itens foi executado neste card.\n",
    "monitoramento.md": "# Plano de monitoramento\n\n1. Confirmar que o processo está ativo.\n2. Confirmar que o JSON pode ser lido.\n3. Executar testes antes da publicação.\n4. Registrar falhas de salvamento sem expor conteúdo sensível.\n\nO plano não afirma que existe monitor em produção.\n",
    "deploy_linux.md": "# Roteiro Linux\n\n1. Usar usuário sem privilégios administrativos.\n2. Copiar o projeto e manter `dados/` com permissão mínima.\n3. Conferir `python --version`.\n4. Rodar testes e estilo antes de iniciar o processo.\n5. Verificar logs e permitir rollback para a versão anterior.\n\nNenhum servidor foi acessado.\n",
    "integracao.md": "# Critério de integração futura\n\nA execução futura só será aceita se a imagem iniciar o mesmo `app.py`, os dados permanecerem em volume e a demonstração cobrir CRUD, consulta de vulnerabilidades, riscos e simulação. Também será preciso guardar evidência da execução, do teste e do tempo solicitado pela disciplina.\n",
    "consultas_join.sql": "SELECT a.id, a.nome, v.cve, v.cvss\nFROM ativo a\nINNER JOIN vulnerabilidade v ON v.ativo_id = a.id;\n\nSELECT a.id, a.nome, v.cve\nFROM ativo a\nLEFT JOIN vulnerabilidade v ON v.ativo_id = a.id;\n",
    "relatorios_group_by.sql": "SELECT a.nome, COUNT(v.cve) AS total, AVG(v.cvss) AS media_cvss\nFROM ativo a LEFT JOIN vulnerabilidade v ON v.ativo_id = a.id\nGROUP BY a.id, a.nome;\n\nSELECT prioridade, COUNT(*) AS total\nFROM vulnerabilidade\nGROUP BY prioridade\nHAVING COUNT(*) > 0;\n",
    "tabela_hash.py": "ativos = {10: 'SRV-WEB-01', 20: 'DB-ESTOQUE-01'}\nprint(ativos.get(20, 'Ativo não encontrado'))\n",
    "arvore_busca.py": "def inserir(no, valor):\n    if no is None:\n        return [valor, None, None]\n    lado = 1 if valor < no[0] else 2\n    no[lado] = inserir(no[lado], valor)\n    return no\n\ndef em_ordem(no):\n    return [] if no is None else em_ordem(no[1]) + [no[0]] + em_ordem(no[2])\n\nraiz = None\nfor item in [5, 2, 8, 1, 3]:\n    raiz = inserir(raiz, item)\nprint(em_ordem(raiz))\n",
    "grafo_busca.py": "from collections import deque\n\ngrafo = {1: [2, 3], 2: [4], 3: [], 4: []}\n\ndef bfs(inicio):\n    fila, vistos = deque([inicio]), {inicio}\n    ordem = []\n    while fila:\n        atual = fila.popleft()\n        ordem.append(atual)\n        for vizinho in grafo[atual]:\n            if vizinho not in vistos:\n                vistos.add(vizinho)\n                fila.append(vizinho)\n    return ordem\n\ndef dfs(atual, vistos=None):\n    vistos = set() if vistos is None else vistos\n    vistos.add(atual)\n    for vizinho in grafo[atual]:\n        if vizinho not in vistos:\n            dfs(vizinho, vistos)\n    return vistos\n\nprint(bfs(1))\nprint(sorted(dfs(1)))\n",
    "merge_sort.py": "def merge_sort(valores):\n    if len(valores) <= 1:\n        return valores\n    meio = len(valores) // 2\n    esquerda = merge_sort(valores[:meio])\n    direita = merge_sort(valores[meio:])\n    resultado = []\n    while esquerda and direita:\n        resultado.append((esquerda if esquerda[0] <= direita[0] else direita).pop(0))\n    return resultado + esquerda + direita\n\nprint(merge_sort([8, 3, 5, 1]))\n",
    "quick_sort.py": "def quick_sort(valores):\n    if len(valores) <= 1:\n        return valores\n    pivo = valores[len(valores) // 2]\n    menores = [v for v in valores if v < pivo]\n    iguais = [v for v in valores if v == pivo]\n    maiores = [v for v in valores if v > pivo]\n    return quick_sort(menores) + iguais + quick_sort(maiores)\n\nprint(quick_sort([8, 3, 5, 1, 3]))\n",
    "testes_pytest.py": "def classificar_cvss(nota):\n    if nota >= 9:\n        return 'Crítica'\n    if nota >= 7:\n        return 'Alta'\n    return 'Demais níveis'\n\ndef test_cvss_critico():\n    assert classificar_cvss(9.8) == 'Crítica'\n\ndef test_cvss_alto():\n    assert classificar_cvss(7.0) == 'Alta'\n\n# A prova integrada da simulação está em test_risco.py no projeto principal.\n",
    "Dockerfile.exemplo": "FROM python:3.13-slim\nWORKDIR /app\nCOPY . .\nCMD [\"python\", \"app.py\"]\n",
    "compose.yml": "services:\n  inventario:\n    build: .\n    stdin_open: true\n    tty: true\n    volumes:\n      - ./dados:/app/dados\n",
}


def gerar():
    for codigo, titulo, estudo, arquivo, aplicacao, explicacao in CARDS:
        pasta = RAIZ / codigo
        pasta.mkdir(exist_ok=True)
        (pasta / "entregavel.tex").write_text(
            texto_latex(codigo, titulo, estudo, arquivo, aplicacao, explicacao),
            encoding="utf-8",
        )
        conteudo = EXEMPLOS.get(
            arquivo,
            f"# {codigo} - {titulo}\n\n{aplicacao}\n\n{explicacao}\n",
        )
        (pasta / arquivo).write_text(conteudo, encoding="utf-8")
        resultado = run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "entregavel.tex"],
            cwd=pasta,
            capture_output=True,
            text=True,
        )
        if resultado.returncode:
            raise RuntimeError(f"Falha ao compilar {codigo}:\n{resultado.stdout[-1000:]}")
        for extensao in (".aux", ".log", ".out"):
            (pasta / f"entregavel{extensao}").unlink(missing_ok=True)


if __name__ == "__main__":
    gerar()
