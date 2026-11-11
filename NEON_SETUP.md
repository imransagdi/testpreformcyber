# CYBER//NET + Neon setup

CYBER//NET reads the pooled Neon connection string from `DATABASE_URL`. It never stores the database password in Python source. If `DATABASE_URL` is absent, the server retains its local SQLite fallback.

## Windows development

1. Install Node.js if it is not already installed.
2. Open PowerShell in this project folder.
3. Install the Neon CLI if needed: `npm install -g neon`.
4. Run `neon login` and complete the browser sign-in yourself.
5. Link the existing Neon project: `neon link --project-id round-queen-79389039 -y`.
6. Pull its connection strings into a local `.env` file: `neon env pull --file .env`.
7. Confirm `.env` contains `DATABASE_URL` (pooled) and optionally `DATABASE_URL_UNPOOLED` (direct). Do not share or commit this file.
8. Install dependencies: `py -m pip install -r requirements.txt`.
9. Start the server with the existing project start command.

The Neon CLI instructions recommend using the pooled connection for ordinary app queries. Keep the direct connection for migration/admin tasks.

## Render

In the Render service, open **Environment** and add `DATABASE_URL` with the same pooled connection string from the local `.env`. Add `DATABASE_URL_UNPOOLED` only if you later need it for a migration command. Do not put either value in GitHub or in source files. Redeploy after saving the environment variables.

## Important

- Windows and Render will use the same Neon database when both have the same `DATABASE_URL`.
- This code creates the `accounts` table and its case-insensitive username index on startup.
- Existing SQLite database files are left untouched. This change does not automatically copy old SQLite accounts into Neon; do that as a separate, verified migration so existing data is not overwritten or duplicated.
- Account login tokens are currently held in server memory, so players may need to log in again after a Render restart. Account records and saved player progress are stored in Neon.
