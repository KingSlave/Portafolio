/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     08/07/2016 10:07:10 a. m.                    */
/*==============================================================*/


drop table if exists ALUMNOS;

drop table if exists ASIGNATURAS;

drop table if exists EVIDENCIAS;

drop table if exists LISTAS;

drop table if exists PORTAFOLIOS;

drop table if exists USUARIOS;

/*==============================================================*/
/* Table: ALUMNOS                                               */
/*==============================================================*/
create table ALUMNOS
(
   NCONTROL             varchar(8) not null,
   APATERNO             varchar(20) not null,
   AMATERNO             varchar(20) not null,
   NOMBRE               varchar(30) not null,
   CARRERA              char(4) not null,
   PASS                 varchar(150),
   primary key (NCONTROL)
);

/*==============================================================*/
/* Table: ASIGNATURAS                                           */
/*==============================================================*/
create table ASIGNATURAS
(
   NGRUPO               int not null,
   NICK                 varchar(15),
   GRUPO                char,
   CARRERA              char(4),
   NOMBREASIGNATURA     varchar(60),
   SEMESTRE             integer,
   UNIDADES             int,
   primary key (NGRUPO)
);

/*==============================================================*/
/* Table: EVIDENCIAS                                            */
/*==============================================================*/
create table EVIDENCIAS
(
   NEVIDENCIA           int not null,
   NGRUPO               int,
   NOMBRE               varchar(40),
   VALOR                float,
   NUNIDAD              int,
   FECHAINICIO          datetime,
   FECHALIMITE          datetime,
   ABIERTO              bool,
   LINKRUBRICA          varchar(100),
   DESCRIPCION          varchar(200),
   primary key (NEVIDENCIA)
);

/*==============================================================*/
/* Table: LISTAS                                                */
/*==============================================================*/
create table LISTAS
(
   FOLIO                int not null,
   NCONTROL             varchar(8),
   NGRUPO               int,
   COMPLEMENTACION      bool,
   PROMEDIOFINAL        float,
   primary key (FOLIO)
);

/*==============================================================*/
/* Table: PORTAFOLIOS                                           */
/*==============================================================*/
create table PORTAFOLIOS
(
   NCONTROL             varchar(8) not null,
   NEVIDENCIA           int not null,
   ARCHIVO              varchar(100),
   FECHAENTREGA         datetime,
   COMENTARIO           varchar(100),
   CALIFICACION         float,
   OBSERVACIONES        varchar(200),
   primary key (NCONTROL, NEVIDENCIA)
);

/*==============================================================*/
/* Table: USUARIOS                                              */
/*==============================================================*/
create table USUARIOS
(
   NICK                 varchar(15) not null,
   NOMBRE               varchar(50),
   PASS                 varchar(150),
   TIPO                 varchar(50),
   primary key (NICK)
);

alter table ASIGNATURAS add constraint FK_REFERENCE_4 foreign key (NICK)
      references USUARIOS (NICK) on delete restrict on update restrict;

alter table EVIDENCIAS add constraint FK_REFERENCE_3 foreign key (NGRUPO)
      references ASIGNATURAS (NGRUPO) on delete restrict on update restrict;

alter table LISTAS add constraint FK_REFERENCE_1 foreign key (NCONTROL)
      references ALUMNOS (NCONTROL) on delete restrict on update restrict;

alter table LISTAS add constraint FK_REFERENCE_2 foreign key (NGRUPO)
      references ASIGNATURAS (NGRUPO) on delete restrict on update restrict;

alter table PORTAFOLIOS add constraint FK_REFERENCE_5 foreign key (NCONTROL)
      references ALUMNOS (NCONTROL) on delete restrict on update restrict;

alter table PORTAFOLIOS add constraint FK_REFERENCE_6 foreign key (NEVIDENCIA)
      references EVIDENCIAS (NEVIDENCIA) on delete restrict on update restrict;

