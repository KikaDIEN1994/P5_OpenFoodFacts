CREATE TABLE [IF NOT EXISTS] Product (
    product_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(128) NOT NULL,
    nutriscore CHAR(1),
    link_url TEXT,
    PRIMARY KEY (product_id)
);

CREATE TABLE [IF NOT EXISTS] Category (
    category_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    category_name VARCHAR(128) NOT NULL,
    PRIMARY KEY (category_id)
);
#2 foreign key of Product and Categozed 
CREATE TABLE [IF NOT EXISTS] Categorized (
    categorized_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    product_name VARCHAR(128) NOT NULL,
    nutriscore CHAR(1),
    link_url TEXT,
    PRIMARY KEY (categorized_id)
);

    #2 foreign key of Product, 1 for the product and another for subtitut 
CREATE TABLE [IF NOT EXISTS] FAVORIS (

    categorized_id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
    
)