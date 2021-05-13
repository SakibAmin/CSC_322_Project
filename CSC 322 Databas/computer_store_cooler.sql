-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: computer_store
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `cooler`
--

DROP TABLE IF EXISTS `cooler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cooler` (
  `cooler_id` int NOT NULL AUTO_INCREMENT,
  `company_id` int DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `fan_rpm` varchar(255) DEFAULT NULL,
  `type_of_cooler` varchar(255) DEFAULT NULL,
  `Radiator` int DEFAULT NULL,
  `socket` varchar(255) DEFAULT NULL,
  `rgb` varchar(255) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `in_stock` int DEFAULT NULL,
  `sold` int DEFAULT NULL,
  `total_profit` int DEFAULT NULL,
  PRIMARY KEY (`cooler_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `cooler_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `computer_parts_companies` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cooler`
--

LOCK TABLES `cooler` WRITE;
/*!40000 ALTER TABLE `cooler` DISABLE KEYS */;
INSERT INTO `cooler` VALUES (1,15,'Cooler Master Hyper 212','650-2000RPM','Air',0,'All','Yes',50,32,45,2250),(2,10,'NZXT Kraken Z73','500-1800 RPM','Liquid',360,'All','Yes',280,23,60,16800),(3,10,'NZXT Kraken X63','500-2000RPM','Liquid',280,'All','Yes',150,34,44,6600),(4,16,'Arctic Liquid Freezer II','200-1700RPM','Liquid',420,'All','No',348,44,13,4524),(5,17,'Noctua NH-U14S TR4 SP3','300-1500RPM','Air',0,'sTRX4','No',90,12,21,1890);
/*!40000 ALTER TABLE `cooler` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-13  5:56:37
