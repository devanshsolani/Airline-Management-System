-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: projectdb1
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `bookedflights`
--

DROP TABLE IF EXISTS `bookedflights`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookedflights` (
  `passid` int(11) NOT NULL,
  `pname` varchar(45) NOT NULL,
  `nopass` varchar(45) NOT NULL,
  `depdate` varchar(45) NOT NULL,
  `arrdate` varchar(45) DEFAULT NULL,
  `depcity` varchar(45) NOT NULL,
  `arrcity` varchar(45) NOT NULL,
  `ftime` varchar(45) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookedflights`
--

LOCK TABLES `bookedflights` WRITE;
/*!40000 ALTER TABLE `bookedflights` DISABLE KEYS */;
INSERT INTO `bookedflights` VALUES (1014,'DEV','1','05/02/2020','---','Goa','Leh','9:00 pm'),(1014,'DEV','1','06/02/2020','---','Chennai','Goa','11:00 am'),(1014,'DEV','1','06/02/2020','---','Cochin','Mumbai','5:00 pm'),(1014,'DEV','1','07/02/2020','---','Cochin','Lucknow','3:00 pm'),(1014,'DEV','1','07/02/2020','07/02/2020','Delhi','Kolkata','1:00 pm'),(1014,'DEV','1','07/02/2020','---','Leh','Hyderabad','3:00 pm'),(1014,'DEV','1','07/02/2020','---','Goa','Nagpur','0'),(1014,'DEV','1','07/02/2020','---','Delhi','Leh','9:00 pm'),(1014,'DEV','1','11/02/2020','---','Goa','Mumbai','9:00 pm');
/*!40000 ALTER TABLE `bookedflights` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-03 21:32:17
