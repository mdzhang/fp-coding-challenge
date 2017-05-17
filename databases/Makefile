init-emails-db:
	cat ./fixtures/emails.sql | sqlite3 ./fixtures/emails.db

open-emails-db:
	sqlite3 ./fixtures/emails.db

init-ranks-db:
	createdb postgres && psql postgres < fixtures/ranks.sql

open-ranks-db:
	psql postgres
