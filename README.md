# Demo Marketplace

This repository contains a local Copilot CLI marketplace for Devoxx demo plugins.

## What is in this repository

- `.github/plugin/marketplace.json`: the marketplace definition
- `.claude-plugin`: a symlink to `.github/plugin` for Claude-compatible tooling
- `plugins/`: the local plugin inventory

## Current inventory

### Plugins

- `devoxx-games` (`plugins/devoxx-games`)
  - Version: `1.1.1`
  - Description: Game-focused Copilot CLI skills for the Devoxx demos, including locale support workflows for devoxx-quest.

- `gps-processing` (`plugins/gps-processing`)
  - Version: `1.1.0`
  - Description: GPX file analysis skills: calculate distances (km, miles, nautical miles), count trackpoints, and extract metadata from GPS tracks.

### Skills

- `add-language-devoxx-quest` (plugin: `devoxx-games`)
  - Location: `plugins/devoxx-games/skills/add-language-devoxx-quest/SKILL.md`
  - Purpose: add a new language/locale to the `devoxx-quest` Phaser game by generating locale files and patching the game sources.

- `gpx-management` (plugin: `gps-processing`)
  - Location: `plugins/gps-processing/skills/gpx-management/SKILL.md`
  - Purpose: analyze GPX files to calculate total distance (km, miles, nautical miles), count trackpoints, and extract track metadata.

## How the marketplace is structured

The marketplace root is declared in `.github/plugin/marketplace.json` with:

- marketplace name: `demo-marketplace`
- plugin root: `./plugins`

Today, that marketplace exposes two plugins: `devoxx-games` and `gps-processing`.

## How to use this repository

1. Clone the repository, or reference it directly from GitHub.
2. Register the marketplace in Copilot CLI.
3. Browse or install the plugins exposed by the marketplace.

Once added, Copilot CLI can discover the plugins and the skills defined in this repository.

## How the symlinked Claude path works

`.claude-plugin` is a symlink to `.github/plugin`:

```bash
.claude-plugin -> .github/plugin
```

This means both paths refer to the same marketplace files. Updating `marketplace.json` under `.github/plugin` also updates what is seen through `.claude-plugin`, without duplicating files.

## Add this marketplace in Copilot CLI

### From GitHub

```bash
copilot plugin marketplace add github-conferences-france/copilot-marketplace-demo
```

### From a local checkout

```bash
copilot plugin marketplace add /absolute/path/to/demo-marketplace
```

Once registered, you can browse the available plugins:

```bash
copilot plugin marketplace browse demo-marketplace
```

And install a plugin from the marketplace:

```bash
copilot plugin install devoxx-games@demo-marketplace
```

## Notes

- The English README is the primary documentation.
- The French translation is available in `README.fr.md`.
