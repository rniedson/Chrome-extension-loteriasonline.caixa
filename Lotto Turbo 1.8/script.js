function processarEntrada(entrada) {
    // Primeiro, divide a entrada pelas quebras de linha para separar os jogos
    let jogos = entrada.split('\n');

    // Processa cada jogo para normalizar os delimitadores
    jogos = jogos.map(jogo => {
        // Substitui sequências de espaços, tabulações e vírgulas por uma única vírgula
        let numeros = jogo.replace(/[\s,]+/g, ',').trim();
        // Remove possíveis vírgulas duplicadas (caso existam)
        numeros = numeros.replace(/,+/g, ',');
        // Remove vírgulas no início ou fim do jogo
        numeros = numeros.replace(/(^,)|(,$)/g, '');
        return numeros;
    });

    // Retorna os jogos processados
    return jogos;
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('adicionarNumeros').addEventListener('click', function() {
        const combinacoesTexto = document.getElementById('combinacoes').value;
        const combinacoes = processarEntrada(combinacoesTexto);

        combinacoes.forEach((combinacao, index) => {
            setTimeout(() => {
                console.log(`Adicionando combinação ${index + 1}:`, combinacao);
                // Converte a string de números separados por vírgulas de volta em um array
                const numeros = combinacao.split(',').map(Number);
                chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
                    chrome.tabs.sendMessage(tabs[0].id, {
                        action: "adicionarNumeros",
                        combinacoes: numeros  // Envia cada jogo processado individualmente como array
                    });
                });
            }, index * 1000); // Ajuste o delay conforme necessário
        });
    });
});
