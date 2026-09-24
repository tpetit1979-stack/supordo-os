# Technical Stack Contract

Contrainte transversale, **pas une couche canonique numérotée**. Ce document
ne remplace, ne supersède, ne modifie et ne réinterprète pas `16`→`19`
(`docs/product-blueprint-antigravity/`). Il ne définit aucun écran métier,
aucune route métier, aucune table métier, aucun schéma métier, aucun
workflow métier, aucune décision `OPEN`. Aucune recommandation existante
n'est transformée en décision ici.

Rôle : les rails techniques imposés pour garantir la portabilité du produit
SUPORDO, indépendamment de tout outil IA de développement.

## Principe central

**NO DEVELOPMENT TOOL IS PART OF THE SUPORDO ARCHITECTURE.**

Google Antigravity, Claude Code, Cursor, Lovable ou tout autre outil de
développement restent des outils externes et remplaçables. Aucune
dépendance runtime à l'un d'eux. Aucune donnée ou métadonnée propre à ces
outils dans le modèle métier.

## Frontend

- React
- TypeScript
- Vite
- React Router — mode SPA client uniquement
- TanStack Query
- shadcn/ui
- Tailwind CSS
- React Hook Form
- Zod

## Backend

- Supabase PostgreSQL
- Supabase Auth
- Row Level Security
- Supabase Storage
- Supabase Edge Functions — uniquement lorsque nécessaires

## Tests

- Vitest
- React Testing Library
- Playwright

## Outillage

- npm
- Git
- GitHub comme future source de vérité du code

## Architecture

- Un seul repository applicatif : `supordo-app`.
- Frontend sous `src/`.
- Supabase as code sous `supabase/`.
- Migrations versionnées dans Git.
- Tests sous `tests/`.
- Documentation durable de l'application sous `docs/`.
- Aucune dépendance runtime à Antigravity, Claude Code, Cursor, Lovable ou
  un autre outil de développement.
- Aucune donnée ou métadonnée propre à ces outils dans le modèle métier.
- Pas de Dexie/PWA/offline avant la tranche produit concernée.

## Ce que ce document ne fait pas

Ne définit aucun écran, route, table ou schéma métier. Ne tranche aucune
question `OPEN` du registre `16` §6. Ne remplace pas `17`
(`BUILD-GATES-AND-SLICE-CONTRACT.md`) pour l'ordonnancement des tranches, ni
`19` (`SLICE-HANDOFF-TEMPLATE.md`) pour le format d'un packet de tranche.
