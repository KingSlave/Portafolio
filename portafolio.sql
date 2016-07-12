CREATE DATABASE  IF NOT EXISTS `portafolio` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `portafolio`;
-- MySQL dump 10.13  Distrib 5.6.24, for Win32 (x86)
--
-- Host: localhost    Database: portafolio
-- ------------------------------------------------------
-- Server version	5.6.26-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `alumno`
--

DROP TABLE IF EXISTS `alumno`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alumno` (
  `NCONTROL` varchar(8) NOT NULL,
  `APATERNO` varchar(20) NOT NULL,
  `AMATERNO` varchar(20) NOT NULL,
  `NOMBRE` varchar(30) NOT NULL,
  `CARRERA` char(4) NOT NULL,
  `PASS` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`NCONTROL`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `asignatura`
--

DROP TABLE IF EXISTS `asignatura`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `asignatura` (
  `NGRUPO` int(11) NOT NULL,
  `NICK` varchar(15) DEFAULT NULL,
  `GRUPO` char(1) DEFAULT NULL,
  `CARRERA` char(4) DEFAULT NULL,
  `CLAVEASIGNATURA` varchar(10) DEFAULT NULL,
  `NOMBREASIGNATURA` varchar(60) DEFAULT NULL,
  `SEMESTRE` int(11) DEFAULT NULL,
  `UNIDADES` int(11) DEFAULT NULL,
  `PERIODO` varchar(20) DEFAULT NULL COMMENT 'Periodo escolar:   ENERO - JUNIO,   AGOSTO - ENERO',
  PRIMARY KEY (`NGRUPO`),
  KEY `FK_REFERENCE_4` (`NICK`),
  CONSTRAINT `FK_REFERENCE_4` FOREIGN KEY (`NICK`) REFERENCES `usuario` (`NICK`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Temporary view structure for view `calificacion`
--

DROP TABLE IF EXISTS `calificacion`;
/*!50001 DROP VIEW IF EXISTS `calificacion`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE VIEW `calificacion` AS SELECT 
 1 AS `nick`,
 1 AS `ngrupo`,
 1 AS `grupo`,
 1 AS `claveAsignatura`,
 1 AS `nombreAsignatura`,
 1 AS `semestre`,
 1 AS `ncontrol`,
 1 AS `nombre`,
 1 AS `aPaterno`,
 1 AS `aMaterno`,
 1 AS `nunidad`,
 1 AS `rubro`,
 1 AS `valor`,
 1 AS `calificacion`,
 1 AS `linkRubrica`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `evidencia`
--

DROP TABLE IF EXISTS `evidencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `evidencia` (
  `NGRUPO` int(11) NOT NULL,
  `NOMBRE` varchar(40) NOT NULL,
  `NUNIDAD` int(11) NOT NULL,
  `VALOR` float DEFAULT NULL,
  `FECHAINICIO` datetime DEFAULT NULL,
  `FECHALIMITE` datetime DEFAULT NULL,
  `ABIERTO` tinyint(1) DEFAULT NULL,
  `LINKRUBRICA` varchar(100) DEFAULT NULL,
  `DESCRIPCION` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`NGRUPO`,`NOMBRE`,`NUNIDAD`),
  CONSTRAINT `FK_REFERENCE_3` FOREIGN KEY (`NGRUPO`) REFERENCES `asignatura` (`NGRUPO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `lista`
--

DROP TABLE IF EXISTS `lista`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `lista` (
  `FOLIO` int(11) NOT NULL,
  `NCONTROL` varchar(8) DEFAULT NULL,
  `NGRUPO` int(11) DEFAULT NULL,
  `COMPLEMENTACION` tinyint(1) DEFAULT NULL,
  `PROMEDIOFINAL` float DEFAULT NULL,
  PRIMARY KEY (`FOLIO`),
  KEY `FK_REFERENCE_1` (`NCONTROL`),
  KEY `FK_REFERENCE_2` (`NGRUPO`),
  CONSTRAINT `FK_REFERENCE_1` FOREIGN KEY (`NCONTROL`) REFERENCES `alumno` (`NCONTROL`),
  CONSTRAINT `FK_REFERENCE_2` FOREIGN KEY (`NGRUPO`) REFERENCES `asignatura` (`NGRUPO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `portafolio`
--

DROP TABLE IF EXISTS `portafolio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `portafolio` (
  `NCONTROL` varchar(8) NOT NULL,
  `NGRUPO` int(11) NOT NULL,
  `NOMBRE` varchar(40) NOT NULL,
  `NUNIDAD` int(11) NOT NULL,
  `ARCHIVO` varchar(100) DEFAULT NULL,
  `FECHAENTREGA` datetime DEFAULT NULL,
  `COMENTARIO` varchar(100) DEFAULT NULL,
  `CALIFICACION` float DEFAULT NULL,
  `OBSERVACIONES` varchar(200) DEFAULT NULL,
  `RESULTADO` varchar(40) DEFAULT NULL COMMENT 'Permite indicar si la evidencia ha sido ACEPTADA, RECHAZADA, PENDIENTE DE REENVIO, etc. ',
  `FECHAREENVIO` datetime DEFAULT NULL,
  `NUMOPOR` int(11) DEFAULT NULL,
  PRIMARY KEY (`NCONTROL`,`NGRUPO`,`NOMBRE`,`NUNIDAD`),
  KEY `FK_REFERENCE_6` (`NGRUPO`,`NOMBRE`,`NUNIDAD`),
  CONSTRAINT `FK_REFERENCE_5` FOREIGN KEY (`NCONTROL`) REFERENCES `alumno` (`NCONTROL`),
  CONSTRAINT `FK_REFERENCE_6` FOREIGN KEY (`NGRUPO`, `NOMBRE`, `NUNIDAD`) REFERENCES `evidencia` (`NGRUPO`, `NOMBRE`, `NUNIDAD`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `usuario`
--

DROP TABLE IF EXISTS `usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `usuario` (
  `NICK` varchar(15) NOT NULL,
  `NOMBRE` varchar(50) DEFAULT NULL,
  `PASS` varchar(150) DEFAULT NULL,
  `TIPO` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`NICK`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Final view structure for view `calificacion`
--

/*!50001 DROP VIEW IF EXISTS `calificacion`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `calificacion` AS select `asignatura`.`NICK` AS `nick`,`portafolio`.`NGRUPO` AS `ngrupo`,`asignatura`.`GRUPO` AS `grupo`,`asignatura`.`CLAVEASIGNATURA` AS `claveAsignatura`,`asignatura`.`NOMBREASIGNATURA` AS `nombreAsignatura`,`asignatura`.`SEMESTRE` AS `semestre`,`alumno`.`NCONTROL` AS `ncontrol`,`alumno`.`NOMBRE` AS `nombre`,`alumno`.`APATERNO` AS `aPaterno`,`alumno`.`AMATERNO` AS `aMaterno`,`portafolio`.`NUNIDAD` AS `nunidad`,`portafolio`.`NOMBRE` AS `rubro`,`evidencia`.`VALOR` AS `valor`,`portafolio`.`CALIFICACION` AS `calificacion`,`evidencia`.`LINKRUBRICA` AS `linkRubrica` from (((`portafolio` join `asignatura`) join `alumno`) join `evidencia`) where ((`asignatura`.`NGRUPO` = `portafolio`.`NGRUPO`) and (`alumno`.`NCONTROL` = `portafolio`.`NCONTROL`) and (`evidencia`.`NGRUPO` = `portafolio`.`NGRUPO`) and (`evidencia`.`NOMBRE` = `portafolio`.`NOMBRE`) and (`evidencia`.`NUNIDAD` = `portafolio`.`NUNIDAD`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-07-12  3:52:50
