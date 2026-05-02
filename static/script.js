console.log("BOARD:", ultimoBoard);

const tabuleiro = document.getElementById("tabuleiro");

let selecionado = null;

const pecas = {
    "P":"♙","R":"♖","N":"♘","B":"♗","Q":"♕","K":"♔",
    "p":"♟","r":"♜","n":"♞","b":"♝","q":"♛","k":"♚",
    ".":""
};

let ultimoBoard = [];

function desenhar(board) {
    console.log("DESENHANDO BOARD:", board);

    if (!board) {
        console.log("Board inválido");
        return;
    }

    ultimoBoard = board;

    const tabuleiro = document.getElementById("tabuleiro");
    tabuleiro.innerHTML = "";

    for (let l = 0; l < 8; l++) {
        for (let c = 0; c < 8; c++) {

            const div = document.createElement("div");

            div.className = (l + c) % 2 === 0 ? "branca" : "preta";

            const coord = String.fromCharCode(97 + c) + (8 - l);

            const peca = board?.[l]?.[c] ?? ".";

            div.innerText = pecas[peca] || "";

            div.addEventListener("click", () => {
                console.log("CLICOU:", coord);
                clicar(coord);
            });

            tabuleiro.appendChild(div);
        }
    }
}

function coordToIndex(coord) {
    const c = coord.charCodeAt(0) - 97;
    const l = 8 - parseInt(coord[1]);
    return [l, c];
}

function clicar(coord) {

    if (selecionado === coord) {
        selecionado = null;
        atualizar();
        return;
    }

    if (!selecionado) {
        const [l, c] = coordToIndex(coord);

        if (ultimoBoard[l][c] === ".") return;

        selecionado = coord;
        atualizar();
        return;
    }

    const [l, c] = coordToIndex(coord);
    const [lSel, cSel] = coordToIndex(selecionado);

    const pecaOrigem = ultimoBoard[lSel][cSel];
    const pecaDestino = ultimoBoard[l][c];

    if (
        (pecaOrigem === pecaOrigem.toUpperCase() && pecaDestino === pecaDestino.toUpperCase()) ||
        (pecaOrigem === pecaOrigem.toLowerCase() && pecaDestino === pecaDestino.toLowerCase())
    ) {
        selecionado = coord;
        atualizar();
        return;
    }

    fetch("https://xadrez-python-1.onrender.com/move", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            origem: selecionado,
            destino: coord
        })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);

        if (data.erro) {
            alert(data.erro);
        }

        selecionado = null;
        atualizar();
    })
    .catch(err => {
        console.error(err);
        alert("Erro ao conectar com o servidor.");
        selecionado = null;
    });
}

function atualizar() {
    fetch("/board")
        .then(res => res.json())
        .then(data => {
            desenhar(data);
        })
        .catch(err => {
            console.error("Erro ao carregar tabuleiro", err);
        });
}

function resetar() {
    fetch("/reset", {
        method: "POST"
    })
    .then(() => atualizar());
}

atualizar();