# S3_15 — avaliação heurística e acessibilidade

Objeto: [protótipo navegável no Figma](https://www.figma.com/proto/EI6VJsocmy9R93dPi4lACK/Invent%C3%A1rio-de-Ativos-%E2%80%94-Prot%C3%B3tipo-S3_15?node-id=3-2&p=f&scaling=min-zoom&content-scaling=fixed&page-id=0%3A1&starting-point-node-id=3%3A2), com painel inicial e tela de cadastro. Avaliação em 13/10/2026 baseada no fluxo demonstrado e nas [10 heurísticas de Nielsen](https://www.nngroup.com/articles/ten-usability-heuristics/). O protótipo é visual e não executa persistência; ausência de comportamento no protótipo não prova defeito no programa de terminal.

| Heurística | Observação no fluxo | Ajuste/validação necessária |
|---|---|---|
| 1. Visibilidade do estado | Painel mostra contagens; o botão abre o cadastro. | Incluir confirmação e estado de erro após Salvar; não foram demonstrados. |
| 2. Mundo real | Termos “ativo”, “tipo” e “responsável” são próximos do domínio. | Explicar “risco efetivo” quando entrar no painel. |
| 3. Controle e liberdade | Há caminho claro do painel para o formulário. | Mostrar Voltar/Cancelar e preservar dados ao retornar; fluxo não demonstra isso. |
| 4. Consistência | “Ativo” aparece nas duas telas. | Padronizar rótulos e posição das ações em futuras telas. |
| 5. Prevenção de erros | Formulário apresenta os campos principais. | Indicar obrigatórios e regras de ID/nome antes do envio. |
| 6. Reconhecimento | Contagens e exemplos reduzem necessidade de memória. | Oferecer opções de tipo em vez de exigir texto livre. |
| 7. Flexibilidade | Fluxo curto favorece primeira utilização. | Avaliar busca, atalhos e filtros para inventários maiores. |
| 8. Estética e minimalismo | Poucas informações por tela mantêm foco. | Evitar truncamento de rótulos e verificar legibilidade em janelas menores. |
| 9. Recuperação de erros | O protótipo não demonstra validação real. | Mensagem deve apontar campo, motivo e correção, mantendo valores preenchidos. |
| 10. Ajuda | Não há ajuda demonstrada no fluxo. | Incluir instruções breves de formato e exemplos ao lado dos campos. |

## WCAG 2.1: o que pode e o que não pode ser concluído

Os princípios POUR são: perceptível, operável, compreensível e robusto. A cor visível no Figma não basta para declarar conformidade. Para [1.4.3 contraste de texto](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html), medir cada par de cores usado em texto normal (alvo AA 4,5:1) e grande (3:1); não há medição registrada. Para [1.4.11 contraste não textual](https://www.w3.org/WAI/WCAG21/understanding/non-text-contrast.html), medir bordas/estados necessários para reconhecer controles (3:1). Não atribuí aprovação de contraste sem valores de cor verificados.

Para 2.1.1 (teclado) e 2.4.7 (foco visível), testar a implementação funcional com Tab/Shift+Tab/Enter e foco perceptível; um frame do Figma não prova isso. Para [3.3.2 rótulos ou instruções](https://www.w3.org/WAI/WCAG21/Understanding/labels-or-instructions), associar cada campo a um rótulo programático, não depender só de placeholder. Para 3.3.1 (identificação de erro), explicar o erro em texto e apontar o campo. Para 1.3.1 (informação e relações), usar títulos, lista/tabela e agrupamentos semânticos na versão HTML. O arquivo `prototipo.html` já usa `<main>`, títulos e tabela com `<caption>`; o formulário final ainda precisa dessas associações e testes.

**Conclusão:** o Figma comprova a existência de telas e a navegação inicial. O relatório identifica riscos de usabilidade e critérios WCAG aplicáveis. Não declara conformidade WCAG completa nem teste com tecnologia assistiva sem execução correspondente.
