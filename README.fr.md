# Demo Marketplace

Ce dépôt contient une marketplace locale pour les plugins Copilot CLI utilisés dans les démos Devoxx.

## Contenu du dépôt

- `.github/plugin/marketplace.json` : la définition de la marketplace
- `.claude-plugin` : un lien symbolique vers `.github/plugin` pour les outils compatibles Claude
- `plugins/` : l’inventaire local des plugins

## Inventaire actuel

### Plugin

- `devoxx-games` (`plugins/devoxx-games`)
  - Version : `1.0.0`
  - Description : ensemble de skills orientées jeu pour les démos Devoxx, notamment les workflows de support de langues pour devoxx-quest.

### Skill

- `add-language-devoxx-quest`
  - Emplacement : `plugins/devoxx-games/skills/add-language-devoxx-quest/SKILL.md`
  - Rôle : ajouter une nouvelle langue/locale au jeu Phaser `devoxx-quest` en générant les fichiers de locale et en modifiant les sources du jeu.

## Structure de la marketplace

La racine de la marketplace est déclarée dans `.github/plugin/marketplace.json` avec :

- nom de la marketplace : `demo-marketplace`
- racine des plugins : `./plugins`

Aujourd’hui, cette marketplace expose un seul plugin : `devoxx-games`.

## Utilisation du dépôt

1. Clonez le dépôt, ou référencez-le directement depuis GitHub.
2. Enregistrez la marketplace dans Copilot CLI.
3. Parcourez ou installez les plugins exposés par la marketplace.

Une fois ajoutée, Copilot CLI peut découvrir les plugins et les skills définis dans ce dépôt.

## Fonctionnement du chemin Claude via lien symbolique

`.claude-plugin` est un lien symbolique vers `.github/plugin` :

```bash
.claude-plugin -> .github/plugin
```

Cela signifie que les deux chemins pointent vers les mêmes fichiers de marketplace. Modifier `marketplace.json` dans `.github/plugin` met donc aussi à jour ce qui est visible via `.claude-plugin`, sans duplication de fichiers.

## Ajouter cette marketplace dans Copilot CLI

### Depuis GitHub

```bash
copilot plugin marketplace add github-conferences-france/copilot-marketplace-demo
```

### Depuis une copie locale

```bash
copilot plugin marketplace add /chemin/absolu/vers/demo-marketplace
```

Une fois la marketplace enregistrée, vous pouvez parcourir les plugins disponibles :

```bash
copilot plugin marketplace browse demo-marketplace
```

Et installer un plugin depuis la marketplace :

```bash
copilot plugin install devoxx-games@demo-marketplace
```

## Notes

- Le README en anglais est la documentation principale.
- La traduction française est disponible dans `README.fr.md`.
