const ativos = [
  { nome: "Notebook do Laboratório", tipo: "Notebook", criticidade: "Média" },
  { nome: "Servidor de Arquivos", tipo: "Servidor", criticidade: "Alta" },
  { nome: "Roteador Principal", tipo: "Roteador", criticidade: "Crítica" },
];

const lista = document.getElementById("lista-ativos");
lista.innerHTML = ativos.map(function (ativo) {
  return "<article class='cartao'><h2>" + ativo.nome + "</h2><p>Tipo: " +
    ativo.tipo + "</p><p>Criticidade: " + ativo.criticidade + "</p></article>";
}).join("");
