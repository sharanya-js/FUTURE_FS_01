# Personal Professional Portfolio

This repo contains a full-stack personal portfolio.

Structure

- `/client` — Vite + React frontend (dark theme). Run with `npm run dev`.
- `/server` — Node.js + Express backend for contact form. Run with `npm start`.

Quick start

1. Create `.env` files from the `.env.example` files in each folder.
2. Start backend:

```bash
cd server
npm install
npm start
```

3. Start frontend:

```bash
cd client
npm install
npm run dev
```

Deployment

- Frontend: Vercel/Netlify (build output from Vite)
- Backend: Render/Railway/Heroku — configure environment variables for `MONGO_URI` and email credentials.

Local test

Start the server (from project root):

```bash
cd server
npm install
npm run dev
```

Start the client:

```bash
cd client
npm install
npm run dev
```

Test contact endpoint (server must be running):

```bash
node server/test-contact.js
```

Environment variables

- `server/.env` — set `MONGO_URI`, `EMAIL_HOST`, `EMAIL_USER`, `EMAIL_PASS`, `EMAIL_TO`.
- `client/.env` — set `VITE_API_URL` to point at the running backend (default is http://localhost:5000).
