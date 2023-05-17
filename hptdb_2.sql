/*==============================================================*/
/* Nom de SGBD :  MySQL 5.0                                     */
/* Date de création :  14/05/2023 21:14:45                      */
/*==============================================================*/


drop table if exists Article;

drop table if exists Categorie;

drop table if exists ensemble;

/*==============================================================*/
/* Table : Article                                              */
/*==============================================================*/
create table Article
(
   id                   int not null,
   nom                  char(25),
   description          char(30),
   prix                 int,
   quantite             int,
   primary key (id),
   key AK_Identifiant_1 (id)
);

/*==============================================================*/
/* Table : Categorie                                            */
/*==============================================================*/
create table Categorie
(
   id                   int not null,
   nom                  char(25),
   primary key (id)
);

/*==============================================================*/
/* Table : ensemble                                             */
/*==============================================================*/
create table ensemble
(
   Art_id               int not null,
   Cat_id               int not null,
   primary key (Art_id, Cat_id)
);

alter table ensemble add constraint FK_association1 foreign key (Art_id)
      references Article (id) on delete restrict on update restrict;

alter table ensemble add constraint FK_association1 foreign key (Cat_id)
      references Categorie (id) on delete restrict on update restrict;

