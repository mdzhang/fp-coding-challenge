init-emails-db:
	cat ./fixtures/emails.sql | sqlite3 ./fixtures/emails.db

open-emails-db:
	sqlite3 ./fixtures/emails.db

init-ranks-db:
	createdb postgres && psql postgres < fixtures/ranks.sql

open-ranks-db:
	psql postgres

run-find-duplicates:
	cat find_duplicates.sql | sqlite3 ./fixtures/emails.db

run-generate-ranks:
	cat generate_ranks.sql | psql postgres
