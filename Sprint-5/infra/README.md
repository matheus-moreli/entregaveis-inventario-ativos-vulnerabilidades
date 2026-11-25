# Infraestrutura de referência

A configuração TLS usa um projeto Compose de laboratório, separado da implantação oficial. Defina INVENTARIO_PROJETO com o caminho absoluto da raiz do código, S5_SENHA_ARQUIVO com o caminho absoluto de um arquivo legível pelo contêiner contendo uma senha de teste, e S5_TLS_DIR com o caminho absoluto para o diretório contendo fullchain.pem e privkey.pem. O certificado precisa ser válido para localhost e confiado no ambiente que executa a verificação.

Na raiz da pasta da S5, use **docker compose -f infra/compose.tls.yaml config --quiet**. Com o daemon disponível, execute **docker compose -f infra/compose.tls.yaml up --build -d**. Confira o redirecionamento pela porta 8080 e a saúde em https://localhost:8443/saude. O serviço interno usa o volume do laboratório.

O workflow verificar-s5.yml é um modelo para o repositório do projeto. Sua publicação só é acionada por uma tag de versão depois das verificações.
