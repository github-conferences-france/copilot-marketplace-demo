---
name: add-language-devoxx-quest
description: Add a new language to the devoxx-quest game and update the required locale files and source code.
---

# Add Language to Devoxx-Quest

Use this skill to handle the language addition end-to-end:
- Translate the UI JSON from English
- Create all 3 locale files (`{code}.json`, `{code}-quiz.json`, `{code}-talks.json`)
- Patch `src/i18n/index.ts`, `src/scenes/PreloadScene.ts`, and `src/scenes/SettingsScene.ts`

## Steps

1. **Identify the 3 required parameters** from the user's message (or ask if missing):
   - `code` — ISO 639-1 code (e.g. `de`, `es`, `ja`, `pt`, `nl`)
   - `nativeName` — name in that language (e.g. `Deutsch`, `Español`, `日本語`)
   - `englishName` — name in English (e.g. `German`, `Spanish`, `Japanese`)

   For well-known languages, infer all 3 from the language name — don't ask if obvious.

2. **Create or update the required files** for that language:
   - Add the locale JSON files
   - Register the locale in the i18n setup
   - Make the language selectable in the game settings or preload flow where needed

3. **Confirm success** with a brief message: which files were created or patched.

## Notes
- Unless the user explicitly asks to translate quiz or talks content, they can stay in English by default.
- If the user mentions a language but you're unsure of the ISO code or native name, infer from common knowledge (e.g. "Spanish" → `es`, `Español`).
- No build step needed — just reload the dev server.
