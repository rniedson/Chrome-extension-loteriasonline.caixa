chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
    if (request.action === "adicionarNumeros") {
        const combinacoes = request.combinacoes.split('\n').map(linha =>
            linha.trim().split(/\s+|,/).map(item => item.trim()).filter(item => item)
        );
        console.log("Combinacoes recebidas:", combinacoes);
        adicionarCombinacoesAoCarrinho(combinacoes);
    }
});

function ajustarQuantidadeDezenas(quantidadeDesejada) {
    const quantidadeAtualElemento = document.querySelector('.input-mais-menos span.ng-binding');
    const quantidadeAtual = parseInt(quantidadeAtualElemento.textContent, 10);
    const diferenca = quantidadeDesejada - quantidadeAtual;
    const botaoAumentar = document.querySelector('#aumentarnumero');
    const botaoDiminuir = document.querySelector('#diminuirnumero');

    for (let i = 0; i < Math.abs(diferenca); i++) {
        if (diferenca > 0) {
            botaoAumentar.click();
        } else if (diferenca < 0) {
            botaoDiminuir.click();
        }
    }
}

function adicionarCombinacoesAoCarrinho(combinacoes) {
    combinacoes.forEach((combinacao, index) => {
        setTimeout(() => {
            ajustarQuantidadeDezenas(combinacao.length);
            combinacao.forEach(item => {
                if (item.startsWith('T')) {
                    selecionarTrevo(item);
                } else {
                    selecionarNumero(item);
                }
            });
            setTimeout(() => adicionarAoCarrinho(), 1000);
        }, index * 3000);
    });
}

function selecionarNumero(numero) {
    const idNumero = `n${numero.toString().padStart(2, '0')}`;
    try {
        const elementoNumero = document.querySelector(`#${idNumero}`);
        if (elementoNumero) {
            console.log(`Clicando no número: ${numero}`);
            elementoNumero.click();
        } else {
            console.error(`Número ${numero} não encontrado.`);
        }
    } catch (error) {
        console.error(`Erro ao selecionar o número ${numero}:`, error);
    }
}

function selecionarTrevo(trevo) {
    const numeroTrevo = trevo.substring(1);
    const idTrevo = `trevo${numeroTrevo}`;
    try {
        const elementoTrevo = document.querySelector(`#${idTrevo}`);
        if (elementoTrevo) {
            console.log(`Selecionando trevo: ${trevo}`);
            elementoTrevo.click();
        } else {
            console.error(`Trevo ${trevo} não encontrado.`);
        }
    } catch (error) {
        console.error(`Erro ao selecionar o trevo ${trevo}:`, error);
    }
}

function adicionarAoCarrinho() {
    try {
        const botaoCarrinho = document.querySelector('#colocarnocarrinho');
        if (botaoCarrinho) {
            console.log("Adicionando ao carrinho.");
            botaoCarrinho.click();
        } else {
            console.error('Botão de adicionar ao carrinho não encontrado.');
        }
    } catch (error) {
        console.error('Erro ao adicionar ao carrinho:', error);
    }
}
