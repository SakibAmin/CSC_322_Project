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
-- Table structure for table `cpu`
--

DROP TABLE IF EXISTS `cpu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cpu` (
  `cpu_id` int NOT NULL AUTO_INCREMENT,
  `company_id` int DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `number_of_cores` int DEFAULT NULL,
  `clock_speed` varchar(225) DEFAULT NULL,
  `boosted_clock_speed` varchar(255) DEFAULT NULL,
  `integrated_graphics` varchar(255) DEFAULT NULL,
  `socket` varchar(255) DEFAULT NULL,
  `cooler` varchar(255) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `in_stock` int DEFAULT NULL,
  `sold` int DEFAULT NULL,
  `total_profit` int DEFAULT NULL,
  PRIMARY KEY (`cpu_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `cpu_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `computer_parts_companies` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cpu`
--

LOCK TABLES `cpu` WRITE;
/*!40000 ALTER TABLE `cpu` DISABLE KEYS */;
INSERT INTO `cpu` VALUES (1,1,'Intel Core i3-10100',4,'3.6GHz','4.3GHz','Intel UHD Graphics 630','LGA1200','Yes',115,20,15,1725),(2,1,'Intel Core i5-10400',6,'2.9GHz','4.3GHz','Intel UHD Graphics 630','LGA1200','Yes',150,45,16,2400),(3,1,'Intel Core i7-10700K',8,'3.8GHz','5.1GHz','Intel UHD Graphics 630','LGA1200','No',315,65,55,17325),(4,1,'Intel Core i9-10900K',10,'3.7GHz','5.3GHz','Intel UHD Graphics 630','LGA1200','No',436,30,5,2180),(5,2,'AMD Ryzen 3 3200G',4,'3.6GHz','4 GHz','Radeon Vega 8','AM4','Yes',100,22,12,1200),(6,2,'AMD Ryzen 5 3600',6,'3.6GHz','4.2GHz','N/A','AM4','Yes',200,34,44,8800),(7,2,'AMD Ryzenn 7 3700X',8,'3.6GHz','4.4GHz','N/A','AM4','Yes',320,12,66,21120),(8,2,'AMD Threadripper 3990X',64,'2.9GHz','4.3Ghz','N/A','sTRX4','No',3959,34,22,87098);
/*!40000 ALTER TABLE `cpu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11 17:00:04
