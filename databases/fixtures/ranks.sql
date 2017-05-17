--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.3
-- Dumped by pg_dump version 9.6.3

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: postgres; Type: COMMENT; Schema: -; Owner: -
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner:
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner:
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: results; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE results (
    id integer NOT NULL,
    score real NOT NULL
);


--
-- Data for Name: results; Type: TABLE DATA; Schema: public; Owner: -
--

COPY results (id, score) FROM stdin;
1	3.5
2	3.6500001
3	4
4	3.8499999
5	4
6	3.6500001
\.


--
-- Name: results results_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY results
    ADD CONSTRAINT results_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

