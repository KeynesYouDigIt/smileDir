CREATE DATABASE providers;

\c providers

CREATE TABLE provider_contact (
    -- With more time, would like to add a UUID
    provider_name CHAR(200) NOT NULL,
    phone CHAR(10) NOT NULL UNIQUE,
    email CHAR(320) NOT NULL,

    -- Info below is optional, as API call does not provide it.
    type_of_care CHAR(200),
    address CHAR(50), --https://smartystreets.com/docs/cloud/us-street-api
    city CHAR(50),
    state_postal_initials CHAR(2),
    zip CHAR(5)
);