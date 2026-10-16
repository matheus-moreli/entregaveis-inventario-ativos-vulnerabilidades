# S3_20 — Redes, segurança, LGPD, estatística e sustentabilidade

**Sistema analisado:** Inventário de Ativos e Vulnerabilidades, versão do repositório principal em 13/10/2026. Os seis registros são exemplos didáticos; não há medição de um parque real. Fontes legais: [LGPD, Lei 13.709/2018](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm) e [guia de segurança da ANPD](https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia_seguranca_da_informacao_para_atpps___defeso_eleitoral.pdf).

## Comunicação da aplicação

O menu original usa arquivo JSON local e não precisa de rede. No Trabalho 2, o container oferece consultas HTTP somente leitura `/saude` e `/riscos` na porta TCP 8080. O cliente endereça o host por IPv4, por exemplo `127.0.0.1` para a própria máquina. Em uma rede `192.168.1.0/24`, a máscara `255.255.255.0` separa os 24 bits da rede e os oito bits de host; o endereço concreto do servidor deve ser obtido no ambiente da disciplina, não presumido.

Em TCP/IP, IP roteia pacotes entre hosts; TCP entrega um fluxo ordenado e confirma recebimento. Antes do HTTP, o three-way handshake usa SYN do cliente, SYN+ACK do servidor e ACK do cliente. A requisição HTTP só segue após essa conexão. UDP não estabelece esse fluxo nem garante entrega/ordem por si; é útil quando a aplicação tolera perdas ou implementa suas próprias garantias. Como as consultas do inventário precisam de resposta íntegra e ordenada, HTTP sobre TCP é apropriado. Se o serviço for exposto fora do host, usar HTTPS por proxy e controle de acesso; o protótipo atual não implementa TLS.

## Segurança e controle de acesso proposto

O estado atual não possui login nem autorização. Portanto **não deve ser publicado na internet com dados reais**. A porta no host deve ficar ligada a `127.0.0.1` ou restrita por firewall/rede privada durante o ensaio. A interface HTTP é somente leitura; o menu permite escrita a quem tem acesso ao terminal e arquivo. Proposta de menor privilégio para evolução: operador pode cadastrar/atualizar ativos e vulnerabilidades; analista pode consultar ativos e riscos; auditor pode consultar histórico e evidências; administrador gerencia papéis e backups. Cada ação deve ser negada por padrão sem permissão explícita. Autenticação confirma quem é a pessoa; autorização decide o que ela pode fazer. Defesa em profundidade inclui isolamento de rede, autenticação, autorização por ação, conta de container sem root, proteção do volume, backup e logs com acesso limitado. Essas camadas são proposta, não funcionalidades já implementadas.

## Dados pessoais e LGPD

O campo `responsavel` pode identificar uma pessoa natural quando guarda nome individual; nesse caso é dado pessoal (art. 5º). Nome de host, CVE e CVSS são, em regra, dados técnicos, mas sua combinação com responsável pode revelar informações sobre uma pessoa ou função. A base demonstrativa usa nomes de equipes e dados fictícios. O sistema não pede dado sensível das categorias do art. 5º, II.

Para uso real, definir finalidade, necessidade, transparência, exatidão e segurança conforme princípios do art. 6º; identificar uma hipótese legal aplicável do art. 7º antes da coleta; restringir campos e prazo de guarda; permitir correção do responsável; limitar acesso e registrar alterações; adotar medidas técnicas e administrativas contra acesso não autorizado, conforme art. 46. A escolha concreta de base legal e retenção depende do contexto institucional. O protótipo não contém autenticação, gestão de titulares nem política de retenção; logo este relatório **não afirma conformidade plena com a LGPD**.

## Estatística descritiva dos ativos demonstrativos

Os riscos efetivos calculados pelo Trabalho 2, na ordem dos IDs 1–6, são `[9.8, 10.0, 9.8, 12.8, 0.0, 7.8]`. Há seis ativos. Média = `8.3667`, mediana = `9.8`, moda = `9.8`, desvio padrão populacional ≈ `4.0157`. A média é puxada para baixo pelo ativo sem vulnerabilidade registrada; isso **não prova ausência de risco** nesse ativo. O risco 12.8 pode exceder a escala CVSS 0–10 porque é resultado de agregação e propagação, não uma nota CVSS individual. A amostra é pequena e fictícia; não permite inferência estatística sobre um parque real. O script `analise_dados.py` reproduz as medidas.

## Sustentabilidade tecnológica

Inventariar tipo, responsável e dependências ajuda a identificar equipamentos subutilizados, planejar manutenção e evitar substituição prematura. Também permite priorizar atualizações que prolonguem vida útil sem deixar falhas abertas. A aplicação local e simples tem baixo custo de infraestrutura comparado a uma plataforma contínua maior, mas o container ligado 24 horas consome energia; a exigência acadêmica de 24 horas não deve virar padrão operacional sem necessidade. Não há medições de energia, emissões ou descarte neste projeto, portanto nenhum benefício ambiental quantitativo é reivindicado. Para medir impacto, registrar horas de uso, consumo elétrico, vida útil e destino de descarte, com critérios consistentes antes/depois.

## Limites e verificação

O serviço Docker e o CRUD são projetos separados dentro da atividade: a API Flask S3_19 é uma demonstração de persistência SQLite, não a interface de produção do inventário principal. O HTML S3_17 consome essa API local. O build Docker e a execução de 24 horas no servidor da disciplina continuam pendentes de acesso e coleta de prova; os testes Python do CI não substituem esse requisito.
