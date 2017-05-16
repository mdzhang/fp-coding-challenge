PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE users(
    Id INT PRIMARY KEY NOT NULL,
    Email VARCHAR(255) NOT NULL
);
INSERT INTO "users" VALUES(1234,'mpilgrim@example.com');
INSERT INTO "users" VALUES(2534,'spilgrim@example.com');
INSERT INTO "users" VALUES(36245,'mpilgrim@example.com');
COMMIT;
