PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE accounts
             (Username text, Password text, SipServer text, OutboundProxy text );
INSERT INTO "accounts" VALUES('3053053050','myPassword3050','10.10.10.100','8.8.8.8');
INSERT INTO "accounts" VALUES('3053053051','myPassword3051','10.10.10.100','8.8.4.4');
COMMIT;
