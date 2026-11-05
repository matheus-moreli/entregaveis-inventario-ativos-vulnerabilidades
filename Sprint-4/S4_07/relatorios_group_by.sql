SELECT a.nome, COUNT(v.cve) AS total, AVG(v.cvss) AS media_cvss
FROM ativo a LEFT JOIN vulnerabilidade v ON v.ativo_id = a.id
GROUP BY a.id, a.nome;

SELECT prioridade, COUNT(*) AS total
FROM vulnerabilidade
GROUP BY prioridade
HAVING COUNT(*) > 0;
