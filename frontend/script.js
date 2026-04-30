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

            // cor da casa
            div.className = (l + c) % 2 === 0 ? "branca" : "preta";

            const coord = String.fromCharCode(97 + c) + (8 - l);

            // peça bonita
            div.innerText = pecas[casa];

            // destaque seleção
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

// converte coordenada (ex: e2 → índice do array)
function coordToIndex(coord) {
    const c = coord.charCodeAt(0) - 97;
    const l = 8 - parseInt(coord[1]);
    return [l, c];
}

// clique do usuário
function clicar(coord) {

    // primeira seleção
    if (!selecionado) {

        const [l, c] = coordToIndex(coord);

        // não deixa selecionar vazio
        if (ultimoBoard[l][c] === ".") return;

        selecionado = coord;
        atualizar();
        return;
    }

    // tentativa de jogada
    fetch("http://127.0.0.1:5000/move", {
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

        // se backend mandar erro
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

// busca o board atualizado
function atualizar() {
    fetch("http://127.0.0.1:5000/board")
        .then(res => res.json())
        .then(data => {
            desenhar(data);
        })
        .catch(() => {
            console.log("Erro ao carregar tabuleiro");
        });
}

// inicia
atualizar();