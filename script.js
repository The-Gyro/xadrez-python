console.log("JS CARREGOU");
const tabuleiro = document.getElementById("tabuleiro");

let selecionado = null;

// peças bonitas
const pecas = {
    "P":"♙","R":"♖","N":"♘","B":"♗","Q":"♕","K":"♔",
    "p":"♟","r":"♜","n":"♞","b":"♝","q":"♛","k":"♚",
    ".":""
};

let ultimoBoard = [];

// desenha o tabuleiro
function desenhar(board) {
    ultimoBoard = board;
    tabuleiro.innerHTML = "";

    for (let l = 0; l < 8; l++) {
        for (let c = 0; c < 8; c++) {

            const casa = board[l][c];
            const div = document.createElement("div");

            div.className = (l + c) % 2 === 0 ? "branca" : "preta";

            const coord = String.fromCharCode(97 + c) + (8 - l);

            div.innerText = pecas[casa];

            if (coord === selecionado) {
                div.style.border = "2px solid red";
            } else {
                div.style.border = "1px solid black";
            }

            div.onclick = () => clicar(coord);

            tabuleiro.appendChild(div);
        }
    }
}

// converte coordenada
function coordToIndex(coord) {
    const c = coord.charCodeAt(0) - 97;
    const l = 8 - parseInt(coord[1]);
    return [l, c];
}

// clique
function clicar(coord) {

    // 👉 se clicar na mesma peça → desmarca
    if (selecionado === coord) {
        selecionado = null;
        atualizar();
        return;
    }

    // 👉 primeira seleção
    if (!selecionado) {
        const [l, c] = coordToIndex(coord);

        if (ultimoBoard[l][c] === ".") return;

        selecionado = coord;
        atualizar();
        return;
    }

    // 👉 se clicar em OUTRA peça do MESMO time → troca seleção
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

    // 👉 jogada normal
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
    .catch(() => {
        alert("Erro ao conectar com o servidor.");
        selecionado = null;
    });
}

// atualizar board
function atualizar() {
    fetch("https://xadrez-python-1.onrender.com/board")
        .then(res => res.json())
        .then(data => {
            desenhar(data);
        })
        .catch(() => {
            console.log("Erro ao carregar tabuleiro");
        });
}

function resetar() {
    fetch("https://xadrez-python-1.onrender.com/reset", {
        method: "POST"
    })
    .then(() => atualizar());
}

// iniciar
atualizar();