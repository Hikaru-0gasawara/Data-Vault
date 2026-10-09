# !games

Tudo que **não** é jogo: o complemento de [`games/`](../games). Aqui ficam as
listas do que quero assistir e ler e as anotações soltas.
Parte do [Data-Vault](..).

## Conteúdo

| Pasta | O que é | Listas |
|-------|---------|--------|
| [`things-to-watch/`](things-to-watch) | Filmes (por gênero) e séries para assistir | [`horror-terror/films.md`](things-to-watch/horror-terror/films.md) · [`romance/films.md`](things-to-watch/romance/films.md) · [`series/series.md`](things-to-watch/series/series.md) |
| [`things-to-read/`](things-to-read) | Livros para ler | [`books.md`](things-to-read/books.md) |
| [`things-to-remember/`](things-to-remember) | Anotações soltas em texto puro | `python.txt` · `random.txt` |

## Estrutura

```
!games/
├── things-to-watch/
│   ├── horror-terror/   films.md
│   ├── romance/         films.md
│   └── series/          series.md  (todas as séries, de qualquer gênero)
├── things-to-read/      books.md
└── things-to-remember/  python.txt, random.txt
```

## Como as listas funcionam

As listas de `things-to-watch/` e `things-to-read/` são checklists em Markdown:
troque `- [ ]` por `- [x]` ao assistir ou ler. Todas seguem o mesmo formato, com
duas seções:

1. **Minha lista** — o que eu mesmo escolhi.
2. **🤖 Indicações do Claude** — sugestões geradas por IA a partir da minha lista.
   Ficam sempre separadas, com a data, e cada item traz `Baseado em: …`
   apontando o que o motivou. Não são curadoria minha; quando eu gostar de uma,
   movo para "Minha lista".

`things-to-remember/` é texto puro, sem checklist nem indicações.

Para criar um gênero novo de filme, copie a estrutura de
[`horror-terror/films.md`](things-to-watch/horror-terror/films.md) para
`things-to-watch/<genero>/films.md`. Séries vão sempre em `series/series.md`,
com o gênero anotado na linha.

## Indicações do Claude

Todas feitas em 2026-10-08, com título, ano e diretor conferidos na web.

| Lista | Indicações |
|-------|------------|
| [Filmes de terror](things-to-watch/horror-terror/films.md) | 11 filmes |
| [Séries](things-to-watch/series/series.md) | 7 séries |
| [Livros](things-to-read/books.md) | 7 livros |
| [Filmes de romance](things-to-watch/romance/films.md) | nenhuma — a lista ainda está vazia |

## Sobre o nome

O `!` faz a pasta aparecer antes de `games/` nas listagens. No bash/zsh ele
dispara expansão de histórico, então cite o nome entre aspas simples:

```bash
cd '!games'
```
