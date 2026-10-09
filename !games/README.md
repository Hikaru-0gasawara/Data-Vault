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
troque `- [ ]` por `- [x]` ao assistir ou ler. Cada arquivo tem, nesta ordem:

1. **Minha lista** — o que eu mesmo escolhi.
2. **🤖 Indicações do Claude** — sugestões do Claude (Anthropic).
3. **🤖 Indicações do ChatGPT** — sugestões do ChatGPT (OpenAI).

Uma IA nova entra como mais uma seção `## 🤖 Indicações do <IA>` no fim do
arquivo. Indicações não são curadoria minha: quando eu gostar de uma, movo para
"Minha lista".

`things-to-remember/` é texto puro, sem checklist nem indicações.

## Formato das indicações

Toda seção de indicações de IA segue o mesmo formato, para que as listas
fiquem comparáveis:

- **Cabeçalho:** `## 🤖 Indicações do <IA>`, seguido de uma citação (`>`) que
  diz quem fez (IA e empresa), a data, que **não são curadoria minha**, o que
  foi conferido e o que não foi (ex.: streaming).
- **Grupos por tema:** `**Tema** (a partir de <itens da Minha lista>)`.
  Uma rodada posterior vira um grupo novo com `— acrescentado em AAAA-MM-DD`
  no fim do título, dentro da mesma seção. Não há subseção por rodada.
- **Filme ou série, uma linha por item:**
  `- [ ] **Título em português** (*título original*, ano, país/plataforma) — descrição curta. _Baseado em: X, Y._`
  Se o título em português for igual ao original, ele não se repete. Se não
  foi confirmado, o item diz `título em português não confirmado`.
- **Livro, uma linha por item:**
  `- [ ] **Título em português** — Autor (*título original*); nota curta. _Baseado em: X._`
- **`Baseado em`** cita itens da Minha lista. Itens de outra lista levam a
  origem entre parênteses: `Caveat (lista de terror)`.
- **Fica de fora:** links, blocos "por onde começar" ou "destaques" e texto em
  primeira pessoa da IA. O arquivo é escrito na minha voz.
- **Sem repetição:** nenhuma indicação repete a Minha lista ou outra seção.

Para criar um gênero novo de filme, copie a estrutura de
[`horror-terror/films.md`](things-to-watch/horror-terror/films.md) para
`things-to-watch/<genero>/films.md`. Séries vão sempre em `series/series.md`,
com o gênero anotado na linha.

## Indicações por IA

| Lista | Minha lista | Claude | ChatGPT |
|-------|-------------|--------|---------|
| [Filmes de terror](things-to-watch/horror-terror/films.md) | 9 | 14 | 12 |
| [Séries](things-to-watch/series/series.md) | 6 | 10 | 10 |
| [Livros](things-to-read/books.md) | 3 | 9 | 10 |
| [Filmes de romance](things-to-watch/romance/films.md) | 0 | 0 — lista vazia | 7, exploratórias |

- **Claude:** 2026-10-08 e 2026-10-09. Títulos, anos e diretores conferidos na
  web.
- **ChatGPT:** 2026-10-08, em duas rodadas. Formato alinhado ao padrão acima
  pelo Claude em 2026-10-09, com títulos em português conferidos.

## Sobre o nome

O `!` faz a pasta aparecer antes de `games/` nas listagens. No bash/zsh ele
dispara expansão de histórico, então cite o nome entre aspas simples:

```bash
cd '!games'
```
