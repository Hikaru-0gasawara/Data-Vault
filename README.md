# Data-Vault

Cofre pessoal dos arquivos que quero versionados e à mão: configs de jogos,
listas do que assistir e ler, e anotações soltas. Cada pasta é independente e
tem o seu próprio README.

## Conteúdo

| Pasta | O que é |
|-------|---------|
| [`games/`](games) | Configs e referências dos jogos que eu jogo |
| [`games/cs2/`](games/cs2) | **Counter-Strike 2** — `autoexec.cfg` e miras (crosshairs) intercambiáveis |
| [`games/tft/`](games/tft) | **Teamfight Tactics** — registro de sites de referência (JSON + CLI), notas por patch e prints de partidas |
| [`!games/`](!games) | Tudo que **não** é jogo: listas do que assistir e ler, e anotações soltas |
| [`!games/things-to-watch/`](!games/things-to-watch) | Filmes (por gênero) e séries para assistir |
| [`!games/things-to-read/`](!games/things-to-read) | Livros para ler |
| [`!games/things-to-remember/`](!games/things-to-remember) | Anotações soltas em texto puro |

## Estrutura

```
games/
├── cs2/                  CS2 .cfg (autoexec + miras)
└── tft/                  data/ (sources.json), scripts/ (CLI), notes/ (por patch), imgs/ (prints)
!games/
├── things-to-watch/
│   ├── horror-terror/    films.md
│   ├── romance/          films.md
│   └── series/           series.md  (todas as séries, de qualquer gênero)
├── things-to-read/       books.md
└── things-to-remember/   python.txt, random.txt
```

## Convenções

- As listas de `!games/` são checklists em Markdown (`- [ ]` → `- [x]` ao concluir),
  com uma seção **Minha lista** e outra **🤖 Indicações do Claude** — sugestões
  geradas por IA, sempre separadas, com data e `Baseado em: …`. Detalhes e
  contagem das indicações em [`!games/README.md`](!games/README.md).
- Pastas e arquivos têm nome em inglês; o conteúdo das listas é em português.
