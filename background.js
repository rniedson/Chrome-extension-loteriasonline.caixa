// Exemplo de um service worker simples no Manifest V3 para uma extensão do Chrome

chrome.runtime.onInstalled.addListener(() => {
  console.log('Extensão "Caveira da Sorte" instalada.');
  // Aqui você pode inicializar o que for necessário para a sua extensão,
  // como configurações padrões no chrome.storage
});

chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  // Processa a mensagem recebida
  if (message.action === "iniciarAdicaoDeJogos") {
    console.log('Iniciando adição de jogos...');
    // Exemplo de ação para iniciar a adição de jogos.
    // Pode ser necessário obter detalhes da aba ativa ou outras informações.
    // Este é um ponto de partida para expandir conforme a necessidade da sua extensão.
    chrome.tabs.sendMessage(sender.tab.id, {action: "adicionarJogos", combinacoes: message.combinacoes}, response => {
      console.log("Resposta do content script:", response);
      sendResponse({status: 'Processo de adição iniciado'});
    });
    return true; // Indica que a resposta será enviada de forma assíncrona.
  }
  // Você pode adicionar mais condições aqui para tratar diferentes ações
  // como ajustes de configurações, armazenamento de dados, ou outras interações com a página da web.
});

// Adicione aqui outras funções que você necessitar, como funções para manipular abas,
// janelas, armazenar e recuperar dados do chrome.storage, entre outras funcionalidades
// que podem enriquecer a sua extensão.

// Lembre-se que o background.js atua como um "background worker", ouvindo eventos,
// mensagens e agindo conforme a lógica definida para a sua extensão.
