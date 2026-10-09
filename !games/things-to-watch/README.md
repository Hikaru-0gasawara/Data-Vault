# things-to-watch

Filmes e séries que quero assistir. Filmes são separados por gênero; séries
ficam juntas, qualquer que seja o gênero.
Parte de [`!games`](..), no [Data-Vault](../..).

## Conteúdo

| Pasta | Lista | O que tem |
|-------|-------|-----------|
| [`horror-terror/`](horror-terror) | [`films.md`](horror-terror/films.md) | Filmes de terror |
| [`romance/`](romance) | [`films.md`](romance/films.md) | Filmes de romance (lista pessoal vazia; indicações exploratórias do ChatGPT) |
| [`series/`](series) | [`series.md`](series/series.md) | Todas as séries, de qualquer gênero |

## Como as listas funcionam

- Cada lista é um checklist em Markdown: troque `- [ ]` por `- [x]` ao assistir.
- Formato de cada item: `**Título em português** — *título original* (ano, plataforma) · observação`.
- Toda lista tem três seções:
  - **Minha lista** — o que eu mesmo escolhi.
  - **🤖 Indicações do Claude** — sugestões geradas por IA a partir da minha
    lista. Ficam sempre separadas, cada uma com `Baseado em: …` apontando o item
    que a motivou. Quando eu gostar de uma, movo para "Minha lista".
  - **🤖 Indicações do ChatGPT** — novas sugestões do ChatGPT (OpenAI), sempre
    ao final do arquivo, abaixo das indicações do Claude. Trazem data,
    justificativa, `Baseado em: …` e links de referência, sem repetir títulos.
    Em romance, a base são as outras listas, porque a lista pessoal está vazia.
- **Novo gênero de filme:** crie `<genero>/films.md` copiando a estrutura de
  [`horror-terror/films.md`](horror-terror/films.md).
- **Série de terror (ou de qualquer gênero):** vai em `series/series.md`, com o
  gênero anotado na linha — não em uma pasta de gênero.
