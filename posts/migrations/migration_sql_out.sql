-- Exported from Django MigrateSQL

BEGIN
;
--
-- Create model Category
--
CREATE TABLE "posts_category" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"category_d esc" varchar(128) NOT NULL);
--
-- Create model Content
--
CREATE TABLE "posts_content" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"create_date" datetime NOT NULL,
	"edit_date" datetime NOT NULL,
	"title" varchar(512) NOT NULL,
	"slug" varchar(50) NOT NULL UNIQUE,
	"content" text NOT NULL);
--
-- Create model Tag
--
CREATE TABLE "posts_tag" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"tag_desc" varchar(128) NOT NULL);
--
-- Create model User
--
CREATE TABLE "posts_user" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"username" varchar(128) NOT NULL,
	"email" varchar(254) NOT NULL,
	"password" varchar(128) NOT NULL,
	"first_name" varchar(64) NOT NULL,
	"last_name" varchar(64) NOT NULL);
--
-- Add field author to content
--
ALTER TABLE "posts_content" RENAME TO "posts_content__old";

CREATE TABLE "posts_content"(
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"create_date" datetime NOT NULL,
	"edit_date" datetime NOT NULL,
	"title" varchar(512) NOT NULL,
	"slug" varchar(50) NOT NULL UNIQUE,
	"content" text NOT NULL,
	"author_id" integer NOT NULL REFERENCES "posts_user" ("id"));
INSERT INTO
   "posts_content" ("id", "create_date", "edit_date", "title", "slug", "content", "author_id") 
   SELECT
      "id",
      "create_date",
      "edit_date",
      "title",
      "slug",
      "content",
      NULL 
   FROM
      "posts_content__old";
DROP TABLE "posts_content__old";
CREATE INDEX "posts_content_author_id_a8f4257b" 
ON "posts_content" ("author_id");
--
-- Add field category to content
--
ALTER TABLE "posts_content" RENAME TO "posts_content__old";
CREATE TABLE "posts_content" (
	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
	"create_date" datetime NOT NULL,
	"edit_date" datetime NOT NULL,
	"title" varchar(512) NOT NULL,
	"slug" varchar(50) NOT NULL UNIQUE, "content" text NOT NULL,
	"author_id" integer NOT NULL REFERENCES "posts_user" ("id"),
	"category_id" integer NOT NULL REFERENCES "posts_category" ("id"));
INSERT INTO
   "posts_content" ("id", "create_date", "edit_date", "title", "slug", "content", "author_id", "category_id") 
   SELECT
      "id",
      "create_date",
      "edit_date",
      "title",
      "slug",
      "content",
      "author_id",
      NULL 
   FROM
      "posts_content__old";
DROP TABLE "posts_content__old";
CREATE INDEX "posts_content_author_id_a8f4257b" 
ON "posts_content" ("author_id");
CREATE INDEX "posts_content_category_id_3073b9f1" 
ON "posts_content" ("category_id");
COMMIT;

