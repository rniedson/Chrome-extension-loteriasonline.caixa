// Espera pelo carregamento completo do DOM
document.addEventListener('DOMContentLoaded', function() {
    // Adiciona um ouvinte de eventos ao botão "Apostar"
    document.getElementById('adicionarNumeros').addEventListener('click', function() {
        // Captura o valor inserido no textarea "combinacoes"
        const combinacoes = document.getElementById('combinacoes').value;
        // Envia uma mensagem para o content script da aba ativa
        chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
            chrome.tabs.sendMessage(tabs[0].id, {
                action: "adicionarNumeros",
                combinacoes: combinacoes
            });
        });
    });

    // Implementação do menu responsivo
    // var navbarToggle = document.getElementById('js-navbar-toggle');
    // var menu = document.getElementById('js-menu');

    // Adiciona um ouvinte de eventos para alternar a visibilidade do menu em telas menores
    // navbarToggle.addEventListener('click', function() {
    //   menu.classList.toggle('active');
    });

