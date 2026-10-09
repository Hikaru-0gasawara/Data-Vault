# games

Tudo que é de jogos fica aqui: uma pasta por jogo, cada uma com o seu próprio README.
Parte do [Data-Vault](..). Listas e anotações que não são de jogos ficam em
[`!games/`](../!games).

## Jogos

| Pasta | Jogo | Formato | O que tem |
|-------|------|---------|-----------|
| [`cs2/`](cs2) | Counter-Strike 2 | Arquivos de config | `autoexec.cfg` (binds, buy binds, aliases, viewmodel e sensibilidade) e miras intercambiáveis: `csr`, `donk`, `dotc`, `dotg`, `tap` e `lol1` |
| [`tft/`](tft) | Teamfight Tactics | Dados + script | Registro de sites de referência em JSON, CLI em Python, modelo de notas por patch e prints de partidas |

Os dois são independentes: `cs2/` é só config para copiar para dentro do jogo;
`tft/` tem um script que lista, valida e sincroniza a tabela de fontes do próprio README.

## Início rápido

**CS2** — copie os `.cfg` para a pasta de configs do jogo:

```
Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg
```

Depois, no console do jogo, `exec tap` (ou `donk`, `dotg`…) troca a mira.
Instalação completa em [`cs2/README.md`](cs2/README.md).

> **Atenção:** o `autoexec.cfg` começa com `unbindall`, ou seja, apaga **todos**
> os seus binds atuais antes de aplicar os dele. Faça backup da sua config antes.

**TFT** — a partir da raiz do repositório (Python 3.9+, só biblioteca padrão):

```bash
python games/tft/scripts/tft_sources.py list     # lista as fontes
python games/tft/scripts/tft_sources.py check    # valida o registro
```

Todos os comandos (`add`, `sync`, `open`) em [`tft/README.md`](tft/README.md).

## Estrutura

```
games/
├── cs2/    autoexec.cfg + miras (.cfg)
└── tft/
    ├── data/      sources.json (fonte da verdade) e sources.schema.json
    ├── scripts/   tft_sources.py (CLI)
    ├── notes/     TEMPLATE.md — notas por patch
    └── imgs/      prints de partidas, nomeados <patch>-<modo>-<resultado>.png
```

## Adicionando outro jogo

1. Crie `games/<jogo>/` com um nome curto em minúsculas, como `cs2` e `tft`.
2. Escreva um README na pasta: o que tem, como instalar/usar e avisos que
   importem (como o `unbindall` acima).
3. Adicione uma linha na tabela deste README e na tabela do
   [README da raiz](../README.md).
